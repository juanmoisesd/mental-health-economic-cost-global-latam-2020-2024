"""Economic cost of mental health disorders: global and Latin America data 2020-202
DOI:https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/FQEYVN"""
__version__="1.0.0"
import pandas as pd,io,requests
def load_data(f=None):
  rid="https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/FQEYVN".split(".")[-1];m=requests.get("https://zenodo.org/api/records/"+rid,timeout=30).json();csvs=[x for x in m.get("files",[]) if x["key"].endswith(".csv")]
  if not csvs:raise ValueError("No CSV")
  tgt=next((x for x in csvs if f and x["key"]==f),csvs[0]);return pd.read_csv(io.StringIO(requests.get(tgt["links"]["self"],timeout=60).text))
def cite():return "de la Serna, Juan Moisés (2025). Economic cost of mental health disorders: global and Latin A"
def info():print("DOI: https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/FQEYVN\nGitHub: https://github.com/juanmoisesd/mental-health-economic-cost-global-latam-2020-2024")
