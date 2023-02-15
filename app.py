"""Create time-distance matrix between major cities in Australia."""

import arcgis
import pandas as pd

import os
from dotenv import load_dotenv

load_dotenv() # look in the ".env" file for env vars



def print_result(result):
    """Print useful information from the result."""
    pd.set_option("display.max_rows", None)
    pd.set_option("display.max_colwidth", None)

    output_matrix = result["odCostMatrix"]
    cost_names = output_matrix.pop("costAttributeNames")

    print("Travel costs in Minutes, Miles, Kilometers")
    for origin_id, matrix in output_matrix.items():
        for destination_id, costs in matrix.items():
            print(f"{origin_id} - {destination_id}: {costs}")
        print("-" * 50)


def main():
    """Program execution logic."""
    # inputs
    cities = {
        "spatialReference": {
            "wkid": 4326
        },
        "features": [
            {
                "geometry": {
                    "x": 153.03660,
                    "y": -27.486320
                },
                "attributes": {
                    "ObjectID": 101
                }
            },
            {
                "geometry": {
                    "x": 144.983120,
                    "y": -37.817870
                },
                "attributes": {
                    "ObjectID": 102
                }
            },
            {
                "geometry": {
                    "x": 151.223490,
                    "y": -33.891220
                },
                "attributes": {
                    "ObjectID": 103
                }
            },
            {
                "geometry": {
                    "x": 149.133490,
                    "y": -35.316850
                },
                "attributes": {
                    "ObjectID": 104
                }
            },
            {
                "geometry": {
                    "x": 138.596810,
                    "y": -34.917470
                },
                "attributes": {
                    "ObjectID": 105
                }
            }
        ]
    }

    # Connect to the origin destination cost matrix service and call it
    api_key = os.getenv("ARCGIS_API_KEY")
    portal = arcgis.GIS("https://www.arcgis.com", api_key=api_key)
    od_cost_matrix = arcgis.network.ODCostMatrixLayer(portal.properties.helperServices.odCostMatrix.url,
                                                      gis=portal)
    result = od_cost_matrix.solve_od_cost_matrix(origins=cities,
                                                 destinations=cities,
                                                 )
    print_result(result)



if __name__ == "__main__":
    main()