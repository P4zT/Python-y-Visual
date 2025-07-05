Practicas de UCAMP
Para crear mi código empecé investigando y apoyándome con  la demo que nos  brindaron. 
Al tener una referencia de cómo iniciar mi código, comencé colocando formulas del Índice de Masa Corporal, las operaciones  que llevan a obtener el índice de masa  corporal del usuario,  así como colocar una referencia de su índice de masa corporal.
Una vez terminado empecé abriendo un “def main” para organizar lo que alojara las impresiones al usuario, el llenado de datos y por último la impresión de su Índice de Masa Corporal.
Para darle la bienvenida la usuario coloque un “print(“”)” para poder insertar el mensaje de bienvenido. Coloque de nuevo “print(“”)” en blanco para darle un espacio entre líneas de mensaje para el usuario y no hacerlo todo abultado.
Continue abriendo un “try” de lo poco que investigue se ocupa para poder darle un numero entero a una variable. También lo coloque para el usuario no pueda colocar otro carácter que no sea el deseado.
Continue con un “While True:” para hacer un bucle hasta que el usuario coloque el valor deseado, se coloca una variable “n” y se le da el valor de nombre del usuario. A continuación, un “if not” para que el usuario no pueda dejar en blanco la primera solicitud, “else” se encargara de repetir si no coloco correctamente el valor esperado, al dejarla en blanco arrojara un mensaje de “El nombre no pude estar vacio”, de lo contrario, si el usuario coloca un nombre continuamos.
Repito el mismo código, pero ahora agregando una nueva variable “pa” para su primer apellido y “sp” para su segundo apellido.
Imprimimos el nombre del usuario junto un mensaje de “calcularemos tu IMC”. 
Coloco de nuevo un “While True:” para las variables de edad, peso y altura, pero esta vez agregaremos un “if” solamente para que el numero ingresado sea mayo a cero colocando “if numero > 0”, esta vez se agregara un “except ValueError” para detectar un error al ingresar un valor de texto en vez de un número.
Repito con los tres datos solicitados y al termino de esto empezamos a realizar impresiones de su nivel de peso llamando a las formulas colocas al inicio del código, igual llamamos a las variables “kilo” y “centimetro”.
Colocamos varios “print(“”)” para poder darle su IMC y realizar espacios entre líneas de texto, le daremos una indicación de tomar acciones dependiendo su nivel de peso y que consulte a su médico si es necesario.
Por ultimo damos las gracias por utilizar el programa.
(Espero haber explicado de la mejor manera, no soy tan bueno explicando, pero hice mi mayor esfuerzo)
#Igual coloque comentarios en el código para lograr separar ciertos códigos específicos.
Reflexión; Es importante saber nuestro índice de masa corporal, ya que puede prevenir futuros problemas de salud. Al programar necesitaras de todos los medios posibles, investigaciones a fondo del tema, códigos referentes que ayuden a lograr el objetivo, ayudarnos investigando no significa que copiemos un código de otro programador totalmente, pero podemos tomar referencias e investigar por qué usa esas líneas de códigos.
