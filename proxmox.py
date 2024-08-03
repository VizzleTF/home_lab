from proxmoxer import ProxmoxAPI
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxmox = ProxmoxAPI("10.11.12.13", user="root@pam", password="", verify_ssl=False)

def get_all_vms():
    vms = []
    for node in proxmox.nodes.get():
        node_name = node['node']
        for vm in proxmox.nodes(node_name).qemu.get():
            vms.append({
                'node': node_name,
                'vmid': vm['vmid'],
                'name': vm['name'],
                'status': vm['status']
            })
    return vms

def vm_action(node, vmid, action):
    try:
        proxmox.nodes(node).qemu(vmid).status.post(action)
    except Exception as e:
        print(f"Error performing {action} on VM {vmid} on node {node}: {str(e)}")

def vmstart(node, vmid):
    vm_action(node, vmid, 'start')

def vmstop(node, vmid):
    vm_action(node, vmid, 'stop')

def vmreset(node, vmid):
    vm_action(node, vmid, 'reset')