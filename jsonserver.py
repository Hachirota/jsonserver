from flask import Flask, jsonify
import subprocess


app = Flask(__name__)

@app.route('/status')
def send_status():
    hstnme = str(subprocess.check_output("hostname")).strip()
    ipadd =  str(subprocess.check_output(["hostname", "-i"])).strip()
    cpu = str(subprocess.check_output("nproc")).strip()
    mem = str(subprocess.check_output(['awk', '$1 == \"MemTotal:\" {print $2/1024/1024}', '/proc/meminfo'])).strip()

    sysinfo = {
    "hostname": hstnme,
    "ip_address": ipadd,
    "cpus": cpu,
    "memory": str(mem) + " GB"}

    return jsonify(sysinfo)

if __name__ == "__main__":
    app.run(port=8080)
