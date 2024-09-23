#ifndef _SERIALLOGGER_H
#define _SERIALLOGGER_H

#include <Arduino.h>

// Enable or disable logging at compile time
#ifndef SERIAL_LOGGER_ENABLED
    #define SERIAL_LOGGER_ENABLED 1  // Set to 0 to disable all logging
#endif

class SerialLogger {
public:
    // Initialize Serial if needed
    void init(long baudRate = 115200) {
        Serial.begin(baudRate);
        while (!Serial) { ; }  // Wait for Serial to be ready
    }

    // Logging functions (enabled/disabled based on SERIAL_LOGGER_ENABLED)
    template<typename T>
    void log(T content) {
        if (SERIAL_LOGGER_ENABLED) {
            Serial.print(content);
        }
    }

    template<typename T>
    void logln(T content) {
        if (SERIAL_LOGGER_ENABLED) {
            Serial.println(content);
        }
    }

    // Print functions (always work like Serial.print/println, regardless of logging flag)
    template<typename T>
    void print(T content) {
        Serial.print(content);
    }

    template<typename T>
    void println(T content) {
        Serial.println(content);
    }
    
    // Overloaded versions for multiple data types
    template<typename T1, typename T2>
    void log(T1 content1, T2 content2) {
        if (SERIAL_LOGGER_ENABLED) {
            Serial.print(content1);
            Serial.print(content2);
        }
    }

    template<typename T1, typename T2>
    void logln(T1 content1, T2 content2) {
        if (SERIAL_LOGGER_ENABLED) {
            Serial.print(content1);
            Serial.println(content2);
        }
    }

    template<typename T1, typename T2>
    void print(T1 content1, T2 content2) {
        Serial.print(content1);
        Serial.print(content2);
    }

    template<typename T1, typename T2>
    void println(T1 content1, T2 content2) {
        Serial.print(content1);
        Serial.println(content2);
    }
};

// Declare Logger as an external variable
extern SerialLogger Logger;

#endif  // _SERIALLOGGER_H
