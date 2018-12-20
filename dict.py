phonebook = {
    "치킨집" : "02-000-0000",
    "피자집" : "062-444-4444"
}
# print(phonebook["치킨집"])

winner = {
    "송민호" : "1살",
    "강민지" : "2살",
    "서상준" : "3살",
    "안현상" : "4살",
    "박현진" : "84세",
}

bts = {
    "피카츄":14,
    "꼬북이":15,
    "라이츄":16,
    "파이리":2,
}

idol = {
    "winner":winner,
    "bts":bts
}
# print(idol)
# print(idol["bts"]["파이리"])


score = {
    "수학":50,
    "국어":70,
    "영어":100
}
# for key, value in score.items():
#     print(key)
#     print(value)
    
# for key in score.keys():
#     # print(key)

# for value in score.values():
#     # print(value)
    
score_sum = 0
for value in score.values():
    score_sum = score_sum + value
#print(score_sum/3)

ssafy = {
    "location": ["서울", "대전", "구미", "광주"],
    "language": {
        "python": {
            "python standard library": ["os", "random", "webbrowser"],
            "frameworks": {
                "flask": "micro",
                "django": "full-functioning"
            },
            "data_science": ["numpy", "pandas", "scipy", "sklearn"],
            "scrapying": ["requests", "bs4"],
        },
        "web" : ["HTML", "CSS"]
    },
    "classes": {
        "gj1":  {
            "lecturer": "ChangE",
            "manager": "pro1",
            "class president": "서희수",
            "groups": {
                "두드림": ["구종민", "김녹형", "윤은솔", "이준원", "이창훈"],
                "런치타임": ["문영국", "박나원","박희승", "서희수", "황인식"],
                "Friday": ["강민지", "박현진", "서상준", "안현상", "최진호"],
                "TMM": ["김훈", "송건희", "이지선", "정태준", "조호근"],
                "살핌": ["문동식", "이중봉", "이지희", "차상권", "최보균"]
            }
        },
        "gj2": {
            "lecturer": "teacher2",
            "manager": "pro2"
        },
        "gj3": {
            "lecturer": "teacher3",
            "manager": "pro3"
        }
    }
}

print(len(ssafy["location"]))

if "requests" in ssafy["language"]["python"]["python standard library"]:
    print("true")
else:
    print("false")
    

print(ssafy["classes"]["gj1"]["class president"])


