import json
import os

import requests
import trimesh

with open("assets/PeriodicTable.json", "r") as file:
    data = json.load(file)


def get_glb_model(elementName: str) -> str:
    element = next(e for e in data["elements"] if e["name"] == elementName)
    model_path = os.path.join("assets/models/", f"{elementName.lower()}.glb")

    if not os.path.exists(model_path):
        response = requests.get(element["bohr_model_3d"])
        with open(model_path, "wb") as model:
            model.write(response.content)

    return model_path


def main() -> None:
    oxygen_path = get_glb_model("Oxygen")
    mesh = trimesh.load(oxygen_path)
    if isinstance(mesh, trimesh.Trimesh):
        scene = mesh.scene()
    else:
        scene = mesh
    scene.background = [0, 0, 0, 255]  # type: ignore[attr-defined]
    scene.show()


if __name__ == "__main__":
    main()
