# String tool

text = input("Enter a string: ")

print("1. Uppercase")
print("2. Lowercase")
print("3. Slice")
print("4. Length")
print("5. Show characters")

choice = input("Choose (1-5): ")

if choice == "1":
    print(text.upper())

elif choice == "2":
    print(text.lower())

elif choice == "3":
    start = int(input("Start index: "))
    end = int(input("End index: "))
    print(text[start:end])

elif choice == "4":
    print(len(text))

elif choice == "5":
    for c in text:
        print(c)

else:
    print("Wrong choice")
