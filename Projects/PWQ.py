---> About : 
         My Project Title was PWQ with MLA. 
         The Main Goal was to predict wine Qualtiy Based on chemical Features using ML Models.
        It helps both producers and consumers by estimating wine quality before production or purchase.
--------------------------------------------------------------------------------------------------------------------------------------------------------------
---> What is ur Role in ur Project?
            
##Role :
I worked as the backend developer in our team, where I handled data preprocessing, model training, 
                                       and integrating the best ML model into a backend prediction system.”
## How preprocessing?
   Using Python Libraries like Pandas & Numpy.

## Chemical Attributes
Fixed Acidity , Volatile Acidity , Citric Acid, Residual Sugar  , Chlorides
            
Algorithms use :
“We used different algorithms like Random Forest, SVM, and KNN — and Random Forest performed the best, so we finalized it for prediction.”
-----------------------------------------------------------------------------------------------------------------------------------------------------------
----> Scikit-Learn : is a powerful, open-source 'ML' Library for Python.It Provides Simple & Efficenet Tools for Data Mining, Data Preprocessing analysis etc.
----> Random Forest :  is a powerful 'MLA' used for classification & Regression Tasks.
----> WHY RF? High Accurancy , Handles large Datasets.
----> How it Works RF?
      Data Sampling : It Randomly Selects Subsets of the Training Data
      Feature Selection : For each Tree, It also selects a Random subsets of Features.
      Tree Building : Each Decision Tree is Trained on its own subset.
      voting/Averging : For Classification, Random Forest Takes the Majority vote of all Trees.For Regression, It Takes the average of all Predictions.

----->What Challenges you faced How did you overcome?
      I faced as a Backend Developer included in Data Cleaning, Integrating ML model for Predictions.
      I overcome them by using pandas, sckit-learn & setting up a virtal Environment using Anaconda.
-----> How Did You Implement Backend Logic? With Code?
     Train & Save Model (Done During Development ) 
     Load saved Model in Backend
     Expose Prediction via a simple scripter
---------------------------------------------     
// Code Backed Logic 

   import pandas as pd
   import joblib
   # Load Saved Model & scalar
   Model = joblib.load('random-forest=model.pkl')
   scalar = joblib.load('scalar.pkl')
   def predict_wine_Quality(data):
   # convert I/P dict to Data Frames
   df = pd.Data_frame([data])
   scaled = scalar.taransform(df)
   return model.predict (scaled)[0]
  ----------------------------------------

* joblib : is python library used to save & Load 'MLA'
* PKl : extension stands for 'pickel' used to save python objects(like mlm, scalers)

------------------------------------------------------------------------
Output Prediction 
. 3-4 ---> BAD
. 5-6 ---> AVERAGE
. 7-8 ----> GOOD
---------------------------------------------------------------
Technologies:
IDE : Jupter / Ananconda matplotlib
P.L : Python
Algorithms : ML
H/W : Cpu , Gpu, Ram
Libraries : Pandas, Numpy, Scikit-Learn
--------------------------------------------------
