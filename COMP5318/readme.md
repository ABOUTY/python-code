 



COMP5318/COMP4318 – Machine Learning and Data Mining

# Assignment 1: Classification



## 1. Data loading, pre-processing and printing

The dataset for this assignment is the Breast Cancer Wisconsin. It contains 699 examples described by 9 numeric attributes. There are two classes – **class1,** corresponding to benign breast cancer tumours, and **class2**, corresponding to malignant breast cancer tumours. The features are computed from a digitized image of a biopsy sample of breast tissue for a subject.

 

The dataset should be downloaded from Canvas: **breast-cancer-wisconsin.csv**. This file includes the attribute (feature) headings and each row corresponds to one individual. Missing attributes in the dataset are recorded with a **‘?’**.

 

You will need to pre-process the dataset, before you can apply the classification algorithms. Three types of pre-processing are required: filling in the missing values, normalisation and changing the class values. After this is done, you need to print the first 10 rows of the pre-processed dataset.

 

1. Filling in the missing attribute values - The **missing attribute values** should be replaced with the mean value of the column using sklearn.impute.**SimpleImputer**.
2. Normalising the data **- Normalisation** of each attribute should be performed using a min-max scaler to normalise the values between [0,1] with sklearn.preprocessing.**MinMaxScaler**.
3. Changing the class values - The classes **class1** and **class2** should be changed to **0** and **1**

respectively.

4. Print the first 10 rows of the pre-processed dataset. The feature values should be formatted to 4 decimal places using .4f, the class value is an integer. A function **print_data** has been provided in the template to help you achieve this.

 

For example, if your normalised data looks like this:

 

| Clump Thickness | Uniformi  ty of Cell Size | Uniformi ty  of Cell Shape | Marginal Adhesion | Single Epithelial Cell Size | Bare Nuclei | Bland Chromati  n | Normal Nucleoli | Mitose s | Class |
| --------------- | ------------------------- | -------------------------- | ----------------- | --------------------------- | ----------- | ----------------- | --------------- | -------- | ----- |
| 0.1343          | 0.4333                    | 0.5432                     | 0.8589            | 0.3737                      | 0.9485      | 0.4834            | 0.9456          | 0.4329   | 0     |
| 0.1345          | 0.4432                    | 0.4567                     | 0.4323            | 0.1111                      | 0.3456      | 0.3213            | 0.8985          | 0.3456   | 1     |
| 0.4948          | 0.4798                    | 0.2543                     | 0.1876            | 0.9846                      | 0.3345      | 0.4567            | 0.4983          | 0.2845   | 0     |

 

Then your program should print:



 

![文本框: 0.1343,0.4333,0.5432,0.8589,0.3737,0.9485,0.4834,0.9456,0.4329,0 0.1345,0.4432,0.4567,0.4323,0.1111,0.3456,0.3213,0.8985,0.3456,1 0.4948,0.4798,0.2543,0.1876,0.9846,0.3345,0.4567,0.4983,0.2845,0 ](file:///C:/Users/32534/AppData/Local/Temp/msohtmlclip1/01/clip_image002.png)

 

(You need to print the first 10 rows not the first 3.)

 

Please note that we will test your code with another dataset, and your pre-processing should be written

with this in mind. See the “Marking Criteria” section for more detail.

 

## 2. Defining functions for the classification algorithms

 

 

### Part 1: Cross-validation without parameter tuning

 

You will now apply multiple classifiers to the pre-processed dataset, in particular: Nearest Neighbor, Logistic Regression, Naïve Bayes, Decision Tree, Bagging, Ada Boost and Gradient Boosting. All classifiers should use the **sklearn** modules from the tutorials**.** All random states in the classifiers should be set to **random_state=0**.

 

You need to evaluate the performance of these classifiers using 10-fold stratified cross-validation from

**sklearn.model_selection.StratifiedKFold** with these options:

 

##### cvKFold=StratifiedKFold(n_splits=10, shuffle=True, random_state=0)

 

**You will need to pass cvKFold (the stratified folds) as an argument when calculating the cross-validation accuracy, not cv=10 as in the tutorials. This ensures that random_state=0.**

 

For each classifier, write a function that accepts the required input and returns the average cross-validation score:

 

##### def exampleClassifier(X, y, [options]):

**…**

**return scores.mean()**

where **X** contains the attribute values and **y** contains the class (as in the tutorial exercises). More specifically, the headers of the functions for the classifiers are given below:

## Logistic Regression

##### def logregClassifier(X, y)

**…**

**return scores.mean()**

It should use LogisticRegression from sklearn.linear_model.

 

## Naïve Bayes

##### def nbClassifier(X, y)

**…**

**return scores.mean()**

It should use GaussianNB from sklearn.naive_bayes



## Decision Tree

##### def dtClassifier(X, y)

**…**

**return scores.mean()**

It should use DecisionTreeClassifier from sklearn.tree, with information gain (the entropy criterion)

 

## Ensembles: Bagging, Ada Boost and Gradient Boosting

##### def bagDTClassifier(X, y, n_estimators, max_samples, max_depth)

**…**

**return scores.mean()**

 

 

**def adaDTClassifier(X, y, n_estimators, learning_rate, max_depth)**

**…**

**return scores.mean()**

 

 

**def gbClassifier(X, y, n_estimators, learning_rate)**

**…**

**return scores.mean()**

 

 

These functions should implement Bagging, Ada Boost and Gradient Boosting using BaggingClassifier, AdaBoostClassifier and GradientBoostingClassifier from sklearn.ensemble. Bagging and Ada Boost should combine decision trees and use information gain.

 

 