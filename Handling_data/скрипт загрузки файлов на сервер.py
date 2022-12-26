import pysftp
import sys
import paramiko

server_path = '/dir/'
f1 = 'script.py'

host	 = "ip"
port	 = 1974
user     = "user"
password = "*******"

transport = paramiko.Transport((host, int(port)))
transport.connect(username=user, password=password)
sftp = paramiko.SFTPClient.from_transport(transport)

sftp.chdir(server_path)
sftp.put(f1, f1)
sftp.close()

print('Upload done.')