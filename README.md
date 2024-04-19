# 🗣️Project: SpartaMarket
#### 카드를 수집하는 게시글

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
- **Backend** : Flask
- **Database ORMR** : SQLAlchemy
- **Idea Brainstorming Tools and Environments** : Slack, Zep, Notion, figma
<br>

## 📝 Project Architecture

- **wireframe**

https://www.figma.com/file/AUgJMaoptrCo32HkvGSYhS/sparta_market?type=whiteboard&node-id=0-1&t=cgiAgykbrQ58Dogk-0

- **ERD**

https://drive.google.com/file/d/1-t8pzZDOuCaNdM8Tw0UoU-DQHvk6gtGu/view?usp=sharing

## Template View



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



- API 명세서 : <>
