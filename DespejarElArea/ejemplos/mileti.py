#RobotName: Mileti
from RobotRL import RobotRL

robot = RobotRL()
velocidad=100
def avanzar(velocidad,tiempo):
    robot.setVI(velocidad)
    robot.setVD(velocidad)
    robot.esperar(tiempo)


def retroceder(velocidad,tiempo):
    robot.setVI(velocidad*-1)
    robot.setVD(velocidad*-1)
    robot.esperar(tiempo)


def girarDerecha(velocidad,tiempo):
    robot.setVI(velocidad)
    robot.setVD(velocidad*-1)
    robot.esperar(tiempo)


while robot.step():
    
    while robot.getColorPiso()>50:
       avanzar(velocidad,0.1)
    girarDerecha(50,0.5)
        
        
