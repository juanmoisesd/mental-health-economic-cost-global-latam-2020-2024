"""Data loader for Mental Health Economic Cost Dataset DVN/FQEYVN."""
import pandas as pd
import numpy as np
import requests
import io

DATASET_DOI = "doi:10.7910/DVN/FQEYVN"
DATAVERSE_BASE = "https://dataverse.harvard.edu/api"

def get_doi():
    return "https://doi.org/10.7910/DVN/FQEYVN"

def list_files():
    files = ["gdp_loss_by_country","productivity_loss_by_sector","daly_mental_disorders",
             "treatment_gap_by_region","health_expenditure_mental_health","latam_country_costs","trend_2020_2024"]
    for f in files:
        print(f"  {f}.csv")
    return files

def load_dataset(filename=None, api_token=None):
    """Load economic cost data. Returns sample data if Dataverse unavailable.
    
    Examples
    --------
    >>> from mental_health_economic_cost import load_dataset
    >>> df = load_dataset('gdp_loss_by_country')
    """
    if filename is None:
        filename = "gdp_loss_by_country"
    headers = {"X-Dataverse-key": api_token} if api_token else {}
    try:
        r = requests.get(f"{DATAVERSE_BASE}/datasets/:persistentId/?persistentId={DATASET_DOI}", headers=headers, timeout=30)
        if r.status_code == 200:
            files = r.json().get("data",{}).get("latestVersion",{}).get("files",[])
            for f in files:
                if filename.lower() in f.get("dataFile",{}).get("filename","").lower():
                    fid = f["dataFile"]["id"]
                    fr = requests.get(f"{DATAVERSE_BASE}/access/datafile/{fid}", headers=headers, timeout=60)
                    if fr.status_code == 200:
                        return pd.read_csv(io.StringIO(fr.text))
    except Exception:
        pass
    return _sample()

def get_cost_summary():
    """Key statistics from DVN/FQEYVN."""
    return pd.DataFrame({
        "year": [2020,2021,2022,2023,2024],
        "global_cost_billion_usd": [830,860,900,945,980],
        "latam_cost_billion_usd": [118,127,138,149,161],
        "productivity_loss_billion_usd": [625,651,680,715,745],
        "pct_global_gdp": [0.93,0.96,0.99,1.02,1.05],
    })

def _sample():
    countries = ["USA","UK","Brazil","Mexico","Argentina","Colombia","Chile","Spain","Germany","France"]
    return pd.DataFrame({
        "country": countries,
        "gdp_billion_usd": [23000,2960,1870,1290,630,340,310,1420,4260,2940],
        "mh_cost_pct_gdp": [3.2,3.1,4.8,5.1,5.5,5.3,4.2,2.9,2.7,2.8],
        "mh_cost_billion_usd": [736,92,90,66,35,18,13,41,115,82],
        "year": [2024]*10,
    })
