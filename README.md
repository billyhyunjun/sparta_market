# 🗣️Project: SpartaMarket
### 커뮤니티와 거래를 합친 카드수집 사이트

<br>

## 👨‍🏫 Project Introduction
SpartaMarket는 게시글 작성을 통한 포인트로 카드 뽑기 및 상점에서 판매/구입하여 카드 도감을 수집하는 커뮤니티 사이트입니다.

<br>

## ⏲️ Development time
- 2024.04.22(월) ~ 2023.05.02(목)
<br>

## 🧑‍🤝‍🧑 Development Function: 
- **사용자 계정** : 회원가입, 로그인, 로그아웃 기능을 제공합니다. 각 계정에는 포인트가 있으며 포인트로 물건을 구매하거나 카드 뽑기를 할 수 있습니다.
- **게시글 관리** : 게시글 작성, 수정, 삭제, 검색 기능을 제공합니다. 게시글 작성을 하면 100포인트가 지급이 되며, 각 게시물에 댓글 작성시 10포인트가 지급이 됩니다.
- **상점 관리** : 상점 등록, 수정, 삭제, 구매 기능을 제공합니다. 각 상점에 내가 보유한 카드를 판매 할 수 있으며 다른 판매글은 내 포인트로 구매가 가능합니다.
- **유저 프로필 및 기타 기능** : 유저 프로필 보기, 팔로우, 카드 보유 현황, 가챠 등의 기능이 있습니다.
- **카드 도감** : 보유하고 있는 카드 목록을 확인할 수 있는 문서가 있습니다.

<br>

