# my_module.py
def count_uppercase(s: str) -> int:
    
    return sum(1 for c in s if c.isupper())
  