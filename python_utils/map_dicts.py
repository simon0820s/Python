items=[
    {
        'product':'camisa',
        'price':'100'
    },
    {
        'product':'pantalones',
        'price':'200'
    },
    {
        'product':'chaqueta',
        'price':'300'
    }
]
#Leer solo precios
prices=list(map(lambda item:item['price'],items))
print(prices)

def add_taxes(item):
    item['taxes']= float(item['price']) * 1.19
    return item

#modificar
new_items=list(map(add_taxes,items))
print(new_items)