
# 🎲 Monopoly Full-Stack Game

A complete Monopoly board game implementation with React frontend and Flask backend, featuring JWT authentication, social login, and persistent game state.


## 📑 Table of Contents
 - ✨ Features
 - ⚡ Quick Start
 - 🔑 Authentication Setup
 - 📡 API Endpoints
 - 🎮 Usage
 - 🛠️ Technologies Used
 - 🔒 Security Features
 - 🚀 Production Considerations
 
## ✨ Features

🔐 Authentication
 - JWT-based authentication with access & refresh tokens

 - Email/password registration & login

 - Google & GitHub OAuth social login

 - Secure logout with token revocation

 - Protected routes and API endpoints

 🎮 Game Features
 - Interactive Monopoly board with 40 tiles

 - Dice rolling mechanics & doubles detection

 - Player movement and turn management

 - Property ownership & rent payments

 - Money management (bank balance tracking)

 - Save & resume games

 - Multiple concurrent games per user

 - Game deletion 


## ⚡ Quick Start
🔧 Backend Setup

```
cd backend
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
python app.py
```
Runs on → `http://localhost:5173`
## 🔑 Authentication Setup
- Register

        1. Username
        2. Email 
        3. Password 
## 📡 API Endpoints
Authentication
 
    - `POST /register` → Register

    - `POST /login` → Login

    - `POST /refresh` → Refresh token

    - `POST /logout` → Logout

    - `GET /me` → Current user

Game Management
    - `POST /create` → Create game

    - `GET /<game_id>` → Get game state

    - `PUT /<game_id>/state` → Update state

    - `POST /<game_id>/save` → Save game

    - `POST /<game_id>/resume` → Resume game

    - `DELETE /<game_id>` → Delete game

    - `GET /my-games` → Get user’s games

## 🎮 Usage
    1. Register/Login (email or social login)

    2. Dashboard → View or create games

    3. Play → Roll dice, move, buy properties, pay rent

    4. Save → Save progress anytime

    5. Resume → Continue from dashboard

    6. Logout → End secure session
## 🛠️ Technologies Used
- Backend: Flask · Flask-JWT-Extended · Flask-CORS · Authlib
- Frontend: React 18 · React Router · Axios · Vite · CSS3
## 🔒 Security Features

- JWT tokens (access = 1h, refresh = 30d)

- Token revocation on logout

- Protected API routes

- Password hashing with bcrypt (recommended)

- Secure HTTP-only cookies

- CORS configuration
## 🚀 Production Considerations

- Use HTTPS everywhere

- Store secrets in environment variables

- Replace in-memory DB with PostgreSQL/MySQL

- Add Redis for caching & session storage

- Use CDN for static assets

- Add monitoring (Sentry, logs, alerts)
## Authors

- [@KAYABINGHI](https://www.github.com/KAYABINGHI)
- [@Angellucy460](https://www.github.com/Angellucy460)
- [@Adrienkym](https://www.github.com/Adrienkym)
- [@SALEH-abdulwahab](https://www.github.com/SALEH-abdulwahab)
## Contributing

- Contributions are welcome!
- Fork the repo, create a branch, commit your changes, and submit a PR 🚀
