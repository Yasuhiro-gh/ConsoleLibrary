# ConsoleLibrary
Консольное приложение для управления библиотекой книг
> В качестве тестового задания
## Функционал

В роли хранилища используется json файл

Книги состоят из:
* ID
* Title
* Author
* Year
* Status: "В наличии", "Выдана"

Функции библиотеки:
  
1. Добавление книги
2. Удаление книги
3. Поиск книг
4. Изменение статуса книги
5. Отображение всей библиотеки

## Запуск

Добавление книги
```
python -m ConsoleLibrary --add
```
Удаление книги
```
python -m ConsoleLibrary --delete
```
Отображение библиотеки
```
python -m ConsoleLibrary --list
```
Поиск книг
```
python -m ConsoleLibrary --search
```
Изменение статуса книги
```
python -m ConsoleLibrary --change
```
## Тесты
Запуск тестов
```
python -m unittest tests.test_library
```


