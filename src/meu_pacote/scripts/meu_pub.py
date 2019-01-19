#!/usr/bin/python
#-*- coding:utf-8 -*-

import rospy	#Biblioteca principal para usar o ROS em Python
from std_msgs.msg import String	#Mensagem String para enviar nos topicos

def meu_pub():	#Funcao que sera chamada para publicar
	pub = rospy.Publisher('NomeDoTopico', String, queue_size = 10)
	rospy.init_node('NomeDoNo', anonymous=True)
	rate = rospy.Rate(2) #Frequencia em Hz
	while not rospy.is_shutdown():	#Enquanto o prog ainda estiver rodando
		nossa_str = "Ola Mundo! Horas: %s" % rospy.get_time()
		pub.publish(nossa_str) #Publica nossa string de informacao
		rate.sleep()	#Aguarda a freq. configurada

#Verifica se esse eh o arquivo principal chamado
if __name__ == "__main__":
	try:
		meu_pub()
	except rospy.ROSInterruptException:
		print 'Deu Exceção!'
	
