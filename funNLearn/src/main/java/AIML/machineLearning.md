## What is Machine Learning?

A computer program is said to learn from experience E with respect to some class of tasks T and performance 
measure P, if its performance at tasks in T, as measured by P,  improves with experience E.

Example: playing checkers.
* E = the experience of playing many games of checkers
* T = the task of playing checkers.
* P = the probability that the program will win the next game.

In general, any machine learning problem can be assigned to one of two broad classifications:

### Supervised learning
In supervised learning, we are given a data set and already know what our correct output should look like, 
having the idea that there is a relationship between the input and the output.

#### Categories: 
* Regression
  + we are trying to predict results within a continuous output, meaning that we are trying to map 
    input variables to some continuous function.

* Classification.  
  + we are instead trying to predict results in a discrete output. In other words, we are trying to map input 
    variables into discrete categories.
  + the output is usually a discrete value(true/false, [0, 1, 2, 3])

#### Examples
* Housing example
  + Given data about the size of houses on the real estate market, try to predict their price. 
    Price as a function of size is a continuous output, so this is a regression problem.
  + We could turn housing example into a classification problem by instead making our output about whether 
    the house "sells for more or less than the asking price." Here we are classifying the houses based on price into 
    two discrete categories.

* Regression - Given a picture of a person, we have to predict their age on the basis of the given picture

* Classification - Given a patient with a tumor, we have to predict whether the tumor is malignant or benign.


### Unsupervised learning
* Unsupervised learning allows us to approach problems with little or no idea what our results should look like. 
  We can derive structure from data where we don't necessarily know the effect of the variables.
* We can derive this structure by clustering the data based on relationships among the variables in the data.
* With unsupervised learning there is no feedback based on the prediction results.

* Examples:
  + Given a set of news articles, group them into sets of articles about the same stories
  + given a database of customer data, automatically discover market segments and group
    customers into different market segments. 
  +  
