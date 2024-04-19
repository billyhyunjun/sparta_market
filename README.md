# 🗣️Project: SpartaMarket
### 카드를 수집하는 게시글

<br>

## 👨‍🏫 Project Introduction
SpartaMarket는 게시글을 작성해서 포인트를 모아서 카드를 뽑아서 필요 없는 카드는 상점에서 팔 수 있도록 하여 카드 도감을 모을 수 있게 하는 상점입니다.

<br>

## ⏲️ Development time
- 2024.04.15(월) ~ 2023.04.19(금)
- 아이디어 노트 작성
- 아이디어 발표
- 와이어프레임
- 기능구현
- 발표
<br>

## 🧑‍🤝‍🧑 Development Function: 
- ** 사용자 계정 ** : 회원가입, 로그인, 로그아웃 기능을 제공합니다. 각 계정에는 포인트가 있으며 포인트로 물건을 구매하거나 카드 뽑기를 할 수 있습니다.
- ** 게시글 관리 ** : 게시글 작성, 수정, 삭제, 검색 기능을 제공합니다. 게시글 작성을 하면 100포인트가 지급이 되며, 각 게시물에 댓글 작성시 10포인트가 지급이 됩니다.
- ** 상점 관리 ** : 상점 등록, 수정, 삭제, 구매 기능을 제공합니다. 각 상점에 내가 보유한 카드를 판매 할 수 있으며 다른 판매글은 내 포인트로 구매가 가능합니다.
- ** 유저 프로필 및 기타 기능 ** : 유저 프로필 보기, 팔로우, 카드 보유 현황, 가챠 등의 기능이 있습니다.
- ** 카드 도감 ** : 보유하고 있는 카드 목록을 확인할 수 있는 문서가 있습니다.

<br>

## 💻 Development Environment
- **Programming Language** : Python 3.10
- **Web Framework** : Django
- **Template Engine** : Jinja2
- **Database** : SQLite3 (for development and testing)
- **IDE** : Visual Studio Code
- **Version Control** : Git, GitHub
<br>

## ⚙️ Technology Stack
- **Frontend** : HTML, CSS, JavaScript
- **Backend** : Django
- **Database ORMR** : SQLite3
- **Idea Brainstorming Tools and Environments** : figmam, drow.io
<br>

## 📝 Project Architecture

- **WireFrame**

https://www.figma.com/file/AUgJMaoptrCo32HkvGSYhS/sparta_market?type=whiteboard&node-id=0-1&t=cgiAgykbrQ58Dogk-0

- **ERD**

https://drive.google.com/file/d/1-t8pzZDOuCaNdM8Tw0UoU-DQHvk6gtGu/view?usp=sharing

## 🖥️Template View

<details>
<summary>View Template (click here) </summary>
<div markdown="1">       

## ** index **
- 메인화면으로 화면 상단 네브바에는 유저의 정보 밑 바로가기키가 있으며, 중단에는 최근에 작성된 게시글과 판매글이 업로드 됩니다. 그리고 하단에는 메인가기 및 도감확인, 웹페이시 사용법이 표기 되어 있습니다.

