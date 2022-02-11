# Analysis advertisements on Bolha

In this project I will analyze the top 10.000 products in the section of Computers on the slovenian flea market website [Bolha](https://www.bolha.com/racunalnistvo) sorted by descending price. The analysis is done in jupyter notebook in slovene language.

## Getting started

As to not cause issues by ddosing the site all data that my analysis is based on is saved in the folder `data/` using `download_data.py` and compiled into `data.csv` by `filter.py`. If you wish to run the analysis on fresh data simply run the preceding programs to get fresh data.

## Dependencies

To run the analysis `python` library `pandas` and a way to run jupyter notebooks is required. You can install the dependencies by running
```
pip install pandas
```

## Analysis

Each entry in the database consists of:
* Name of advert
* Location (city and district)
* Date of publication
* Price
* Type of product (derived from name)

### Hypotheses and goals

Some of the hypotheses and goals I will try to find out with my data analysis are:
* Create an algorithm to classify product (derive type from name)
* Which types of product are most expensive
* Corellation between time of publication and product price
* Determine which cities have the greatest amount of advertisements on the website
* Determine what most popular product for each city is
