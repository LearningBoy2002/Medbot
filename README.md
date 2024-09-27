# Med bot - Medical Query Assistant

Med bot is an intelligent medical chatbot powered by the Llama-2-7B-Chat model. It's designed to answer medical queries based on information extracted from medical documents in PDF format. The bot uses advanced natural language processing techniques to understand user queries and provide accurate, relevant responses.

## Features

- Utilizes the Llama-2-7B-Chat.Q4_0.gguf model for natural language understanding and generation
- Processes and stores medical knowledge from PDF documents using Pinecone Vector Database
- Provides relevant and accurate responses to medical queries
- Easy to set up and run

## Prerequisites

- Python 3.8.xx
- Pinecone account (for API key)
- Sufficient storage space for the model and medical documents

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/LearningBoy2002/Medbot.git
   cd Medbot
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Create a Pinecone account and obtain your API key.

4. Create a `.env` file in the project root and add your Pinecone API key:
   ```
   PINECONE_API_KEY=your_api_key_here
   ```

5. Download the Llama-2-7B-Chat model:
   - Visit [https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF/blob/main/llama-2-7b-chat.Q4_0.gguf](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF/blob/main/llama-2-7b-chat.Q4_0.gguf)
   - Download the model file
   - Create a folder named `model` in the project root
   - Place the downloaded model file in the `model` folder

6. Prepare your medical documents:
   - Collect medical books or documents in PDF format
   - Place these PDF files in a folder within the project (e.g., `data/`)

## Running the Bot

To start the Med bot, run the following command in your terminal:

```
python app.py
```

The application will start, and you can begin interacting with the bot by sending medical queries.

## Usage

Once the bot is running, you can ask medical questions, and the bot will provide responses based on the information extracted from your medical documents.

## Customization

You can customize the bot by adding more medical documents to improve its knowledge base. Simply add new PDF files to the designated folder, and the bot will incorporate this information in its responses.

## Disclaimer

This bot is for informational purposes only and should not be considered a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of your physician or other qualified health provider with any questions you may have regarding a medical condition.
