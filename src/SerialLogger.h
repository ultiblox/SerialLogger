// SerialLogger.h (modified)
#if SIMPLE_LOGGER_ENABLED

#define LOG_INFO(msg)    Serial.print("[INFO] "); Serial.print(__FILE__); Serial.print(":"); Serial.print(__LINE__); Serial.print(" - "); Serial.println(msg)
#define LOG_WARN(msg)    Serial.print("[WARN] "); Serial.print(__FILE__); Serial.print(":"); Serial.print(__LINE__); Serial.print(" - "); Serial.println(msg)
#define LOG_ERROR(msg)   Serial.print("[ERROR] "); Serial.print(__FILE__); Serial.print(":"); Serial.print(__LINE__); Serial.print(" - "); Serial.println(msg)
#define LOG_DEBUG(msg)   Serial.print("[DEBUG] "); Serial.print(__FILE__); Serial.print(":"); Serial.print(__LINE__); Serial.print(" - "); Serial.println(msg)

#else

// Empty macros when logging is disabled
#define LOG_INFO(msg)
#define LOG_WARN(msg)
#define LOG_ERROR(msg)
#define LOG_DEBUG(msg)

#endif // SIMPLE_LOGGER_ENABLED
