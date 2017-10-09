'''
* Control de LED en Arduino desde Raspberry Pi
* Ver: <<LINK A GIT>>
'''

import serial

arduino = serial.Serial('/dev/ttyACM0', 9600) #Objeto arduino linkeado al puerto serie

print ("Comenzando comunicacion serial con Arduino: ")

while True:
    comando = raw_input('Introduce una H para encender y una L para apagar: ') #Input por teclado
    arduino.write(comando) #Envia el comando por el puerto serial
    if comando == 'H'
        print('LED Encendido')
    elif comando == 'L'
        print ('LED Apagado')

arduino.close() #Cerramos la comunicacion serie
