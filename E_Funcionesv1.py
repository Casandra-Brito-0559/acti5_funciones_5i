print("Manejo de funciones V1")
def hola_mundo():
    print("Haloooo")

def Mensa(msg):
    print(msg)

def EscribeNC(Nombre,apellido):
    print(Nombre,apellido)
    print(f"Tu nombre completo es {Nombre} {apellido}")

def suma2n(n1,n2):
    s=n1+n2
    return f"LA suma de {n1} y de {n2} es de :",s
    
## Llamando a la funcion
hola_mundo()
Mensa("Hola WhatsAPP") ## Llama mensa con 1 parametro
Mensa("El profe me sorprende mandando mensajes :OOOOOO")
EscribeNC("Taylor"," Swift")

print("--Funciones que regresan valoreas--")
print(suma2n(2,2))
print(suma2n(16,46))