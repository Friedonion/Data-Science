# 데이터 사이언스 (Data Science, ITE4005) 프로그래밍 과제

한양대학교 컴퓨터소프트웨어학부 **데이터 사이언스(ITE4005)** 과목의 프로그래밍 과제 저장소입니다.  
라이브러리 의존성 없이 순수 Python(Pure Python)으로 알고리즘들을 최적화하여 구현하였습니다.

## 👤 개발자 정보
* **학번**: 2020055350
* **이름**: 강현중

---

## 📂 과제 요약

| 과제명 | 폴더명 | 적용 알고리즘 | 실행 명령어 예시 |
| :--- | :--- | :--- | :--- |
| **SP1** | [`sp1_apriori`](./sp1_apriori/) | Apriori (연관 규칙) | `python apriori.py 5 input.txt output.txt` |
| **SP2** | [`sp2_decision_tree`](./sp2_decision_tree/) | Decision Tree (의사결정나무) | `python dt.py dt_train.txt dt_test.txt dt_result.txt` |
| **SP3** | [`sp3_dbscan`](./sp3_dbscan/) | DBSCAN (밀도 기반 클러스터링) | `python clustering.py input1.txt 8 15 22` |

---

## 🔍 과제별 소개

### 1️⃣ SP1: Apriori 알고리즘
* **목표**: 대규모 트랜잭션 데이터베이스에서 빈발 항목 집합을 추출하고 연관 규칙 생성
* **핵심**: 후보 집합 생성 및 가지치기(Pruning)를 통한 탐색 공간 최적화

### 2️⃣ SP2: 의사결정나무 분류기
* **목표**: 정보 획득량(Information Gain) 및 엔트로피(Entropy) 기반의 의사결정나무 학습 및 테스트 분류 예측
* **핵심**: 재귀적 트리 생성 및 범주형 데이터 분류 로직 구현

### 3️⃣ SP3: DBSCAN 알고리즘
* **목표**: 공간상에서 밀도 기반 군집화 수행 및 아웃라이어(Noise) 식별
* **핵심**: **그리드 기반 공간 분할(Grid-based Spatial Partitioning)** 기법을 도입하여 대용량 포인트를 $O(N)$ 성능 수준으로 초고속 탐색 최적화

---

## 🛠️ 공통 빌드 검증
```bash
python -m py_compile sp1_apriori/apriori.py
python -m py_compile sp2_decision_tree/dt.py
python -m py_compile sp3_dbscan/clustering.py
```
*모든 디렉토리 내부에는 상세 시각화 자료와 설계 복잡도가 분석된 **공식 보고서 PDF**(`2020055350.pdf`)가 동봉되어 있습니다.*
