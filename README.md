# Semantic Search using Vector Database
## Project Overview
Traditional keyword-based search often fails to capture the actual meaning of user queries. This project builds a semantic search system that retrieves similar customer reviews based on meaning using vector embeddings and FAISS.

## Objective
Develop a system that:
- Converts customer reviews into vector embeddings
- Stores them in a vector database
- Retrieves similar reviews based on semantic meaning

## Key Concepts Used
- Embeddings (Vector Representation)
- Vector Database (FAISS)
- Approximate Nearest Neighbor (ANN)
- Semantic Search vs Keyword Search

## Project Structure
```
SEMANTIC_SEARCH_USING_VECTOR_DB/
|
|-- data/
|   |-- 7817_1.csv             # Dataset (Amazon reviews)
|
|-- src/
|   |-- load_and_clean_data.py # Data loading & preprocessing
│   |-- embedder_and_searching.py # Embedding + FAISS search
│   |-- main.py                # Entry point for running system
│                 
|-- requirements.txt           # Dependencies
|-- .gitignore
|-- README.md
```

## How it works
1. Data Preprocessing
    - Load Amazon review dataset
    - Clean text (remove noise, lowercasing, etc.)

2. Vector Representation (Embeddings)
    - Convert each review into a vector using a model (e.g., Sentence Transformers)
    - These vectors capture semantic meaning

3. Vector Database (FAISS)
    - Store embeddings using FAISS index
    - Enables fast similarity search

4. Approximate Nearest Neighbor (ANN)
    - Instead of brute-force comparison, FAISS finds closest vectors efficiently
    - Improves speed significantly for large datasets

5. Query Flow
    - When user inputs a query:
        - Convert query → embedding
        - Search FAISS index
        - Retrieve Top 5 similar reviews

## Installation
```
Clone the repository
-> git clone https://github.com/Parashuram-V-Pawar/Semantic_search_using_vector_db.git

Move to project folder
-> cd Semantic_search_using_vector_db

Create Virtual Environment
-> python -m venv venv
-> source venv/bin/activate   # Mac/Linux
-> venv\Scripts\activate      # Windows

Install Dependencies
-> pip install -r requirements.txt

Run project
-> python3 -m src.main.py
```

## Author
```
Parashuram V Pawar
GitHub username: Parashuram-V-Pawar
```