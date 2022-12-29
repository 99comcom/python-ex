def my_abs(number): # 함수 생성 def
    if(number <0):
        result=number * -1
    else:
        result=number
    return result

while True:
    number=input("숫자를 입력하세요?(0:종료)")
    if(number=="0"):
        print("프로그램을 종료합니다.")
        break
    elif(not number.isnumeric()):
      print("숫자로 입력바랍니다.")
      
        
number=input("숫자를 입력하세요")
print("{0}의 절대값은 ={1} ".format(number,my_abs(int(number))))