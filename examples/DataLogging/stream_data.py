import serial

# Key mapping for human-readable labels
key_mapping = {
    "T": "Temperature (°C)",
    "H": "Humidity (%)",
    "L": "Loop Count"
}

def parse_data_line(line):
    """
    Parse a single line of serial data into key-value pairs.
    :param line: Raw serial data line from Arduino
    :return: Dictionary of parsed key-value pairs
    """
    parsed_data = {}
    if line.startswith("D;"):  # Check for data line marker
        kv_pairs = line[2:].strip().split(';')  # Remove prefix and split key-value pairs
        for pair in kv_pairs:
            if ':' in pair:  # Ensure key-value format
                key, value = pair.split(':', 1)
                parsed_data[key] = value
    return parsed_data

def process_data(data):
    """
    Example function to handle parsed data.
    :param data: Dictionary of parsed key-value pairs
    """
    # Extract specific variables
    temperature = data.get("T")
    humidity = data.get("H")
    loop_count = data.get("L")

    # Print data snapshot
    print("=== Data Snapshot ===")
    if temperature:
        print(f"Temperature: {temperature}°C")
    if humidity:
        print(f"Humidity: {humidity}%")
    if loop_count:
        print(f"Loop Count: {loop_count}")
    print("=====================")

    # === User Customization Area ===
    # Add your own code here to work with the data.

    # Example: Publish to an API
    # import requests
    # requests.post("http://your-api.com/data", json=data)

    # Example: Save to a file
    # with open("data_log.csv", "a") as f:
    #     f.write(",".join(data.values()) + "\n")

def main():
    """
    Main loop to read and process data from the serial port.
    """
    port = "/dev/ttyUSB0"  # Update to your serial port
    baud_rate = 115200  # Ensure this matches the Arduino sketch

    try:
        with serial.Serial(port, baud_rate, timeout=1) as ser:
            print(f"Listening on {port} at {baud_rate} baud...")
            while True:
                line = ser.readline()  # Read raw bytes
                try:
                    line = line.decode("utf-8", errors="ignore").strip()  # Decode with error handling
                except UnicodeDecodeError:
                    print("Warning: Received non-UTF-8 data, skipping line.")
                    continue  # Skip to the next iteration

                if line:  # If line is not empty
                    try:
                        parsed_data = parse_data_line(line)
                        process_data(parsed_data)  # Pass parsed data to user-defined function
                    except Exception as e:
                        print(f"Error processing data: {e}")
    except serial.SerialException as e:
        print(f"Serial error: {e}")
    except KeyboardInterrupt:
        print("Exiting program.")

if __name__ == "__main__":
    main()