# pywinauto-supporter

```
from pywinauto_supporter.utils import blink

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

```




    app = Application(backend='uia').connect(process=int(process_id)) #프로세스 pid로 연결하는 방법
    #app = Application(backend='uia').connect(title_re="Notepad\+\+") #정규식으로 프로그램 title을 검색해서 연결하는 방법
    blink(handle)
```
