from src.helper import load_pdf, text_split, download_hugging_face_embeddings
from pinecone import Pinecone, ServerlessSpec
from langchain.vectorstores import Pinecone as PineconeVectorStore
from dotenv import load_dotenv
import os


load_dotenv()

data = load_pdf("data/")
text_chunks = text_split(data)
embeddings = download_hugging_face_embeddings()


#Pinecone Information

pc = Pinecone(
    api_key=os.environ.get("PINECONE_API_KEY")
)

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