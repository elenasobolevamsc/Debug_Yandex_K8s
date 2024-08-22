FROM python:3.10-slim

WORKDIR /app

COPY frontend.py .

COPY requirements.txt .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

EXPOSE 7860

# Define environment variable
ENV GRADIO_SERVER_NAME="0.0.0.0"
ENV GRADIO_SERVER_PORT="7860"

# Run the Gradio app
CMD ["python", "frontend.py"]