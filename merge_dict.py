#!/usr/bin/python3
from itertools import chain
from collections import ChainMap

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

Alternative 1: .update()
========================
dict1.update(dict2)
print(dict1)

Alternative 2: (|) operater
===========================
merged_dict = dict1 | dict2
print(merged_dict)

Alternative 3: Double asterisk (**)
===================================
merged_dict = {**dict1, **dict2}
print(merged_dict)

Alternative 4: itertools.chain()
================================
merged_dict = dict(chain(dict1.items(), dict2.items()))
print(merged_dict)

Alternative 5: collections.ChainMap()
=====================================
merged_dict = ChainMap(dict2, dict1)
print(dict(merged_dict))
