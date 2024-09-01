# Machine Learning Market Predictor

Author: Jasmine Shrestha

## Overview

The Machine Learning Market Predictor is a sophisticated tool designed to predict stock prices using various machine learning models, including Linear Regression, Random Forest, and LSTM neural networks. The application fetches financial data from Yahoo Finance, performs feature engineering with technical indicators, and allows users to visualize predictions. A user-friendly GUI is provided for easy interaction with the tool.

## Features

- **Data Scraping**: Fetches historical stock data from Yahoo Finance.
- **Feature Engineering**: Adds technical indicators like Moving Averages, RSI, and MACD to the dataset.
- **Model Training**: Supports Linear Regression, Random Forest, and LSTM models for predicting stock prices.
- **Prediction Visualization**: Displays predictions alongside actual stock prices using Matplotlib.
- **Model Comparison**: Allows users to compare the performance of different models based on Mean Squared Error (MSE).
- **Data Management**: Provides options to view, customize date ranges, and save predictions to CSV files.
- **User Interface**: A Tkinter-based GUI for intuitive operation, including buttons for predicting, comparing models, and viewing data.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/machine-learning-market-predictor.git
   cd machine-learning-market-predictor
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   python main.py
   ```

## Usage

1. Launch the application and enter the stock symbol (e.g., AAPL).
2. Choose a prediction model (Linear Regression, Random Forest, LSTM).
3. Click "Predict" to generate and visualize stock price predictions.
4. Use additional features like viewing historical data, comparing models, and saving predictions.

## Directory Structure

- **cache/**: Stores cached stock data to reduce redundant downloads.
- **models/**: Saves trained machine learning models for future use.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

