import json
from urllib.parse import urlencode
from types import SimpleNamespace
from api import index  # this imports your Vercel-style handler

# Simulate a request
query = urlencode({'name': ['K', 'Bob']})
fake_request = SimpleNamespace(query_string=query.encode())
fake_response = SimpleNamespace(
    headers={},
    json=lambda body: print(json.dumps(body, indent=2))
)

# Run handler
index.handler(fake_request, fake_response)
