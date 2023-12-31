from collections import Counter

def top_characters(s):
    char_counts = Counter(s)
    sorted_chars = sorted(char_counts.items(), key=lambda x: (-x[1], x[0]))
    for char, count in sorted_chars[:3]:
        print(char, count)

company_name = input()
top_characters(company_name)

