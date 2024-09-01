import streamlit as st
import numpy as np
import pickle
from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences

#Load the LSTM Model
model_l=load_model('next_word_lstm.h5')
model_g = load_model('next_word_gru.h5')

#3 Laod the tokenizer
with open('tokenizer.pickle','rb') as handle:
    tokenizer=pickle.load(handle)

# Function to predict the next word
def predict_next_word(model, tokenizer, text, max_sequence_len):
    token_list = tokenizer.texts_to_sequences([text])[0]
    if len(token_list) >= max_sequence_len:
        token_list = token_list[-(max_sequence_len-1):]  # Ensure the sequence length matches max_sequence_len-1
    token_list = pad_sequences([token_list], maxlen=max_sequence_len-1, padding='pre')
    predicted = model.predict(token_list, verbose=0)
    predicted_word_index = np.argmax(predicted, axis=1)
    for word, index in tokenizer.word_index.items():
        if index == predicted_word_index:
            return word
    return None

# streamlit app
st.title("Next Word Prediction With LSTM and GRU ")
input_text=st.text_input("Enter the sequence of Words","To be or not to")
option = st.selectbox('Models :',('LSTM', 'GRU'))
st.write('You selected:', option)
if st.button("Predict Next Word"):
    if option =='LSTM':   
        max_sequence_len = model_l.input_shape[1] + 1  # Retrieve the max sequence length from the model input shape
        next_word = predict_next_word(model_l, tokenizer, input_text, max_sequence_len)
        st.write(f'Next word: {next_word}')
    if option == "GRU":
        max_sequence_len = model_g.input_shape[1] + 1  # Retrieve the max sequence length from the model input shape
        next_word = predict_next_word(model_g, tokenizer, input_text, max_sequence_len)
        st.write(f'Next word: {next_word}')
