# Prasunet_ML_05

## Task Description:
Develop a model that can accurately recognize food items from images and estimate their calorie content, enabling users to track their dietary intake and make informed food choices.

### Dataset Used:
https://www.kaggle.com/datasets/dansbecker/food-101

## Project Overview

This project involves building a deep learning model using a pretrained ResNet50 architecture for classifying food images. The model has been trained to predict various food items and estimate their calorie content. Additionally, a Flask web application has been created to serve the model, allowing users to upload an image of food and receive the predicted food item along with an estimated calorie count.

## Project Structure

### Model: 
The deep learning model was built using the ResNet50 architecture pretrained on the ImageNet dataset. The model was fine-tuned to classify food images based on a custom food dataset.
### Flask Application: 
The Flask web application serves the model. Users can upload food images through the interface, and the app will respond with the predicted food item and calorie estimation.

### To run the Project, follow these steps:
1. Open the food_Calorie_Detection.ipynb in Google Colab.
2. Connect to a GPU runtime and run the jupyter file.
3. Save the best_model_10classes file in local storage.
4. Git clone the Repository.
5. Install all dependecies.
6. Change current working directory to root of this repo.
7. Execute flask run.
