# Python Integration

The `stream_data.py` script is designed to parse and process data from your Arduino. Follow these steps to get started.

## Getting Started

### Prepare Your Environment

1. **Install Python 3.x**:
   - Ensure you have Python 3.x installed on your system.

2. **Install Required Libraries**:
   - Install the `pyserial` library by running:
     ```bash
     pip install pyserial
     ```

### Upload the Arduino Sketch

1. Open the `DataLogging.ino` sketch in the Arduino IDE.
2. Select the correct board and port in the Arduino IDE.
3. Upload the sketch to your Arduino.

### Run the Script

1. Connect your Arduino to your computer via USB.
2. Copy the [stream_data.py](../examples/DataLogging/stream_data.py) script to a folder of your choice
3. Run the Python script:
   ```bash
   python3 stream_data.py
   ```
4. View the parsed data in your terminal:
   ```
   === Data Snapshot ===
   Temperature: 24.5°C
   Humidity: 60.1%
   Loop Count: 3
   =====================
   ```

---

## Understanding the Data

The Arduino sends data in a structured format, using key-value pairs. Each key represents a specific measurement:

| Key | Human-Readable Label | Example Value |
|-----|-----------------------|---------------|
| `T` | Temperature (°C)      | `24.5`        |
| `H` | Humidity (%)          | `60.1`        |
| `L` | Loop Count            | `3`           |

The `stream_data.py` script parses these key-value pairs and displays them in a human-readable format.

---

## Customizing the Script

You can modify the [stream_data.py](../examples/DataLogging/stream_data.py) script to handle data in a way that suits your needs. Custom logic can be added to the `process_data()` function.

### Adding Your Logic

Edit the `process_data()` function to include your logic. Here are some examples:

- **Send Data to a Server**:
  ```python
  import requests
  requests.post(SERVER_URL, json=data)  # Replace SERVER_URL with your endpoint
  ```

- **Save Data to a File**:
  ```python
  with open("output.csv", "a") as f:
      f.write(",".join(data.values()) + "\n")
  ```

- **Trigger an Alert**:
  ```python
  if "T" in data and float(data["T"]) > 30:
      print("Alert: Temperature exceeds 30°C!")
  ```

For more advanced examples, see the [Examples Guide](examples.md).

---

## Troubleshooting

- **No Data Received**:
  - Ensure the correct port is specified in the script (e.g., `/dev/ttyUSB0` or `COM3`).
  - Check that the Arduino sketch is uploaded and running.

- **Incorrect Data**:
  - Verify that the Arduino is using the same baud rate as the script (e.g., `115200`).

- **Serial Port Errors**:
  - Ensure no other application (e.g., Serial Monitor) is using the port.
