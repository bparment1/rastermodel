Modeling raster and images
=====================================

This package provides functionalities to apply statistical and machine learning models to raster and image layers.

The aim is ease of use to develop and test models with spatial raster data.  For instance, sklearn models or functions are applied on pixel by pixel basis. Rather than loading raster datasets in memory with python arrays, the package avoids memory issues by processing chunk by chunk (blocks) raster images. This allows for modeling of large raster without memory bottleneck. 


## Installation

```bash

pip install rastermodel

```
## Functionalities

Current version, version supports application of:

1. sklearn models using simple function (rasterPredict). 

## Upcoming Functionalities

Future iterations will include implementation of rasterApply for user function (e.g. pixel based time series functionalities such as FFT). 
