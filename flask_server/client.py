# -*- coding: utf-8 -*-

from pprint import pprint
from requests_toolbelt import MultipartEncoder
import requests

m = MultipartEncoder(
        fields={
            'field0': 'value',
            'num': '2',
            'picture': ('picture.jpg', open('atom.jpg', 'rb'), 'image/jpg')}
        )

r = requests.post(
        # 'http://httpbin.org/post',
        'http://localhost:5000/post',
        data=m,
        headers={'Content-Type': m.content_type}
        )

pprint(r.__dict__)
pprint(vars(r))
