# 키, 몸무게, 결과 변수 생성 후 0으로 초기화.
height = 0
weight = 0
result = 0

# BMI 지수의 기준점을 aar 배열을 생성하여 초기화.
arr = [18.5, 23, 25]

# input을 사용하여 키를 입력받음.
# try-except를 사용하여 예외처리함.
# height에 입력받은 문자열을 float으로 변환.
# try: 실행시킬 구문
try:
    height = float(input("당신의 키를 입력해주세요.\n"))
    
# except: 오류 발생 시 출력구문
except:
    print("숫자로 입력해주세요.\n")
    
    # exit()를 사용하여 오류 발생 시 프로그램 종료.
    exit()
    
# input을 사용하여 키를 입력받음.
# try-except를 사용하여 예외처리함.  
# weight에 입력받은 문자열을 float으로 변환.
# try: 실행시킬 구문
try:
    weight = float(input("당신의 몸무게를 입력해주세요\n"))
    
# except: 오류 발생 시 출력구문
except:
    print("숫자로 입력해주세요.\n")
    
    # exit()를 사용하여 오류 발생 시 프로그램 종료.
    exit()
    	

# BMI 지수를 계산하는 공식. 몸무게를 키의 제곱으로 나누는데 몸무게는 Kg이고 키는 m이기 때문에 단위를 맞춰준다. 
# ex) 몸무게 70, 키 170일 경우 70 / 1.7 로 계산한다. 
# 계산 후 소수점 자리를 맞추기 위해 100을 곱함.
result = (weight / (height * height * 0.01)) * 100

# f-string을 사용하여 결과값을 소숫점 두자리수 까지만 출력하며, 소수점 3자리에서 반올림한다.
fresult = f"{result:.2f}"

# 결과값을 출력한다. 기존 코드에서는 str을 사용하여 결과값을 출력했다. 
# 파이썬에서는 문자열과 숫자의 +를 허용하지 않기 때문에 str을 사용하여 문자열로 바꿔주어야 한다.
print("당신의 BMI 지수는 " + str(fresult) + " 입니다.\n")

# 조건문
# result가 arr[0]에 해당하는 18.5보다 작으면 출력
if float(fresult) < arr[0]:
	print("당신은 저체중입니다.\n")
 
# result가 arr[0]에 해당하는 18.5보다 크고, arr[1]에 해당하는 23보다 작으면 출력한다. &를 사용하여 두 조건 모두 만족해야한다.
elif (float(fresult) > arr[0]) & (float(fresult) < arr[1]):
	print("당신은 정상체중입니다.\n")

# result가 arr[1]에 해당하는 23보다 크고, arr[2]에 해당하는 25보다 작으면 출력한다. &를 사용하여 두 조건 모두 만족해야한다.
elif (float(fresult) > arr[1]) & (float(fresult) < arr[2]):
	print("당신은 과체중입니다.\n")

# result가 arr[2]에 해당하는 25보다 크면 출력.
elif float(fresult) > arr[2]:
	print("당신은 비만입니다.\n")