# SabzEnergy

A Python package for solar and wind energy analysis using ERA5 data, built with `atlite`, `pvlib`, and `SolarEnergy`.

## Features

- Download and process ERA5 weather data.
- Calculate solar energy potential using `pvlib`.
- Calculate wind energy potential using `atlite`.
- Ready-to-use Jupyter notebook examples for Berlin, Hamburg, Münster, and München.

## Installation

Clone the repository and install it in editable mode:

```bash
git clone https://github.com/yourusername/SabzEnergy.git
cd SabzEnergy
pip install -e .
```

To run the notebooks, start Jupyter Lab:

```bash
jupyter lab
```

## Structure

Similar to MintPy, the project is structured as a Python package with examples in the `notebooks/` directory.

- `sabzenergy/`: Core package source code.
- `notebooks/`: Example workflows for different regions.
- `tests/`: Unit tests.

