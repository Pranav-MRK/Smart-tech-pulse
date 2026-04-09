from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings


# start Embeddings 
embedding_model = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

#  load vector 
vector_db = Chroma(
    collection_name="news_collection",
    embedding_function=embedding_model,
    persist_directory="./chroma_db"
)
def store_news(news_list):
    documents = []

    for news in news_list:
        content = f"{news['title']} {news['summary']}"
        documents.append(content)

    vector_db.add_texts(documents)
    vector_db.persist()

def query_news(user_interests):
    query = " ".join(user_interests)

    results = vector_db.similarity_search(query, k=5)

    return [doc.page_content for doc in results]
