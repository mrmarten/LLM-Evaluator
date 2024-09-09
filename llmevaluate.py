import json
import os
import ssl
import streamlit as st

import urllib.request
import urllib.error

from dotenv import load_dotenv

load_dotenv()

def allowSelfSignedHttps(allowed):
    # bypass the server certificate verification on client side
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context

allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.

# Define the URLs for the three different models
urls = [
    os.environ.get('URL1'),
    os.environ.get('URL2'),
    os.environ.get('URL3')
]

# Define the API keys for the three different models
api_keys = [
    os.environ.get('API_KEY_1'),
    os.environ.get('API_KEY_2'),
    os.environ.get('API_KEY_3')
]

# Streamlit app
st.title("Llama 3.1 test")

# User input
user_input = st.text_area("Enter your question", height=200)

# User input for tokens, temperature, and top p

num_tokens = st.number_input("Number of Tokens - Allows the user to input the number of tokens for model inference", value=700)  # Allows the user to input the number of tokens for model inference

# Allows the user to increase the amount of randomness in the generated text
temperature = st.slider("Temperature - Allows the user to increase the amount of randomness in the generated text", min_value=0.1, max_value=1.0, value=0.8, step=0.1)

# Allows the user to control the diversity of the generated text
top_p = st.slider("Top P - Allows the user to control the diversity of the generated text", min_value=0.1, max_value=1.0, value=0.1, step=0.1)

# Password input
password = st.text_input("Enter the password:")
if password != os.environ.get('PASSWORD'):
    st.warning("Incorrect password. Please try again.")
    st.stop()

# Display user input for tokens, temperature, and top p
#st.write("Number of Tokens:", num_tokens)
#st.write("Temperature:", temperature)
# Button to trigger inference
if st.button("Infer"):
    # Inference for each model
    for i in range(len(urls)):
        url = urls[i]
        api_key = api_keys[i]

        if not api_key:
            raise Exception("A key should be provided to invoke the endpoint")

        data = {
            "messages": [
                {
                    "role": "user",
                    "content": user_input
                }
            ],
            "max_tokens": num_tokens,
            "temperature": temperature,
            "top_p": top_p,
            "best_of": 1,
            "presence_penalty": 0,
            "use_beam_search": "false",
            "ignore_eos": "false",
            "skip_special_tokens": "false",
            "stream": "false"
        }

        body = str.encode(json.dumps(data))
        headers = {'Content-Type': 'application/json', 'Authorization': ('Bearer ' + api_key)}
        req = urllib.request.Request(url, body, headers)
        try:
            response = urllib.request.urlopen(req)
            result = response.read()
            if i == 0:
                st.subheader("405B Model:")
            elif i == 1:
                st.subheader("70B Model:")
            elif i == 2:
                st.subheader("8B Model:")
            result = result.decode("utf-8")
            result = json.loads(result)
            message = result["choices"][0]["message"]["content"]
            st.text_area("Response", value=message, height=600)
            st.write("\t", end="")
        except urllib.error.HTTPError as error:
            st.error("The request failed with status code: " + str(error.code))
            st.error(error.info())
            st.error(error.read().decode("utf8", 'ignore'))

# Button to reset the response boxes
if st.button("Reset"):
    st.text_input("Enter your question")
    st.empty()
