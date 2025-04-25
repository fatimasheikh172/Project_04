print("🔢 Welcome to the 🤖  Calculator!")

while True:
    try:
        num1 = float(input("\n🔸 Enter first number: "))
        operator = input("🔹 Enter operator (+, -, *, /, %, **): ")
        num2 = float(input("🔸 Enter second number: "))

        if operator == "+":
            result = num1 + num2
            emoji = "➕"
        elif operator == "-":
            result = num1 - num2
            emoji = "➖"
        elif operator == "*":
            result = num1 * num2
            emoji = "✖️"
        elif operator == "/":
            if num2 == 0:
                print("🚫 Error: Cannot divide by zero ❌")
                continue
            result = num1 / num2
            emoji = "➗"
        elif operator == "%":
            result = num1 % num2
            emoji = "🧮"
        elif operator == "**":
            result = num1 ** num2
            emoji = "💥"
        else:
            print("⚠️ Invalid operator. Please try again.")
            continue

        print(f"\n✅ Result {emoji}: {result:.2f}")

    except ValueError:
        print("❌ Invalid input! Please enter numeric values only.")

    again = input("\n🔁 Do you want to perform another calculation? (yes/no): ").lower()
    if again != "yes":
        print("\n👋 Thanks for using the calculator! Have a great day! 🌟")
        break
