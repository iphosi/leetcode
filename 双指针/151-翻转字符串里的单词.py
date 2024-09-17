

def reverseWords(s: str) -> str:
    return ' '.join(s.strip().split()[::-1])
