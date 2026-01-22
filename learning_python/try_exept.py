temperature_sensor = None

try:
    current_temp = temperature_sensor.read()
    print(f"Current Temperature: {current_temp}")
except AttributeError:
    print("Error: Sensor not connected. Switching to backup sensor.")