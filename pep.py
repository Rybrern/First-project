def calculadora():
    print("Calculadora Básica")
    print("Operaciones disponibles:")
    print("1. Suma (+)")
    print("2. Resta (-)")
    print("3. Multiplicación (*)")
    print("4. División (/)")
    print("5. Salir")
    
    while True:
        try:
            # Solicitar operación
            operacion = input("Seleccione una operación (1-5 o +,-,*,/): ").strip()
            
            # Verificar si quiere salir
            if operacion == '5' or operacion.lower() == 'salir':
                print("¡Hasta luego!")
                break
            
            # Validar operación
            if operacion not in ['1', '2', '3', '4', '+', '-', '*', '/']:
                print("Operación no válida. Intente nuevamente.")
                continue
            
            # Solicitar números
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            
            # Realizar operación
            if operacion == '1' or operacion == '+':
                resultado = num1 + num2
                print(f"Resultado: {num1} + {num2} = {resultado}")
            elif operacion == '2' or operacion == '-':
                resultado = num1 - num2
                print(f"Resultado: {num1} - {num2} = {resultado}")
            elif operacion == '3' or operacion == '*':
                resultado = num1 * num2
                print(f"Resultado: {num1} * {num2} = {resultado}")
            elif operacion == '4' or operacion == '/':
                if num2 == 0:
                    print("Error: No se puede dividir por cero")
                else:
                    resultado = num1 / num2
                    print(f"Resultado: {num1} / {num2} = {resultado}")
            
            # Preguntar si quiere continuar
            continuar = input("¿Desea realizar otra operación? (s/n): ").strip().lower()
            if continuar != 's' and continuar != 'si':
                print("¡Hasta luego!")
                break
                
        except ValueError:
            print("Error: Por favor ingrese números válidos.")
        except Exception as e:
            print(f"Ocurrió un error: {e}")

# Ejecutar la calculadora
if __name__ == "__main__":
    calculadora()