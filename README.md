# **Next Word Prediction with LSTM and GRU**

This project provides a web application for predicting the next word in a sequence using pre-trained LSTM and GRU models. The application is built with Streamlit and utilizes Keras models and tokenizers for text processing and prediction.

## **Project Overview**

The application allows users to input a sequence of words and select either an LSTM or GRU model to predict the next word in the sequence. The prediction is based on pre-trained models and a tokenizer saved using Pickle.

## **Features**

- **LSTM and GRU Models**: Two different models for next-word prediction.
- **Tokenizer**: A tokenizer for converting text to sequences of integers.
- **Streamlit Interface**: A web-based interface for user interaction.

## **Requirements**

- Python 3.x
- Streamlit
- NumPy
- TensorFlow
- Pickle

You can install the required libraries using:

```bash
pip install streamlit numpy tensorflow
```

## **Files**

1. **`next_word_lstm.h5`**: Pre-trained LSTM model for next-word prediction.
2. **`next_word_gru.h5`**: Pre-trained GRU model for next-word prediction.
3. **`tokenizer.pickle`**: Pickle file containing the tokenizer used for text preprocessing.
4. **`app.py`**: Main Streamlit application file.

## **Usage**

1. **Run the Streamlit Application**:

   Navigate to the directory containing `app.py` and run:

   ```bash
   streamlit run app.py
   ```

2. **Interact with the App**:

   - **Input Text**: Enter a sequence of words in the text input field.
   - **Select Model**: Choose between 'LSTM' and 'GRU' using the dropdown menu.
   - **Predict Next Word**: Click the 'Predict Next Word' button to get the predicted next word.


## **Notes**

- Ensure that the model files and tokenizer pickle file are located in the same directory as `app.py`.
- The models should be trained and saved using similar architecture and tokenization settings.

## **Contact**

For any questions or issues, please contact [Your Name] at [Your Email].

---

This readme provides a comprehensive overview of the project, including setup instructions, code explanations, and usage guidelines.
