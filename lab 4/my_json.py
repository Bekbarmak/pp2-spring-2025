import json

with open("sample-data.json", "r") as file:
    data = json.load(file)

print("Interference status")
print("=" * 90)
print(f"{'DN':<50} {'Description':<20} {'Speed':<7} {'MTU'}")
print("-" * 90)

for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    dn = attributes["dn"]
    description = attributes.get("descr", "")
    speed = attributes.get("speed", "inherit")
    mtu = attributes["mtu"]
    print(f"{dn:<50} {description:<20} {speed:<7} {mtu}")