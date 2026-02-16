# ICE - Personal Finance Application

Backend MVP built with FastAPI.
Frontend MVP with React + Vite.

## Features
- Users
- Transactions (income, expense, freeze)
- Monthly summary
- Edit & delete transactions

### Backend

backend/
│
├─ app/
│   ├─ __init__.py
│   ├─ main.py           # entry point de l'app
│   ├─ models.py         # tots els models SQLAlchemy (User, Category, Transaction)
│   ├─ schemas.py        # Pydantic models per request/response
│   ├─ database.py       # engine, session, inicialització SQLite
│   ├─ crud.py           # funcions per manipular la BD (create, read, etc.)
│   ├─ seed.py           # categories per defecte
│   └─ routes/
│       ├─ __init__.py
│       ├─ transactions.py
│       ├─ categories.py
│       └─ users.py
│
├─ venv/                 # el teu entorn virtual
└─ requirements.txt


### Frontend

src/
├── pages/
│   ├── Login.jsx
│   ├── Dashboard.jsx
│   ├── TransactionsPage.jsx
│
├── components/
│   ├── SummaryCards.jsx
│   ├── ChartSection.jsx
│   ├── TransactionList.jsx
│   ├── TransactionForm.jsx
│
├── services/
│   └── api.js
│
├── App.jsx
└── main.jsx

