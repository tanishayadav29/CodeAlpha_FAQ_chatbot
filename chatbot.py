import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


faq = pd.read_csv("faq_data.csv")

questions = faq["question"]

vectorizer = TfidfVectorizer(
    stop_words="english"
)

question_vectors = vectorizer.fit_transform(
    questions
)


def get_response(user_input):

    user_vector = vectorizer.transform(
        [user_input]
    )

    similarity = cosine_similarity(
        user_vector,
        question_vectors
    )

    best_match = similarity.argmax()

    confidence = similarity[0][best_match]

    if confidence < 0.20:
        return (
            "Sorry, I could not find a matching answer."
        )

    return faq.iloc[
        best_match
    ]["answer"]