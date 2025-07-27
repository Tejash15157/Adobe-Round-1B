import os
import json
import time
from semantic import rank_sections
from parser import extract_sections

def main():
    input_dir = "/app/input"
    output_file = "/app/output/output.json"

    with open(os.path.join(input_dir, "persona.json")) as f:
        persona_data = json.load(f)

    all_sections = []
    for filename in os.listdir(input_dir):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(input_dir, filename)
            all_sections.extend(extract_sections(pdf_path, filename))

    ranked = rank_sections(all_sections, persona_data["job"])

    result = {
        "metadata": {
            "documents": list(set(s["document"] for s in all_sections)),
            "persona": persona_data["persona"],
            "job": persona_data["job"],
            "timestamp": time.ctime()
        },
        "top_sections": ranked[:10]
    }

    with open(output_file, "w") as f:
        json.dump(result, f, indent=2)

if __name__ == "__main__":
    main()
