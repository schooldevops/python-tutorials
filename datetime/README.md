# Python datetime 활용하기

- 날짜 처리는 프로그래밍에서 빠져서는 안되는 매우 중요한 요소이다. 
- 날짜 정보를 포매팅하고, 원하는 날자로 이동하는 등의 날짜 연산을 처리해 보자. 

## 날짜 처리 패키지 모듈 알아보기 

- 날자처리나 패키지 모듈에 대해서 알아 보자. 
- 임포트를 위해서는 2가지 방법을 이용할 수 있다. 
  
```python 
import inspect
import datetime 
from datetime import datetime as dt 

print(inspect.getfile(datetime))
print(inspect.getfile(dt))
```

- 결과 확인하기. 

```go
/usr/local/Cellar/python@3.9/3.9.7/Frameworks/Python.framework/Versions/3.9/lib/python3.9/datetime.py
/usr/local/Cellar/python@3.9/3.9.7/Frameworks/Python.framework/Versions/3.9/lib/python3.9/datetime.py

```

- 결과를 보면 둘다 동일한 datetime.py 모듈을 로드 하고 있다. 

## 로드된 모듈 확인하기 

```python
print(datetime)
print(dt) 
```

```go
<module 'datetime' from '/usr/local/Cellar/python@3.9/3.9.7/Frameworks/Python.framework/Versions/3.9/lib/python3.9/datetime.py'>
<class 'datetime.datetime'>
```

- 그러나 둘은 서로 다른 형태로 임포트 되었다. 
  - import datetime 의 경우 모듈로 로드 되었다. 
  - from datetime import datetime as dt 는 클래스로 로드 되었다. 

- 동일한 모듈이지만 사실 datetime 모듈 내에 datetime 라는 패키지가 있으며 다음을 확인하면 동일한 모듈임을 확인할 수 있다. 

```python
print(datetime.datetime)
print(dt)

print(datetime.datetime.now())
print(dt.now())
```

```go
<class 'datetime.datetime'>
<class 'datetime.datetime'>

2022-01-18 14:46:01.788903
2022-01-18 14:46:01.788924
```

- 우리가 원하는 결과가 나왔다. datetime.datetime 과 dt 는 같은 역할을 하는 클래스임을 확인했다. 
- 지금부터 우리는 `from datetime import datetime as dt` 를 이용하여 datetime 기능을 알아볼 것이다. 

## 날짜 생성하기. 

### 생성자 이용하기. 

```python
from datetime import datetime as dt

d_time = dt(2022, 1, 1, 10, 30, 30)
print(d_time)
```

- 위와 같이 년, 월, 일, 시, 분 ,초 를 이용하여 날자를 생성할 수 있다. 

- 결과

```go
2022-01-01 10:30:30
```

### 현재 날자 조회하기. 

```pytyhon
d_time = dt.now()
print(d_time)
```

- now() 함수를 이용하여 현재 날자를 가져 올 수 있다. 
- 참고로 now() 는 밀리초 단위까지 모두 표현됨을 알 수 있다. 
  
- 결과 
  
```go
2022-01-18 14:57:21.588527
```

## 날자 차이 계산하기. 

- 날짜 타이는 단순히 연산자를 이용하여 날짜 차이를 확인할 수 있다.

```python
d_time1 = dt(2022, 1, 1, 10, 30, 30)
d_time2 = dt.now() 

print(d_time2 - d_time1)
```

- 결과 확인하기 

```go 
17 days, 4:31:34.565786
```

- 17일 차이가 남을 확인할 수 있다. 
- 위 결과를 이용하기에는 어려움로 다음과 같이 내장 필드를 이용할 수 있다. 

### 날자 차이 계산하기 

```python 
print(type(d_time2 - d_time1))
print((d_time2 - d_time1).days)
print((d_time2 - d_time1).seconds)
print((d_time2 - d_time1).microseconds)
```

```go
<class 'datetime.timedelta'>
17
16498
128684
```

- 차이 결과 타입은 timedelta 클래스임을 알 수 있다. 
- timedelta 에 잇는 days, seconds 를 이용하여 결과된 시간, 초, 마이크로초 를 확인할 수 있다. 

## 특정 시점부터 경과된 날짜와 시간정보 조회하기

- timedelta 클래스와 날짜 연산을 이용하면 특정 시점부터 경과된 시간 혹은 이전 날짜등 다양한 날자를 조회할 수 있다. 

```python

from datetime import timedelta
print('한달전: ', (d_time2 + timedelta(mon = -30)))
print('한달후: ', (d_time2 + timedelta(month = 30)))
print('10일전: ', (d_time2 + timedelta(days = -10)))
print('10일후: ', (d_time2 + timedelta(days = 10)))
print('10시간전: ', (d_time2 + timedelta(hours = -10)))
print('10시간후: ', (d_time2 + timedelta(hours = 10)))
print('10분전: ', (d_time2 + timedelta(minutes = -10)))
print('10분후: ', (d_time2 + timedelta(minutes = 10)))
print('10초전: ', (d_time2 + timedelta(seconds = -10)))
print('10초후: ', (d_time2 + timedelta(seconds = 10)))
```

- 결과

```go
한달전:  2021-12-19 15:21:05.521747
한달후:  2022-02-17 15:21:05.521747
10일전:  2022-01-08 15:21:05.521747
10일후:  2022-01-28 15:21:05.521747
10시간전:  2022-01-18 05:21:05.521747
10시간후:  2022-01-19 01:21:05.521747
10분전:  2022-01-18 15:11:05.521747
10분후:  2022-01-18 15:31:05.521747
10초전:  2022-01-18 15:20:55.521747
10초후:  2022-01-18 15:21:15.521747
```

