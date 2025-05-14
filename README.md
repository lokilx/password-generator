# Password Generator

A simple command-line tool to generate random strong passwords with customizable options.

## Features

- Generate passwords of custom length
- Include or exclude character sets (uppercase, lowercase, digits, special symbols)
- Generate multiple passwords at once
- Ensures at least one character from each selected character set
- Randomizes character positions for maximum security

## Requirements

- Python 3.x

## Usage

```bash
python password_generator.py [OPTIONS]
```

### Options

- `-l, --length LENGTH` - Password length (default: 12)
- `--no-uppercase` - Exclude uppercase letters
- `--no-lowercase` - Exclude lowercase letters
- `--no-digits` - Exclude digits
- `--no-symbols` - Exclude special symbols
- `-c, --count COUNT` - Number of passwords to generate (default: 1)
- `-h, --help` - Show help message

### Examples

Generate a single password with default settings (12 characters, all character types):
```bash
python password_generator.py
```

Generate a longer password (16 characters):
```bash
python password_generator.py -l 16
```

Generate 5 passwords of length 8:
```bash
python password_generator.py -l 8 -c 5
```

Generate a password without special symbols:
```bash
python password_generator.py --no-symbols
```

Generate passwords using only digits and uppercase letters:
```bash
python password_generator.py --no-lowercase --no-symbols
``` 