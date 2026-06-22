import requests
import pandas as pd

scheme_codes = {
    125497: "HDFC_Top_100_Direct",
    119551: "SBI_Bluechip",
    120503: "ICICI_Bluechip",
    118632: "Nippon_Large_Cap",
    119092: "Axis_Bluechip",
    120841: "Kotak_Bluechip"
}

for code, name in scheme_codes.items():

    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)

    data = response.json()

    nav_df = pd.DataFrame(data["data"])

    filename = f"data/raw/{name}.csv"

    nav_df.to_csv(filename, index=False)

    print(f"{name} saved successfully!")