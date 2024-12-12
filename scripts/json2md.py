import argparse
import json
import sys
import logging

# Configure logging
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Helper function to convert a number to its ordinal representation
def ordinal(n):
    if 11 <= n % 100 <= 13:
        return f"{n}th"
    elif n % 10 == 1:
        return f"{n}st"
    elif n % 10 == 2:
        return f"{n}nd"
    elif n % 10 == 3:
        return f"{n}rd"
    else:
        return f"{n}th"

def json_to_markdown(json_data, filter):
    logger.info("Starting JSON to Markdown conversion.")
    header = json_data["_header"]
    gpus = {k: v for k, v in json_data.items() if k != "_header"}

    # Apply filter if provided
    if filter:
        logger.debug("Applying GPU filter: %s", filter)
        gpus = {k: v for k, v in gpus.items() if k in filter}

    # Define categories for separation
    specs_attributes = [attr for attr, details in header.items() if "unit" in details and details["unit"] in ("TFLOPS", "TOPS")]
    architecture_attributes = [attr for attr in header if attr not in specs_attributes]

    # Function to handle concatenation for attributes with "_generation"
    def get_concatenated_value(gpu, attribute):
        # Check for a corresponding "_generation" attribute
        generation_attr = f"{attribute}_generation"
        value = gpu.get(attribute, "?")
        if value is None:
            value = "?"
        elif value == 0:
            value = "N/A"
        if generation_attr in gpu:
            generation_value = gpu.get(generation_attr)
            # if value is a number
            if isinstance(generation_value, (int, float)):
                value = f"{value} ({ordinal(generation_value)} gen)"
            elif generation_value is not None:
                value = f"{value} (gen {generation_value})"
        return value

    # Function to generate table rows for a category
    def generate_rows(attributes):
        rows = []
        for attribute in attributes:
            # Check for a corresponding "_generation" attribute, it will be concatenated to the attribute name if possible
            if attribute.endswith("_generation") and attribute[:-len("_generation")] in header:
                continue
            details = header[attribute]
            attribute_name = details["full_name"]
            unit = f" ({details['unit']})" if "unit" in details else ""
            row = [f"{attribute_name}{unit}"]
            for gpu in gpus.values():
                value = get_concatenated_value(gpu, attribute)
                row.append(str(value))
            rows.append(" | ".join(row))
        return rows

    # Generate table
    table_header = ["Attribute (Unit)"] + [gpu.get("name", k) for k, gpu in gpus.items()]
    table_lines = [" | ".join(table_header)]
    table_lines.append(" | ".join(["---"] * len(table_header)))

    # Add specs part
    table_lines.extend(generate_rows(specs_attributes))

    # Add architecture part
    table_lines.append("**Architecture Details**" + " | " * len(table_header))  # Section header
    table_lines.extend(generate_rows(architecture_attributes))

    return "\n".join(table_lines)

# Main function 
def main():
    parser = argparse.ArgumentParser(description="Convert JSON GPU Specs to Markdown")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("file", type=str, nargs="?", help="Input JSON file (default: read from stdin)")
    parser.add_argument("--filter", nargs="+", help="Optional list of GPUs to include in the output.")
    args = parser.parse_args()

    logger.debug(f"Arguments received: {args}")

    if args.file is not None:
        try:
            with open(args.file, "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            logger.critical("Error: File '%s' not found.", args.file)
            sys.exit(1)
    else:
        try:
            data = json.load(sys.stdin)
        except json.JSONDecodeError:
            logger.critical("Error: Invalid JSON input.")
            sys.exit(1)

    markdown = json_to_markdown(data, filter=args.filter)
    print(markdown)

if __name__ == "__main__":
    main()