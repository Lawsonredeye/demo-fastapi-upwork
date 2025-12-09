from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import re
import uvicorn


app = FastAPI()


class DataItem(BaseModel):
    text: str | None = None
    language: str | None = None


@app.post("/transform")
async def transform_data(data: DataItem):
    transformed_list = [token for token in re.split(r'[,;!#^&*()\s]+', data.text.strip()) if token]
    length = len(transformed_list)
    has_digit = contains_digit(transformed_list)
    return {
        "tokens": transformed_list,
        "count": length,
        "has_digit": has_digit
    }


def contains_digit(items: List[str]) -> bool:
    for item in items:
        if any(char.isdigit() for char in item):
            return True
    return False


if __name__ == "__main__":
    uvicorn.run(app)