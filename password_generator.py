import random
import string
import argparse

def generate_password(length=12, use_uppercase=True, use_lowercase=True, 
                     use_digits=True, use_symbols=True):
    uppercase_chars = string.ascii_uppercase
    lowercase_chars = string.ascii_lowercase
    digit_chars = string.digits
    symbol_chars = string.punctuation
    
    chars = ""
    if use_uppercase:
        chars += uppercase_chars
    if use_lowercase:
        chars += lowercase_chars
    if use_digits:
        chars += digit_chars
    if use_symbols:
        chars += symbol_chars
    
    if not chars:
        raise ValueError("At least one character set must be enabled")
    
    password = []
    if use_uppercase:
        password.append(random.choice(uppercase_chars))
    if use_lowercase:
        password.append(random.choice(lowercase_chars))
    if use_digits:
        password.append(random.choice(digit_chars))
    if use_symbols:
        password.append(random.choice(symbol_chars))
    
    remaining_length = length - len(password)
    if remaining_length > 0:
        password.extend(random.choice(chars) for _ in range(remaining_length))
    
    random.shuffle(password)
    
    return ''.join(password)

def main():
    parser = argparse.ArgumentParser(description='Generate a random strong password')
    parser.add_argument('-l', '--length', type=int, default=12, help='Password length (default: 12)')
    parser.add_argument('--no-uppercase', action='store_true', help='Exclude uppercase letters')
    parser.add_argument('--no-lowercase', action='store_true', help='Exclude lowercase letters')
    parser.add_argument('--no-digits', action='store_true', help='Exclude digits')
    parser.add_argument('--no-symbols', action='store_true', help='Exclude special symbols')
    parser.add_argument('-c', '--count', type=int, default=1, help='Number of passwords to generate (default: 1)')
    
    args = parser.parse_args()
    
    if args.length < 4:
        print("Warning: Short passwords are not secure. Using minimum length of 4.")
        args.length = 4
    
    for i in range(args.count):
        try:
            password = generate_password(
                length=args.length,
                use_uppercase=not args.no_uppercase,
                use_lowercase=not args.no_lowercase,
                use_digits=not args.no_digits,
                use_symbols=not args.no_symbols
            )
            print(password)
        except ValueError as e:
            print(f"Error: {e}")
            return 1
    
    return 0

if __name__ == "__main__":
    main() 