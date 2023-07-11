# win32gui-supporter

```
from win32gui_supporter.utils import blink

handle = None 
process_id = None 
for name, value in self.tree_model.props_dict.get(data):
    if name == "handle":
        try:
            handle = int(value)
        except:
            pass
    elif name == "process_id":
        try:
            process_id = int(value)
        except:
            pass

if handle and process_id:
    blink(process_id, handle)
```
