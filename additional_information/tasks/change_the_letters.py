# todo: 34:42 -> 35:51

# todo| Напишите программу, которая
# todo| считывает одно предложение
# todo| и две буквы, letter_1 и letter_2.
# todo| Напечатайте это предложение
# todo| без последних символов,
# todo| и где letter_1 заменена
# todo| на letter_2.
# todo| Например: При вводе "Happy New Year!!!", "e", "o".
# todo| Ожидаем увидеть: "Happy Now Yoar".

sentence = input("Введите предложение: ")  # todo| translate => предложение
letter_1 = input("Какую букву поменять? -> : ")
letter_2 = input("На какую букву поменять? -> : ")

sentence = sentence.replace(letter_1, letter_2)  # todo| с помощью функции replace
#                                                        -> заменяем letter_1 на letter_2,
#                                                        и потом результат сохраняем в sentence.

print(f'Вот что у нас получилось: ',sentence[:-3])  # todo| с помощью среза([:-3]),
#                                                           убираем 3 символа из sentence
