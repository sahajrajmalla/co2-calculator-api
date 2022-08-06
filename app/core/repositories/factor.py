from __future__ import annotations

import pandas as pd


def fetch_factor_data() -> dict:
    air_tranport_data = pd.read_csv('data/CO2 Emission dataset - Air Transport.csv')
    land_tranport_data = pd.read_csv('data/CO2 Emission dataset - Land Transport.csv')
    diet_data = pd.read_csv('data/CO2 Emission dataset - Diet.csv')
    electricity_data = pd.read_csv('data/CO2 Emission dataset - Electricity.csv')

    data = {
        'air_tranport': air_tranport_data,
        'land_tranport': land_tranport_data,
        'diet': diet_data,
        'electricity': electricity_data,
    }

    factor_response = {}

    for key, value in data.items():
        factor_response[key] = value.to_dict(orient='records')

    return factor_response
