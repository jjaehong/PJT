# 장고
from django.shortcuts import render

# pandas + 장고
import numpy as np
import pandas as pd
csv_path = 'weathers/data/austin_weather.csv'

# matplotlib + 장고
import matplotlib.pyplot as plt
from io import BytesIO
import base64
plt.switch_backend('Agg')

# 그래프에 한글 활용
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# 데이터 읽어오기
df = pd.read_csv(csv_path)
df.describe()

# Create your views here.

def problem1(request):
    context = {
        'df':df,
    }
    print(df)
    return render(request,'weathers/problem1.html', context)


def problem2(request):

    df = pd.read_csv(csv_path)

    # 그래프 초기화
    plt.clf()


    # 날짜 필드 : 날짜 형식으로 변환
    df["Date"] = pd.to_datetime(df["Date"])

    
    # plot 생성
    plt.plot(df['Date'], df['TempHighF'], label='최고 기온')
    plt.plot(df['Date'], df['TempAvgF'], label='평균 기온')
    plt.plot(df['Date'], df['TempLowF'], label='최저 기온')
    plt.title("온도 변화")
    plt.ylabel("온도(F)")
    plt.xlabel("날짜")    
    plt.legend()

    
    # 데이터 입력받아 이미지 파일 변환
    buffer = BytesIO()
    plt.savefig(buffer,format='png')
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n','')
    buffer.close()

    
    context = {
        'chart_image': f'data:image/png;base64,{image_base64}',
    }

    return render(request, 'weathers/problem2.html',context)


def problem3(request):

    df = pd.read_csv(csv_path)

    # 그래프 초기화
    plt.clf()

    # 날짜 필드 : 날짜 형식으로 변환
    df["Date"] = pd.to_datetime(df["Date"])
    
    # date, 최고기온, 평균기온, 최저기온 만 골라서 df 다시만들고
    df = df[["Date" , "TempHighF" , "TempAvgF", "TempLowF"]]
    # print(df.columns)
    
    # 온도 필드 : 최고기온, 평균기온, 최저기온이 문자열이니까
    # 평균 값 계산을 위해 "숫자 형식"으로 변환
    df["TempHighF"] = pd.to_numeric(df["TempHighF"])
    df["TempAvgF"] = pd.to_numeric(df["TempAvgF"])
    df["TempLowF"] = pd.to_numeric(df["TempLowF"])
    # print(df)

    # 월 별 평균데이터로 변환
    df = df.groupby(df['Date'].dt.to_period('M')).mean()
   
    # plot 생성
    plt.plot(df['Date'], df['TempHighF'], label='최고 기온')
    plt.plot(df['Date'], df['TempAvgF'], label='평균 기온')
    plt.plot(df['Date'], df['TempLowF'], label='최저 기온')
    plt.title("온도 변화")
    plt.ylabel("온도(F)")
    plt.xlabel("날짜")    
    plt.legend()

    # 데이터 입력받아 이미지 파일 변환
    buffer = BytesIO()
    plt.savefig(buffer,format='png')
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n','')
    buffer.close()

    context = {
        'chart_image': f'data:image/png;base64,{image_base64}',
    }

    return render(request,'weathers/problem3.html',context)




def problem4(request):
    
    df = pd.read_csv(csv_path)
    df = df[["Events"]]
    # print(df)

    # cnt 변수
    No_events = 0
    Rain = 0
    Thunderstorm = 0
    Fog = 0
    Snow = 0

    # 총 데이터 돌면서
    for i in range(1319):

        # 쉼표, 공백 전처리 후 split
        df["Events"][i] = df["Events"][i].replace(' , ',' ').split()

        # 리스트로 들어오네?
        print(df["Events"][i])

        # 빈 리스트면?
        if len(df["Events"][i]) == 0:
            No_events += 1

        # 리스트 자체에서 돌면서 + 1
        for j in df["Events"][i]:
            if j == "Rain":
                Rain += 1
            elif j == "Thunderstorm":
                Thunderstorm += 1
            elif j == 'Fog':
                Fog += 1
            elif j == "Snow":
                Snow += 1

    # bar 생성  
    plt.clf()
    x = ['No_events','Rain','Thunderstorm','Fog','Snow']
    y = [No_events,Rain,Thunderstorm,Fog,Snow]
    plt.bar(x,y)
    plt.title("Event Counts")
    plt.ylabel("Count")
    plt.xlabel("Events")

    # 데이터 입력받아 이미지 파일 변환
    buffer = BytesIO()
    plt.savefig(buffer,format='png')
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n','')
    buffer.close()

    context = {
        'chart_image': f'data:image/png;base64,{image_base64}',
    }

    return render(request,'weathers/problem4.html', context)

    