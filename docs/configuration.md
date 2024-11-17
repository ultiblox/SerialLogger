# Configuration Guide

## Log Levels

Control the verbosity of the logging output using the following log levels:

| Macro               | Description                            |
|---------------------|----------------------------------------|
| `LOG_LEVEL_DEBUG`   | Logs everything (debug, info, data).   |
| `LOG_LEVEL_INFO`    | Logs info and data messages only.      |
| `LOG_LEVEL_DATA`    | Logs data messages only.               |
| `LOG_LEVEL_NONE`    | Disables all logging.                  |

### Example Usage
```cpp
// Uncomment the desired log level
//#define LOG_LEVEL LOG_LEVEL_DEBUG
//#define LOG_LEVEL LOG_LEVEL_INFO
#define LOG_LEVEL LOG_LEVEL_DATA
```

## Log Formats

Choose between human-readable or machine-readable formats:

| Macro               | Description                            |
|---------------------|----------------------------------------|
| `LOG_FORMAT_HUMAN`  | Outputs human-readable logs.           |
| `LOG_FORMAT_MACHINE`| Outputs machine-readable logs.         |

### Example Usage
```cpp
// Uncomment the desired log format
//#define LOG_FORMAT LOG_FORMAT_HUMAN
#define LOG_FORMAT LOG_FORMAT_MACHINE
```

### Behavior in Examples
- **Human-Readable Format (`LOG_FORMAT_HUMAN`)**:
  Outputs user-friendly text logs, e.g.,:
  ```
  Temperature: 24.5
  Humidity: 60.1
  Loop Count: 3
  ```
- **Machine-Readable Format (`LOG_FORMAT_MACHINE`)**:
  Outputs compact, structured logs for parsing, e.g.,:
  ```
  D;T:24.5;H:60.1;L:3;
  ```

## Direct Printing

Use the `print` and `println` methods for direct output to the serial console, independent of log levels:
```cpp
Logger.print("Always enabled message.");
Logger.println("This is directly printed to Serial.");
```

These calls are unaffected by log levels or formats.

---

For further configuration options and API usage, see the [README](../README.md).