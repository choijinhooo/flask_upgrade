from flask import Flask, render_template, request
import random
import requests
import json
from faker import Faker


app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
    
@app.route('/lotto')
def lotto():
    #로또 정보 가져오기
    url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=837"
    res = requests.get(url).text
    lotto_dict = json.loads(res)
    
    #1등 당첨 번호를 week 리스트에 넣기
    week = []
    for i in range(1,7):
        number = lotto_dict["drwtNo{}".format(i)]
        week.append(number)
        
    # 보너스 번호를 bonus 변수에 넣기
    bonus = lotto_dict["bnusNo"]
    
    #임의의 로또 번호 생성
    num_list = range(1,46)
    pick = random.sample(num_list,6)
    pick.sort()
    
    #비교해서 몇등인지 저장하기
    match = len(set(pick) & set(week))
    
    if match==6:
        text = "1등"
    elif match==5:
        if bonus in pick:
            text = "2등"
        else:
            text = "3등"
    elif match==4:
        text = "4등"
    elif match==3:
        text = "5등"
    else:
        text = "꽝"
        
    
    
    # cnt = 0
    # for n in pick:
    #     if n in week:
    #         cnt=cnt+1
    #         print(cnt)
    
    # if cnt==6:
    #     rank=1
    # elif cnt==5:
    #     rank=2
    # elif cnt==4:
    #     rank=3
    # elif cnt==3:
    #     rank=4
    # elif cnt==2:
    #     rank=5
    # else:
    #     rank="꼴"
        
   
    # 사용자에게 데이터 넘겨주기
    return render_template("lotto.html",lotto=pick, week=week, text=text)
    

@app.route('/ping')
def ping():
    return render_template("ping.html")
   
@app.route('/pong')
def pong():
    input_name = request.args.get('name')
    fake = Faker('ko_KR')
    fake_job = fake.month_name()
    return render_template("pong.html", html_name=input_name, fake_job=fake_job)
    