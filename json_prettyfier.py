import json
import sys

class JsonPrettyfier:
    def __init__(self, filepath):
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                self.data = json.load(file)
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON format: {e}")
        except Exception as e:
            raise RuntimeError(f"Error reading file {e}")
        self._document_parts = []

    def structure(self, text, indent):
        if indent <= 3:
            self._document_parts.append(f"<h{indent}> {text} </h{indent}>")
        else:
            self._document_parts.append(f"<p> {text} </p>")

    def parse_value(self, value, indent):
        if isinstance(value, dict):
            for k, v in value.items():
                self.structure(f"{k}:", indent)
                self.parse_value(v, indent + 1)
        elif isinstance(value, list):
            for item in value:
                self.parse_value(item, indent)
        else:
            self.structure(str(value), indent)

    def parsing(self):
        self.parse_value(self.data, indent=1)

    def to_html(self):
        html = "<html>\n<head><title>JSON Pretty Print</title></head>\n<body>\n"
        html += "\n".join(self._document_parts)
        html += "\n</body>\n</html>"
        return html

    def save(self, output_file):
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(self.to_html())
            print(f"✅ HTML saved to '{output_file}'")
        except Exception as e:
            raise RuntimeError(f"Error writing to output file: {e}")
        
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Incorrect number of arguments given. \n\n Usage: json_prettyfier.py input.json output.html")
        sys.exit(1)
        
    input_file = sys.argv[1]
    output_file =sys.argv[2]
    
    prettyfier = JsonPrettyfier(input_file)
    prettyfier.parsing()
    prettyfier.save(output_file)
