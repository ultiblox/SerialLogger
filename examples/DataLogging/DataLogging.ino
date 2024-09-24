// Configure the log level
#define LOG_LEVEL LOG_LEVEL_DATA // DATA logging level
//#define LOG_LEVEL LOG_LEVEL_INFO // INFO logging level
//#define LOG_LEVEL LOG_LEVEL_DEBUG // DEBUG logging level

// Configure the log format
//#define LOG_FORMAT LOG_FORMAT_HUMAN // Human readable
#define LOG_FORMAT LOG_FORMAT_MACHINE // Machine readable

#include "SerialLogger.h"

SerialLogger Logger;

int loopNumber = 1;

void setup() {
    Logger.init(115200);

    Logger.data("Temperature", "T", 24.8);
    Logger.data("Humidity", "H", 58.7);
    Logger.dataln();
}

void loop() {
    Logger.data("Temperature", "T", 24.5);
    Logger.data("Humidity", "H", 60.1);
    Logger.data("Loop", "L", loopNumber);
    Logger.dataln();

    loopNumber++;

    delay(1000);
}
