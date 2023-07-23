from proxmoxer import ProxmoxAPI
import urllib3


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def vmstatus(id):
    try:
        proxmox = ProxmoxAPI(
            "10.11.12.13", user="root@pam", password="300124", verify_ssl=False
        )
        for vm in proxmox.nodes("home").qemu.get():
            if vm['vmid'] == id :
                return vm['status']
    except Exception:
        print('error')

def vmstop(id):
    try:
        proxmox = ProxmoxAPI(
            "10.11.12.13", user="root@pam", password="300124", verify_ssl=False
        )
        proxmox.nodes("home").qemu(id).status.post('stop')
    except Exception:
        print('error')

def vmstart(id):
    try:
        proxmox = ProxmoxAPI(
            "10.11.12.13", user="root@pam", password="300124", verify_ssl=False
        )
        proxmox.nodes("home").qemu(id).status.post('start')
    except Exception:
        print('error')

def vmreset(id):
    try:
        proxmox = ProxmoxAPI(
            "10.11.12.13", user="root@pam", password="300124", verify_ssl=False
        )
        proxmox.nodes("home").qemu(id).status.post('reset')
    except Exception:
        print('error')

print(vmstatus(103))