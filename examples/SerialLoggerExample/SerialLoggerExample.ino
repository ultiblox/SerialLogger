#include "SerialLogger.h"

// Define the Logger instance here
SerialLogger Logger;

int loopNumber = 1;

void setup() {
    Logger.init(115200);  // Initialize Serial communication
    Logger.logln("Starting system...");

    Logger.logln("This is an info message.");
    Logger.logln("This is a warning message.");
    Logger.logln("This is an error message.");
    Logger.logln("This is a debug message.");
}

void loop() {
    Logger.log("Loop running... ");
    Logger.logln(loopNumber);

    delay(1000);  // Simulate some work
    loopNumber++;
}
