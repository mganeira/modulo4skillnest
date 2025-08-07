#Código del profe

def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero")
    return a / b
if __name__ == "__main__":
    try:
        resultado = dividir(10, 0)
        print("El resultado es:", resultado)
    except ZeroDivisionError as e:
        print("Excepción capturada")
        print(e)
        
# raise es para para lanzar excepciones de forma intencional en nuestro código. En validaciones se usa para detener 
# la ejecución cuando los datos no son válidos, como raise ValueError("El número debe ser positivo") cuando validamos entrada de usuario.
#  También se puede usar raise sin argumentos dentro de un except para volver a lanzar la misma excepción capturada.
