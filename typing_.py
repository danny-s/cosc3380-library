from typing import Union, Iterable

import web

Fields = Union["web.MultiField", dict[str, str], Iterable[tuple[str, str]]]
Headers = Fields
Status = Union[str, int]
ResponseBody = Union[str, bytes, Iterable[bytes]]

QuerySet = dict[str, list[str]]