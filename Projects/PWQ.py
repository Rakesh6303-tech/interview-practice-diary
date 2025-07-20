---> About : My Project Title was PWQ with MLA. The Main Goal was to predict wine Qualtiy Based on chemical Features using ML Models. & It Helps producers & Consumers.
---> What is ur Role in ur Project?
      I worked as the Backend Developer in My Team project 
      My Responsibility Inclued: Preprocessing the DataSet: Using Python Libraries like Pandas & Numpy.
      My Main tasks Included Data Preprocessing using python,Training & evaluating M.L.M / Like Random Forest,SVM, & KNN & Integrating the best performing model into a Backend Prediction System.
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
