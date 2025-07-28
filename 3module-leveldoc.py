# "Every Python file should start with a module docstring:"

"""
weather_data_manager.py

This module provides the WeatherDataManager class for handling all weather
data operations in the weather application. It includes functionality for:

- Fetching weather data from external APIs
- Caching responses to minimize API calls
- Persisting historical data in SQLite
- Converting between unit systems
- Managing user preferences for data display

The module is designed to be the single source of truth for weather data
in the application, ensuring consistency and proper error handling.

Usage:
    from weather_data_manager import WeatherDataManager
    
    manager = WeatherDataManager(api_key=os.getenv('WEATHER_API_KEY'))
    manager.update_location("Boston")
    weather = manager.get_current_weather()

Requirements:
    - requests >= 2.25.0
    - sqlite3 (included with Python)
    - python-dateutil >= 2.8.0

Environment Variables:
    WEATHER_API_KEY: API key for weather service (required)
    WEATHER_CACHE_DIR: Directory for cache files (optional)
    WEATHER_DB_PATH: Path to database file (optional)
"""