- 지원되는 날짜 단위는 weeks, days, hours, minutes, seconds, milliseconds. microseconds 를 지원한다. 
- 안타깝게도 months를 지원하지 않으며, weeks나 days를 이용하여 전달을 계산해야한다. 

## 날짜 포맷하기. 

- 날짜 포맷을 위해서는 strftime 메소드를 이용하여 포매팅 할 수 있다. 

```python
print('2022-01-01  ', d_time1.strftime('%Y-%m-%d'))
print('2022-01-01 13:30:30 ', d_time1.strftime('%Y-%m-%d %H:%M:%S'))
print('2022-01-01 01:30:30', d_time1.strftime('%Y-%m-%d %I:%M:%S'))
```

- 결과 

```go
formatting date
2022-01-01   2022-01-01
2022-01-01 13:30:30  2022-01-01 13:30:30
2022-01-01 01:30:30 2022-01-01 01:30:30
```

- 관련 정보는 https://docs.python.org/ko/3/library/datetime.html#strftime-strptime-behavior 를 참조하자. 
  
| 지시자                                | 의미                                                                                                                      | 예                                                        |
| :------------------------------------ | :------------------------------------------------------------------------------------------------------------------------ | :-------------------------------------------------------- |
| %a                                    | 요일을 로케일의 축약된 이름으로.                                                                                          | "Sun, Mon, …, Sat (en_US);                                |
| So, Mo, …, Sa (de_DE)"                | -1                                                                                                                        |                                                           |
| %A                                    | 요일을 로케일의 전체 이름으로.                                                                                            | "Sunday, Monday, …, Saturday (en_US);                     |
| Sonntag, Montag, …, Samstag (de_DE)"  | -1                                                                                                                        |                                                           |
| %w                                    | 요일을 10진수로, 0은 일요일이고 6은 토요일입니다.                                                                         | 0, 1, …, 6                                                |
| %d                                    | 월중 일(day of the month)을 0으로 채워진 10진수로.                                                                        | 01, 02, …, 31                                             |
| %b                                    | 월을 로케일의 축약된 이름으로.                                                                                            | "Jan, Feb, …, Dec (en_US);                                |
| Jan, Feb, …, Dez (de_DE)"             | -1                                                                                                                        |                                                           |
| %B                                    | 월을 로케일의 전체 이름으로.                                                                                              | "January, February, …, December (en_US);                  |
| Januar, Februar, …, Dezember (de_DE)" | -1                                                                                                                        |                                                           |
| %m                                    | 월을 0으로 채워진 10진수로.                                                                                               | 01, 02, …, 12                                             |
| %y                                    | 세기가 없는 해(year)를 0으로 채워진 10진수로.                                                                             | 00, 01, …, 99                                             |
| %Y                                    | 세기가 있는 해(year)를 10진수로.                                                                                          | 0001, 0002, …, 2013, 2014, …, 9998, 9999                  |
| %H                                    | 시(24시간제)를 0으로 채워진 십진수로.                                                                                     | 00, 01, …, 23                                             |
| %I                                    | 시(12시간제)를 0으로 채워진 십진수로.                                                                                     | 01, 02, …, 12                                             |
| %p                                    | 로케일의 오전이나 오후에 해당하는 것.                                                                                     | "AM, PM (en_US);                                          |
| am, pm (de_DE)"                       | (1), (3)                                                                                                                  |                                                           |
| %M                                    | 분을 0으로 채워진 십진수로.                                                                                               | 00, 01, …, 59                                             |
| %S                                    | 초를 0으로 채워진 10진수로.                                                                                               | 00, 01, …, 59                                             |
| %f                                    | Microsecond as a decimal number, zero-padded to 6 digits.                                                                 | 000000, 000001, …, 999999                                 |
| %z                                    | ±HHMM[SS[.ffffff]] 형태의 UTC 오프셋 (객체가 나이브하면 빈 문자열).                                                       | (비어 있음), +0000, -0400, +1030, +063415, -030712.345216 |
| %Z                                    | 시간대 이름 (객체가 나이브하면 빈 문자열).                                                                                | (비어 있음), UTC, GMT                                     |
| %j                                    | 연중 일(day of the year)을 0으로 채워진 십진수로.                                                                         | 001, 002, …, 366                                          |
| %U                                    | 연중 주 번호(일요일이 주의 시작)를 0으로 채워진 10진수로. 첫 번째 일요일에 선행하는 새해의 모든 날은 주 0으로 간주합니다. | 00, 01, …, 53                                             |
| %W                                    | 연중 주 번호(월요일이 주의 시작)를 십진수로. 첫 번째 월요일에 선행하는 새해의 모든 말은 주 0으로 간주합니다.              | 00, 01, …, 53                                             |
| %c                                    | 로케일의 적절한 날짜와 시간 표현.                                                                                         | "Tue Aug 16 21:30:00 1988 (en_US);                        |
| Di 16 Aug 21:30:00 1988 (de_DE)"      | -1                                                                                                                        |                                                           |
| %x                                    | 로케일의 적절한 날짜 표현.                                                                                                | "08/16/88 (None);                                         |
| 08/16/1988 (en_US);                   |                                                                                                                           |                                                           |
| 16.08.1988 (de_DE)"                   | -1                                                                                                                        |                                                           |
| %X                                    | 로케일의 적절한 시간 표현.                                                                                                | "21:30:00 (en_US);                                        |
| 21:30:00 (de_DE)"                     | -1                                                                                                                        |                                                           |
| %%                                    | 리터럴 '%' 문자.                                                                                                          | %    |                                                     |