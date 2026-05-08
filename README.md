# bookbot

BookBot is my first [Boot.dev](https://www.boot.dev) project — a command-line tool that analyzes novels and generates a statistical report of word and character usage.

## Demo

```
--- Begin report of books/frankenstein.txt ---
77986 words found in the document
The 'e' character was found 46043 times
The 't' character was found 30365 times
The 'a' character was found 26743 times
...
--- End report ---
```

## Features

- Counts total number of words in any plain text file
- Counts frequency of each alphabetic character, sorted by most common
- Accepts any `.txt` file as input via command-line argument
- Works with classic novels from [Project Gutenberg](https://www.gutenberg.org/)

## Requirements

- Python 3.x
- Linux or macOS (or Windows with WSL2)

## Installation

```bash
git clone https://github.com/your-username/bookbot.git
cd bookbot
```

No external dependencies — uses Python standard library only.

## Usage

```bash
python3 main.py books/frankenstein.txt
```

You can pass any `.txt` file as the argument:

```bash
python3 main.py books/moby_dick.txt
```

## Project Structure

```
bookbot/
├── books/
│   └── frankenstein.txt
├── main.py
└── README.md
```

## Books

Download free plain text books from [Project Gutenberg](https://www.gutenberg.org/) and drop them in the `books/` directory.

Frankenstein can be fetched directly:

```bash
wget -O books/frankenstein.txt https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/frankenstein.txt
```

## License