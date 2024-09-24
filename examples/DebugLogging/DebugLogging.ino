// Configure the log level
//#define LOG_LEVEL LOG_LEVEL_DATA // DATA logging level
//#define LOG_LEVEL LOG_LEVEL_INFO // INFO logging level
#define LOG_LEVEL LOG_LEVEL_DEBUG // DEBUG logging level

// Configure the log format
#define LOG_FORMAT LOG_FORMAT_HUMAN // Human readable
//#define LOG_FORMAT LOG_FORMAT_MACHINE // Machine readable

#include "SerialLogger.h"

SerialLogger Logger;

int loopNumber = 1;

void setup() {
    Logger.init(115200);

    Logger.debugln("[DEBUG] System starting...");

    Logger.infoln("[INFO] System initialized and running");

    Logger.data("Temperature", "T", 25.4);
    Logger.data("Humidity", "H", 60.2);
    Logger.dataln();
}

void loop() {
    Logger.debug("[DEBUG] Loop number: ");
    Logger.debugln(loopNumber);

    Logger.data("Temperature", "T", 24.8);
    Logger.data("Humidity", "H", 58.7);
    Logger.dataln();

    delay(1000);
    loopNumber++;
}
