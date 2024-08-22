import gradio as gr
import pandas as pd
import requests

# Define a function that handles the API request
def send_request(file):
    # Load the CSV file into a pandas DataFrame
    df = pd.read_csv(file.name)

    # Convert DataFrame to JSON (this depends on your API requirements)
    data_json = df.to_json(orient='split')
    payload = {'data': data_json}

    # Example API endpoint (replace with your actual endpoint)
    url = "http://api:8000/best_model"

    # Send POST request to the API (you may need to adjust headers and data format)
    response = requests.post(url, json=payload)

    res = pd.read_json(response.json()['pred'], orient='split')
    res.columns = ['Prediction']
    pred_res = pd.concat([df, res], axis=1)

    # Return the response from the API
    return pred_res

# Create a Gradio interface
with gr.Blocks() as demo:
    # Add a file uploader for CSV files
    csv_file = gr.File(label="Upload your CSV file")

    # Add a button to trigger the API request
    submit_button = gr.Button("Send to API")

    # Define the action when the button is clicked
    submit_button.click(fn=send_request, inputs=csv_file, outputs=gr.JSON(label="API Response"))

# Launch the interface
demo.launch()