# QuietPlace
## 조용한 작업공간을 위한 Quiet Place

### git clone을 하고나면 해야할 것들

1. 가상환경을 만들어줍시다.

> `python -m venv .venv`

2. 가상환경을 실행시켜줍시다.

> `source .venv/bin/activate` --> Mac OS 기준

> 윈도우일 경우 다음 링크를 참조
>
> https://velog.io/@kjhoon0330/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EA%B0%80%EC%83%81%ED%99%98%EA%B2%BD-%EC%84%B8%ED%8C%85-%EB%B0%8F-Django-install

3. 의존성 설치를 해줍시다.

> pip install -r requirements.txt 

> 위 명령어는 requirements.txt에 미리 만들어둔 의존성 리스트들을 한꺼번에 다운 받을 수 있게 해줍니다!

4. migrate 한번 합시당

> `python manage.py migrate`

5. 이제 실행시켜봅시다.

> `python manage.py runserver`

> 이때 hello World! 떠주면 성공!
