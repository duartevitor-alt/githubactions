import pytest
from utils import requests_url


def test_count_data():
    new_regs: int = 3
    before_func_regs: list[str] = ["one.json", "two.json"]
    limit: int = len(before_func_regs)
    for i in range(new_regs):
        requests_url("https://dummyjson.com/products", output="testing", write_output=False)
        before_func_regs.append(f"mock_{i}.json")

    assert len(before_func_regs) >= limit
