# Examples

`SerialLogger` comes with several example sketches to demonstrate its functionality. Below is an overview of each example and its key features.

## DataLogging
Logs sensor data in a machine-readable format. Ideal for structured logging and integration with external tools like Python.

### Key Features
- Uses `LOG_LEVEL_DATA` for concise data-only logging.
- Configured for `LOG_FORMAT_MACHINE` to produce structured output.
- Includes a complementary Python script ([stream_data.py](python-integration.md)) to parse the logs.

### Example Output
```
D;T:24.5;H:60.1;L:3;
```

See the [Python Integration Guide](python-integration.md) for details on parsing this data.

---

## DebugLogging
Demonstrates how to use debug-level logs to troubleshoot your Arduino code with detailed messages.

### Key Features
- Uses `LOG_FORMAT_HUMAN` for readability.
- Logs debug, info, and data messages for development.

### Example Output
```
[DEBUG] Starting system...
Temperature: 24.5
Humidity: 60.1
```

---

## InfoLogging
Logs only essential information and sensor data. Useful for reducing verbosity in production systems.

### Key Features
- Uses `LOG_LEVEL_INFO` to suppress debug messages.
- Provides concise logs for important updates.

### Example Output
```
[INFO] System running...
Temperature: 24.5
Humidity: 60.1
```