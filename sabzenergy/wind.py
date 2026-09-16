"""
Module for wind energy potential calculations using atlite.
"""
import atlite

def calculate_wind_potential(cutout, turbine="Vestas_V112_3MW"):
    """
    Calculate wind power generation potential for a given cutout.
    """
    print(f"Calculating wind generation potential using turbine: {turbine}")
    
    # Using atlite's built-in wind potential calculation
    wind_generation = cutout.wind(
        turbine=turbine
    )
    
    return wind_generation

