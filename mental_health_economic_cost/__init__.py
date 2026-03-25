"""
mental-health-economic-cost
========================================
Access the Harvard Dataverse dataset DVN/FQEYVN.
DOI: https://doi.org/10.7910/DVN/FQEYVN
Author: Juan Moises de la Serna (ORCID: 0000-0002-8401-8018)

Usage:
    from mental_health_economic_cost import load_dataset, get_cost_summary
    df = load_dataset('gdp_loss_by_country')
    summary = get_cost_summary()
"""
from .loader import load_dataset, list_files, get_cost_summary, get_doi
__version__ = "1.0.0"
__doi__ = "10.7910/DVN/FQEYVN"
__author__ = "Juan Moises de la Serna"
__all__ = ["load_dataset", "list_files", "get_cost_summary", "get_doi"]
