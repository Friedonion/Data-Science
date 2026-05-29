# 데이터 사이언스 (Data Science, ITE4005) 프로그래밍 과제 모음

한양대학교 컴퓨터소프트웨어학부 **데이터 사이언스(ITE4005)** 과목에서 수행한 3가지 핵심 프로그래밍 과제(Programming Assignments)를 통합 정리한 저장소입니다. 

본 저장소는 다양한 기계학습 및 데이터 마이닝 알고리즘을 파이썬(Pure Python)을 활용하여 라이브러리 의존성 없이 최적의 성능으로 직접 구현하고 검증한 결과물들을 포함하고 있습니다.

## 👤 개발자 정보
* **학번**: 2020055350
* **이름**: 강현중 (Hyunjun Kang)
* **소속**: 한양대학교 컴퓨터소프트웨어학부

---

## 📂 과제별 디렉토리 및 상세 소개

### 1️⃣ SP1: Apriori 알고리즘 ([sp1_apriori](./sp1_apriori/))
* **개요**: 대규모 트랜잭션 데이터베이스로부터 빈발 항목 집합(Frequent Itemsets)을 추출하고, 신뢰도(Confidence)와 지지도(Support)를 계산하여 유의미한 **연관 규칙(Association Rules)**을 생성하는 고전적 데이터 마이닝 알고리즘입니다.
* **구현 방식**: 
  * 라이브러리(Pandas, Mlxtend 등) 없이 순수 Python 데이터 구조만을 활용하여 트랜잭션을 인덱싱하였습니다.
  * 후보 항목 집합(Candidate Itemsets)의 생성 및 가지치기(Pruning) 과정에서 지지도 요건을 충족하지 못하는 항목 집합을 동적으로 제거하여 탐색 공간을 효과적으로 축소하였습니다.
* **실행 명령어**:
  ```bash
  python apriori.py [최소지지도_백분율] [입력파일명] [출력파일명]
  # 예시:
  python apriori.py 5 input.txt output.txt
  ```

### 2️⃣ SP2: 의사결정나무 분류기 ([sp2_decision_tree](./sp2_decision_tree/))
* **개요**: 입력된 훈련 데이터셋(Training Dataset)의 각 속성(Attributes)들을 평가하여 분류 예측 능력을 극대화하는 **의사결정나무(Decision Tree)**를 생성하고, 미지의 테스트 데이터를 올바른 클래스로 예측하는 머신러닝 분류 알고리즘입니다.
* **구현 방식**:
  * 각 속성 분기마다 **엔트로피(Entropy)** 및 **정보 획득량(Information Gain)**을 수학적으로 엄밀하게 구현하여 분기 속성을 선정하였습니다.
  * 재귀적인 트리 생성 및 분류 함수를 내장하여 복잡한 범주형(Categorical) 데이터에 대응하도록 설계하였습니다.
* **실행 명령어**:
  ```bash
  python dt.py [훈련데이터파일명] [테스트데이터파일명] [결과출력파일명]
  # 예시:
  python dt.py dt_train.txt dt_test.txt dt_result.txt
  ```

### 3️⃣ SP3: DBSCAN 밀도 기반 클러스터링 ([sp3_dbscan](./sp3_dbscan/))
* **개요**: 밀도가 높은 공간상의 포인트를 연결하여 군집을 형성하는 대표적인 비지도 학습 알고리즘으로, 공간의 기하학적 형태에 제한을 받지 않고 강인하게 **아웃라이어(Noise/Outlier)**를 식별 및 분류하는 알고리즘입니다.
* **구현 방식**:
  * **그리드 기반 공간 분할 (Grid-based Spatial Partitioning - Cell-based 최적화)** 기법을 독자적으로 구현하였습니다.
  * 공간상의 좌표계를 `Eps` 크기의 격자(Grid) 단위로 사전에 버킷 매핑함으로써, 모든 점의 이웃을 찾기 위해 $O(N^2)$ 시간이 걸리던 전수 탐색 거리를 P가 속한 인접 9개 격자 내부로 좁혀 **$O(N)$ 시간 복잡도 수준으로 극적인 속도 최적화**를 달성하였습니다. (8,000개 이상의 공간 포인트를 0.5초 이내에 분류 가능)
  * 탐색 도중 Core Point와 이전에 노이즈로 오인되었던 경계 점(Border Point)들을 BFS/이웃 큐(`seedSet`) 확장을 통해 정교하게 포섭하도록 구현하였습니다.
* **실행 명령어**:
  ```bash
  python clustering.py [데이터파일명] [희망군집수_n] [Eps] [MinPts]
  # 예시:
  python clustering.py input1.txt 8 15 22
  ```

---

## 🛠️ 공통 실행 및 빌드 검증

본 저장소에 제공되는 모든 소스 코드(`.py`)는 파이썬 기본 런타임 환경에서 동작하도록 빌드 검증이 완료되었으며, 외부 서드파티 패키지가 불필요하므로 이식성이 무척 우수합니다.
```bash
# 구문 무결성 및 정적 빌드 검증 명령어
python -m py_compile sp1_apriori/apriori.py
python -m py_compile sp2_decision_tree/dt.py
python -m py_compile sp3_dbscan/clustering.py
```

각 디렉토리 내부에는 제출했던 공식 한글 보고서인 **`2020055350.pdf`** 문서들이 동봉되어 있으므로, 알고리즘 설계 사상 및 시간복잡도 분석, 시각화 자료(draw.io 및 스크린샷)는 해당 보고서들을 함께 확인하시기 바랍니다.
