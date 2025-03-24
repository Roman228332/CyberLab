"""
RSA-шифрование (учебный пример)

Параметры:
- p, q: простые числа (по умолчанию 5 и 11)
- Алфавит: русские буквы в нижнем регистре

Использование:
1. Запустите скрипт: `python rsa.py`
2. Введите слово для шифровки.
3. Программа выведет зашифрованный и расшифрованный текст.
"""

def main():
    # ввод данных
    text = input("Введите слово для зашифровки: ").lower()
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

    # генерация ключей
    char_to_num = {char: i + 1 for i, char in enumerate(alphabet)}
    p, q = 5, 11
    n = p * q
    m = (p - 1) * (q - 1)
    e = 7

    # поиск обратного числа d
    def mod_inverse(e, m):
        for d in range(1, m):
            if (e * d) % m == 1:
                return d
        return None

    d = mod_inverse(e, m)
    if d is None:
        raise ValueError("Ошибка: не удалось найти обратный элемент для e")

    # шифрование
    def encrypt(char_to_num, e, n, text):
        encrypted = []
        for char in text:
            index_symbols = char_to_num[char]
            encrypted_symbols = (index_symbols ** e) % n
            encrypted.append(str(encrypted_symbols))
        return encrypted

    encrypted_list = encrypt(char_to_num, e, n, text)
    encrypted_text_solid = ''.join(encrypted_list)
    print(f"Зашифрованное слово: {encrypted_text_solid}")

    # дешифрование
    def decrypt(char_to_num, d, n, encrypted_list):
        num_to_char = {v: k for k, v in char_to_num.items()}
        decrypted = []
        for shifr in encrypted_list:
            decrypted_symbols = (int(shifr) ** d) % n
            decrypted.append(num_to_char[decrypted_symbols])
        return ''.join(decrypted)

    decrypted_text = decrypt(char_to_num, d, n, encrypted_list)
    print(f"Расшифрованное слово: {decrypted_text}")


if __name__ == "__main__":
    main()
