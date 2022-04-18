from datetime import datetime
import socket
import sys
import time

try:
    s = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
except socket.error:
    print( "Bağlantı başarısız :(" )
    sys.exit()

print( "Socket Oluşturuldu!" )

host = '127.0.0.1'
port = 7878

try:
    remote_ip = socket.gethostbyname(host)
except socket.gaierror:
    print( "Ana bilgisayar adı çözülemedi" )
    sys.exit()

print( "IP Addres: " + remote_ip )

print( "Socket Connected to " + host + " using IP " + remote_ip )

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Bağlandı {addr}")
        while True:
            time.sleep(1)
            saat = datetime.now()
            id_ = "a11_01"
            deger = "test"
            str_ = "{0}|{1}|{2}\n".format(saat,id_,deger)
            print(str_)
            data = bytes(str_, 'utf-8')
            conn.send(data)
