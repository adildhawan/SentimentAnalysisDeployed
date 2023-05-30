import streamlit as st
import requests
!uvicorn sentimentapp:app --reload
# Set up the main structure of the Streamlit app
def main():
    st.title('Twitter Sentiment Analysis Dashboard')
    user_input = st.text_area("Enter a tweet for sentiment analysis", "")
    
    if st.button("Analyze"):
        if user_input:
            data = {'text': user_input}
            response = requests.post("http://127.0.0.1:8000/predict", json=data)
            prediction = response.json()
            st.write(f'The predicted sentiment is: {prediction["prediction"]}')
        else:
            st.write("Please enter a tweet for sentiment analysis.")
    
if __name__ == '__main__':
    main()
