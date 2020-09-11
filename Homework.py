fruits=['Apple', 'Banana', 'Tomato', 'Potato']
phones={
    'name':'iPhone',
    'stock':42,
    'price':65432.1
}
phones['memory']=64
print()
print(phones)
print(phones.get('stock'))

print()
phones['products']=fruits
phones['products'].append('Cucumber')
print(phones['products'][0])
print(len(phones['products']))
print(phones['products'])
print(phones)