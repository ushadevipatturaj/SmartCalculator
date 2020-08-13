from collections.abc import Hashable
objects_dict = {}
for i in objects:
    if isinstance(i, Hashable):
        objects_dict[i] = i.__hash__()