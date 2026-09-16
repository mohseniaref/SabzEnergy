"""
Module for fetching and managing climate data using atlite (ERA5).
"""
import os
import atlite
from sabzenergy.utils.locations import get_bounding_box

def create_cutout(city_name, year, output_dir="data", padding=0.5):
    """
    Create an atlite cutout for a specific city and year using ERA5 data.
    Requires CDS API key to be configured.
    """
    os.makedirs(output_dir, exist_ok=True)
    
    # Get bounding box
    min_lon, max_lon, min_lat, max_lat = get_bounding_box(city_name, padding)
    
    # Define cutout parameters
    cutout_name = f"{city_name}_{year}.nc"
    cutout_path = os.path.join(output_dir, cutout_name)
    
    # If it already exists, just load and return it
    if os.path.exists(cutout_path):
        print(f"Cutout {cutout_name} already exists. Loading...")
        return atlite.Cutout(cutout_path)
    
    print(f"Creating cutout for {city_name} for the year {year}...")
    cutout = atlite.Cutout(
        path=cutout_path,
        module="era5",
        x=slice(min_lon, max_lon),
        y=slice(min_lat, max_lat),
        time=slice(f"{year}-01-01", f"{year}-12-31")
    )
    
    # Prepare the cutout (downloads data from CDS)
    print("Preparing cutout (this may take a while depending on CDS queue)...")
    cutout.prepare()
    
    return cutout

