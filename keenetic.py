import paramiko

host = '10.11.12.1'
user = 'admin'
secret = '300124'
port = 22

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())


def piholeon():
    client.connect(hostname=host, username=user, password=secret, port=port)
    client.exec_command('no interface ISP ip dhcp client name-servers')
    client.close()

def piholeoff():
    client.connect(hostname=host, username=user, password=secret, port=port)
    client.exec_command('interface ISP ip dhcp client name-servers')
    client.close()
