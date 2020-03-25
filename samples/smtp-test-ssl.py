import ssl;
import socket;
import re;
import base64;

SMTP_SERVER = 'smtp.mail.ru';
SMTP_PORT= 465;
SMTP_AUTH_LOGIN = 'логин'
SMTP_AUTH_PASS = 'пароль'

def read(f):
    ans="";
    line=f.readline().strip();
    while re.match("\d{3} ",line)==None:
        print("S: "+line);
        ans+=line+"\n";
        line=f.readline().strip();
    print("S: "+line);
    ans+=line+"\n";
    return(ans);

def write(f,s):
    f.write(s+"\n");
    f.flush();
    print("C: "+s);

def b64(s):
    return(base64.b64encode(s.encode()).decode())

def test_ssl_smtp():
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM);
    ssl_sock = ssl.SSLSocket(sock);
    ssl_sock.connect((SMTP_SERVER,SMTP_PORT));

    f = ssl_sock.makefile('rw');

    ans=read(f);

    write(f,"ehlo test");
    ans=read(f);

    write(f,"auth login");
    ans=read(f);

    write(f,b64(SMTP_AUTH_LOGIN));
    ans=read(f);

    write(f,b64(SMTP_AUTH_PASS));
    ans=read(f);

    write(f,"quit");
    ans=read(f);

if __name__ == "__main__":
    test_ssl_smtp()