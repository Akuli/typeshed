from tkinter import Event, Misc, Widget
from typing import Optional, Protocol

class DndSource(Protocol):
    def dnd_end(self, target: Optional[Widget], event: Optional[Event[Misc]]) -> None: ...
