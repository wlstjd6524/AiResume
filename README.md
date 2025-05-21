## 👨‍🏫 프로젝트 소개
AI 기반 이력서 분석 및 직무 적합도 평가 시스템

## 💻 개발환경
- Python 3.11.1
- Pandas, Numpy
- scikit-learn
- NLTK

## 📌 프로젝트개요
이 프로젝트는 다양한 이력서를 자동으로 분석하고, 클러스터링과 기준 이력서 유사도를 기반으로 해당 이력서가 특정 직무에 얼마나 적합한지를 정량적으로 평가하는 AI 기반 시스템입니다. 이력서 자동 선별, 채용 필터링, 인재 탐색 자동화에 활용될 수 있습니다.

프로젝트는 크게 두 가지 평가 방식을 지원합니다.

1. **클러스터 기반 평가**  
   TF-IDF 벡터화를 통해 이력서를 수치화하고, KMeans 클러스터링을 통해 이력서들을 자동 분류한 후, 클러스터 중심과의 유사도로 점수를 매깁니다.

2. **기준 이력서 기반 평가**  
   특정 직무(예: JAVA Backend Programmer)의 기준 이력서를 별도 파일로 제공하면, 모든 이력서들과 비교하여 유사도 점수를 계산해 적합한 인재를 선별합니다.

## ✒️ 프로젝트 목표
- 대량의 이력서를 자동 분류하고 분석하여 선별 시간을 단축
- 직무 적합도 기반으로 우수한 인재를 빠르게 식별
- 기준 이력서를 통한 맞춤형 인재 추천 기능 구현
  
## 🔨 프로젝트 아키텍처
![Image](https://github.com/user-attachments/assets/c5bf52bd-b4ef-4ced-ab84-ea67315c394d)

## 🔍 주요 기능
- 이력서 자동 전처리 및 정제 (소문자화, 불용어 제거, 표제어 추출 등)
- TF-IDF 벡터화를 통한 수치화
- KMeans 클러스터링을 통한 그룹화
- 코사인 유사도 기반 유사도 점수 산출
- 기준 이력서를 기반으로 한 직무 적합성 평가

## 📱출력
- 클러스터 기반 평가 main.py 컴파일 결과 <br> <br>
![Image](https://github.com/user-attachments/assets/56e66667-ddc9-408e-9d56-11e8d1675d91)

![Image](https://github.com/user-attachments/assets/85a8b503-4776-40b3-b504-39f38c289fdf)

![Image](https://github.com/user-attachments/assets/a1aad515-9a9b-443a-83c4-592b6ece2f03)

![Image](https://github.com/user-attachments/assets/4e6861b8-2f24-43bd-abee-e17ece460bbc)

![Image](https://github.com/user-attachments/assets/5515c5e5-ded0-47dc-8896-30c7d71ebea9)

- 기준 이력서 기반 평가 reference_base_scoring.py 컴파일 결과 <br> <br>
![Image](https://github.com/user-attachments/assets/511496dd-2996-42b4-9e4c-2286e81235c9)

![Image](https://github.com/user-attachments/assets/0d39b177-1ffa-4527-9113-f9300e4a3eb8)
