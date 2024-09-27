from flask import Flask, render_template, jsonify, request
from src.helper import download_hugging_face_embeddings
from pinecone import Pinecone, ServerlessSpec
from langchain.vectorstores import Pinecone as PineconeVectorStore
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain.llms import LlamaCpp
from dotenv import load_dotenv
from src.prompt import *
import os





app = Flask(__name__)

load_dotenv()

pc = Pinecone(
    api_key=os.environ.get("PINECONE_API_KEY")
)
embeddings = download_hugging_face_embeddings()
index_name = "medbotest"

if index_name not in pc.list_indexes().names():
    pc.create_index(
        name=index_name, 
        dimension=384,  
        metric='cosine',  
        spec=ServerlessSpec(
            cloud='aws',
            region='us-west-2'
        )
    )


docsearch=PineconeVectorStore.from_existing_index(index_name, embeddings)

PROMPT=PromptTemplate(template=prompt_template, input_variables=["context", "question"])
chain_type_kwargs={"prompt": PROMPT}

llm = LlamaCpp(
    model_path="./model/llama-2-7b-chat.Q4_0.gguf",
    temperature=0.8,
    max_tokens=512,
    n_gpu_layers=-1,  
)

qa = RetrievalQA.from_chain_type(
    llm=llm, 
    chain_type="stuff", 
    retriever=docsearch.as_retriever(search_kwargs={'k': 2}),
    return_source_documents=True, 
    chain_type_kwargs=chain_type_kwargs
)

@app.route("/")
def index():
    return render_template('chat.html')

@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    print(input)
    result=qa({"query": input})
    print("Response : ", result["result"])
    return str(result["result"])



if __name__ == '__main__':
    app.run(host="0.0.0.0", port= 8080, debug= True)
