from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="rastermodel",
    version="0.0.5",
    description="A Python package for modeling with rasters and images.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/bparment1/rastermodel",
    author=["Benoit Parmentier", "Mohammad Eshghi"],
    author_email=["benoit.parmentier@gmail.com", "meshghi@uoregon.edu"],
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.7",
        "Topic :: Image Processing :: Computer Vision",
    ],
    keywords="raster spatial geospatial analysis ml ai image processing",
    packages=["rastermodel"],
    include_package_data=True,
    install_requires=["numpy>=1.17.2",
                      "seaborn",
                      "matplotlib",
                      "rasterio",
                      "pandas",
                      "geopandas",
                      "georasters",
                      "gdal",
                      "descartes",
                      "pysal",
                      "cartopy",
                      "pyproj",
                      "osgeo",
                      "sklearn",
                      "shapely",
                      "webcolors",],
    entry_points={
        "console_scripts": [
            "rastermodel=rastermodel.cli:main",
        ]
    },
    dependency_links=["https://github.com/ML-KULeuven/SAR-PU/master#egg=package-1.0"]
    zip_safe=False,
)
