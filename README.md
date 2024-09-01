# **Next Word Prediction with LSTM and GRU**

This project provides a web application for predicting the next word in a sequence using pre-trained LSTM and GRU models. The application is built with Streamlit and utilizes Keras models and tokenizers for text processing and prediction.

## **Project Overview**

The application allows users to input a sequence of words and select either an LSTM or GRU model to predict the next word in the sequence. The prediction is based on pre-trained models and a tokenizer saved using Pickle.

## **Features**

- **LSTM and GRU Models**: Two different models for next-word prediction.
- **Tokenizer**: A tokenizer for converting text to sequences of integers.

## **Requirements**

- Python 3.x
- NumPy
- TensorFlow


You can install the required libraries using:

```bash
pip install -r requirement.txt
```

## Code Overview

### Building and Training the Models

The `building_model.ipynb` notebook contains the code for:

1. **Data Collection**:
   - Loads Shakespeare's Hamlet text from the NLTK corpus and saves it to `hamlet.txt`.

2. **Text Processing**:
   - Tokenizes the text and creates input sequences for training.
   - Pads sequences to ensure uniform input size.

3. **Model Training**:
   - Defines and trains an LSTM model and a GRU model using TensorFlow/Keras.
   - Saves the trained models to `next_word_lstm.h5` and `next_word_gru.h5`, respectively.

4. **Model Prediction**:
   - Defines a function to predict the next word based on the trained model and input text.

5. **Saving the Models**:
   - Saves the tokenizer and models to files for future use.


## **Files**

1. **`next_word_lstm.h5`**: Pre-trained LSTM model for next-word prediction.
2. **`next_word_gru.h5`**: Pre-trained GRU model for next-word prediction.
3. **`tokenizer.pickle`**: Pickle file containing the tokenizer used for text preprocessing.


## Running the Code

1. Install the required packages.
2. Ensure that `next_word_lstm.h5`, `next_word_gru.h5`, and `tokenizer.pickle` are in the same directory as your script.
3. Run the provided example code or integrate it into your own application.


## **Notes**

- Ensure that the model files and tokenizer pickle file are located in the same directory as `app.py`.
- The models should be trained and saved using similar architecture and tokenization settings.



