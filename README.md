# pywinauto-supporter

```
import pywinauto
from pywinauto_supporter.utils import blink

app = pywinauto.application.Application(backend='uia').connect(title='계산기')

top_window = app.top_window()
blink(top_window.handle)

one_window = top_window.child_window(title="1")
#one_window.wrapper_object().click_input()
#blink(one_window.handle)
```
