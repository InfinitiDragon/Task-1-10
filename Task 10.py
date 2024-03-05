user_data = {
  "ID": 99,
  "Прізвище": "Феодофій",
  "Ім'я": "Фаталідонато",
  "Група": "КК-КК-К2",
  "Курс": 23,
  "Книги (борг)": [],
  "Статистика книг": []
}

print("\nІнформація про читача:")
for key, value in user_data.items():
  print(f"{key}: {value}")

while True:
  print("\nМеню:")
  print("1. Вивести карту читача")
  print("2. Взяти книгу у борг")
  print("3. Повернути книгу")
  print("0. Вийти з програми")
  choice = input("Виберіть опцію: ")

  if choice == "1":
      print("\nІнформація про читача:")
      for key, value in user_data.items():
          print(f"{key}: {value}")
  elif choice == "2":
      book_name = input("\nВведіть назву книги, яку хочете взяти у борг: ")
      user_data["Книги (борг)"].append(book_name)
      print(f"\nКнига '{book_name}' додана у список борг.")
  elif choice == "3":
      borrowed_books = user_data["Книги (борг)"]
      if borrowed_books:
          print("\nКниги у боргу:")
          print('\n'.join(borrowed_books))
          book_name = input("\nВведіть назву книги, яку хочете повернути: ")
          if book_name in map(str, borrowed_books):
              borrowed_books.remove(book_name)
              user_data["Статистика книг"].append(book_name)
              print(f"\nКнига '{book_name}' успішно повернена.")
          else:
              print(f"\nКниги '{book_name}' немає у списку борг.")
      else:
          print("\nНемає книг у боргу.")
  elif choice == "0":
      print("\nПрограма завершила роботу.")
      break
  else:
      print("\nНевірний вибір. Спробуйте ще раз.")