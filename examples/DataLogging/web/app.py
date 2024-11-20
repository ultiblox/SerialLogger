from flask import Flask, jsonify
import dash
from dash import dcc, html
import dash_daq as daq
from threading import Thread
import serial
import logging

logging.basicConfig(level=logging.DEBUG)

# Flask app
app = Flask(__name__)

# Dash app (mounted at `/`)
dash_app = dash.Dash(__name__, server=app, url_base_pathname="/")
dash_app.layout = html.Div(
    style={"backgroundColor": "#121212", "color": "white", "textAlign": "center"},
    children=[
        html.H1("Data Logger", style={"marginBottom": "20px"}),
        html.Div(
            style={"display": "flex", "justifyContent": "center", "gap": "30px"},
            children=[
                # Temperature Gauge
                daq.Gauge(
                    id="temperature-gauge",
                    label="Temperature",
                    min=0,
                    max=50,
                    value=0,  # Initial value
                    color={"gradient": True, "ranges": {"green": [0, 25], "yellow": [25, 40], "red": [40, 50]}},
                ),
                # Humidity Gauge
                daq.Gauge(
                    id="humidity-gauge",
                    label="Humidity",
                    min=0,
                    max=100,
                    value=0,  # Initial value
                    color={"gradient": True, "ranges": {"blue": [0, 50], "green": [50, 80], "red": [80, 100]}},
                ),
                # Loop Counter
                html.Div(
                    style={"backgroundColor": "#1e1e1e", "borderRadius": "10px", "padding": "20px"},
                    children=[
                        html.H3("Loop Count"),
                        html.P(id="loop-counter", children="0", style={"fontSize": "24px", "margin": "0"}),
                    ],
                ),
            ],
        ),
        # Add an interval component
        dcc.Interval(
            id="interval-component",
            interval=1000,  # Update every 1000 ms (1 second)
            n_intervals=0,  # Counter for number of updates
        ),
    ],
)

# Dummy Data Storage
latest_data = {"T": 0, "H": 0, "L": 0}

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
                        latest_data = {
                            kv.split(":")[0]: float(kv.split(":")[1]) for kv in pairs if ":" in kv
                        }
                        logging.info(f"Updated latest_data: {latest_data}")
    except Exception as e:
        logging.error(f"Error reading serial data: {e}")

# API for JSON data
@app.route("/data")
def get_data():
    return jsonify(latest_data)

# Dash App Callbacks for Dynamic Updates
@dash_app.callback(
    [dash.dependencies.Output("temperature-gauge", "value"),
     dash.dependencies.Output("humidity-gauge", "value"),
     dash.dependencies.Output("loop-counter", "children")],
    [dash.dependencies.Input("interval-component", "n_intervals")]  # Use the interval as input
)
def update_dashboard(n_intervals):
    # Perturb values slightly to ensure UI updates
    temperature = latest_data.get("T", 0) + 0.0001 * n_intervals
    humidity = latest_data.get("H", 0) + 0.0001 * n_intervals
    loop_count = int(latest_data.get("L", 0))

    # Add logging for debugging
    logging.info(f"Updating UI: T={temperature}, H={humidity}, L={loop_count}")
    
    return temperature, humidity, loop_count

# Start Serial Reader in Background Thread
Thread(target=read_serial_data, daemon=True).start()

if __name__ == "__main__":
    app.run(debug=True)
