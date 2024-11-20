from flask import Flask, jsonify, send_from_directory
import serial
import threading
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

SERIAL_PORT = "/dev/ttyUSB0"  # Adjust as needed
BAUD_RATE = 115200
latest_data = {}

def read_serial_data():
    global latest_data
    try:
        with serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1) as ser:
            while True:
                line = ser.readline().decode('utf-8').strip()
                logging.debug(f"Raw Serial Line: {line}")
                if "D;" in line:  # Check if "D;" exists in the line
                    line = line[line.index("D;"):]  # Strip everything before "D;"
                    if line.endswith(";"):
                        content = line[2:-1]  # Remove "D;" prefix and final ";"
                        pairs = content.split(";")
                        latest_data = {kv.split(":")[0]: float(kv.split(":")[1]) for kv in pairs if ":" in kv}
                        logging.info(f"Updated latest_data: {latest_data}")
    except Exception as e:
        logging.error(f"Error reading serial data: {e}")

@app.route("/")
def serve_index():
    return send_from_directory("templates", "index.html")

@app.route("/data")
def get_data():
    return jsonify(latest_data)

@app.route("/<key>")
def get_value(key):
    value = latest_data.get(key.upper(), None)
    if value is None:
        return jsonify({"error": "Key not found"}), 404
    return jsonify({key: value})

if __name__ == "__main__":
    threading.Thread(target=read_serial_data, daemon=True).start()
    app.run(debug=True)