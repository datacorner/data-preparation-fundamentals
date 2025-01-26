# Data preparation handbook (code and resources)
[![](img/Cover-book-MEAP.jpg)](https://mng.bz/1XaR)

The [book is currently available in the Manning Early Access Program (MEAP)](https://mng.bz/1XaR)), Feel free to take advantage of this opportunity and share your valuable feedback!

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
* [Chapter python code](./code/chapter%208/)

### Chapter 9 - Visual data preparation with Alteryx
**Note:** In this chapter, we’ll use Alteryx *v2024.1.1.93 Patch:3* to demonstrate how to leverage a visual data preparation solution. To get started, you’ll need to install the Alteryx client. The installation procedure is described [here](./code/README.md#Installing-Alteryx).

The Alteryx exports (yxmd files) can be found [here](./code/chapter%209/), you can just copy the file on your desktop and open them by using the Alteryx client.

### Chapter 10 - Data preparation at scale
Available soon

### Chapter 11 - Trends and future challenges
Available soon

# Profiling
Most of the datasets used in this book have already been profiled. The outcomes can be found [here](/profiles).
