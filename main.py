from flask import Flask, render_template, request
import proxmox

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/containers.html', methods=['GET', 'POST'])
def containers():
    vms = proxmox.get_all_vms()

    if request.method == 'POST':
        action = request.form.get('action')
        vmid = request.form.get('vmid')
        node = request.form.get('node')

        if action == 'start':
            proxmox.vmstart(node, vmid)
        elif action == 'reset':
            proxmox.vmreset(node, vmid)

        # Refresh VM status after action
        vms = proxmox.get_all_vms()

    return render_template('containers.html', vms=vms)

if __name__ == '__main__':
    app.run(port='80')