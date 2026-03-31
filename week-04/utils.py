# visas "matemātikas" funkcijas, lai nepiegružotu galveno programmu
def calc_line_total(item):
    """Aprēķina viena produkta kopsummu (daudzums x cena)."""
    return item['qty'] * item['price']

def calc_grand_total(items):
    """Summē visu produktu kopsummas."""
    return sum(calc_line_total(item) for item in items)

def count_units(items):
    """Saskaita kopējo vienību skaitu."""
    return sum(item['qty'] for item in items)