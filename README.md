#Twitoff Bloom
Twitoff Bloom is a web application built with Python and Flask that allows users to analyze and predict Twitter user behavior based on their tweets. This application integrates with the Twitter API to fetch user data and tweets, which are then processed and stored in a SQLite database. It also utilizes natural language processing (NLP) techniques to vectorize tweet text and perform machine learning-based predictions.

Features
User Data Retrieval: Fetches user information and tweets from Twitter using the Twitter API.
Data Storage: Stores user data and tweets in a SQLite database for efficient retrieval and analysis.
Text Vectorization: Utilizes the spaCy library to vectorize tweet text, converting it into numerical representations.
Machine Learning Prediction: Implements logistic regression to predict user behavior based on tweet content.
Web Interface: Provides a user-friendly web interface to interact with the application and view prediction results.
Installation
To run the Twitoff Bloom application locally, follow these steps:

Clone the repository: git clone https://github.com/Adamfroggy/Twitoff_bloom.git
Navigate to the project directory: cd Twitoff_bloom
Install dependencies: pip install -r requirements.txt
Set up environment variables: Create a .env file with your Twitter API keys.
Initialize the SQLite database: flask reset
Start the Flask server: flask run
Usage
Once the application is running, you can access it via your web browser at http://localhost:5000. Use the provided interface to interact with the application, retrieve user data, and make predictions based on tweet content.

Contributing
Contributions to Twitoff Bloom are welcome! If you encounter any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request on GitHub.

Credits
This project was developed by [Your Name] as part of a [course, personal project, etc.]. It utilizes various open-source libraries and tools, including Flask, tweepy, spaCy, and scikit-learn.

License
This project is licensed under the MIT License. See the LICENSE file for more details.
