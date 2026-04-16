import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

def get_embeddings(texts):
    embeddings =  model.encode(texts, show_progress_bar=True)
    embeddings = np.array(embeddings).astype('float32')
    faiss.normalize_L2(embeddings)
    return embeddings

def create_faiss_index(embeddings):
    dimension = embeddings.shape[1]
    index = faiss.IndexHNSWFlat(dimension, 32)
    index.add(embeddings)
    print("Total vectors stored:", index.ntotal)
    return index

def vector_search(query, index=None, reviews=None, top_k=5):
    query_vector = model.encode([query])
    query_vector = np.array(query_vector).astype('float32')
    faiss.normalize_L2(query_vector)
    distances, indices = index.search(query_vector, top_k)
    results = []
    for i, idx in enumerate(indices[0]):
        results.append({
            "review": reviews[idx],
            "score": float(distances[0][i])
        })
    return results

def keyword_search(query, reviews, top_k=5):
    results = []
    for review in reviews:
        if query.lower() in review.lower():
            results.append(review)
        if len(results) >= top_k:
            break
    return results
