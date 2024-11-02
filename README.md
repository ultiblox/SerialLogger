# SerialLogger Library

## Overview

The `SerialLogger` library provides a lightweight, configurable logging system for Arduino projects. It supports different log levels, flexible output formats, and simple direct printing to the serial port.

### Key Features:

- **Log levels**: `DEBUG`, `INFO`, and `DATA`, allowing you to control the verbosity of logs.
- **Log formats**: Human-readable or machine-readable, ideal for structured logging.
- **Direct printing**: Use `print` and `println` for direct output to `Serial` that is always enabled.

## Installation

### Standard Installation

To install the library, run:

```bash
bash install.sh
```

### Development Installation (Symlink)

For active development:

```bash
bash install-symlink.sh
```

## Building the Library

Compile the example sketches with:

```bash
bash build.sh
```

## Examples

The library includes the following example sketches:

- **`DebugLogging.ino`**: Logs debug, info, and data in human-readable format.
- **`InfoLogging.ino`**: Logs only info and data, without debug messages.
- **`DataLogging.ino`**: Logs data in a machine-readable format for structured output.

## Log Levels

You can control the verbosity of logs by setting the log level before including `SerialLogger.h`:

```cpp
#define LOG_LEVEL LOG_LEVEL_DEBUG  // Logs everything: debug, info, data
#define LOG_LEVEL LOG_LEVEL_INFO   // Logs only info and data, skips debug
#define LOG_LEVEL LOG_LEVEL_DATA   // Logs only data
#include "SerialLogger.h"
```

### Example Usage:

- **Debug Level**:
  
  ```cpp
  Logger.debugln("This is a debug message.");
  ```

- **Info Level**:
  
  ```cpp
  Logger.infoln("System is running.");
  ```

- **Data Logging**:
  
  ```cpp
  Logger.data("Temperature", "T", 25.4);
  Logger.dataln();  // Finalize the data line
  ```

## Log Formats

You can choose between human-readable and machine-readable formats:

```cpp
#define LOG_FORMAT LOG_FORMAT_HUMAN   // Human-readable format
#define LOG_FORMAT LOG_FORMAT_MACHINE // Machine-readable format
#include "SerialLogger.h"
```

### Example Outputs:

- **Human-readable**:
  
  ```c
  Temperature: 25.40
  Humidity: 60.10
  ```

- **Machine-readable**:
  
  ```c
  D;T:25.40;H:60.10;
  ```

## Direct Printing

The `print` and `println` methods allow direct output to `Serial`:

```cpp
Logger.print("Always enabled message.");
Logger.println("This is directly printed to Serial.");
```

- **Note**: These calls are **not disableable**. For logs you want to control with log levels, use `info` or `debug`.


## License
[This project is licensed under the UltiBlox License.](https://ultiblox.org/license)