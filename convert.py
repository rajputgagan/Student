import json
import yaml
import sys
import os

def json_to_yaml(input_file, output_file):
    with open(input_file, "r") as f:
        data = json.load(f)

    with open(output_file, "w") as f:
        yaml.dump(data, f, default_flow_style=False)

    print(f"Converted JSON to YAML: {output_file}")

def yaml_to_json(input_file, output_file):
    with open(input_file, "r") as f:
        data = yaml.safe_load(f)

    with open(output_file, "w") as f:
        json.dump(data, f, indent=2)

    print(f"Converted YAML to JSON: {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage:")
        print("  python3 convert.py json2yaml input.json output.yaml")
        print("  python3 convert.py yaml2json input.yaml output.json")
        sys.exit(1)

    mode = sys.argv[1]
    input_file = sys.argv[2]
    output_file = sys.argv[3]

    if not os.path.exists(input_file):
        print(f"Error: input file not found: {input_file}")
        sys.exit(1)

    try:
        if mode == "json2yaml":
            json_to_yaml(input_file, output_file)
        elif mode == "yaml2json":
            yaml_to_json(input_file, output_file)
        else:
            print("Invalid mode. Use json2yaml or yaml2json")
            sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
