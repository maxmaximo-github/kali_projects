from dns import resolver


domain_names = {
    # "r3.example.com": "2001:db8:cafe:1::300",
    # "r4.example.com": "2001:db8:cafe:1::400",
    # "r5.example.com": "2001:db8:cafe:1::500",
    "r9.example.com": "2001:db8:cafe:1::900"
}

register_list = []
for key in domain_names.keys():

    answers = resolver.query(f"{key}", "AAAA")
    print(answers)

    for answer in answers:
        register_list.append(f"Host {key} has {answer}")

for register in register_list:
    print(f"{register}")


# for datum in answer:

#    print(datum)