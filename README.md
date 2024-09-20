# SerialLogger Library

## Overview
The `SerialLogger` library provides a lightweight, easy-to-use logging mechanism for Arduino. It allows you to log messages with different severity levels (INFO, WARN, ERROR) using configurable macros.

## Features
- Simple logging macros (INFO, WARN, ERROR).
- Configurable enable/disable flags to control output.
- Lightweight and optimized for resource-constrained environments.

## Installation

### 1. Standard Installation (Copy)
To install the library by copying it to the Arduino libraries folder, run the following command:
```bash
bash install.sh
```
This will copy the library to the Arduino libraries folder at `~/Arduino/libraries/SerialLogger`.

### 2. Development Installation (Symlink)
If you are actively developing the library and want to create a symbolic link instead of copying the files, run:
```bash
bash install-symlink.sh
```
This will create a symlink from your current workspace to the Arduino libraries folder, so any changes you make in the workspace will reflect immediately in the Arduino IDE.

## Building the Library
You can compile the example sketches using the **`build.sh`** script:
```bash
bash build.sh
```
This script uses the Arduino CLI to compile all the example sketches in the library.

## Preparing the Environment
If you don't have Arduino CLI installed, you can install it using the **`prepare.sh`** script:
```bash
bash prepare.sh
```
This script will install the latest version of Arduino CLI to your system or user directory.

## License
This library is open source, distributed under the MIT License.