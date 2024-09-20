// SerialLogger.h
#ifndef SERIAL_LOGGER_H
#define SERIAL_LOGGER_H

#include <Arduino.h>

#if SERIAL_LOGGER_ENABLED

// Updated macros without F(msg)
#define LOG_INFO(msg)  \
  Serial.print(F("[INF] ")); \
  Serial.print(F("Line ")); \
  Serial.print(__LINE__); \
  Serial.print(F(" - ")); \
  Serial.println(msg)

#define LOG_WARN(msg)  \
  Serial.print(F("[WRN] ")); \
  Serial.print(F("Line ")); \
  Serial.print(__LINE__); \
  Serial.print(F(" - ")); \
  Serial.println(msg)

#define LOG_ERROR(msg) \
  Serial.print(F("[ERR] ")); \
  Serial.print(F("Line ")); \
  Serial.print(__LINE__); \
  Serial.print(F(" - ")); \
  Serial.println(msg)

#define LOG_DEBUG(msg) \
  Serial.print(F("[DBG] ")); \
  Serial.print(F("Line ")); \
  Serial.print(__LINE__); \
  Serial.print(F(" - ")); \
  Serial.println(msg)

#else

// Empty macros when logging is disabled
#define LOG_INFO(msg)
#define LOG_WARN(msg)
#define LOG_ERROR(msg)
#define LOG_DEBUG(msg)

#endif // SERIAL_LOGGER_ENABLED

#endif // SERIAL_LOGGER_H

