import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Load scientific knowledge
with open("knowledge/knowledge.json", "r", encoding="utf-8") as f:
    documents = json.load(f)


# Create searchable text vectors
texts = [doc["content"] for doc in documents]

vectorizer = TfidfVectorizer(stop_words="english")
document_vectors = vectorizer.fit_transform(texts)


def retrieve(query: str, n: int = 5):
    """
    Retrieve the most relevant scientific knowledge
    for a user's environmental question.
    """

    query_vector = vectorizer.transform([query])

    similarities = cosine_similarity(
        query_vector,
        document_vectors
    )[0]

    # Get highest-scoring documents
    top_indices = similarities.argsort()[::-1][:n]

    retrieved = []

    for index in top_indices:
        retrieved.append({
            "content": documents[index]["content"],
            "source": documents[index]["source"],
            "title": documents[index]["title"],
            "topic": documents[index]["topic"],
            "relevance_score": round(
                float(similarities[index]), 3
            )
        })

    return retrieved