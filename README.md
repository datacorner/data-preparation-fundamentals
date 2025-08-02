# The Art of Data Alchemy (Book's resources)

The The Art of Data Alchemy is a practical guide to cleaning and organizing the messy, tangled data you’ll encounter in the real world. You’ll learn techniques you can use to get your data ready for almost any task—from reports and analysis, to building machine learning models.

In Data Preparation for AI and Analytics you’ll:
* Understand the importance of data quality
* Use AI to clean and prepare data
* Take advantage of Python and visual tools like Alteryx
* Apply the right data preparation technique for the right outcome

The Art of Data Alchemy is for anyone who works with data, from seasoned data architects to marketing pros and business analysts. It presents data preparation methods with clear language and concrete examples. You’ll explore tried-and-true approaches along with emerging generative AI techniques. You’ll especially appreciate the insights into automation and data governance.

## About the book
The Art of Data Alchemy teaches you to tackle the challenges you’ll face as you work with data. You’ll master popular data wrangling tools like Python and Alteryx. Complex data prep concepts are broken down into clear, manageable steps and fully illustrated with engaging data sets—including data on the Titanic disaster, rating video games, sentiment analysis of Los Angeles restaurant recommendations, and more. The book is packed with vital advice for complex tasks, including merging multiple data sets, alerting systems for data quality, and scaling data preparation into large cloud-based pipelines. Learn universal techniques for data enrichment and transformation, and specialized approaches optimized for machine learning, analytics, and creating AI.

## About the reader
For data workers of all skill levels, who know Python and the basics of SQL.

## About the author
Benoît Cayla is a computer engineer with over 25 years of data management experience and an expert in data management and AI. Throughout his career, he has had the privilege of working with major players like IBM, Informatica, and Tableau, contributing to large-scale projects in manufacturing, insurance, and finance. 

# The book resources
## Requirements 
[Install and configure your environment](/code/README.md)

## Resources available per chapter
Some datasets have been modified from their original versions for compatibility with the provided code examples. To ensure the code works as intended, it is recommended to use the modified datasets (as they are referenced already). However, for reference and additional context, links to the original datasets are also included.
### Chapter 1 - Introduction to data preparation
**N.A.**

### Chapter 2 - Unveiling the secrets of data
* [Original Titanic dataset and description](https://www.kaggle.com/competitions/titanic)
* [Chapter python code](./code/chapter%202/)
* [Dataset used in the the book](./data/titanic/)
	
### Chapter 3 - Data quality challenges
* [Original Titanic dataset and description](https://www.kaggle.com/competitions/titanic)
* [Chapter python code](./code/chapter%202/)
* [Dataset used in the the book](./data/titanic/)
	
### Chapter 4 - Techniques for data transformation
* [Original Video games dataset](https://www.kaggle.com/datasets/mohamedtarek01234/steam-games-reviews-and-rankings)
* [Chapter python code](./code/chapter%204/)
* [Dataset used in the the book](./data/vgames/)
	
### Chapter 5 - Reveiling informations
**Warning:** In this chapter several specific Python and system libraries need to be installed beforehand. Please follow the procedure [here](./code/README.md#Specific-libraries-for-chapter-5)
* **Top restaurants in LA (2023)**
	* [Original dataset and description](https://www.kaggle.com/datasets/lorentzyeung/top-240-recommended-restaurants-in-la-2023)
	* [Chapter python code](./code/chapter%205/)
	* [Dataset used in the the book](./data/restaurants/)
* **BBC News**
	* [Original dataset and description](https://www.kaggle.com/datasets/gpreda/bbc-news)
	* [Chapter python code](./code/chapter%205/)
	* [Dataset used in the the book](./data/bbcnews/)
* [Folder Images](./data/images/)
* **Titanic disaster**
	* [Original Titanic dataset and description](https://www.kaggle.com/competitions/titanic)
	* [Chapter python code](./code/chapter%202/)
	* [Dataset used in the the book](./data/titanic/)
		
### Chapter 6 - Data preparation for machine learning and AI
* [Original Bike rental dataset and description](https://www.kaggle.com/competitions/bike-sharing-demand/data)
* [Chapter python code](./code/chapter%206/)
* [Dataset used in the the book](./data/bikerental/)

### Chapter 7 - Data preparation for dashboards and reports
* [Original Superstore dataset and description](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final)
* [Chapter python code](./code/chapter%207/)
* [Dataset used in the the book](./data/superstore/)

### Chapter 8 - Generative AI for data preparation
**Note:** This chapter utilizes Google AI's capabilities (specifically, Gemini) because it offers a free-to-use LLM (Large Language Model). To ensure a smooth setup, follow the environment preparation instructions provided [here](./code/README.md#Leveraging-Google-AI).
* [Original Titanic dataset and description](https://www.kaggle.com/competitions/titanic)
* [Chapter python code](./code/chapter%208/)
* [Dataset used in the the book](./data/titanic/)

### Chapter 9 - Visual data preparation with Alteryx
**Note:** In this chapter, we’ll use Alteryx *v2024.1.1.93 Patch:3* to demonstrate how to leverage a visual data preparation solution. To get started, you’ll need to install the Alteryx client. The installation procedure is described [here](./code/README.md#Installing-Alteryx).

The Alteryx exports (yxmd files) can be found [here](./code/chapter%209/), you can just copy the file on your desktop and open them by using the Alteryx client.

### Chapter 10 - Data preparation at scale
**Note:** In this chapter, we’ll use [databricks Community Edition](https://community.cloud.databricks.com) to illustrate how to manage a dataset in a ditributed environment (Spark).
* [Messy Food Waste Dataset](https://www.kaggle.com/competitions/messy-food-waste-prediction-dataset/data)
* [Chapter python notebooks](./code/chapter%2010/)
* [Dataset used in the the book](./data/messy-food-waste/)

# Profiling
Most of the datasets used in this book have already been profiled. The outcomes can be found [here](/profiles).
