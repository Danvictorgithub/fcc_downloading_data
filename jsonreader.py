from pathlib import Path
import json

path = Path("./eq_data_1_day_m1.geojson")
contents = path.read_text()
all_eq_data = json.loads(contents)

path = Path("./readable_eq_data.geojson")
readable_contents = json.dumps(all_eq_data,indent=2)
path.write_text(readable_contents)

print(readable_contents)