## 💻 Development Environment
- **Programming Language** : Python 3.10
- **Web Framework** : Django
- **Database** : SQLite3 
- **Server Deployment** : AWS EC2 (t1.micro)
- **Idea Brainstorming Tools** : [figma](https://www.figma.com/board/AUgJMaoptrCo32HkvGSYhS/sparta_market?node-id=0-1&t=ejx4qWt9wHHgTUV4-1)

<br>

## 📚 Development scope
   - **유저**
        - 사용자 인증 및 권한 관리: 사용자 등록, 로그인, 로그아웃
        - 사용자 정보 수정 및 삭제: 프로필 수정, 계정 삭제
   - **게시글**
        - 게시글 CRUD: 게시글 작성, 조회, 수정, 삭제 및 권한 기능
        - 댓글 CRUD: 댓글 작성, 조회, 수정, 삭제 및 권한 기능
        - 게시글 목록: 모든 게시글의 리스트 조회 기능
   - **장터**
        - 판매글 CRUD: 판매글 작성, 조회, 수정, 삭제 및  권한 기능
        - 판매글 목록: 모든 판매글의 리스트 조회 기능
   - **카드**
        - 카드 뽑기: 사용자 카드 뽑기 기능
        - 카드 도감: 뽑은 카드의 상세 정보 조회
     
<br>

## 🖥️Template View

<details>
<summary> 탬플릿 미리보기 (click here) </summary>
<div markdown="1">       

## **index**
- 네브바에는 유저의 정보 밑 바로가기 중단에는 최근에 작성된 게시글과 판매글 하단에는 메인, 도감확인, 웹페이지 사용법이 표기

![image](https://github.com/billyhyunjun/sparta_market/assets/157565164/58633751-83ce-46f6-9091-e8161ac4d079)


## **login**
- 로그인 및 회원가입
  
![image](https://github.com/billyhyunjun/sparta_market/assets/157565164/c654bec2-1f11-4ee2-916e-b146ad67a55f)


## **signup**
  
![image](https://github.com/billyhyunjun/sparta_market/assets/157565164/7d1517f5-7446-4ea0-97a8-00bf85a1b0fe)


## **articles**
- 최신순의 게시글 표기되며 검색이 가능하며 정렬이 가능
  
![image](https://github.com/billyhyunjun/sparta_market/assets/157565164/6e6c8e1d-5f52-4c96-824b-3704c44d826b)


## **articles/create**
- 이미지 첨부 및 해시태그를 넣어서 작성이 가능. 글 작성시 100포인트 추가.
  
![image](https://github.com/billyhyunjun/sparta_market/assets/157565164/9b6dac65-794e-4c71-85d1-c8775414e1aa)


## **article/view**
- 게시글의 좋아요 및 작성자의 프로필 확인이 가능하고 댓글 작성 시 10포인트를 받습니다.
  
![image](https://github.com/billyhyunjun/sparta_market/assets/157565164/74c31c21-d1f1-4759-95b9-6906c3322f57)


## **article/update**
- 작성자의 아이디 또는 관리자 아이디로 접속시 삭제 또는 수정 가능.
  
![image](https://github.com/billyhyunjun/sparta_market/assets/157565164/acdf22a4-2609-4152-a4e8-ace3a36d88b5)


## **hashtag**
- 해시태그를 눌러 해당 해시태그와 관련된 글을 확인 할 수 있습니다.
  
![image](https://github.com/billyhyunjun/sparta_market/assets/157565164/8fb60b49-0c8f-422a-8c4c-f9dc36fc523b)


## **gatcha**
-  1회당 100포인트를 사용하여 50가지의 카드중에 랜덤 흭득.
  
![image](https://github.com/billyhyunjun/sparta_market/assets/157565164/25717d3e-2c55-4fef-a680-193fedb27ac6)

![image](https://github.com/billyhyunjun/sparta_market/assets/157565164/72504d46-39b5-413b-8c46-dfffd049c81f)


## **my_card**
- 현재 보유한 총 카드 수 및 도감 완성 목록을 확인 가능.
  
![image](https://github.com/billyhyunjun/sparta_market/assets/157565164/dbf5bf2c-5914-471b-8f9f-6a620cdccd76)


## **stores**
- 카드를 판매 하는 페이지, 보유 포인트로 구매 가능.
  
![image](https://github.com/billyhyunjun/sparta_market/assets/157565164/516f972b-4afa-478f-813c-63d5a11098b7)


## **store/create**
- 보유한 카드중 선택하여 판매.
  
![image](https://github.com/billyhyunjun/sparta_market/assets/157565164/50c72736-12c8-4ca8-ba89-ae9f55cffe51)


## **my_sell_card**
- 보유한 모든 카드를 볼 수 있으며, 중복된 카드를 선택하여 상점 판매.
  
![image](https://github.com/billyhyunjun/sparta_market/assets/157565164/89b27c66-4ab6-443b-b518-6f4081d1cbdd)


## **store/view**
- 작성된 게시글을 확인, 포인트로 구매 가능.
  
![image](https://github.com/billyhyunjun/sparta_market/assets/157565164/3f9c3b8f-80d7-4e21-93aa-51b9ddbe5919)


## **store/update**
- 수정 시 카드변경은 불가능, 가격 또는 내용 변경 가능.

![image](https://github.com/billyhyunjun/sparta_market/assets/157565164/0a68725f-2d10-41ab-a817-ea8e1a1144bf)


## **card_document**
- 카드 도감 확인.
  
![image](https://github.com/billyhyunjun/sparta_market/assets/157565164/dfcbfda4-f0a7-4a5e-83d5-e6d6c73dc368)


## **adout**
- 웹페이지 설명.
  
![image](https://github.com/billyhyunjun/sparta_market/assets/157565164/a8e43458-d9c5-4a5d-ae1a-e35443c573c5)


## **profile**
- 팔로우 기능 및 프로필 수정 삭제.
  
![image](https://github.com/billyhyunjun/sparta_market/assets/157565164/8261b827-0d3d-4902-97d0-0021209405fc)


## **profile, update**
- 프로필의 사진과 이름 비밀번호가 수정이 가능하나 아이디를 변경할 수는 없습니다.
  
![image](https://github.com/billyhyunjun/sparta_market/assets/157565164/0014ddba-02d5-4d83-8ea4-ad340b310785)


## **like_view**
- 해당 프로필 유저가 좋아요를 누른 게시물을 확인 가능.
  
![image](https://github.com/billyhyunjun/sparta_market/assets/157565164/40c348d7-40a2-46b5-bd77-69136d709161)


</div>
</details>
<br>

## 🕵️Quality Assurance testing

- QA테스트: [Notion QA 테스트 케이스](https://parallel-radiator-f96.notion.site/sparta_market-12ecafd9e0a080628f70d3314c058259?pvs=4)

<br> 

## ✒️ API

# 사용자 관련 엔드포인트

| 엔드포인트                      | HTTP 메소드 | 요청 파라미터               | 응답 형식                           | 응답 코드                 |
|--------------------------------|-------------|-----------------------------|-------------------------------------|---------------------------|
| `/users/profile/<username>/`   | GET         | 없음                        | 사용자 프로필 정보(JSON 형식)      | 200: 성공, 404: 사용자 없음 |
| `/users/follow/<user_id>/`     | POST        | 없음                        | 없음                                | 200: 성공, 400: 오류, 404: 사용자 없음 |
| `/users/gatcha/`               | POST        | 없음                        | 가챠 결과(JSON 형식)               | 200: 성공, 400: 포인트 부족 |

# 게시글 관련 엔드포인트

| 엔드포인트                      | HTTP 메소드 | 요청 파라미터               | 응답 형식                           | 응답 코드                 |
|--------------------------------|-------------|-----------------------------|-------------------------------------|---------------------------|
| `/articles/create/`            | POST        | 제목, 내용 등               | 생성된 게시글 ID 및 메시지(JSON 형식) | 200: 성공, 400: 오류     |
| `/articles/delete/<article_id>/`| POST       | 없음                        | 없음                                | 200: 성공, 400: 오류     |



