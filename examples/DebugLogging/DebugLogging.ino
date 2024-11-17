// Example: DebugLogging with Python Integration
// Demonstrates debug messages and structured data logging.

#define LOG_LEVEL LOG_LEVEL_DEBUG // Enable debug logging
#define LOG_FORMAT LOG_FORMAT_MACHINE // Use machine-readable format

#include "SerialLogger.h"

SerialLogger Logger;

int loopCounter = 0;

void setup() {
    Logger.init(115200); // Initialize logger with baud rate

    Logger.debugln("[DEBUG] System starting...");
    Logger.infoln("[INFO] System initialized and running");

    // Initial data logs
    Logger.data("StartupMessage", "MSG", "Arduino Started");
    Logger.dataln();
}

void loop() {
    // Simulated sensor data
    float temperature = random(20, 30) + random(0, 10) / 10.0;
    float humidity = random(40, 60) + random(0, 10) / 10.0;
    unsigned long timestamp = millis();

    // Debugging log
    Logger.debug("[DEBUG] Loop number: ");
    Logger.debugln(loopCounter);

    // Structured data logs
    Logger.data("Temperature", "T", temperature);
    Logger.data("Humidity", "H", humidity);
    Logger.data("Timestamp", "TS", timestamp);
    Logger.data("LoopCount", "LC", loopCounter);
    Logger.dataln();

    loopCounter++;
    delay(1000); // Delay for 1 second
}