# pywinauto-supporter

```
import pywinauto
from pywinauto_supporter.utils import blink

app = pywinauto.application.Application(backend='uia').connect(title='계산기')
#app = pywinauto.application.Application(backend='uia').connect(process=process_id)
#app = Application(backend='uia').connect(title_re="Notepad\+\+") #정규식으로 프로그램 title을 검색해서 연결하는 방법
top_window = app.top_window()

blink(top_window.handle)

one_window = top_window.child_window(title="1")
#one_window.wrapper_object().click_input()
#blink(one_window.handle)
```
