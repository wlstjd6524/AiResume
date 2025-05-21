# reference_based_scoring.py

import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from src.preprocessing.cleaner import clean_text
from src.features.embedding import get_tfidf_vectors

def main():
    # 1. 데이터 불러오기 및 전처리
    df = pd.read_csv("data/Resume.csv")
    df['cleaned'] = df['Resume_str'].apply(clean_text)

    # 2. 기준 이력서 로딩 및 전처리
    with open("data/reference_resume.txt", "r", encoding='utf-8') as f:
        reference_text = f.read()
    reference_cleaned = clean_text(reference_text)

    # 3. 벡터화
    corpus = df['cleaned'].tolist() + [reference_cleaned]
    vectors, vectorizer = get_tfidf_vectors(corpus)
    reference_vector = vectors[-1]  # 마지막이 기준 이력서
    resume_vectors = vectors[:-1]   # 앞부분이 일반 이력서

    # 4. 유사도 계산
    similarities = cosine_similarity(reference_vector.reshape(1, -1), resume_vectors)[0]
    df['similarity_score'] = similarities

    # 5. 상위 이력서 출력
    top_n = df.sort_values(by='similarity_score', ascending=False).head(5)

    print("\n 기준 이력서 기반 상위 5개 이력서 점수 및 일부 내용:\n")
    for idx, row in top_n.iterrows():
        print(f" 이력서 인덱스: {idx}")
        print(f" 유사도 점수: {row['similarity_score']:.4f}")
        print(f" 원본 내용 일부:\n{row['Resume_str'][:300]}...")
        print("-" * 80)

if __name__ == "__main__":
    main()