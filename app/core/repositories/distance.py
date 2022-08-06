from __future__ import annotations

import pandas as pd
from geopy.distance import geodesic
from app.utils.measure_distance import haversine_np

airport = pd.read_csv('data/airport_coordinates.csv')


def get_top_cloest_airport(ref_lat, ref_lon, top_n: int = 1000):
    dist_list = []

    for index, lat, lon in zip(airport['index'], airport['lat'], airport['lon']):
        dist = haversine_np(ref_lat, ref_lon, lat, lon)
        dist_list.append([index, dist])

    top_1000_cloest = [
        dist[0] for dist in sorted(
            dist_list, key=lambda x: x[1], reverse=False,
        )
    ][0:top_n]
    response_data = airport[
        airport['index'].isin(
            top_1000_cloest,
        )
    ].to_dict(orient='records')
    return response_data


def measure_geodesic_distance(lat1, lon1, lat2, lon2):
    first_coor = (lat1, lon1)
    second_coor = (lat2, lon2)
    return geodesic(first_coor, second_coor).km
