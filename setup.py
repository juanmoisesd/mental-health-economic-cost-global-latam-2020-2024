from setuptools import setup, find_packages
setup(
    name="mental-health-economic-cost-global-latam-2020-2024",
    version="1.0.0",
    description="Economic cost of mental health disorders: global and Latin America data 2020-2024. GDP loss, product",
    author="de la Serna, Juan Moisés",
    url="https://github.com/juanmoisesd/mental-health-economic-cost-global-latam-2020-2024",
    packages=find_packages(),
    install_requires=["pandas>=1.3.0","requests>=2.26.0"],
    python_requires=">=3.7",
    classifiers=["Programming Language :: Python :: 3","License :: OSI Approved :: MIT License","Topic :: Scientific/Engineering"],
    keywords="dalys, dataset, economics, gdp-loss, latin-america, mental-health, open-data, productivity, zenodo, open-data",
)