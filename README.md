# Modeling raster and images

This package provides functionalities to apply statistical and machine learning models to raster and image layers.

It aims at making easy the use of sklearn or function on pixel by pixel basis. Rather than loading, raster datasets in python arrays, the package avoids memory issues by processing chunk by chunk (blocks) raster images. 

Current version, version supports application of sklearn models using simple function (rasterPredict). Future iterations will include implementation of rasterApply for user function (e.g. pixel based time series functionalities such as FFT). 
