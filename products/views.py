from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Product
from .forms import ProductForm


@login_required
def product_list(request):
    products = Product.objects.filter(is_active=True)
    return render(request, 'products/list.html', {'products': products})


@login_required
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk, is_active=True)
    return render(request, 'products/detail.html', {'product': product})


@login_required
def product_add(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.created_by = request.user
            product.save()
            messages.success(request, f'"{product.title}" has been added successfully!')
            return redirect('products:list')
        else:
            messages.error(request, 'Please fix the errors below.')
    else:
        form = ProductForm()
    return render(request, 'products/form.html', {'form': form, 'action': 'Add'})


@login_required
def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f'"{product.title}" has been updated!')
            return redirect('products:list')
        else:
            messages.error(request, 'Please fix the errors below.')
    else:
        form = ProductForm(instance=product)
    return render(request, 'products/form.html', {'form': form, 'action': 'Edit', 'product': product})


@login_required
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        title = product.title
        product.delete()
        messages.success(request, f'"{title}" has been deleted.')
        return redirect('products:list')
    return render(request, 'products/confirm_delete.html', {'product': product})
