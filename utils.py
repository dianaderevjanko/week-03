def capitalize(text):
    """
    Pārveido teksta pirmo burtu par lielo.
    Parametri: text (str)
    Atgriež: str (tekstu ar lielo sākumburtu)
    Piemērs: capitalize("hello") -> "Hello"
    """
    # 1. Pārbaude (validācija) - vai mums iedots teksts?
    if not isinstance(text, str):
        raise ValueError("Ievadei jābūt tekstam!")
    
    # 2. Darbība - paņem pirmo burtu lielu un pieliec pārējo tekstu
    if len(text) == 0:
        return ""
    
    return text[0].upper() + text[1:]

if __name__ == "__main__":
    # Šeit mēs izsaucam funkciju un printējam tās atbildi
    rezultats = capitalize("diana")
    print(f"Rezultāts: {rezultats}")