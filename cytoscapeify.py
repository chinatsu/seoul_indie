from yaml import load
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader
from json import dumps
from jinja2 import Environment, FileSystemLoader


with open("data/seoul_indie.yaml", "r") as f:
    data = load(f, Loader=Loader)


def get_nodes(data):
    nodes = []
    for node in data["nodes"]:
        nodes.append({"data": {"type": node["type"], "id": node["id"], "name": node["name"], "url": node.get("url", "")}})
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
    elements_json = dumps({"nodes": nodes, "edges": edges}, indent=2, ensure_ascii=False)

    env = Environment(loader=FileSystemLoader("."))
    template = env.get_template("template/seoul_indie.html")
    output = template.render(elements_json=elements_json)

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(output)

if __name__ == "__main__":
    build()