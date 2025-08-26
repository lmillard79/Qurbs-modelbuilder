# Pull Request: URBS Model Implementation

## Overview

This PR implements complete URBS (Unified River Basin Simulator) functionality in the pyromb library, replacing the previous incomplete implementation with a proper text-based command system that generates URBS-compatible model files.

## Key Changes

### ✅ Core Implementation
- **Complete URBS Model Rewrite** (`src/pyromb/model/urbs.py`)
  - Replaced RORB-style numeric codes with URBS text commands
  - Implemented proper command structure: `RAIN`, `ADD RAIN`, `STORE`, `GET`, `ROUTE`, `PRINT`
  - Added named parameters (L= for length, Sc= for slope)
  - Handles slope unit conversion (m/m for URBS vs % for RORB)

### ✅ Dual File Architecture
- **`.vec` file**: URBS command sequence with model headers
- **`.cat` file**: Subcatchment parameter data in CSV format
- Separate writer classes: `UrbsVectorWriter` and `UrbsCatWriter`
- Proper URBS file structure following documentation specifications

### ✅ QGIS Plugin Integration
- **Build URBS Plugin**: Complete QGIS Processing algorithm
- Real GIS data processing from vector layers (basins, reaches, confluences)
- Plugin hierarchy fixes and interface corrections
- Debug logging for troubleshooting

### ✅ Documentation
- **`README_URBS.md`**: Comprehensive quick start guide
- **`URBS_Implementation_Plan.md`**: Technical implementation documentation  
- **`QGIS_Development_Workflow.md`**: Development process notes
- Updated logic documentation in `/documentation` folder

## Technical Details

### URBS Command Examples
```
RAIN #1 L=1000 Sc=0.010
STORE.
ADD RAIN #2 L=1500 Sc=0.008
GET.
ROUTE THRU #3 L=2000 Sc=0.005
PRINT. MODEL_OUTLET
```

### File Structure
- **Vector file** (`.vec`): Text commands and model configuration
- **Catchment file** (`.cat`): CSV with subcatchment parameters
- Proper headers and END statements following URBS specification

## Code Organization

### New Files
- `README_URBS.md` - User documentation
- `URBS_Implementation_Plan.md` - Technical documentation
- `QGIS_Development_Workflow.md` - Development notes
- `archive/` - Relocated test and development scripts

### Modified Files
- `src/pyromb/model/urbs.py` - Complete rewrite
- Updated documentation files

### Removed/Archived Files
- Legacy test scripts moved to `archive/`
- `urbs_new.py` and `urbs_old_backup.py` archived
- Development and debugging scripts organized

## Testing & Validation

### ✅ QGIS Integration Testing
- Tested with real GIS data (22 basins, 33 reaches)
- Plugin loads and runs successfully in QGIS 3.40.8
- Generates proper URBS file outputs

### ✅ File Format Validation
- `.vec` files contain proper URBS command structure
- `.cat` files match expected CSV format
- Headers and syntax follow URBS documentation

## Breaking Changes

- **URBS model interface**: Now generates dual files instead of single output
- **Command structure**: Text-based commands replace numeric codes
- **File extensions**: `.vec` and `.cat` instead of single file output

## Dependencies

- No new external dependencies added
- Compatible with existing pyromb architecture
- Requires QGIS 3.x for plugin functionality

## Usage

```python
# Create URBS model
from pyromb.model import URBS
model = URBS("MyModel")

# Generate files from traveller
vec_content, cat_content = model.getFiles(traveller)
```

## QGIS Plugin Usage

1. Load required vector layers (basins, reaches, confluences, centroids)
2. Run **Processing > Runoff Model: URBS > Build URBS Control Vector**
3. Specify input layers and output location
4. Algorithm generates both `.vec` and `.cat` files

## Related Issues

- Addresses URBS implementation requirements
- Enables proper dual-file URBS model generation
- Provides QGIS integration for GIS-based model building

---

**Testing Environment**: QGIS 3.40.8, Python 3.12  
**Branch**: `URBS_development`  
**Ready for**: Merge to main branch after review
