# New York Yellow Taxi

## Profit Maximization for Yellow Taxi Driver

- Name: `Anh Phi Vu`

## Introduction

This project aim to answer the question on "How to maximize profit of NYC yellow taxi driver picking up passenger from JFK airport?" by providing a quantitative analysis on the data obtained from the TLC website. The data sets cover trips taken by NYC yellow taxi from January 2020 to March 2020. There are also flights arrival data within the USA with corresponded time frame from January 2020 to March 2020. 

## Datasets

* TLC taxi data: https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page
* Flights data: https://www.bts.dot.gov/browse-statistical-products-and-data/bts-publications/airline-service-quality-performance-234-time

## Requirement

All the script and notebooks were run on a Macbook Pro 2023 with M2 Pro, 1TB SSD and 32GB RAM. 
All the requirement packages are stored under `requirement.txt` file. 

## Directories

* All Jupyter Notebooks are in the `notebooks` directory.
* All `.py` scripts are under the `scripts` directory.
* All datas downloaded straight from the source using `download.py` are in the `data/landing` folder.
* All the datas after raw - preprocessed are in the `data/raw` folder.
* All the datas after curated - preprocessed and ready for analysis are in the `data/curated` folder.
* All plots are saved in the `plots` folder.
* The report `.tex` files are in the `report` directory.

## Pipeline

**To run the data pipeline, please follow the steps below:**

1. Visits the `scripts` directory and run `download.py`
There will be three `.zip` files. This is the flights data, simpmly open the zip file to extract the `.asc` flights data and rename it to `flight_data_2020_01`, `flight_data_2020_02`, and `flight_data_2020_03`. `download.py` will saved the data to `data/landing` directory.

2. Visits the `notebooks` directory and run `taxi_raw-preprocess.ipynb` and `flight_raw-preprocess.ipynb`
These notebooks detailes all the raw - preprocessing steps and outputs it to the `data/raw` directory.

3. Visits the `notebooks` directory and run `taxi_curated-preprocess.ipynb` and `flight_curated-preprocess.ipynb`
These notebooks detailes all the curated - preprocessing steps and outputs it to the `data/curated` directory.

4. Visits the `notebooks` directory and run `pre_analysis_preparation.ipynb`
This notebooks do a pre - analysis on the taxi data to prepare it for modelling. It outputs the data to `data/curated` directory.

5. Visits the `notebooks` directory and run `taxi_data_prep_linmod.ipynb`
This notebooks prepare the data to be ready for linear regression. It outputs the data to `data/curated` directory. 

**Now, all the datas needed are available and ready to do analysis.**

6. Visits the `notebooks` directory and run `exploratory_analysis.ipynb`
This notebooks do an exploratory analysis on taxi and flights data. All plots output are saved in the `plots` folder.

7. Visits the `notebooks` directory and run `geopd_visual.ipynb`
This notebooks draw a geopandas visualization and save it to the `plots` directory.

8. Visits the `notebooks` directory and run `lin_reg.ipynb`
This notebooks fit a Linear Regression model to the data. All plots output are saved in the `plots` folder.

9. Visits the `notebooks` directory and run `RFR.ipynb`
This notebooks fit a Random Forest Regression to the data. All plots output are saved in the `plots` folder.
