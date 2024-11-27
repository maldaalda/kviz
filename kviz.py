

# Soubor, kde se budou ukládat otázky
FILENAME = "questions.json"

# Načtení otázek ze souboru nebo vytvoření výchozího seznamu
try:
    with open(FILENAME, "r") as file:
        data = file.read().strip()  # Odstranění prázdných mezer
        questions = json.loads(data) if data else []
except (FileNotFoundError, json.JSONDecodeError):
    questions = [
        {"question": "Kolik nohou má pavouk?", "answer": "8"},
        {"question": "Jaké je hlavní město ČR?", "answer": "praha"},
        {"question": "Co je 3 x 3?", "answer": "9"}
    ]

def play_quiz():
    print("Vítejte v kvízu!")
    score = 0

    for q in questions:
        user_answer = input(q["question"] + " ").lower()
        if user_answer == q["answer"]:
            print("Správně!")
            score += 1
        else:
            print(f"Špatně! Správná odpověď je '{q['answer']}'.")
    
    print(f"Konec! Získali jste {score} bodů z {len(questions)}.")

def add_question():
    print("\nChcete přidat novou otázku? (ano/ne)")
    if input("> ").lower() == "ano":
        new_question = input("Zadejte novou otázku: ")
        new_answer = input("Zadejte správnou odpověď: ").lower()
        questions.append({"question": new_question, "answer": new_answer})
        with open(FILENAME, "w") as file:
            json.dump(questions, file, indent=4)
        print("Otázka byla úspěšně přidána!\n")
    else:
        print("Žádná nová otázka nebyla přidána.\n")

# Hlavní smyčka programu
while True:
    print("\n--- Kvíz ---")
    print("1. Spustit kvíz")
    print("2. Přidat novou otázku")
    print("3. Ukončit program")

    choice = input("Vyberte možnost: ")
    if choice == "1":
        play_quiz()
    elif choice == "2":
        add_question()
    elif choice == "3":
        print("Děkujeme za hraní! Nashledanou.")
        break
    else:
        print("Neplatná volba, zkuste to znovu.")
