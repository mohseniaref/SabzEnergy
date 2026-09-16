"""
Module for solar energy potential calculations using atlite and pvlib.
"""
import atlite

def calculate_solar_potential(cutout, panel="CSi"):
    """
    Calculate solar PV potential for a given cutout.
    """
    print(f"Calculating solar generation potential using panel type: {panel}")
    
    # Using atlite's built-in PV potential calculation which utilizes pvlib under the hood
    pv_generation = cutout.pv(
        panel=panel,
        orientation='latitude_optimal'
    )
    
    return pv_generation

def calculate_pvlib_directly(lat, lon, start, end, weather_data):
    """
    If we want to use pvlib directly with custom weather data.
    """
    import pvlib
    from pvlib.pvsystem import PVSystem
    from pvlib.location import Location
    from pvlib.modelchain import ModelChain
    from pvlib.temperature import TEMPERATURE_MODEL_PARAMETERS
    
    location = Location(lat, lon, tz='UTC')
    
    # Sandi module and ABB inverter
    sandia_modules = pvlib.pvsystem.retrieve_sam('SandiaMod')
    cec_inverters = pvlib.pvsystem.retrieve_sam('cecinverter')
    
    module = sandia_modules['Canadian_Solar_CS5P_220M___2009_']
    inverter = cec_inverters['ABB__MICRO_0_25_I_OUTD_US_208__208V_']
    temperature_parameters = TEMPERATURE_MODEL_PARAMETERS['sapm']['open_rack_glass_glass']
    
    system = PVSystem(
        surface_tilt=lat, 
        surface_azimuth=180,
        module_parameters=module,
        inverter_parameters=inverter,
        temperature_model_parameters=temperature_parameters
    )
    
    mc = ModelChain(system, location)
    mc.run_model(weather_data)
    
    return mc.results.ac

