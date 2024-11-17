# Installation Guide

Follow these steps to install the `SerialLogger` library for use in your Arduino projects.

## Standard Installation

Use the provided script to install the library:
```bash
bash install.sh
```

This command copies the library files to your Arduino libraries directory.

---

## Development Installation (Symlink)

For active development, create a symlink to the library instead of copying files:
```bash
bash install-symlink.sh
```

This allows you to edit the library directly without needing to reinstall it after changes.

---

## Building the Library

To compile the example sketches:
```bash
bash build.sh
```
This verifies that the library is correctly installed and functional.

---

For additional support, refer to the [official Arduino documentation](https://www.arduino.cc/reference/en/).