
html_content = "<html><head><meta name=\"color-scheme\" content=\"light dark\"><meta charset=\"utf-8\"></head><body><pre>[{\"id\":1,\"name\":\"Item A\"},{\"id\":2,\"name\":\"Item B\"}]
</pre><div class=\"json-formatter-container\"></div></body></html>"
start_index = html_content.find("<pre>") + len("<pre>")
end_index = html_content.find("</pre>")
json_string = html_content[start_index:end_index].strip()

import json
items = json.loads(json_string)

item_name_99 = None
for item in items:
    if item.get("id") == 99:
        item_name_99 = item.get("name")
        break
print(item_name_99)
