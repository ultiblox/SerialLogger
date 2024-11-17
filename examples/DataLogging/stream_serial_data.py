import serial

def parse_data_line(line):
    """
    Parses a machine-readable line into a dictionary.
    """
    parsed_data = {}
    if line.startswith("D;"):  # Machine-readable format starts with 'D;'
        try:
            # Remove 'D;' and split into key-value pairs
            kv_pairs = line[2:].strip().split(';')
            for pair in kv_pairs:
                if ':' in pair:
                    key, value = pair.split(':', 1)
                    parsed_data[key] = value
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
            while True:
                # Read a line from the serial buffer
                line = ser.readline().decode('utf-8').strip()
                if line:
                    # Parse the line into a structured format
                    data = parse_data_line(line)
                    if data:
                        print(f"Snapshot: {data}")
    except serial.SerialException as e:
        print(f"Serial error: {e}")
    except KeyboardInterrupt:
        print("Exiting program.")

if __name__ == "__main__":
    main()