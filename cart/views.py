from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from products.models import Product
from .models import Cart, CartItem, Order, OrderItem


def get_or_create_cart(user):
    cart, _ = Cart.objects.get_or_create(user=user, is_active=True)
    return cart


@login_required
def cart_view(request):
    cart = get_or_create_cart(request.user)
    return render(request, 'cart/cart.html', {'cart': cart})


@login_required
def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk, is_active=True)
    cart = get_or_create_cart(request.user)
    item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        item.quantity += 1
        item.save()
        messages.success(request, f'Added another "{product.title}" to your cart.')
    else:
        messages.success(request, f'"{product.title}" added to your cart!')
    return redirect('cart:view')


@login_required
def remove_from_cart(request, pk):
    item = get_object_or_404(CartItem, pk=pk, cart__user=request.user)
    title = item.product.title
    item.delete()
    messages.info(request, f'"{title}" removed from cart.')
    return redirect('cart:view')


@login_required
def update_quantity(request, pk):
    item = get_object_or_404(CartItem, pk=pk, cart__user=request.user)
    quantity = int(request.POST.get('quantity', 1))
    if quantity < 1:
        item.delete()
        messages.info(request, 'Item removed from cart.')
    else:
        item.quantity = quantity
        item.save()
    return redirect('cart:view')


@login_required
def checkout(request):
    cart = get_or_create_cart(request.user)
    if not cart.items.exists():
        messages.warning(request, 'Your cart is empty.')
        return redirect('cart:view')

    if request.method == 'POST':
        # Create the order
        order = Order.objects.create(
            user=request.user,
            total=cart.get_total(),
            status='completed'
        )
        for item in cart.items.all():
            OrderItem.objects.create(
                order=order,
                product=item.product,
                product_title=item.product.title,
                price=item.product.price,
                quantity=item.quantity,
            )
        # Clear cart
        cart.items.all().delete()
        cart.is_active = False
        cart.save()
        messages.success(request, 'Order placed successfully!')
        return redirect('cart:success', pk=order.pk)

    return render(request, 'cart/checkout.html', {'cart': cart})


@login_required
def order_success(request, pk):
    order = get_object_or_404(Order, pk=pk, user=request.user)
    return render(request, 'cart/success.html', {'order': order})
