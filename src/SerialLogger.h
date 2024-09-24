#ifndef _SERIALLOGGER_H
#define _SERIALLOGGER_H

#include <Arduino.h>

// Define log levels
#define LOG_LEVEL_NONE  0   // No logging
#define LOG_LEVEL_DATA  1   // Only data logs
#define LOG_LEVEL_INFO  2   // Standard logs and data logs
#define LOG_LEVEL_DEBUG 3   // All logs (debug, info, data)

// Set the desired log level (default is DEBUG)
#ifndef LOG_LEVEL
    #define LOG_LEVEL LOG_LEVEL_DEBUG
#endif

// Define output formats
#define LOG_FORMAT_HUMAN   1  // Human-readable output
#define LOG_FORMAT_MACHINE 0  // Machine-readable output

// Set the default log format (default is HUMAN)
#ifndef LOG_FORMAT
    #define LOG_FORMAT LOG_FORMAT_HUMAN
#endif

class SerialLogger {
private:
    bool firstDataEntry = true;  // Track the first data entry in machine-readable mode

public:
    // Initialize Serial
    void init(long baudRate = 115200) {
        Serial.begin(baudRate);
        while (!Serial) { ; }  // Wait for Serial to be ready
    }

    // Debug logging (only if log level is DEBUG)
    template<typename T>
    void debug(T content) {
        #if LOG_LEVEL >= LOG_LEVEL_DEBUG
            Serial.print(content);
        #endif
    }

    template<typename T>
    void debugln(T content) {
        #if LOG_LEVEL >= LOG_LEVEL_DEBUG
            Serial.println(content);
        #endif
    }

    // Info logging (only if log level is INFO or higher)
    template<typename T>
    void info(T content) {
        #if LOG_LEVEL >= LOG_LEVEL_INFO
            Serial.print(content);
        #endif
    }

    template<typename T>
    void infoln(T content) {
        #if LOG_LEVEL >= LOG_LEVEL_INFO
            Serial.println(content);
        #endif
    }

    // Data logging with both friendly label and short key (only if log level is DATA or higher)
    template<typename T>
    void data(const char* friendlyLabel, const char* shortKey, T value) {
        #if LOG_LEVEL >= LOG_LEVEL_DATA
            #if LOG_FORMAT == LOG_FORMAT_HUMAN
                // Human-readable output: FriendlyLabel: value
                Serial.print(friendlyLabel);
                Serial.print(": ");
                Serial.println(value);
            #elif LOG_FORMAT == LOG_FORMAT_MACHINE
                // Machine-readable output: Start line with 'D;' and append key:value;
                if (firstDataEntry) {
                    Serial.print("D;");  // Start of data line
                    firstDataEntry = false;  // Reset after first entry
                }
                Serial.print(shortKey);
                Serial.print(":");
                Serial.print(value);
                Serial.print(";");
            #endif
        #endif
    }

    // Finalize the line for data logging
    void dataln() {
        #if LOG_LEVEL >= LOG_LEVEL_DATA
            #if LOG_FORMAT == LOG_FORMAT_MACHINE
                Serial.println();  // Complete the machine-readable line
                firstDataEntry = true;  // Reset for the next data sequence
            #endif
        #endif
    }

    // Print functions (always enabled, regardless of log level)
    template<typename T>
    void print(T content) {
        Serial.print(content);
    }

    template<typename T>
    void println(T content) {
        Serial.println(content);
    }
};

// Declare Logger as an external variable
extern SerialLogger Logger;

#endif  // _SERIALLOGGER_H
