domain_names = {
    "r3": "2001:db8:cafe:1::300",
    "r4": "2001:db8:cafe:1::400",
    "r5": "2001:db8:cafe:1::500"
}

for value, key in domain_names.items():
    print(f"ip host {value} {key}")