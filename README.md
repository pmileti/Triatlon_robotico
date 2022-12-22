# Triatlón Robótico por Pablo Mileti
Simulador del Triatlón Robótico de los Torneos Bonaerenses basado en el trabajo de Ricardo Moran y Gonzalo Zabala (CAETI - UAI) para la Roboliga.

En mi caso tomé el simulador de Sumo que ellos crearon para poder diseñar y programar las dos disciplinas restantes del Triatlón Robótico de los Torneos Bonaerenses. Todo esto fue desarrollado para utilizar en la pandemia COVID 2020, sin embargo también sirve para practicar la programación antes de armar un robot.

Aquí en este repositorio están las 3 disciplinas del Triatlón Robótico de los Torneos Bonaerenses para practicar programando en Python.

# Para simularlo:

Por un lado se debe instalar el Simulador Webots (R2021a). Es bastante pesado y ocupa mas de 2GB en disco. Como contra requiere de una buena placa de video, puede no funcionar en ciertas computadoras. La instalación es muy sencilla, solo deben presionar siempre siguiente hasta finalizar.

Como complemento debemos instalar el lenguaje Python, una versión igual o posterior a la 3.7.7. Es fundamental al instalar Python seleccionar previamente la opción de añadir Python a las variables de entorno (puede aparecer también como Add Python to environment variables o add to PATH) , si no tildan esa opción en la instalación Webots no tendrá acceso a Python y nada funcionará.

Finalmente deben descargarse las 3 disciplinas llamadas worlds o mundos que son las que están aquí. Deben descomprimir y desde Webots ir al menú File--> Open World  y acceder a cada mundo ubicado en la carpeta world de cada disciplina.

Dentro de la carpeta de cada disciplina encontrarán un carpeta llamada ejemplos con un código que pueden tomar como guía o modelo para desarrollar el propio. 

A continuación los links para descargar ambos y el archivo comprimido con las 3 disciplinas:

Webots: https://github.com/cyberbotics/webots/releases/tag/R2021a

Python: https://www.python.org/downloads/release/python-377/

# Despejar el área
![Despejar el area](https://github.com/pmileti/Triatlon_robotico/blob/main/preview_Despejar.png)

# Velocidad y control
![Velocidad y control](https://github.com/pmileti/Triatlon_robotico/blob/main/preview_Velocidad.png)

# Sumo
![Sumo](https://github.com/pmileti/Triatlon_robotico/blob/main/preview_Sumo.png)

# Ejemplos de programación del robot:

```
#RobotName: Mileti
from RobotRL import RobotRL

robot = RobotRL()
robot.setVI(95)
robot.setVD(100)
robot.esperar(1.7)

while robot.step():
	if (robot.getDI()==100 and robot.getDD()==100):  #No detecta nada cerca ninguno de los dos sensores
		robot.setVI(-50)
		robot.setVD(50)
	else:
		robot.setVI(100)
		robot.setVD(100)
		robot.esperar(0.7)
```

# Reglamento propio basado en el original
Este es el reglamento con explicación de la ubicación de los sensores del robot para cada disciplina [Reglamento mayo 2021](https://github.com/pmileti/Triatlon_robotico/blob/main/Reglamento%20Triatl%C3%B3n%20Rob%C3%B3tico%20-%20Mayo%202021.pdf)
