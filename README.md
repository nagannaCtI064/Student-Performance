
# Predicting Student Performance

## **Overview**
This project predicts student performance using machine learning techniques. It features a frontend built with HTML/CSS and a backend implemented in Flask, with MongoDB used to store predicted values. The objective is to provide a user-friendly interface where users can input student data and receive performance predictions based on a trained machine learning model.

## **Features**
- **Prediction Model**: Utilizes machine learning algorithms to predict student performance.
- **Data Processing**: Implements data preprocessing techniques and feature engineering to optimize model performance.
- **Frontend**: User-friendly interface built with HTML/CSS for data input and result display.
- **Backend**: Flask application handling data requests and model predictions.
- **Database**: MongoDB for storing input data and prediction results.
- **Visualization**: Provides visual insights into model predictions and performance metrics.

## **Technologies Used**
- Python
- Flask
- MongoDB
- HTML/CSS
- JavaScript (if applicable)
- Machine Learning Algorithms (e.g., Random Forest, Gradient Boosting)

## **Installation**
1. Clone the repository:https://github.com/nagannaCtI064/Student-Performance/
2. Install dependencies:requirements.txt
3. Set up MongoDB:
- Install MongoDB from [here](https://www.mongodb.com/try/download/community).
- Start the MongoDB server:
  ```
  mongod
  ```
- Create a database and collection for storing student data and predictions.

4. Configure the database connection:
- Update the MongoDB connection string in your Flask application.

## **Usage**
1. Navigate to the project directory:local
2. Start the Flask server:python app.py
3. Open your web browser and go to `http://localhost:5000` to access the application.
4. Input student data through the web interface and submit to receive performance predictions.

## **Screenshots**
**INPUT**
![image](https://github.com/user-attachments/assets/161953b1-c382-47ca-a82f-fc4c7292f6b2)

![image](https://github.com/user-attachments/assets/69905d69-4471-47f3-acf7-c64f457a88ad)
**PREDICTING GRADE**
![image](https://github.com/user-attachments/assets/3b563ae6-c0f3-45d9-ac5f-b5757a02166f)

**DATA STRORED IN MONGODB**
![image](https://github.com/user-attachments/assets/bac39f8c-272e-43ca-bf04-7782ee409fb6)


## **Contributing**
Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

## **License**
This project is licensed under the Apache License - see the LICENSE file for details.

