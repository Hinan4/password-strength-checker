from password_checker import check_strength, check_breach

def main():
    print("🔐 Password Strength Checker with Breach Detection")
    password = input("Enter a password to check: ")

    score, feedback = check_strength(password)
    print(f"\nStrength Score: {score}/4")
    if feedback['warning']:
        print(f"⚠️ Warning: {feedback['warning']}")
    if feedback['suggestions']:
        print("💡 Suggestions:")
        for s in feedback['suggestions']:
            print(f" - {s}")

    print("\n🔍 Checking for data breaches...")
    count = check_breach(password)
    if count:
        print(f"❌ This password has appeared in {count:,} breaches!")
    else:
        print("✅ This password was NOT found in known breaches.")

if __name__ == "__main__":
    main()
