products = ["pen", "pencil", "eraser", "notebook"]
while True:
    a=input('enter the product name : ')
    if a in products:
        print(f" {a} found at position {products.index(a)}")
    elif a not in products:
        products.append(a)
        print(products)
        break

