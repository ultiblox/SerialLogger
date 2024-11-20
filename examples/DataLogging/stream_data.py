from SerialLoggerHandler import SerialLoggerHandler

def handle_data_received(data):
    print("=== Data Received ===")
    for key, value in data.items():
        print(f"{key}: {value}")
    print("=====================")

logger_handler = SerialLoggerHandler(debug=False)

logger_handler.setPort("/dev/ttyUSB0")
logger_handler.setBaudRate(115200)
logger_handler.setCallback(handle_data_received)

try:
    logger_handler.start()
    print("Press Ctrl+C to stop the logger...")
    while True:  # Keep the script running
        pass
except KeyboardInterrupt:
    print("Stopping the logger...")
    logger_handler.stop()
    print("Logger stopped.")

