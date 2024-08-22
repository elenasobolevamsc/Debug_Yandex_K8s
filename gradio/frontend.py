import gradio as gr
import pandas as pd
import requests

# Define a function that handles the API request
def send_request(file):
    # Load the CSV file into a pandas DataFrame
    df = pd.read_csv(file.name)

    # Convert DataFrame to JSON (this depends on your API requirements)
    data_json = df.to_json(orient="records")

    # Example API endpoint (replace with your actual endpoint)
    url = "https://api.example.com/endpoint"

    # Send POST request to the API (you may need to adjust headers and data format)
    response = requests.post(url, json={"data": data_json})

    # Return the response from the API
    return response.json()

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