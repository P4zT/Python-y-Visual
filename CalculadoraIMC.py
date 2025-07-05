def calcularIMC (peso, altura):
  return peso / (altura * altura)

def nivelDePeso(IMC):
  if IMC < 18.5:
    return "Bajo Peso"
  elif 18.5 <= IMC <= 24.9:
    return "Normal"
  elif 25.0 <= IMC <= 29.99:
    return "Sobre Peso"
  elif 30.0 <= IMC <= 34.9:
    return "Obesidad leve"
  elif 35.0 <= IMC <= 39.9:
    return "Obesidad Media"
  elif 40.0 <= IMC <= 49.9:
    return "Obesidad alta"
  elif IMC >= 50:
    return "Obesidad morbida"
  


def main():
  print ("Hola bienvenido a la calculadora de IMC")
  print("     ")
  try:
      
      n = str(input("Ingrese su nombre: "))

      ap = str(input("Ingresa tu primer apellido: "))

      am = str(input("Ingresa tu apellido materno: "))

      print("    ")

      print ("Hola", n, ap, am, "calcularemos tu IMC:")

      print("     ")

      e = int(input("Ingresa tu edad: "))

      if e <= 0:
          return

      peso = float(input("Ingresa tu peso (KG): "))

      altura = float(input("Ingresa tu altura (M): "))

      if peso <= 0 or altura <= 0:
            return
      
      print("Su nivel de peso es:", nivelDePeso (calcularIMC(peso, altura)))

      print("Gracias", n, ap, am, "por utilizar esta calculadora de IMC")

      print ("Toma acciones dependiendo tu nivel de peso.") 
    
      print("Aqui te lo recuerdo:", nivelDePeso(calcularIMC(peso, altura)))

      print ("Consulta a tu medico")

      print("Gracias")

  except ValueError:
        print("Error: Ingresa valores numéricos válidos.")    

if __name__ == "__main__":
    main()