import argparse
import os
import sys

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Replace a variable in a Markdown template with content from stdin.")
    parser.add_argument("template_filename", help="Path to the template file")
    parser.add_argument("variable_name", help="Name of the variable to replace")
    args = parser.parse_args()

    template_filename = args.template_filename
    variable_name = args.variable_name

    # Check if the template file exists
    if not os.path.exists(template_filename):
        print(f"Error: Template file '{template_filename}' does not exist.")
        sys.exit(1)

    # Read the replacement content from stdin
    if sys.stdin.isatty():
        print("Error: No input provided via stdin.")
        sys.exit(1)

    replacement_content = sys.stdin.read().strip()
    if not replacement_content:
        print("Error: Input provided via stdin is empty.")
        sys.exit(1)

    # Read the template file
    try:
        with open(template_filename, 'r') as template_file:
            template_content = template_file.read()
    except Exception as e:
        print(f"Error reading the template file: {e}")
        sys.exit(1)

    # Replace occurrences of the variable
    placeholder = f"{{{variable_name}}}"
    updated_content = template_content.replace(placeholder, replacement_content)

    print(updated_content)

if __name__ == "__main__":
    main()