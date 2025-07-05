def calcularIMC (kilo, centimetro):
  return kilo / (centimetro * centimetro)

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
      
      while True:
         n = input("Ingresa tu nombre: ").strip()
         if not n:
            print("El nombre no puede estar vacio.")
         else:
            break

      while True:
         pa = input("Ingresa tu primer apellido: ").strip()
         if not pa:
            print("El primer apellido no puede estar vacio.")
         else:
            break

      while True:
         sp = input ("Ingresa tu segundo apellido: ").strip()
         if not sp:
            print("El segundo apellido no puede estar vacio.")
         else:
            break

      print("    ")

      print ("Hola", n, pa, sp, "calcularemos tu IMC:")

      print("     ")

      while True:
         e = input("Ingresa tu edad: ")
         
         try:
            numero = int(e)
            if numero > 0:
             print("Numero valido:", numero)
             break
            else:
               print ("Debe ser un numero positivo,")
         except ValueError:
            print("Error: Solo se permiten números enteros. Intenta de nuevo.")  

      while True:
         peso = input("Ingresa tu peso: ")
         
         try:
            kilo = float(peso)
            if kilo > 0:
             print("Numero valido:", peso)
            break
         except ValueError:
            print("Error: Solo se permiten números enteros o con decimales. Intenta de nuevo.") 

      while True:
         altura = input("Ingresa tu altura: ")
         
         try:
            centimetro = float(altura)
            if centimetro > 0:
             print("Numero valido:", altura)
            break
         except ValueError:
            print("Error: Solo se permiten números enteros. Intenta de nuevo.")  
            break

      print("Su nivel de peso es:", nivelDePeso(calcularIMC(kilo, centimetro)))

      print("Gracias", n, pa, sp, "por utilizar esta calculadora de IMC")

      print ("Toma acciones dependiendo tu nivel de peso.") 
    
      print("Aqui te lo recuerdo:", nivelDePeso(calcularIMC(kilo, centimetro)))

      print ("Consulta a tu medico")

      print("Gracias")

  except ValueError:
        print("Error: Ingresa valores numéricos válidos.")    

if __name__ == "__main__":
    main()