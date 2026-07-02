from yaml import load

try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader
from json import dumps
from jinja2 import Environment, FileSystemLoader
from datetime import datetime

COLORS = {
    "background": "#EAE0CB",
    "foreground": "#33302A",
    "mutedText": "#7C7566",
    "nodePerson": "#5568C9",
    "nodePersonStroke": "#3B4CA0",
    "nodeGroup": "#E0A63A",
    "nodeGroupStroke": "#B9821C",
    "edgeDefault": "#B2A88F",
    "edgeProduced": "#2F7FCB",
    "edgeRemixed": "#2E9E63",
    "edgeFeatured": "#9457C9",
    "edgeCollaboratedWith": "#D9772E",
    "edgeSoundDirectorFor": "#D14B63",
    "edgeGaveLessonsTo": "#1C9AA2",
    "edgeSessionedFor": "#D9772E",
}


with open("data/seoul_indie.yaml", "r") as f:
    data = load(f, Loader=Loader)


def get_nodes(data):
    nodes = []
    for node in data["nodes"]:
        nodes.append(
            {
                "data": {
                    "type": node["type"],
                    "id": node["id"],
                    "name": node["name"],
                    "url": node.get("url", ""),
                }
            }
        )
    return nodes


def get_edges(data):
    edges = []
    for node in data["nodes"]:
        for conn in node.get("connects_to", []):
            if isinstance(conn, dict):
                target = conn["target"]
                label = conn.get("label")
            else:
                target = conn
                label = None

            edge_id = f"{node['id']}_cc_{target}"
            edge_data = {"source": node["id"], "target": target, "id": edge_id}
            if label:
                edge_data["label"] = label
            edges.append({"data": edge_data})
    return edges


def build():
    nodes = get_nodes(data)
    edges = get_edges(data)
    elements_json = dumps(
        {"nodes": nodes, "edges": edges}, indent=2, ensure_ascii=False
    )

    env = Environment(loader=FileSystemLoader("."))
    template = env.get_template("template/seoul_indie.html")
    output = template.render(
        elements_json=elements_json, last_updated=datetime.now().strftime("%Y-%m-%d"), colors=COLORS
    )

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(output)


if __name__ == "__main__":
    build()
