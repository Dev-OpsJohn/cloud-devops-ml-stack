# Dummy Nvidia SMI Exporter for Prometheus
from flask import Flask, Response
import subprocess

app = Flask(__name__)

@app.route("/metrics")
def metrics():
    try:
        result = subprocess.check_output(["nvidia-smi", "--query-gpu=utilization.gpu", "--format=csv,nounits,noheader"])
        utilization = result.decode().strip()
        return Response(f"nvidia_gpu_utilization {utilization}\n", mimetype="text/plain")
    except Exception as e:
        return Response(f"# exporter error: {e}", mimetype="text/plain")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9101)
