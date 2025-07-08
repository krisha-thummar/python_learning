def vowel_count(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    print(count)
vowel_count("hello")