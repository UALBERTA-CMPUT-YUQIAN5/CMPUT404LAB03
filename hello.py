#!/usr/bin/env python3
import os
"""
print("Content-type: text/json")
print()
print(os.environ)
"""

"""
queries = os.environ.get("QUERY_STRING")

print("Content-type: text/plain")
print()
print(queries)
"""


browser = os.environ.get("HTTP_USER_AGENT")

print("Content-type: text/plain")
print()
print(browser)





