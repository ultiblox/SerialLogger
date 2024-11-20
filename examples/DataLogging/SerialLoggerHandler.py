import serial
import threading
import logging

class SerialLoggerHandler:
    def __init__(self, port="/dev/ttyUSB0", baud_rate=115200, timeout=1, debug=False):
        """
        Initialize the SerialLoggerHandler with default configuration.
        """
        self.port = port
        self.baud_rate = baud_rate
        self.timeout = timeout
        self.serial_connection = None
        self.is_listening = False
        self.data_handler = None
        self.debug = debug

        # Configure logging
        logging.basicConfig(level=logging.DEBUG if self.debug else logging.INFO)
        self.logger = logging.getLogger("SerialLoggerHandler")

    def setPort(self, port):
        self.port = port
        self.logger.info(f"Serial port set to: {self.port}")

    def setBaudRate(self, baud_rate):
        self.baud_rate = baud_rate
        self.logger.info(f"Baud rate set to: {self.baud_rate}")

    def setCallback(self, callback):
        if not callable(callback):
            raise ValueError("Callback must be a callable function.")
        self.data_handler = callback
        self.logger.info("Callback function set successfully.")

    def _default_parse_data_line(self, line):
        parsed_data = {}
        if line.startswith("D;"):
            kv_pairs = line[2:].strip().split(";")
            for pair in kv_pairs:
                if ":" in pair:
                    key, value = pair.split(":", 1)
                    parsed_data[key] = value
        return parsed_data

    def _listen_for_serial_data(self):
        self.logger.info(f"Attempting to open serial connection on {self.port}.")
        try:
            with serial.Serial(self.port, self.baud_rate, timeout=self.timeout) as serial_conn:
                self.serial_connection = serial_conn
                if not serial_conn.is_open:
                    self.logger.error("Failed to open serial connection.")
                    return

                self.logger.info(f"Listening on {self.port} at {self.baud_rate} baud.")
                while self.is_listening:
                    try:
                        line = serial_conn.readline().decode("utf-8", errors="ignore").strip()
                        self.logger.debug(f"Raw data received: {line or '<empty>'}")
                        if not line:
                            continue  # Skip empty lines
                        parsed_data = self._default_parse_data_line(line)
                        if parsed_data:
                            self.logger.debug(f"Parsed data: {parsed_data}")
                            if self.data_handler:
                                self.data_handler(parsed_data)
                            else:
                                self.logger.warning("No data handler is set.")
                    except Exception as e:
                        self.logger.error(f"Error processing line: {e}")
        except serial.SerialException as e:
            self.logger.error(f"Serial error: {e}. Is the port in use?")
        except Exception as e:
            self.logger.error(f"Unexpected error: {e}")
        finally:
            self.serial_connection = None
            self.logger.info("Stopped listening.")

    def start(self):
        if self.is_listening:
            self.logger.warning("SerialLoggerHandler is already running.")
            return

        if not self.data_handler:
            raise ValueError("No callback function set. Use setCallback to configure a data handler.")

        self.is_listening = True
        threading.Thread(target=self._listen_for_serial_data, daemon=True).start()
        self.logger.info("SerialLoggerHandler started.")

    def stop(self):
        if not self.is_listening:
            self.logger.warning("SerialLoggerHandler is not running.")
            return

        self.is_listening = False
        if self.serial_connection:
            self.serial_connection.close()
        self.logger.info("SerialLoggerHandler has stopped.")