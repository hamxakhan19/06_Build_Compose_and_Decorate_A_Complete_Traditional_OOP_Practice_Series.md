class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32

# Example
print(TemperatureConverter.celsius_to_fahrenheit(25))
