from flask import Flask, jsonify, render_template, request
from SerialLoggerHandler import SerialLoggerHandler
import logging
from threading import Lock
from serial.tools.list_ports import comports

# Flask app
app = Flask(__name__)

# Serial Logger setup
logger_handler = SerialLoggerHandler(debug=False)
data_lock = Lock()
latest_data = {}

logging.basicConfig(level=logging.DEBUG)

# Serve the web page
@app.route("/")
def index():
    return render_template("index.html")

# API: List available ports
@app.route("/ports")
def list_ports():
    try:
        ports = [port.device for port in comports()]
        app.logger.debug(f"Detected ports: {ports}")
        return jsonify(["Auto"] + ports if ports else ["Auto"])
    except Exception as e:
        app.logger.error(f"Error detecting ports: {e}")
        return jsonify(["Auto"])

# API: Connect to a port (or auto-detect)
@app.route("/connect", methods=["POST"])
def connect():
    port = request.json.get("port", "Auto")
    try:
        if port == "Auto":
            port = logger_handler.detectPort()
            if not port:
                app.logger.error("Auto-detection failed. No suitable port found.")
                return jsonify({"success": False, "error": "Auto-detection failed. No suitable port found."}), 400

        app.logger.info(f"Attempting to connect to port: {port}")
        logger_handler.setPort(port)
        logger_handler.setCallback(update_data)
        logger_handler.start()

        if logger_handler.is_listening:
            app.logger.info(f"Successfully connected to port: {port}")
            return jsonify({"success": True, "port": port, "message": f"Connected to {port}"})
        else:
            app.logger.warning(f"Failed to start listening on port: {port}")
            return jsonify({"success": False, "error": f"Failed to start listening on port: {port}"}), 500
    except Exception as e:
        app.logger.error(f"Connection error: {e}")
        return jsonify({"success": False, "error": str(e)}), 500


# API: Disconnect
@app.route("/disconnect", methods=["POST"])
def disconnect():
    try:
        app.logger.info("Attempting to disconnect...")
        logger_handler.stop()
        app.logger.info("Successfully disconnected.")
        return jsonify({"success": True, "message": "Disconnected"})
    except Exception as e:
        app.logger.error(f"Disconnection error: {e}")
        return jsonify({"success": False, "error": str(e)}), 500

# API: Get connection status
@app.route("/status")
def status():
    status = "connected" if logger_handler.is_listening else "disconnected"
    app.logger.debug(f"Connection status: {status}")
    return jsonify({"status": status})

# API: Get latest data
@app.route("/data")
def get_data():
    with data_lock:
        app.logger.debug(f"Latest data being sent: {latest_data}")
        return jsonify(latest_data)

# Callback: Update the latest data
def update_data(data):
    global latest_data
    app.logger.debug(f"Received new data in callback: {data}")
    with data_lock:
        latest_data = data
        app.logger.debug(f"Updated latest_data: {latest_data}")

if __name__ == "__main__":
    app.run(debug=True)