![image](https://github.com/billyhyunjun/sparta_market/assets/157565164/d73d3c50-22af-44ca-8ccc-472e2899027d)

## ** login **
- 로그인 화면입니다. 해당아이디가 있으면 로그인을 시도 할 수 있으며, 아이디가 없으면 회원가입을 할 수 있습니다.
  
![image](https://github.com/billyhyunjun/sparta_market/assets/157565164/c654bec2-1f11-4ee2-916e-b146ad67a55f)

## ** signup **
- 회원가입을 하는 곳이며, 아이디와 페스워드, 확인 페스워드를 넣으면 회원가입이 완료 됩니다.
  
![image](https://github.com/billyhyunjun/sparta_market/assets/157565164/7d1517f5-7446-4ea0-97a8-00bf85a1b0fe)


## ** articles **
- 현재 작성 되어있는 게시들을 볼 수 있으며 상단에 검색에 내용을 넣어서 검색이 가능하며, 필터 기능으로 제목, 최신 등 정렬이 가능합니다.
  
![image](https://github.com/billyhyunjun/sparta_market/assets/157565164/7e17bb69-8c00-4717-9574-9f7933e44806)


## ** articles/create **
- 게시글을 생성시 이미지가 있다면 첨부가 가능하며, 제목, 내용, 해시태그를 넣어서 작성이 가능합니다. 그리고 글을 작성시 100포인트를 받을 수 있습니다.
  
![image](https://github.com/billyhyunjun/sparta_market/assets/157565164/9b6dac65-794e-4c71-85d1-c8775414e1aa)


## ** article/view **
- 작성된 게시글을 확인 할 수 있으며, 게시글의 좋아요 기능 및 작성자의 프로필 확인이 가능하고, 해시태그를 누르면 해시태그와 관련된 글을 볼 수 있습니다. 또한 댓글이 작성이 가능하며, 댓글 작성 시 10포인트를 받습니다.
  
![image](https://github.com/billyhyunjun/sparta_market/assets/157565164/4dde1720-22a5-4f7e-bdd3-d1dc2d9dd4d8)


## ** article/update **
- 작성자와 동일한 아이디로 접속 또는 관리자 아이디로 접속을 하면 삭제 또는 수정이 가능하며 수정을 하면 작성되었던 게시글과 내용이 나오며 수정하기를 눌러 기존 게시글을 변경할 수 있습니다.
  
![image](https://github.com/billyhyunjun/sparta_market/assets/157565164/acdf22a4-2609-4152-a4e8-ace3a36d88b5)


## ** hashtag **
- 해시태그를 눌러 해당 해시태그와 관련된 글을 확인 할 수 있습니다.
  
![image](https://github.com/billyhyunjun/sparta_market/assets/157565164/8fb60b49-0c8f-422a-8c4c-f9dc36fc523b)


## ** gatcha **
-  보유하고 있는 포인트로 1회당 100포인트를 사용하여 50가지의 카드중에 랜덤으로 1개를 흭득할 수 있으며 흭득한 카드로 도감을 완성하고 필요없는 카드는 판매 할 수 있습니다.
  
![image](https://github.com/billyhyunjun/sparta_market/assets/157565164/25717d3e-2c55-4fef-a680-193fedb27ac6)

![image](https://github.com/billyhyunjun/sparta_market/assets/157565164/72504d46-39b5-413b-8c46-dfffd049c81f)


## ** my_card **
- 현재 내가 보유하고 있는 총 카드의 수와 도감 완성 목록을 확인 할 수 있습니다.
  
![image](https://github.com/billyhyunjun/sparta_market/assets/157565164/dbf5bf2c-5914-471b-8f9f-6a620cdccd76)


## ** stores **
- 현재 카드를 판매 하고 있는 페이지이며 내가 가지고 있는 포인트로 구매가 가능합니다.
  
![image](https://github.com/billyhyunjun/sparta_market/assets/157565164/516f972b-4afa-478f-813c-63d5a11098b7)


## ** store/create **
- 내가 가지고 있는 카드를 이용해서 카드를 판매 할 수 있으며, 카드 고르기를 눌러 카드를 선택한 후 판매를 할 수 있습니다. 
  
![image](https://github.com/billyhyunjun/sparta_market/assets/157565164/50c72736-12c8-4ca8-ba89-ae9f55cffe51)


## ** my_sell_card **
- 현재 내가 가지고 있는 모든 카드를 볼 수 있으며, 필요 없는 카드를 골라서 상점에 판매 할 수 있습니다.
  
![image](https://github.com/billyhyunjun/sparta_market/assets/157565164/89b27c66-4ab6-443b-b518-6f4081d1cbdd)


## ** store/view **
- 작성된 게시글을 확인 할 수 있으며, 내 포인트로 구매가 가능하며, 삭제 수정이 가능합니다.
  
![image](https://github.com/billyhyunjun/sparta_market/assets/157565164/3f9c3b8f-80d7-4e21-93aa-51b9ddbe5919)


## ** store/update **
- 수정시에는 카드변경은 불가능하며 가격과 내용이 변경 가능합니다.

![image](https://github.com/billyhyunjun/sparta_market/assets/157565164/0a68725f-2d10-41ab-a817-ea8e1a1144bf)


## ** card_document **
- 카드 도감에 무슨 카드가 있는지 확인이 가능합니다.
  
![image](https://github.com/billyhyunjun/sparta_market/assets/157565164/dfcbfda4-f0a7-4a5e-83d5-e6d6c73dc368)


## ** adout **
- 웹페이지 설명입니다.
  
![image](https://github.com/billyhyunjun/sparta_market/assets/157565164/a8e43458-d9c5-4a5d-ae1a-e35443c573c5)


## ** profile **
- 내 프로필 및 다른 유저의 프로필을 확인 할 수 있고 팔로우 기능 및 프로필 수정 삭제가 가능합니다.
  
![image](https://github.com/billyhyunjun/sparta_market/assets/157565164/8261b827-0d3d-4902-97d0-0021209405fc)


## ** profile, update **
- 프로필의 사진과 이름 비밀번호가 수정이 가능하나 아이디를 변경할 수는 없습니다.
  
![image](https://github.com/billyhyunjun/sparta_market/assets/157565164/0014ddba-02d5-4d83-8ea4-ad340b310785)


## ** like_view **
- 해당 프로필 유저가 좋아요를 누른 게시물을 확인 할 수 있습니다.
  
![image](https://github.com/billyhyunjun/sparta_market/assets/157565164/40c348d7-40a2-46b5-bd77-69136d709161)


</div>
</details>


## 📌 Key Features

### 1. Post CRUD
   - Users can create new posts and view all posts.
   - Posts can be edited or deleted on the post detail view page.

### 2. Comment CRD
   - All comments on the post are displayed at the bottom of the post detail view page.
   - Users can create, view, and delete comments on the post detail page.

### 3. Sign Up, Log In
   - Membership registration is mandatory for first-time users, enabling them to log in and access the site's features.
   - Only logged-in users can create posts, while both logged-in and anonymous users can view posts and comments.
     
### 5.  Search Functionality
   - Users can search for posts by movie name, article title, author, and content using the post search box.
   - Clicking on search results directs users to the detailed page of the respective post.

### 6. Like Feature
   - Users can like posts on the post details view page.
   - The 'Like' button toggles to 'Dislike' upon clicking and can be undone, allowing users to like a post only once.
     
### 8. Administrator Permissions
   - Administrators with the ID "admin_team8" have the authority to edit or delete posts and comments, irrespective of the post's author.

### 9. Random Card Draw
   - Users can enjoy the excitement of drawing random cards from a predefined set.
   - Each card drawn presents unique attributes or benefits to the user.

### 10. Card Inventory
   - Users can view the cards they currently possess in their inventory.
   - Detailed information about each card, including its rarity and effects, is displayed.
   
### 11. Card Trading
   - Users have the option to sell the cards they no longer need in exchange for points.
   - Points acquired through card sales can be used to purchase other cards from the system.
   
### 12. User Interaction
   - Users can follow and unfollow other users, fostering a sense of community within the platform.
   - The 'Following' list enables users to keep track of updates from their followed users.

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



