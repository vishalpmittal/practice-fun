
### ML AI Pipeline
- Problem Definition 
- Data Sourcing => Data Preparation => Data Segregation
- Model Training => Model Evaluation
- Model Deployment => Model Monitoring

## Numerical Analysis

### Univariant
- __shape__: data shape, x records/ y columns
- __head__: first row in the data with all columns
- __Mean__: simple average considerting all the values
- __Median__: is the value separating lower half from the upper half of the data
- __Percentile__: measure used indicating certain percentage of the dataset is below that value.
- __Standard Deviation__: measure that tells the typical difference between a data value and the mean
- __Maximum__
- __Minimum__
- __Count__: Total # of values
- __Mode__ : Most frequent value
- __Range__ : diff between highest and lowest
- __Outliers__ : data values that are way smaller/larger than the mean. 


### Bivariant

- __Correlation__: measure defining to what extent two or more variables are linearly related. 
  -  __Positive__: increasing one increases the other
  -  __Negative__: increasing one decreases the other
  -  __No__: No relation between the two whatsoever


## Data Visualization 

- Distribution
- Box and whisker plot
  - Upper Extreme
  - Upper Quartile: 75% point
  - Median
  - Lower Quartile: 25% point
  - IQR: Inter Quartile Range (range between upper and lower quartile)
  - Whisker
  - Lower Extreme
  - Outlier  
- Scatter Plot


## Data Scaling
Making your data ready for ML Models
- Sandardization: Removing the mean and scaling to unit variance
- MinMax Scaling: rescaling all attributes to range between zero and one

   Xscaled = (X - Xmin) / (Xmax - Xmin)

- Normalization Scaling: Rescaling each observation (row) to unit value

## Data segregation
segregate data to train vs. data to test. 
- train/test split
- K-Fold Cross Validation: use n-1 sets to train and nth to test. keep swapping the test set. 

## Model Training
- Supervised Learning
  - Regression Algorithm
    - Liner Regression
    - Ridge
    - Lasso
    - Decision Tree..
  - Classification Algorithm

- Unsupervised Learning
  - Clustering Algorithm
  - Pattern Search Algorithm
  - Dimension Reduction Algorithm

- Reinforcement Learning


### Glossary
- Euclidean Distance: distance between two points in euclidean space. Same as distance between two points on an x,y pane. sqrt((x2-x1)^2 + (y2-y1)^2)

- Underfitting: Model predicting without proper trained
- Fitting: prediction with proper trained model

- K-Means Clustering

- Tools 
  - SciPy => NumPy, Matplotlib, Pandas
  - Pandas: Series, DataFrame
  - scikit-learn : open source ML, data mining and analysis library



