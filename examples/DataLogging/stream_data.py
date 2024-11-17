import serial

# Mapping of short keys to human-readable labels
key_mapping = {
    "T": "Temperature (°C)",
    "H": "Humidity (%)",
    "L": "Loop Count"
}

def parse_data_line(line):
    """
    Parses a machine-readable line into a dictionary with human-readable labels.
    """
    parsed_data = {}
    if line.startswith("D;"):  # Only process machine-readable lines
        try:
            # Remove 'D;' and split into key-value pairs
            kv_pairs = line[2:].strip().split(';')
            for pair in kv_pairs:
                if ':' in pair:
                    key, value = pair.split(':', 1)
                    # Map short key to human-readable label if available
                    readable_key = key_mapping.get(key, key)
                    parsed_data[readable_key] = value
        except Exception as e:
            print(f"Error parsing line: {e}")
    return parsed_data

def main():
    # Configure the serial connection
    port = "/dev/ttyUSB0"  # Update this to match your Arduino's port
    baud_rate = 115200

    try:
        with serial.Serial(port, baud_rate, timeout=1) as ser:
            print(f"Connected to {port} at {baud_rate} baud.")
            print("Waiting for data...\n")

            while True:
                # Read a line from the serial buffer
                line = ser.readline().decode('utf-8').strip()
                if line:
                    # Parse the line
                    data = parse_data_line(line)
                    if data:
                        # Display the data in a clean format
                        print("=== Data Snapshot ===")
                        for key, value in data.items():
                            print(f"{key}: {value}")
                        print("=====================\n")
    except serial.SerialException as e:
        print(f"Serial error: {e}")
    except KeyboardInterrupt:
        print("Exiting program.")

if __name__ == "__main__":
    main()