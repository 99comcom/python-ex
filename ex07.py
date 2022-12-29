#Dictionary 생성
dic = {}
print(type(dic)) #실행결과: <class 'dict'>
#Dictionary 값 저장
dic['파이썬'] = 'www.python.org'
dic['마이크로소프트'] = 'www.microsoft.com'
dic['애플'] = 'www.apple.com'
print(dic['파이썬'])
print(dic['마이크로소프트'])
print(dic['애플'])
#Dictionary 값 출력
print(dic.get('애플')) #실행 결과: www.apple.com
print(dic.get('자바')) #실행 결과: None print(dic.get('자바', '과목 없음')) #실행 결과: 과목 없음
print(dic) #실행결과: {'파이썬': 'www.python.org', '마이크로소프트': 'www.microsoft.com', '애플': 'www.apple.com'}
#Dictionary에 저장되어 있는 키의 목록과 값의 목록 출력
print(dic.keys()) #실행 결과: dict_keys(['파이썬', '마이크로소프트', '애플'])
print(dic.values()) #실행 결과: dict_items([('파이썬', 'www.python.org'), ('마이크로소프트', 'www.microsoft.com'), ('애플', 'www.apple.com')]) #키와 값의 쌍으로 이루어진 전체 목록 반환
a = dic.items()
print(a) #실행 결과: dict_items([('파이썬', 'www.python.org'), ('마이크로소프트', 'www.microsoft.com'), ('애플', 'www.apple.com')])
print(type(a)) #실행 결과: <class 'dict_items'> #특정키가 목록 안에 존재하는지 확인
print('애플' in dic.keys()) #실행 결과: True print('www.microsoft.com' in dic.values())
#Dictionary 안에 키-값 쌍을 제거
dic.pop('애플')
print(dic) #실행 결과: {'파이썬': 'www.python.org', '마이크로소프트': 'www.microsoft.com'}
#Dictionary 데이터를 남김없이 정리
dic.clear()
print(dic) #실행결과: {}
