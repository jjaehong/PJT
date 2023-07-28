# PJT 02 (23.07.28)

오늘은 데이터 사이언스에 대해서 관통프로젝트를 진행했다. 
부전공으로 IAB융합전공을 해서 그런지 데이터 수집º정제º분석 내용들을 다시금 보니까 반가웠다.
학부시절에는 그렇게 하기 싫어했는데, 지금은 왜이리 반가운지.. 지금은 데이터쪽으로 진로를 생각도 하고 있기에 그런 것 같다.
이쪽 분야로 나아가기 위해선 도메인 지식과 수학 통계적 역량, 컴퓨터 사이언스 역량이 필요한데,
나로서는 수학 통계적 역량이 부족하다고 느끼기에 앞으로 관련 공부를 할 생각이다.


## 학습한 내용

1. Numpy : 빠른 연산

- 기본 배열 : np.arrange() => range()와 유사
- 2차원 배열 생성 : np.arrange().reshape(x,y)
- 특정 수(n)로 이루어진 배열 생성 : np.full((x,y),n)
- random 생성(1차원,2차원) : np.random.rand(n) / np.random(n1,n2)
- np.random.randint(범위, 개수)
- 2차원에서 인덱싱, 슬라이싱

2. Pandas : 편리한 데이터 정제º분석

- csv 읽어오기 : df = pd.read_csv('경로', encoding = 'cp949')
- 데이터 프레임 생성 : df = pd.DataFrame(array 등)
- df 준비 : df.isnull().sum, df.info(), df.describe()
- 버리기 : dropna()
- 채우기 : fillna()
- 어떤 열 기반으로 행을 그룹화 : groupby() => 분할, ~계산, 통합

- 헤더 이름 지정하기 : df.colums = [이름, 나이, 성별, 직업]
- df 정보 : df.info()
- 요약 통계량 : df.describe()
- 특정 행 조회 : df.loc[2]
- 특정 열 조회 : df.loc[:, '이름']
- 특정 행과 열 조회 : df.loc[[2,5],['나이','직업']]
- 행과 열 삽입º추가하기
- 행 삭제
- 중복된 행 조회 : df.duplicated().sum()
- 중복된 행 제거 : df.drop_duplicates(inplace=True)
- 정렬 : df.sort_values(by =[' '])
- 데이터 타입 변화 : astype()


3. matplotlib : 시각화

- 추세선 : plt.plot(x,y)
- 막대그래프 : bar(x,y)
- 히스토그램 : hist(x,y)


4. 데이터 분석

- 상관관계(corr)
- 회귀분석(regression)



## 어려웠던 부분

새로 데이터 프레임을 만드는 과정에서 변수 하나를 잘못 입력해서 시각화가 안됐었다. 이 변수 하나를 찾고 수정하는 과정이 힘들었다.



