def cart_count(request):
    count = 0
    if request.user.is_authenticated:
        from cart.models import Cart
        cart = Cart.objects.filter(user=request.user, is_active=True).first()
        if cart:
            count = cart.get_item_count()
    return {'cart_count': count}
