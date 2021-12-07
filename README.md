# DataScienceProject
## Draft Abstract
**Title:** Association and prediction of case of corona virus infection with vaccination accumulation.

**Theme:** Vaccination, Covid, Health

**Description:** This project aims to discover the relationship between positive coronavirus inflection with the accumulated vaccine doses for each day begin at December 14, 2020 to when I collected the data October, and try to predict the infection based on model. This project will use linear regression model for first doses accumulation and second dose accumulation to the positive case of corona virus. This project will also use multi-linear model with accumulated dose1, dose2 as independent variables and Covid daily count as dependent variable.

**Relavance:** The data used are from NYC exclusively.

**Data Sources:** https://github.com/nychealth/coronavirus-data/blob/master/trends/cases-by-day.csv, https://github.com/nychealth/covid-vaccine-data/blob/main/doses/doses-by-day.csv

## Visualizations
The first two graphs show the trends of Positive covid case, and cumulative vaccine doses of dose1,dose2 from the time these data made available to October 2021.

![CoronaTrendByMonth](https://user-images.githubusercontent.com/56707953/143976438-a013adb6-0cf8-4759-9e9a-c7beb0b13523.png)
![Vaccine_Trend](https://user-images.githubusercontent.com/56707953/143976509-2d45431a-5f57-4891-a03e-3d62d09cfc08.png)

The Linear Model with cumulative Dose 1 as independent variable to predict case count of corona virus infection.

![association_Dose1](https://user-images.githubusercontent.com/56707953/145104454-d5623bd6-2a47-4952-ba45-172c161e169a.png)

This model predict that when Dose 1 cumulative reach around 6,062,831, the corresponding corona infection would drop to 0. Only 1694 population increase on first dose cumulative will bring down 1 infection on average in this case. In addition, vaccination of dose1 and daily case count are highly correlated.

![ResidualGraph1](https://user-images.githubusercontent.com/56707953/143976598-f71fe250-17b1-430c-b550-35317e8e3a37.png)

The error for this model is huge and having a pattern which denote the inability for this model to predict correctly.

The Linear Model with cumulative Dose 2 as independent variable to predict case count of corona virus infection. 

![association_Dose2](https://user-images.githubusercontent.com/56707953/145104719-750bd57c-88ce-4edd-bf15-12c0204dbcf6.png)

This linear model predict that when Dose 2 cumulative reach around 5,912,397, the corresponding corona infection would drop to 0. Only 1653 population increase on second dose cumulative will bring down 1 infection on average in this case. In additon, vaccination of dose2 and daily case count are highly correlated.

![ResidualGraph2](https://user-images.githubusercontent.com/56707953/143976628-c0f27ca0-8d42-448a-a78a-3a632c2dd08b.png)

The error for this model is also huge and having a pattern which denote the inability for this model to predict correctly.

The multi-linear model with cumulative dose1/2 as independent variables, and virus infection case count as dependent variable
![MultiLinearRegression](https://user-images.githubusercontent.com/56707953/143976652-992d0dcd-849d-4f01-b8eb-3b37009d6e00.png)
![ResidualGraph3](https://user-images.githubusercontent.com/56707953/143976668-e98ba6e9-59e7-4376-b85e-94cd368ed0dc.png)

Like other two models, the residual graphs suggest there are other factor other than vaccine to affect the infection. One can see such pattern from sudden rise of infection in August, September.

![ExpectValue_Pair_Of_Dose12](https://user-images.githubusercontent.com/56707953/143976691-1b57627d-8138-45ca-813f-e3a08535e10b.png)
One possible pair is (5470000, 6602608) which close to the current number of vaccination (5476764, 6152675) recorded in November 8, 2021. Base on this prediction, approximately 449,933 more people need to get first dose of vaccine in order to reach 0 infection. 

