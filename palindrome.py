# Завдання 2
# Створіть програму, яка перевіряє, чи є паліндромом введена фраза.

def check_if_palindrome(phraze):
	phraze_stripped = phraze.replace(" ", "")
	return phraze_stripped == phraze_stripped[::-1]

print(check_if_palindrome("racecar"))
print(check_if_palindrome("taco cat"))
print(check_if_palindrome("taco cats"))

print()

# or using loop
def check_if_palindrome2(phraze):
	phraze_stripped = ""

	for char in phraze:
		if char.isalnum():
			phraze_stripped += char

	return phraze_stripped == phraze_stripped[::-1]

print(check_if_palindrome2("racecar"))
print(check_if_palindrome2("taco cat"))
print(check_if_palindrome2("taco cats"))

print(check_if_palindrome2("123321"))