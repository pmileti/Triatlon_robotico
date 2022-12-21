#RobotName: Mileti
from RobotRL import RobotRL

robot = RobotRL()

def avanzar():
    robot.setVI(70)
    robot.setVD(70)
    robot.esperar(0.05)


def retroceder(tiempo):
    robot.setVI(-70)
    robot.setVD(-70)
    robot.esperar(tiempo)


def girarDerecha():
    robot.setVI(40)
    robot.setVD(10)

def girarIzquierda():
    robot.setVI(10)
    robot.setVD(40)

girarDerecha()
robot.esperar(0.2)
avanzar()

while robot.step():
	avanzar()
	if robot.getColorPisoI()>90 and robot.getColorPisoD()>90: ##Blanco - Blanco
		girarDerecha()
		robot.esperar(0.3)
		
	if robot.getColorPisoI()>90 and robot.getColorPisoD()<90: ##Blanco - Negro
		avanzar()
	if robot.getColorPisoI()<90 and robot.getColorPisoD()<90: ##Negro - Negro
		girarIzquierda()
		robot.esperar(0.3)
		
		
		
   # avanzar()
   # if robot.getColorPisoI()<90:
   #     girarDerecha()
   #     robot.esperar(0.4)
   # if robot.getColorPisoD()<90:
   #     girarIzquierda()
   #     robot.esperar(0.4)
   # if robot.getColorPisoI()<90 and robot.getColorPisoD()<90:
   #     retroceder(0.5)
	
