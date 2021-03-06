from django.shortcuts import render, redirect

def add_to_cart(request,slug):
    username = request.user.username
    price = Item.objects.get(slug = slug).price
    quantity = Item.objects.get(slug = slug).quantity
    discounted_price = Item.objects.get(slug = slug).discounted_price
    if discounted_price > 0:
        original_price = discounted_price
    else:
        original_price = price
    total = original_price*quantity

    data = Cart.objects.create(
        uername = username,
        items = Item.objects.filter(slug = slug)[0],
        slug = slug,
        quantity = quantity,
        total = total
    )
    data.save()
    return redirect('/')

