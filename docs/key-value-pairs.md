# Key-Value Pair Structure

`SerialLogger` uses key-value pairs to represent structured data for compact and efficient communication. This system makes it easy to parse data in external applications while maintaining flexibility.

## Anatomy of a Log Line
A typical log line looks like this:
```
D;T:24.5;H:60.1;L:3;
```

- `D`: Marker for a data log line.
- `T:24.5`: `T` (key) represents "Temperature," and `24.5` is the value.
- `H:60.1`: `H` (key) represents "Humidity," and `60.1` is the value.
- `L:3`: `L` (key) represents "Loop Count," and `3` is the value.

## Keys in Action

### In the Arduino Sketch

Keys are defined in `Logger.data()` calls:
```cpp
Logger.data("Temperature", "T", temperature);
Logger.data("Humidity", "H", humidity);
```
- **Human-Readable Label**: Used for `LOG_FORMAT_HUMAN`, which outputs logs like:
  ```
  Temperature: 24.5
  Humidity: 60.1
  Loop Count: 3
  ```
- **Key**: Used for `LOG_FORMAT_MACHINE`, which outputs structured logs like:
  ```
  D;T:24.5;H:60.1;L:3;
  ```

### In External Applications

The keys (`T`, `H`, `L`) are mapped to human-readable labels for display or further processing:
```python
key_mapping = {
    "T": "Temperature (°C)",
    "H": "Humidity (%)",
    "L": "Loop Count"
}
```

## Debugging Tips

- **Malformed Logs**: Ensure keys and values are properly paired in `Logger.data()` calls.
- **Missing Data**: Verify `Logger.dataln()` is called after all `Logger.data()` calls to complete the log line.
- **Serial Output Check**: Use the Arduino Serial Monitor to confirm log output matches expectations.

## Why Use Key-Value Pairs?
- **Compact**: Minimizes bandwidth by transmitting only essential identifiers.
- **Readable**: Adapts to both human-readable and machine-readable formats.
- **Flexible**: Easily extendable with new keys and values.

---

For additional examples and integration tips, see [Python Integration](python-integration.md).