#RobotName: Pipo
from RobotRL import RobotRL

robot = RobotRL()

def avanzar(velocidad,tiempo):
    robot.setVI(velocidad)
    robot.setVD(velocidad)
    robot.esperar(tiempo)


def retroceder(velocidad,tiempo):
    robot.setVI(velocidad*-1)
    robot.setVD(velocidad*-1)
    robot.esperar(tiempo)


def girarIzquierda(tiempo):
    robot.setVI(50)
    robot.setVD(80)
    robot.esperar(tiempo)


while robot.step():
    avanzar(100,0.01)
    if robot.getColorPiso()<90:  #No ve blanco, 100 blanco - 0 negro
        avanzar(50,0.3)          #avanza un poco mas para sacar 
        girarIzquierda(0.1)
        retroceder(100,1.5)
        while robot.getColorPiso()>90:
            retroceder(100,0.01)
        girarIzquierda(0.1)    
        
        
