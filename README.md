# SerialLogger Library

[UltiBlox on GitHub](https://github.com/UltiBlox/SerialLogger) | [UltiBlox Home](https://ultiblox.org)

## Overview

`SerialLogger` is an open-source Arduino library for structured data logging and debugging. It supports multiple log levels and output formats, making it easy to log information from your Arduino and integrate with external systems.

Core features:
- Configurable log levels: `DEBUG`, `INFO`, `DATA`.
- Flexible output formats: human-readable or machine-readable.
- Simple integration with tools like Python for data parsing.

---

## Quick Start

### Cloning the Repository
To clone the library, run:
```bash
git clone git@github.com:UltiBlox/SerialLogger.git
cd SerialLogger
```

### Installation
Run the installation script to set up the library:
```bash
bash install.sh
```

For development use:
```bash
bash install-symlink.sh
```

### Basic Configuration
Control logging behavior by setting the log level and format in your sketch:
```cpp
// Set log level
#define LOG_LEVEL LOG_LEVEL_DATA

// Set log format
#define LOG_FORMAT LOG_FORMAT_MACHINE

#include "SerialLogger.h"
```

### Running an Example
1. Open one of the example sketches (e.g., `DataLogging.ino`) in the Arduino IDE.
2. Upload it to your Arduino.
3. View the output in the Serial Monitor.
4. If using the `DataLogging` example, parse the output with the [stream_data.py script](docs/python-integration.md).

---

## Examples

The library includes several examples to get you started:
- **DataLogging**: Logs structured data for Python parsing. See the [Python Integration Guide](docs/python-integration.md) for details.
- **DebugLogging**: Logs debug messages for troubleshooting.
- **InfoLogging**: Logs essential information for production.

Detailed descriptions are available in the [examples documentation](docs/examples.md).

---

## API Reference

### Core Methods
- `Logger.data(label, key, value)`: Logs a key-value pair.
- `Logger.dataln()`: Ends the current log line.
- `Logger.info(message)`: Logs an info-level message.
- `Logger.debug(message)`: Logs a debug-level message.
- `Logger.print(message)`: Directly outputs a message to the serial console.
- `Logger.println(message)`: Outputs a message with a newline.

For more details, see the [Configuration Guide](docs/configuration.md).

---

## Next Steps

Explore the following resources for more details:
- [Configuration Options](docs/configuration.md)
- [Key-Value Pair Structure](docs/key-value-pairs.md)
- [Python Integration](docs/python-integration.md)
- [Examples](docs/examples.md)
- [Installation and Development](docs/installation.md)

---

## License

[This project is licensed under the UltiBlox License.](https://ultiblox.org/license)
