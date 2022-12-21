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

