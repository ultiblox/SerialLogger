// SimpleLogger Example
#include "LoggerConfig.h"
#include "SerialLogger.h"

void setup() {
    Serial.begin(115200);
    LOG_INFO("Starting system...");
    LOG_WARN("This is a warning message.");
    LOG_ERROR("This is an error message.");
    LOG_DEBUG("This is a debug message.");
}

void loop() {
    LOG_INFO("Loop running...");
    delay(1000);  // Simulate some work
}

