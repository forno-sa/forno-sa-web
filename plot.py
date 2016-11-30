import serial
import time

def start():
    ser = serial.Serial('/dev/ttyACM0', 9600)
    return ser

def get_values(ser):
    time.sleep(4)
    ser.write(b'i')
    valor = ser.readline()
    valor = float(valor[1:6])

    return valor

def close(ser):
    ser.close()


if __name__ == '__main__':
    print('Começando comunicação...')
    ser = start()
    print('Pegando valor...')
    valor = get_values(ser)
    print('Temperatura: %s' % valor)
    print('Pegando valor...')
    valor = get_values(ser)
    print('Temperatura: %s' % valor)
    print('Fechando conexão serial...')
    close(ser)
