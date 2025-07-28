# Writing Effective Docstrings:

# "Python's docstring conventions provide a standardized way to document your code. Let's look at best practices:"

def fetch_weather_data(location: str, units: str = "imperial", 
                      include_forecast: bool = False) -> dict:
    """
    Fetch current weather data for a specified location.
    
    This function retrieves weather information from the configured weather API,
    processes the response, and returns formatted weather data. It handles
    various error cases including network failures and invalid locations.
    
    Args:
        location (str): The location to fetch weather for. Can be:
            - City name (e.g., "New York")
            - ZIP code (e.g., "10001")
            - Coordinates (e.g., "40.7128,-74.0060")
        units (str, optional): Unit system for measurements. Options:
            - "imperial": Fahrenheit, mph, inHg (default)
            - "metric": Celsius, km/h, hPa
            - "kelvin": Kelvin, m/s, hPa
        include_forecast (bool, optional): Whether to include forecast data.
            Defaults to False.
    
    Returns:
        dict: Weather data containing:
            - 'location': Formatted location name
            - 'current': Current conditions (temperature, humidity, etc.)
            - 'forecast': 5-day forecast (if include_forecast=True)
            - 'timestamp': When data was fetched
    
    Raises:
        APIError: If the weather API returns an error
        NetworkError: If the network request fails
        InvalidLocationError: If the location cannot be found
        RateLimitError: If API rate limit is exceeded
    
    Examples:
        >>> # Get current weather for New York
        >>> weather = fetch_weather_data("New York")
        >>> print(f"Temperature: {weather['current']['temperature']}°F")
        Temperature: 72°F
        
        >>> # Get weather with forecast in metric units
        >>> weather = fetch_weather_data("London", units="metric", 
        ...                             include_forecast=True)
        >>> print(f"Tomorrow: {weather['forecast'][1]['high']}°C")
        Tomorrow: 18°C
    
    Note:
        The function caches results for 5 minutes to reduce API calls.
        Set the environment variable WEATHER_API_KEY before use.
    """
    # Implementation here
    pass



# "This comprehensive docstring tells developers everything they need to know without reading the implementation."



