from SerialLoggerHandler import SerialLoggerHandler

# Friendly labels for the data keys
key_labels = {
    "T": "Temperature (°C)",
    "H": "Humidity (%)",
    "L": "Loop Count"
}

def handle_data_received(data):
    """Process and display received data with friendly labels."""
    output = []
    for key, value in data.items():
        label = key_labels.get(key, key)  # Use friendly labels if available
        output.append(f"{label}: {value}")
    print("\n".join(output))  # Print each key-value pair on a new line
    print()  # Add a blank line for spacing

# Create and configure the logger handler
logger_handler = SerialLoggerHandler(debug=False)
#logger_handler.setPort("/dev/ttyUSB0")
logger_handler.detectPort()
logger_handler.setBaudRate(115200)
logger_handler.setCallback(handle_data_received)

# Start the handler
try:
    print("Streaming serial data...\n")  
    logger_handler.start()
    print("Press Ctrl+C to stop the stream...\n")  
    while True:
        pass
except KeyboardInterrupt:
    print("Stopping the stream...")
    logger_handler.stop()
    print("Stream stopped.")
