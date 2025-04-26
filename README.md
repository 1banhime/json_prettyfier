# JSON Prettyfier

A command-line Python tool to convert heavily nested JSON files to a more readable HTML format

---

## Features

- Parses JSON files with nested dictionaries and lists
- Converts themn into easily reable HTML
- Structure:
    - `<h1>` for indentation level 1
    - `<h2>` for indentation level 2
    - `<h3>` for indentation level 3
    - `<p>` for any indentation beyond 3
- Outputs a HTML document
- Works from any terminal or shell

---

## Usage

```bash
python3 json_prettyfier.py input.json output.html
```

### Other Tools
[1banhime | github](https://github.com/1banhime)