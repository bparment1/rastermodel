import argparse
from rastermodeling import *
from utils import *

# for console scripts
def main():
    parser = argparse.ArgumentParser(description = "Raster Modeling")
    parser.add_argument("-l", "--load", type = str, nargs = 1,
                        metavar = "load_raster", default  = None, help = "Load Raster")
    args = parser.parse_args()
    utils.load_data(args.load_raster)


if __name__ == "__main__":
    main()
