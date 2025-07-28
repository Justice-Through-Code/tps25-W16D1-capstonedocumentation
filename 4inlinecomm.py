# Inline Comments Best Practices:

"While docstrings document the 'what' and 'why', inline comments explain complex 'how' details:"

def calculate_heat_index(temperature: float, humidity: float) -> float:
    """Calculate the heat index (feels-like temperature) using NOAA formula."""
    # Heat index is only valid for temperatures 80°F and above
    if temperature < 80:
        return temperature
    
    # Rothfusz regression formula constants
    # Source: https://www.wpc.ncep.noaa.gov/html/heatindex_equation.shtml
    c1 = -42.379
    c2 = 2.04901523
    c3 = 10.14333127
    c4 = -0.22475541
    c5 = -0.00683783
    c6 = -0.05481717
    c7 = 0.00122874
    c8 = 0.00085282
    c9 = -0.00000199
    
    # Calculate heat index using Rothfusz regression
    heat_index = (c1 + (c2 * temperature) + (c3 * humidity) + 
                  (c4 * temperature * humidity) + (c5 * temperature**2) + 
                  (c6 * humidity**2) + (c7 * temperature**2 * humidity) + 
                  (c8 * temperature * humidity**2) + 
                  (c9 * temperature**2 * humidity**2))
    
    # Apply adjustments for extreme conditions
    if humidity < 13 and 80 <= temperature <= 112:
        # Low humidity adjustment
        adjustment = ((13 - humidity) / 4) * \
                    ((17 - abs(temperature - 95)) / 17) ** 0.5
        heat_index -= adjustment
    elif humidity > 85 and 80 <= temperature <= 87:
        # High humidity adjustment
        adjustment = ((humidity - 85) / 10) * ((87 - temperature) / 5)
        heat_index += adjustment
    
    return round(heat_index, 1)

"Notice how comments explain the algorithm source, formula purpose, and adjustment rationale."
