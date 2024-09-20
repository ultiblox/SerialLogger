// SimpleLogger Example
#include "LoggerConfig.h"
#include "SerialLogger.h"

int loopNumber = 1;

void setup() {
    Serial.begin(115200);
    Serial.println("Starting system...");
    LOG_INFO("Starting system...");
    LOG_WARN("This is a warning message.");
    LOG_ERROR("This is an error message.");
    LOG_DEBUG("This is a debug message.");
}

void loop() {
    LOG_INFO("Loop running...");

    LOG_DEBUG("Loop number: " + String(loopNumber));
    delay(1000);  // Simulate some work
    loopNumber++;
}


