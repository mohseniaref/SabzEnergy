"""
Predefined locations for analysis.
Coordinates are (latitude, longitude).
"""

CITIES = {
    "Berlin": {"lat": 52.5200, "lon": 13.4050},
    "Hamburg": {"lat": 53.5511, "lon": 9.9937},
    "Munster": {"lat": 51.9607, "lon": 7.6261},
    "Munchen": {"lat": 48.1351, "lon": 11.5820},
}

def get_bounding_box(city_name, padding=0.5):
    """
    Get a bounding box around a city for downloading ERA5 data.
    Returns (min_lon, max_lon, min_lat, max_lat).
    """
    if city_name not in CITIES:
        raise ValueError(f"City {city_name} not found. Available cities: {list(CITIES.keys())}")
    
    loc = CITIES[city_name]
    return (
        loc["lon"] - padding,
        loc["lon"] + padding,
        loc["lat"] - padding,
        loc["lat"] + padding
    )

