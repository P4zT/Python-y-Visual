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
  #Declaro variables y operaciones, esto lo hice primero como en el ejemplo

#Abro un bloque de main para trabajar dividido las impresiones al usuario.
def main():
  print ("Hola bienvenido a la calculadora de IMC")
  print("     ")#Coloque estos "Print" en blanco o espacios para darle espacios entre mensajes y no verse abultado y confundido al ingresar datos.
  try:
      
      while True: #Coloque un "While" para hacer un bucle infinito hasta que el usuario coloque un valor correcto. POSDATA; No pude hacer que no ingresaran valores numericos.
         n = input("Ingresa tu nombre: ").strip()
         if not n:
            print("El nombre no puede estar vacio.")
         else:
            break

      while True: #Coloque un "While" para hacer un bucle infinito hasta que el usuario coloque un valor correcto.
         pa = input("Ingresa tu primer apellido: ").strip()
         if not pa: #Si el valor ingresado no es el correcto repite.
            print("El primer apellido no puede estar vacio.")
         else:
            break #El valor es correcto, continua.

      while True: #Coloque un "While" para hacer un bucle infinito hasta que el usuario coloque un valor correcto.
         sp = input ("Ingresa tu segundo apellido: ").strip()
         if not sp:
            print("El segundo apellido no puede estar vacio.")
         else:
            break
#Al colocar sus credenciales, imprimimos sus credenciales para darle una bienvenida y se sienta lo mas incluido posible dentro del progama.
      print("    ")

      print ("Hola", n, pa, sp, "calcularemos tu IMC:")

      print("     ") #Coloque estos "Print" en blanco o espacios para darle espacios entre mensajes y no verse abultado y confundido al ingresar datos.

      while True: #Nuevamente un "While" para ingresar datos hasta que sea el dato correcto.
         e = input("Ingresa tu edad: ")
         
         try:
            numero = int(e)
            if numero > 0: #Esta vez estamos colocando que el dato solicitado sea un valor numerico entero con "int" mayor a cero colocando ">".
             print("Numero valido:", numero)
             break
            else: #Se coloca un "else" para poder reingresar un valor y que no se termine el programa.
               print ("Debe ser un numero positivo,")
         except ValueError:
            print("Error: Solo se permiten números enteros. Intenta de nuevo.")  
#Hasta que el dato no sea correcto, imprimira la linea de arriba para sugerir al usuario la manera correcta de hacerlo.
      while True:
         peso = input("Ingresa tu peso: ")
         
         try:
            kilo = float(peso)
            if kilo > 0: #Se le solicita al usuario colocar un valor numerico, pero esta vez puede ser decimal con "float" y que sea mayor a cero con ">".
             print("Numero valido:", peso)
             break
            else:
              print("Debe ser un numero positivo") #Si el usuario colca un numero menor o igual a cero, arrojara este mensaje para indicarle que hacer
         except ValueError:
            print("Error: Solo se permiten números enteros o con decimales. Intenta de nuevo.") 

      while True:
         altura = input("Ingresa tu altura: ")
         
         try:
            centimetro = float(altura)
            if centimetro > 0: #Nuevamente se solicita al usuario colocar un valor numerico, pero esta vez puede ser decimal con "float" y que sea mayor a cero con ">".
             print("Numero valido:", altura)
             break
            else:
             print("Debe ser un numero positivo")
         except ValueError:
            print("Error: Solo se permiten números con decimales. Intenta de nuevo.")  
         
      print("   ")

      print("Su nivel de peso es:", nivelDePeso(calcularIMC(kilo, centimetro))) #Imprimimos el nivel de peso del usuario.

      print("   ")

      print("Gracias", n, pa, sp, "por utilizar esta calculadora de IMC") #Colocamos su nombre y apellidos para darle una mejor presentacion.

      print("   ")

      print ("Toma acciones dependiendo tu nivel de peso.") #Le recomendamos tomar acciones si asi lo requiere.

      print("   ")
    
      print("Aqui te lo recuerdo:", nivelDePeso(calcularIMC(kilo, centimetro))) #Recordamos al usuario el nivel de peso en caso de no querer subir a leer mas arriba.
      
      print("   ")

      print ("Consulta a tu medico") #Recomendamos consultar un medico en caso de requerirlo.

      print("   ")

      print("Gracias") #Damos las gracias por usar nuestra calculadora.

  except ValueError:
        print("   ")    #Impresion para espacios.

if __name__ == "__main__":
    main()
#Cerramos nuestro bloque con el comando anteriormente escrito.