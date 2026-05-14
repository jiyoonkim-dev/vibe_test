# vibe_test

`vibe_test` is a beginner-friendly starter kit for a future Korean stock dashboard app.

It is inspired by the idea of separating backend and frontend work, but keeps the first version intentionally small so it is easy to read, run, and grow.

## Current structure

```text
vibe_test/
├─ backend/
│  ├─ app/
│  │  ├─ main.py
│  │  └─ routers/
│  │     └─ stocks.py
│  └─ requirements.txt
├─ frontend/
│  ├─ README.md
│  └─ index.html
├─ .env.example
├─ .gitignore
└─ README.md
```

## What this repository is for

- learn GitHub and coding in a small project
- build a simple stock-price checking page step by step
- prepare a backend API that a frontend can call later

## Backend quick start

1. Move into the backend folder:

   ```bash
   cd backend
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

   On Windows PowerShell:

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the FastAPI server:

   ```bash
   uvicorn app.main:app --reload
   ```

5. Open the API in your browser:

   - Home: `http://127.0.0.1:8000/`
   - Demo quote: `http://127.0.0.1:8000/api/stocks/quote/005930`
   - API docs: `http://127.0.0.1:8000/docs`

## Example API responses

### `GET /`

```json
{
  "message": "Welcome to the vibe_test backend",
  "docs": "/docs"
}
```

### `GET /api/stocks/quote/005930`

```json
{
  "symbol": "005930",
  "name": "Samsung Electronics",
  "price": 78200,
  "change": 1100,
  "changeRate": 1.43,
  "market": "KOSPI"
}
```

## Frontend plan

The `frontend/` folder is a placeholder for the future stock UI.

You can also open `frontend/index.html` directly in a browser to see a tiny visual placeholder page.

Good first features to build next:

- a stock search box
- a price summary card
- a simple chart area
- a page that calls the backend quote API

Suggested future stack:

- React or Next.js
- Tailwind CSS
- a chart library such as Recharts or Chart.js

## What to build next

If you want to keep vibe coding, a simple order is:

1. make a basic frontend page in `frontend/`
2. connect it to `/api/stocks/quote/{symbol}`
3. add more sample symbols or connect a real stock data source
4. add chart data and a simple dashboard layout
