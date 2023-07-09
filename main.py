import time
import serial

def write_com_command(port, baud, data, data_stop, delay):
    ser = serial.Serial(port=port, baudrate=baud)
    data_hex = bytes.fromhex(data)
    data_stop_hex = bytes.fromhex(data_stop)
    ser.write(data_hex)
    time.sleep(delay)
    ser.write(data_stop_hex)
    ser.close()


def write_com_action(port, baud, data):
    ser = serial.Serial(port=port, baudrate=baud)
    data_hex = bytes.fromhex(data)
    ser.write(data_hex)
    ser.close()

def write_enter(port, baud):
    ser = serial.Serial(port=port, baudrate=baud)
    ser.write(b'\n')


def send_command(port, baud, login, password, command):
    delay = 0.1
    exit_com = "exit"
    i = 0
    r = 9
    ser = serial.Serial(port=port, baudrate=baud)
    ser.write(b'\n')
    data = login.encode('utf-8')
    ser.write(data)
    ser.write(b'\n')
    time.sleep(delay)
    data = password.encode('utf-8')
    ser.write(data)
    ser.write(b'\n')
    time.sleep(delay)
    data = command.encode('utf-8')
    ser.write(data)
    ser.write(b'\n')
    while i < r:
        data = ser.readline()
        if i == 7:
            data = str(data)
            data_len = len(data)
            index2 = data_len - 1
            index3 = data_len - 2
            index4 = data_len - 3
            index5 = data_len - 4
            index6 = data_len - 5
            index = [0,1,index2,index3,index4,index5,index6]
            result_string = ""
            for i in range(len(data)):
                if i not in index:
                    result_string += data[i]
            print(result_string)
        time.sleep(delay)
        i = i + 1
    time.sleep(delay)   
    data = exit_com.encode('utf-8')
    ser.write(data)
    ser.write(b'\n')
    ser.close()

port = "/dev/ttyUSB0"
baud = "115200"
command = "date"
login = password = "admin"
#Enter
#Enter
#admin
#enter
#admin
#enter
#enter
#reboot
send_command(port, baud, login, password, command)


    

    

    
