from SerialLoggerHandler import SerialLoggerHandler

def handle_data_received(data):
    print("=== Data Received ===")
    for key, value in data.items():
        print(f"{key}: {value}")
    print("=====================")

logger_handler = SerialLoggerHandler(debug=True)

logger_handler.setPort("/dev/ttyUSB0")
logger_handler.setBaudRate(115200)
logger_handler.setCallback(handle_data_received)

try:
    logger_handler.start()
except Exception as e:
    print(f"An error occurred: {e}")

# To stop manually if needed:
# logger_handler.stop()