from fastapi import APIRouter


router = APIRouter()

MOCK_QUOTES = {
    "005930": {
        "symbol": "005930",
        "name": "Samsung Electronics",
        "price": 78200,
        "change": 1100,
        "changeRate": 1.43,
        "market": "KOSPI",
    },
    "000660": {
        "symbol": "000660",
        "name": "SK hynix",
        "price": 204500,
        "change": -2500,
        "changeRate": -1.21,
        "market": "KOSPI",
    },
    "035720": {
        "symbol": "035720",
        "name": "Kakao",
        "price": 41600,
        "change": 300,
        "changeRate": 0.73,
        "market": "KOSPI",
    },
}


@router.get("/quote/{symbol}")
def get_stock_quote(symbol: str) -> dict[str, str | int | float]:
    normalized_symbol = symbol.strip().upper()

    if normalized_symbol in MOCK_QUOTES:
        return MOCK_QUOTES[normalized_symbol]

    return {
        "symbol": normalized_symbol,
        "name": "Demo Stock",
        "price": 0,
        "change": 0,
        "changeRate": 0.0,
        "market": "UNKNOWN",
    }
