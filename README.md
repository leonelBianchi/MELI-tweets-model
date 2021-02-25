# Mercadolibre Twitter Analysis with NLP

**currently working**

## Abstract 

In this project, we extract and analyze Twitter data related to MercadoLibre. This covers a complete analysis, from the posing of the correct questions to be solved, the collection of unstructured data, its structuring, its cleaning and its exploratory analysis and the determination of initiatives to take from them. This also includes the generation of models that find patterns between tweets´s words and rts/favs, using natural language processing concepts.


As the first step in data analysis, we need to ask the right questions to achieve good results as well as identify the main objetive to better know what type of data we´ll be needing to draw conclusions. This questions should be measurable, clear and consice. It is also important to define the problem to solve clearly.

Every step in this statistical analysis must lead to a future decision about something: reach more clients and improve the reputation of the company.

As we know, diferent variables have diferent dificult to be measure. In this case, the dificult is high since they are unstructured and subjetive. But in any statiscal analysis, ee are always negotiating how expensive to collect data and how difficult to achieve good results with a small data set. Due to the scope of this project, we will use an open source library called Tweepy to get data data and try to extract ideas from it.

We also need to know that the distribution is IID (independent and identical distributed) for this particular case of analysis and can´t be extrapolated to other escensarios. The observations are independent (we have different users that use the same platform from the same region and at the same time, talking about the same thing). Also, the observations comes from the same distribution. 

## Research study

* **Exploratory**. We collect and analyze data from twitter without a previous fixed question, teasing out trends and patterns, as well as deviations from the model, outliers, and unexpected results, using quantitative and visual methods. A *confirmatory* study could be done after getting some insights about the data.

* **Observatinonal**. We only look at the twitter activity without altering or causing anything.
* **Compartive**. We compare the performance of the differetns MercadoLibre´s accounts, how differents are the complains in each country, what time produces the greatest impact, etc.


## Objetive

* Understand the dynamics of Twitter users to improve the way Mercado Libre can reach more users, increase its reputation, solve user problems faster and better and invest in content that brings more results and discourage those that do not.
* Use twitter data to develop better business strategies, understand customer´s feeling towards Mercado Libre and its products (such as MercadoPago), how they respond to their campaigns or product launches.


## Questions

* Wich account gets more favs/retweets? 
* What tweets achieve more repercussion?
* What are the main complaints from users?
* From which country are there the most complaints?
* What time are there more complaints?
* How do people respond to each product?
* Are there more positive or negative tweets?


## Pipeline

* **Introduction**: brief explanation of the data extraction process, sources and purposes.
```bash
intro.ipynb
```
* **Data collection**: The data collection is done using the Twitter API. The tweets made by the mercadolibre´s accounts from LATAM and their mentions are stored in csv files.
```bash
data_collection.ipynb
searcher.py
```
* **Data cleaning**: Data stored in Dataframes with pandas and removing uncommon signs, irrelevant information and outliers. Data visualization is needed.
```bash
data_collection.ipynb
```
* **Exploratory data analysis**
```bash
data_collection.ipynb
```
* **Natural Language Processing Model**: created with Keras and Tensorflow, using word embedding layers, and trained with Twitter data.
```bash
data_collection.ipynb
```
* **Sentiment Analysis**: using the nlp model, it is possible to classify each tweet in positive sentiment and negative sentiment.
```bash
data_collection.ipynb
```


## Libraries



```bash
pip install tweepy
pip install pandas
pip install numpy
pip install tensorflow
pip install keras
pip install scikitlearn
pip install seaborn
```
