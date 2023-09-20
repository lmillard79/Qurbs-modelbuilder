# Runoff-model
The Runoff Model Builder QGIS plugin is a convenient wrapper for the Pyromb library so that RORB and WBNM control files can be built directly from QGIS.
  
The Pyromb library and documentation is located here -> [Pyromb](https://github.com/norman-tom/pyromb)
  
Using the plugin is straightforward, it takes four shapefiles that represent the catchment and outputs a control file to be used with either RORB or WBNM. The plugin is a processing plugin and will appear under "Runoff Model" within the Processing Toolbox. Complete use documentation is provided in the Pyromb library repositiory. 

To build a RORB control vector, select the **Build RORB** process.  
To build a WBNM runfile, select the **Build WBNM** process (Currently Unavailable).

Maintained by tom@normcosystems.com

## Dependencies 
The Runoff-model plugin depends on the Python package Pyromb. To install this package for QGIS please refer to the Pyromb homepage (linked above) for instructions. 