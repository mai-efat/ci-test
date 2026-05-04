import click
import json
import sys

@click.command()
@click.argument('filename')
def main(filename):
    """يحول أي ملف لـ JSON"""
    try:
        with open(filename, 'r') as f:
            content = f.read()
        result = {"content": content}
        print(json.dumps(result, indent=4))
    except FileNotFoundError:
        print(f"Error: الملف '{filename}' مش موجود")
        sys.exit(1)

if __name__ == "__main__":
    main()