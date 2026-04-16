import logging
from src.load_and_clean_data import read_data, clean_data
from src.embedder_and_searching import get_embeddings, vector_search, create_faiss_index, keyword_search

logging.basicConfig(level=logging.INFO)

def main(query):
    logging.info("Reading and cleaning data...")
    data = read_data('data/7817_1.csv')
    cleaned_data = clean_data(data)
    logging.info("Completed reading and cleaning data....")

    logging.info("Getting embeddings for cleaned data...")
    embedded_reviews = get_embeddings(cleaned_data)
    logging.info("Completed getting embeddings for cleaned data....")

    logging.info("Creating FAISS index...")
    index = create_faiss_index(embedded_reviews)
    logging.info("Completed creating FAISS index....")

    logging.info("Performing vector search...")
    results = vector_search(query=query, index=index, reviews=cleaned_data)
    print("\nVector search results:")
    for i, result in enumerate(results):
        print(f"Review {i+1}: {result['review']}\n")
    print("\n")
    logging.info("Completed vector search....")

    logging.info("Performing keyword search...")
    results = keyword_search(query=query, reviews=cleaned_data)
    print("\nKeyword search results:")
    for i, result in enumerate(results):
        print(f"Review {i+1}: {result}")
    print("\n")
    logging.info("Completed keyword search....")    

if __name__ == "__main__":
    logging.info("Starting the searching operation...")
    query = "battery drains fast"
    main(query)
    logging.info("completed the searching operation...")