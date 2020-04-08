# COVID-data

The novel coronavirus or COVID-19 is a virus causing acute respiratory disorders. It belongs to the SARS class of viruses. Beginning in a seafood market at Wuhan, Hubei, China, it spread globally and has attained pandemic status. It currently has over a million reported cases.

Epidemiologists study the spread of the disease by trying to model it mathematically. Basic models include the SI model, the SIS model and the SIR model. The population consists of people susceptible to the disease (S), currently infected by it (I) or those who are no longer affected by it, having attained immunity (recovered, R).

The datasets for [India](https://www.kaggle.com/sudalairajkumar/covid19-in-india), [South Korea](https://www.kaggle.com/kimjihoo/coronavirusdataset), [USA](https://www.kaggle.com/sudalairajkumar/covid19-in-usa) and [Italy](https://www.kaggle.com/sudalairajkumar/covid19-in-italy/data) were sourced from Kaggle. They were formatted into a pandas dataframe after extracting the data for cumulative infected, recovered and dead with respect to days from first infection.

![Italy's dataset](https://github.com/sbalan7/COVID-data/blob/master/images/italy_head.png)

The `compareproperties()` function works to make a line plot comparison of a property between any two countries using seaborn, as is shown below.

![Infected, India vs South Korea](https://github.com/sbalan7/COVID-data/blob/master/images/ind_vs_kor.png)

More info can be found [here](https://www.youtube.com/watch?v=dQw4w9WgXcQ).

I would also like to thank Aalaap Nair for helping me with this project.
