def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def interpretar_imc(imc):
    if imc < 18.5:
        return "Bajo peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    elif 30 <= imc < 34.9:
        return "Obesidad grado I"
    elif 35 <= imc < 39.9:
        return "Obesidad grado II"
    else:
        return "Obesidad grado III"

def main():
    print("Calculadora de IMC (Índice de Masa Corporal)")
    try:
        peso = float(input("Ingresa tu peso en kilogramos (kg): "))
        altura = float(input("Ingresa tu altura en metros (m): "))
        
        if peso <= 0 or altura <= 0:
            print("Error: El peso y la altura deben ser mayores a cero.")
            return

        imc = calcular_imc(peso, altura)
        categoria = interpretar_imc(imc)

        print(f"\nTu IMC es: {imc:.2f}")
        print(f"Clasificación: {categoria}")
    except ValueError:
        print("Error: Ingresa valores numéricos válidos.")

if __name__ == "__main__":
    main()