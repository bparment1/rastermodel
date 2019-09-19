# Modeling raster and images

This package provides functionalities to apply statistical and machine learning models to raster and image layers.

The aim is ease of use to develop and test models with spatial raster data.  For instance, sklearn models or functions are applied on pixel by pixel basis. Rather than loading raster datasets in memory with python arrays, the package avoids memory issues by processing chunk by chunk (blocks) raster images. This allows for modeling of large raster without memory bottleneck.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

## Functionalities

Current version, version supports application of:

1. sklearn models using simple function (rasterPredict).

## Upcoming Functionalities

Future iterations will include implementation of rasterApply for user function (e.g. pixel based time series functionalities such as FFT).

### Prerequisites

What things you need to install the software and how to install them

```
numpy,
sklearn,
geopandas
```

### Installation

A step by step series of examples that tell you how to get a development env running

Say what the step will be


```bash

pip install rastermodel

```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Lorem ipsum](https://github.com/bparment1/rastermodel) - blah blah blah
* [Lorem ipsum](https://github.com/bparment1/rastermodel) - blah blah blah
* [Lorem ipsum](https://github.com/bparment1/rastermodel) - blah blah blah

## Contributing

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

## Versioning

For the versions available, see the [tags on this repository](https://github.com/bparment1/rastermodel/tags).

## Authors

* **[Benoit Parmentier]**(https://github.com/bparment1)

* **[Mohammad Eshghi]**(https://github.com/meshghi)

See also the list of [contributors](https://github.com/bparment1/rastermodel/graphs/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
