import pandas as pd
import random
from sklearn.metrics.pairwise import cosine_similarity
from src.preprocessing.cleaner import clean_text
from src.features.embedding import get_tfidf_vectors
from src.training.cluster import cluster_resumes

# 점수 계산 함수 (유사도 기반)
def score_resume_to_best_cluster(resume_vector, cluster_centers):
    similarities = cosine_similarity(resume_vector, cluster_centers)
    return similarities.max()  # 가장 높은 유사도 반환

# 1. 데이터 불러오기
df = pd.read_csv("data/Resume.csv")

# 2. 전처리
df['cleaned'] = df['Resume_str'].apply(clean_text)

# 디버깅 출력: 원본 및 전처리 결과 확인
print("==== 디버깅: 전처리 결과 확인 ====")
sample_idx = random.randint(0, len(df) - 1)
print("원본 이력서 (랜덤 선택):\n", df['Resume_str'][sample_idx])
print("\n전처리된 이력서:\n", df['cleaned'][sample_idx])
print("=================================\n")

# 3. 벡터화
vectors, vectorizer = get_tfidf_vectors(df['cleaned'])

# 4. 클러스터링
model = cluster_resumes(vectors)
cluster_centers = model.cluster_centers_

# 5. 점수화 (랜덤으로 3~5개 이력서 선택해서 점수 계산)
num_samples = random.randint(3, 5)
print(f"\n 랜덤 선택된 {num_samples}개 이력서의 클러스터 기반 점수:\n")

for _ in range(num_samples):
    idx = random.randint(0, len(df) - 1)
    selected_vector = vectors[idx].reshape(1, -1)

    score = score_resume_to_best_cluster(selected_vector, cluster_centers)
    print(f"이력서 인덱스: {idx} | 점수 (최고 유사도 기준): {score:.4f}")

# 6. 전체 이력서에 대해 최고 점수 계산
print("\n 전체 이력서에 대해 최고 유사도 점수 계산 중...\n")
similarities = cosine_similarity(vectors, cluster_centers)
df['score'] = similarities.max(axis=1)

# 7. 상위 이력서 추출 및 출력
top_n = 10
top_resumes = df.sort_values(by='score', ascending=False).head(top_n)

print(f" 상위 점수 이력서 Top {top_n}:\n")
for i, row in top_resumes.iterrows():
    print(f"이력서 인덱스: {i} | 점수: {row['score']:.4f}")
    print("----- 전처리된 내용 일부 -----")
    print(row['cleaned'][:300], "...\n")
