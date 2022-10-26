def suma(**kwargs):
    print(type(kwargs))
suma(x=3,y=5,z=2)

def suma2(**kwargs):
    total=0
    for clave,valor in kwargs.items():
        print(f"{clave} = {valor}")
        total+=valor
    return total
print(suma2(x=3,y=5,z=2))

"""Combinando"""

def megasuma(num1,num2, *args, **kwargs):
    print(f"El primer valor es:{num1}")
    print(f"El segundo valor es:{num2}")
    for item in args:
        print(f"arg = {item}")
    for clave,valor in kwargs.items():
        print(f"{clave} = {valor}")


print("\n")
megasuma(15,50,100,200,300,400,x='uno', y='dos', z='tres')


mis_args=[10,20,30,40]
mis_kwargs={'x':'diez','y':'veinte','z':'treinta'}
print("\n")
megasuma(15,50,*mis_args,**mis_kwargs)