import re

def is_valid_credit_card(card_number):
    if "-" in card_number:
        if any([not (0 < len(seg) < 5) for seg in card_number.split("-")]):
            return 'Invalid'
    # Check if the card number starts with 4, 5, or 6
    if not re.match(r'^[4-6]', card_number):
        return "Invalid"

    # Remove hyphens and check if the length is 16
    card_number = re.sub(r'-', '', card_number)
    if len(card_number) != 16:
        return "Invalid"

    # Check if the card number contains only digits
    if not re.match(r'^\d+$', card_number):
        return "Invalid"

    # Check if there are more than 3 consecutive repeated digits
    if re.search(r'(\d)(?=\1\1\1)', card_number):
        return "Invalid"
    return "Valid"

# Input
n = int(input())
credit_cards = [input() for _ in range(n)]

# Output
for card_number in credit_cards:
    result = is_valid_credit_card(card_number)
    print(result)

