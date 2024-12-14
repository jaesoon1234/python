# 키, 몸무게, 결과를 나타낼낼 변수 생성 후 0으로 초기화.
height = 0
weight = 0
result = 0

# BMI 지수의 기준점을 aar 배열을 생성하여 초기화.
arr = [18.5, 23, 25]

# while 문을 사용하여 프로그램을 반복 시킴. True를 통해 무한반복.
while True:
    # try-except를 사용하여 예외처리함.
    # try: 실행시킬 구문.
    try:
        # input을 사용하여 키를 입력받음.
        # height에 입력받은 문자열을 float으로 변환.
        height = float(input("당신의 키를 입력해주세요. (단위: cm)\n"))
    
    # except: 오류 발생 시 출력구문, 숫자로 입력하지 않으면 해당 print문이 출력.
    except:
        print("숫자로 입력해주세요.\n")
    
        # continue를 사용하여 오류 발생 시(숫자를 입력하지 않으면) 다시 입력하도록 함.
        continue
    
    # try-except를 사용하여 예외처리함.  
    # try: 실행시킬 구문.
    try:
        # input을 사용하여 몸무게를 입력받음.
        # weight에 입력받은 문자열을 float으로 변환.
        weight = float(input("당신의 몸무게를 입력해주세요 (단위: kg)\n"))
    
    # except: 오류 발생 시 출력구문, 숫자로 입력하지 않으면 해당 print문이 출력.
    except:
        print("숫자로 입력해주세요.\n")
    
        # continue를 사용하여 오류 발생 시(숫자를 입력하지 않으면) 다시 입력하도록 함.
        continue
        
    # BMI 지수를 계산하는 공식. 몸무게를 키의 제곱으로 나누는데 몸무게는 Kg이고 키는 m이기 때문에 단위를 맞춰준다. 
    # ex) 몸무게 70, 키 170일 경우 70 / 1.7 로 계산한다. 
    result = weight / ((height * 0.01) ** 2)

    # f-string을 사용하여 결과값을 소수점 두자리수 까지만 출력하며, 소수점 3자리에서 반올림한다.
    fresult = f"{result:.2f}"

    # 결과값 출력. 파이썬에서는 문자열과 숫자의 +를 허용하지 않기 때문에 str을 사용하여 문자열로 바꿔주어야 한다.
    print("당신의 BMI 지수는 " + str(fresult) + " 입니다.\n")

    # 조건문
    # result가 arr[0]에 해당하는 18.5보다 작으면 출력.
    if float(fresult) < arr[0]:
        print("당신은 저체중입니다.\n")
     
    # result가 arr[0]에 해당하는 18.5보다 크고, arr[1]에 해당하는 23보다 작으면 출력한다. &를 사용하여 두 조건 모두 만족해야한다.
    elif (float(fresult) > arr[0]) and (float(fresult) < arr[1]):
        print("당신은 정상체중입니다.\n")

    # result가 arr[1]에 해당하는 23보다 크고, arr[2]에 해당하는 25보다 작으면 출력한다. &를 사용하여 두 조건 모두 만족해야한다.
    elif (float(fresult) > arr[1]) and (float(fresult) < arr[2]):
        print("당신은 과체중입니다.\n")

    # result가 arr[2]에 해당하는 25보다 크면 출력.
    elif float(fresult) > arr[2]:
        print("당신은 비만입니다.\n")
        
    # 반복문 루프가 한 번 돌아가면 구분하기 위하여 출력.
    print("----------------------------------\n")
    
    # exit_program이라는 변수를 만들어 input으로 입력받아서 루프가 한 번 끝난 후 프로그램을 종료할 것인지, 계속 사용할 것인지를 입력받음.
    exit_program = input("[프로그램을 종료하려면 '종료'를 입력해주세요. 계속하려면 Enter 키를 눌러주세요.]\n")
    
    # 조건문, 입력받은 exit_program을 == 연산자를 사용하여 '종료'와 같은지 아닌지를 판별한다.
    if exit_program == '종료':
        
        # 위 반복문이 참이라면 해당 print문을 출력한다.
        print("프로그램 종료.")
        
        # print문 출력 후 exit()를 사용하여 프로그램을 종료한다.
        exit()