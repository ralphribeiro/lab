import serial
import sys
import pandas as pd
import numpy as np
import time

# porta =  '/dev/ttyACM0'
porta = '/dev/ttyUSB0'
baud = 57600

valores = {'yaw': 0.0, 
           'pitch': 0.0,
           'roll': 0.0,
           'temperatura': 0.0,
           'pressao': 0.0,
           'altitude':0.0}

def Coloca_em_variaveis(v):
    global valores

    # v = v.decode('utf-8')
    # quebra = v.find('\n')    
    # v = v[0:quebra]
    # quebra = v.find('\r')
    # v = v[0:quebra]    
    l = v.split(';')

    if len(l) == len(valores):
        valores['yaw'] = l[0]
        valores['pitch'] = l[1]
        valores['roll'] = l[2]
        valores['temperatura'] = l[3]
        valores['pressao'] = l[4]
        valores['altitude'] = l[5]


class ManipulaSerial:
    def __init__(self, p, b):
        self.ser = serial.Serial(port=p, baudrate=b)
        self.buf = bytearray()

    def envia_dado(self, dado):
        dado += '\n'
        self.ser.write(dado.encode('utf-8'))

    def recebe_dado(self):
        dado = self.ser.readline()
        dado = dado.decode('utf-8')
        dado = dado[0:dado.find('\n')]
        dado = dado[0:dado.find('\r')]
        return dado

def main():
    
    arduino = ManipulaSerial(porta, baud)
    df_eixos = pd.DataFrame()

    try:
        while True:
            # entrada = input()
            # if entrada != None:        
            #     arduino.envia_dado(entrada) 
            
            dado = arduino.recebe_dado()
            # if isinstance(dados, str):
            print(dado)


            dado = dado.split(',')
            time_stamp = time.time()            
            dado.insert(3, time_stamp)

            # if len(dado) == 4:
            xyz_series = pd.Series(dado)      
            df_eixos = df_eixos.append(xyz_series, ignore_index=True)
        

    except KeyboardInterrupt:
        # pass
        df_eixos.to_csv('valores.csv',index=False)

main()