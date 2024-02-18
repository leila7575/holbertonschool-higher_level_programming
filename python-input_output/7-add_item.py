#!/usr/bin/python3
"""script that adds all arguments to a Python list,
and save them to a file
"""


import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    data = load_from_json_file("add_item.json")
except Exception:
    data = []

for arg in sys.argv[1:]:
    data.append(arg)

save_to_json_file(data, "add_item.json")
