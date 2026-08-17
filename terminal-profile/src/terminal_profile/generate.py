from pathlib import Path

import yaml
from jinja2 import Environment, FileSystemLoader

import json

BASE_DIR = Path(__file__).parent

profile = yaml.safe_load(
    (BASE_DIR / "profile.yaml").read_text()
)

# Short helper func for formatting the techstack JSON for compact prettyprinting
def format_compact_json(data):
    lines = ["{"]

    items = list(data.items())

    for index, (key, value) in enumerate(items):
        comma = "," if index < len(items) - 1 else ""
        lines.append(f'  "{key}": {json.dumps(value)}{comma}')

    lines.append("}")

    return lines

commands = [
    {
        "name": "whoami",
        "output": [profile["name"]],
    },
    {
        "name": "whereis",
        "output": [profile["location"]],
    },
    {
        "name": "about -e",
        "output": profile["education"],
    },
    {
        "name": "status --current",
        "output": [profile["status"]],
    },
    {
        "name": "curl rana-dip.dev/techstack.json | jq --compact",
        # "output": json.dumps(profile["techstack"],indent=2).splitlines(),
        "output": format_compact_json(profile["techstack"]),
    },
    {
        "name": "cat $HOME/interests.txt",
        "output": [", ".join(profile["interests"])],
    },
    {
        "name": "echo $HOBBIES",
        "output": [", ".join(profile["hobbies"])],
    }
]

# Approximate terminal dimensions based on content
header_height = 40
menu_height = 30
padding = 16
line_height = 20

terminal_lines = sum(
    1 + len(command["output"])
    for command in commands
)

height = (
    header_height
    + menu_height
    + padding
    + terminal_lines * line_height
)

env = Environment(
    loader=FileSystemLoader(BASE_DIR / "templates")
)

template = env.get_template("terminal.svg.j2")

svg = template.render(
    **profile,
    commands=commands,
    width=600,
    height=height,
    font_size=14,
    line_height=line_height,
)

output = BASE_DIR / "profile.svg"
output.write_text(svg)

print(f"Generated {output} successfully")