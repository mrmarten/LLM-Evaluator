# LLM Evaulator App

This application is a Streamlit-based interface for testing and interacting with several LLM models via APIs (in this example i use Azure). It allows users to input queries and get responses from three models of varying models, The app provides an easy-to-use interface to configure model parameters and retrieve results.

## Features

- **Model Interaction**: Test and compare the performance of three different models using your own inputs.
- **Parameter Configuration**: Customize model behavior by adjusting settings like the number of tokens, temperature, and top-p value to control randomness and diversity of the output.
- **Secure Access**: Password-protected access to ensure only authorized users can interact with the models.
- **Error Handling**: The app handles errors gracefully, displaying appropriate messages when something goes wrong.

## How to Use

1. Clone the repository and navigate to the project directory.
2. Install the required dependencies using:

   ```bash
   pip install -r requirements.txt
   ```

## Create a .env file in the root directory and add your API URLs and keys as shown below:
 

URL1=your_first_model_url
URL2=your_second_model_url
URL3=your_third_model_url
API_KEY_1=your_first_model_api_key
API_KEY_2=your_second_model_api_key
API_KEY_3=your_third_model_api_key
PASSWORD=your_password



## Run the app using the command:

streamlit run app.py
Access the app in your browser at http://localhost:8501.


## Configuration Options

Number of Tokens: Adjust the number of tokens for model inference.
Temperature: Control the randomness of the generated text (higher values produce more random results).
Top P: Control the diversity of the generated text (higher values allow more diverse outputs).


## Error Handling
If the API call fails, the app will display error messages including the HTTP status code and error details, helping you troubleshoot issues with the request.