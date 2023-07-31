from flask import Flask, render_template, request
import proxmox, keenetic

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/containers.html', methods=['GET', 'POST'])
def containers():
    if proxmox.vmstatus(103) == 'running':
        adguard = True
    else:
        adguard = False

    if proxmox.vmstatus(101) == 'running':
        plex = True
    else:
        plex = False

    if proxmox.vmstatus(100) == 'running':
        nextcloud = True
    else:
        nextcloud = False

    if proxmox.vmstatus(104) == 'running':
        nginx = True
    else:
        nginx = False

    if request.method == 'POST':
        if request.form.get('action1') == 'AdGuard':
            proxmox.vmreset(103)
        elif request.form.get('action1') == 'Plex':
            proxmox.vmreset(101)
        elif request.form.get('action1') == 'Nextcloud':
            proxmox.vmreset(100)
        elif request.form.get('action3') == 'AdGuard':
            proxmox.vmstart(103)
        elif request.form.get('action1') == 'Proxy':
            proxmox.vmreset(104)
        elif request.form.get('action3') == 'Proxy':
            proxmox.vmstart(104)
        elif request.form.get('action3') == 'Plex':
            proxmox.vmstart(101)
        elif request.form.get('action3') == 'Nextcloud':
            proxmox.vmstart(100)
        elif request.form.get('action2') == 'Провайдера':
            keenetic.piholeoff()
        elif request.form.get('action2') == 'Pihole':
            keenetic.piholeon()


    return render_template('containers.html', nginx=nginx, adguard=adguard, plex=plex, nextcloud=nextcloud)

if __name__ == '__main__':
    app.run(port='80')
