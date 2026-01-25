def hide_card(card):
    card = card.replace(" ", "")
    return "*" * 12 + card[-4:]


card = '3456 9012 5678 1234'
print(hide_card(card))
