from django import template

register = template.Library()


@register.filter(name='is_in_cart')
def is_in_cart(gal,cart):
    keys = cart.keys()
    for id in keys:
       if int(id) == gal.id:
           return True
    return False

@register.filter(name='cart_quantity')
def cart_quantity(gal,cart):
    keys = cart.keys()
    for id in keys:
       if int(id) == gal.id:
           return cart.get(id)
    return 0

@register.filter(name='price_total')
def price_total(gal,cart):  
    return gal.price * cart_quantity(gal,cart)

@register.filter(name='total_cart_price')
def total_cart_price(gal,cart): 
    sum = 0
    for product in gal:
        sum += price_total(product,cart) 
    return sum
