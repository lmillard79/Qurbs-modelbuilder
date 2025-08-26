# Runoff Model

The Runoff Model suite of QGIS plugin generates RURB and URBS control vector files from GIS layers for hydrological modeling.

## Description

The helps builds either RORB or URBS plugin is part of the Runoff Model Builder (pyromb) suite of tools. It takes input GIS layers representing catchment reaches, basins, centroids, and confluences and generates a control vector file (.catg) for the chosed hydrology model.

Both RORB and URBS (Urban Runoff Block Structure) are hydrological models used for catchment runoff modeling in Australia.

## Features

- Generate RORB and URBS control vector files from GIS layers
- Supports the same input layer structure between plugins
- Integrated within the QGIS processing framework

## Installation

### Method 1: Install from QGIS Plugin Manager
1. Open QGIS
2. Go to Plugins > Manage and Install Plugins
3. Search for "Runoff Model Builder"
4. Install for all model builders.

### Method 2: Manual Installation
1. Download or clone this repository
2. Copy the entire folder to your QGIS plugins directory:
   - Windows: `C:\Users\<username>\AppData\Roaming\QGIS\QGIS3\profiles\<profilename>\python\plugins`
   - macOS: `~/Library/Application Support/QGIS/QGIS3/profiles/<profilename>/python/plugins`
   - Linux: `~/.local/share/QGIS/QGIS3/profiles/<profilename>/python/plugins`
3. Restart QGIS
4. Enable the plugin in QGIS Plugin Manager

## Dependencies

This plugin requires the pyromb library to be installed separately.

For Windows users, you may need to install Python packages in QGIS 3 using the OSGeo4W shell:
```
py3_env
pip install pyromb
```

Or follow the guide 'Installing Python packages in QGIS 3 (for Windows)' available at:
https://gis.stackexchange.com/questions/107414/installing-python-packages-in-qgis-3-for-windows

## Usage

1. Open QGIS
2. Go to Processing Toolbox
3. Find "Runoff Model: RORB or URBS" in the algorithms list
4. Run the "Build Control Vector" algorithm
5. Select your input layers:
   - Reach layer (line features)
   - Basin layer (polygon features)
   - Centroid layer (point features)
   - Confluence layer (point features)
6. Specify the output file location
7. Run the algorithm

## Requirements

- QGIS 3.22 or later
- pyromb library (https://github.com/norman-tom/pyromb) v0.3

## License

This plugin is licensed under the GNU General Public License v2.0 or later.

## Author

Tom Norman, Lindsay Millard
