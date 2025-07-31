import json
import os

import requests

with open("assets/PeriodicTable.json", "r") as file:
    data = json.load(file)


def save_model_and_image(elementName: str) -> None:
    element = next(e for e in data["elements"] if e["name"] == elementName)
    model_path = os.path.join("assets/models/", f"{elementName.lower()}.glb")
    image_path = os.path.join("assets/images/", f"{elementName.lower()}.png")

    if not os.path.exists(model_path):
        response = requests.get(element["bohr_model_3d"])
        with open(model_path, "wb") as model:
            model.write(response.content)
    if not os.path.exists(image_path):
        response = requests.get(element["bohr_model_image"])
        with open(image_path, "wb") as image:
            image.write(response.content)


def main() -> None:
    save_model_and_image("Oxygen")


if __name__ == "__main__":
    main()
