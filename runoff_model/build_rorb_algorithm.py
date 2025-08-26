# -*- coding: utf-8 -*-

"""
/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

__author__ = 'Tom Norman'
__date__ = '2023-06-15'
__copyright__ = '(C) 2025 by Tom Norman'

# This will get replaced with a git SHA1 when you do a git archive

__revision__ = '$Format:%H$'

from qgis.PyQt.QtCore import QCoreApplication
from qgis.core import (QgsProcessing,
                       QgsFeatureSink,
                       QgsProcessingAlgorithm,
                       QgsProcessingParameterFeatureSource,
                       QgsProcessingParameterFileDestination)
import pyromb
from .custom_types.qvector_layer import QVectorLayer


class BuildRorbAlgorithm(QgsProcessingAlgorithm):
    """
    Build a RORB control vector from a GIS representation. 

    The plugin depends on python library gisrompy.
    """

    # Constants used to refer to parameters and outputs. They will be
    # used when calling the algorithm from another algorithm, or when
    # calling from the QGIS console.

    OUTPUT = 'OUTPUT'
    IN_REACH = 'IN_REACH'
    IN_BASIN = 'IN_BASIN'
    IN_CENTROID = 'IN_CENTROID'
    IN_CONFLUENCE = 'IN_CONFLUENCE'

    def initAlgorithm(self, config):
        # Input layer for the reaches
        self.addParameter(
            QgsProcessingParameterFeatureSource(
                self.IN_REACH,
                self.tr('Reach'),
                [QgsProcessing.TypeVectorLine]
            )
        )
        # Input layer for the basins
        self.addParameter(
            QgsProcessingParameterFeatureSource(
                self.IN_BASIN,
                self.tr('Basin'),
                [QgsProcessing.TypeVectorPolygon]
            )
        )
        # Input layer for the centroids
        self.addParameter(
            QgsProcessingParameterFeatureSource(
                self.IN_CENTROID,
                self.tr('Centroid'),
                [QgsProcessing.TypeVectorPoint]
            )
        )
        # Input layers for the confluences
        self.addParameter(
            QgsProcessingParameterFeatureSource(
                self.IN_CONFLUENCE,
                self.tr('Confluence'),
                [QgsProcessing.TypeVectorPoint]
            )
        )
        # Output the control vector .cat file. 
        self.addParameter(
            QgsProcessingParameterFileDestination(
                self.OUTPUT,
                self.tr('Control File'),
                "Control Vector (*.cat)" 
            )
        )

    def processAlgorithm(self, parameters, context, feedback):
        # Retrieve the feature source and sink.
        reaches = self.parameterAsSource(parameters, self.IN_REACH, context)
        basins = self.parameterAsSource(parameters, self.IN_BASIN, context)
        centroids = self.parameterAsSource(parameters, self.IN_CENTROID, context)
        confluences = self.parameterAsSource(parameters, self.IN_CONFLUENCE, context)
        sink = self.parameterAsFileOutput(parameters, self.OUTPUT, context)

        ### Build Catchment Objects ###
        # Vector layers 
        reach_vector = QVectorLayer(reaches)
        basin_vector = QVectorLayer(basins)
        centroid_vector = QVectorLayer(centroids)
        confluence_vector = QVectorLayer(confluences)
        # Create the builder. 
        builder = pyromb.Builder()
        # Build each element as per the vector layer.
        tr = builder.reach(reach_vector)
        tc = builder.confluence(confluence_vector)
        tb = builder.basin(centroid_vector, basin_vector)
    
        ### Create the catchment ### 
        catchment = pyromb.Catchment(tc, tb, tr)
        catchment.connect()
        # Create the traveller and pass the catchment.
        traveller = pyromb.Traveller(catchment)

        # Update the progress bar
        feedback.setProgress(1)

        ### Write the file ###
        with open(sink, 'w') as f:
            f.write(traveller.getVector(pyromb.RORB()))

        # Return the results of the algorithm.
        return {self.OUTPUT: sink}

    def name(self):
        """
        Returns the algorithm name, used for identifying the algorithm. This
        string should be fixed for the algorithm, and must not be localised.
        The name should be unique within each provider. Names should contain
        lowercase alphanumeric characters only and no spaces or other
        formatting characters.
        """
        return 'Build RORB'

    def displayName(self):
        """
        Returns the translated algorithm name, which should be used for any
        user-visible display of the algorithm name.
        """
        return self.tr(self.name())

    def group(self):
        """
        Returns the name of the group this algorithm belongs to. This string
        should be localised.
        """
        return self.tr(self.groupId())

    def groupId(self):
        """
        Returns the unique ID of the group this algorithm belongs to. This
        string should be fixed for the algorithm, and must not be localised.
        The group id should be unique within each provider. Group id should
        contain lowercase alphanumeric characters only and no spaces or other
        formatting characters.
        """
        return ''

    def tr(self, string):
        return QCoreApplication.translate('Processing', string)

    def createInstance(self):
        return BuildRorbAlgorithm()

    def shortHelpString(self):
        return self.tr("Build RORBS model files from GIS layers representing catchment reaches, basins, centroids, and confluences.\n\n"
                       "Input layers:\n"
                       "- Reach layer: Line features representing stream reaches with length and slope attributes\n"
                       "- Basin layer: Polygon features representing catchment basins with area and imperviousness\n"
                       "- Centroid layer: Point features representing basin centroids\n"
                       "- Confluence layer: Point features representing stream confluences\n\n"
                       "The algorithm generates one files:\n"
                       "- .catg file: Contains subcatchment data in RORB Graphical format\n\n")