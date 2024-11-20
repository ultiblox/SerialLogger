from flask import Flask, jsonify, render_template
import serial
import logging
from threading import Thread, Lock
import time

logging.basicConfig(level=logging.DEBUG)

# Flask app
app = Flask(__name__)

# Serve the custom index.html at /
@app.route("/")
def index():
    return render_template("index.html")

# API endpoint to provide data to the frontend
@app.route("/data")
def get_data():
    with data_lock:
        return jsonify(latest_data)

# Dummy Data Storage (Thread-safe)
data_lock = Lock()
latest_data = {"T": 24.5, "H": 60.1, "L": 0}

# Serial Reader Function
def read_serial_data():
    global latest_data
    try:
        with serial.Serial("/dev/ttyUSB0", 115200, timeout=1) as ser:
            while True:
                line = ser.readline().decode("utf-8").strip()
                logging.debug(f"Raw Serial Line: {line}")
                if "D;" in line:
                    line = line[line.index("D;") :]
                    if line.endswith(";"):
                        content = line[2:-1]
                        pairs = content.split(";")
                        with data_lock:
                            latest_data = {
                                kv.split(":")[0]: float(kv.split(":")[1]) for kv in pairs if ":" in kv
                            }
                        logging.info(f"Updated latest_data: {latest_data}")
    except serial.SerialException as e:
        logging.error(f"Serial port error: {e}")
        time.sleep(5)  # Retry delay
        read_serial_data()
    except Exception as e:
        logging.error(f"Unexpected error: {e}")

# Start the serial reader in a background thread
Thread(target=read_serial_data, daemon=True).start()

if __name__ == "__main__":
    app.run(debug=False)