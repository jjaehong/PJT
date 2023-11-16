
# DataFrame을 생성하는 함수입니다.
def file_open_by_numpy():
    # np.loadtxt를 사용하여 NumPy 배열을 로드합니다.
    np_arr = np.loadtxt('data/test_data_has_null.csv', delimiter=",", encoding='cp949', dtype=str)
    
    # NumPy 배열에서 pandas DataFrame을 생성합니다.
    # 첫 번째 행을 열 이름으로 가정하고 처리합니다.
    column_names = np_arr[0]  # 첫 번째 행을 열 이름으로 사용
    df = pd.DataFrame(np_arr[1:], columns=column_names)  # 첫 번째 행을 제외한 데이터로 DataFrame 생성
    
    return df

# DataFrame을 JSON으로 변환하여 JsonResponse로 반환하는 뷰입니다.
def dataframe_to_json_view(request):
    global df 
    df = file_open_by_numpy()
    
    df.replace('', 'NULL', inplace=True)

    

    # DataFrame을 사전의 리스트로 변환합니다.
    data_records = df.to_dict('records')

    # 평균나이를 구합니다.
    # len_record는 나이가 NULL이 아닌 것들
    total_age = 0
    print(len(data_records))
    len_record = 0
    for record in data_records:
        if record['나이'] != 'NULL':
            len_record+=1 



    for i in range(50):
        if data_records[i]['나이'] != 'NULL':
            total_age += int(data_records[i]['나이'])
    avg_age = total_age/len_record
    print(avg_age)
    # 새로운 레코드 추가 
    for record in data_records:
        if record['나이'] != 'NULL':
            record['나이분산'] = round(abs(int(record['나이'])-avg_age),2)

    # 평균나이와 가장 비슷한 10명을 구합니다.
    closest_ages = sorted(data_records, key=lambda x:x['나이분산'] if x['나이'] != 'NULL' else int(100))[:10]

    # JsonResponse 객체를 생성하여 반환합니다.
    return JsonResponse({'data': data_records, 'closest_ages': closest_ages},json_dumps_params={'ensure_ascii': False})