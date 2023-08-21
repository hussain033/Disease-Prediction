# Disease Prediction and Symptom Recommender System

Welcome to the Disease Prediction and Symptom Recommender System repository. This project aims to develop an intelligent system that predicts diseases based on user-entered symptoms and recommends related symptoms to help users identify potential health issues.

## Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)

## Overview

The Disease Prediction and Symptom Recommender System consists of two main components: a disease classification model and a symptom recommender system. The disease classification model predicts diseases based on user-entered symptoms using a Logistic Regression algorithm. The symptom recommender system recommends related symptoms to users based on their last symptom input using a K-Nearest Neighbors (KNN) algorithm.

This system is designed to reduce doctor-patient interactions for common diseases, providing users with preliminary information about potential health issues. Please note that the current version is not yet accurate enough for commercial use and real-time deployment.

## Project Structure

```
├── disease_classification_model.ipynb
├── symptom_recommender_system.ipynb
├── datasets/
│   ├── disease_dataset.csv
│   ├── symptom_dataset.csv
├── README.md
├── .gitignore
└── requirements.txt
```

- `disease_classification_model.ipynb`: Jupyter Notebook containing the disease classification model implementation using Logistic Regression.
- `symptom_recommender_system.ipynb`: Jupyter Notebook containing the symptom recommender system implementation using K-Nearest Neighbors.
- `datasets/`: Directory containing dataset files for diseases and symptoms.
- `README.md`: The documentation you're reading right now.
- `.gitignore`: List of files and directories to be ignored by version control.
- `requirements.txt`: List of libraries required for using the model

## Installation

1. Clone the repository to your local machine using:
   ```
   git clone https://github.com/hussain033/Disease-Prediction.git
   ```
2. Install the required dependencies using:
   ```
   pip install -r requirements.txt
   ```
3. Download the dataset files and place them in the `datasets/` directory.

## Usage

1. Open the Jupyter Notebooks `disease_classification_model.ipynb` and `symptom_recommender_system.ipynb`.
2. Follow the instructions in each notebook to train the models and perform predictions.
3. For deployment in a chatbot interface, further development and integration will be required.

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or improvements, please feel free to open an issue or submit a pull request.



