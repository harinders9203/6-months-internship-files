import hashlib
"""
sha256 encoding
a="admin123"
ae=a.encode()
ah=hashlib.sha256(ae)
print(ah.hexdigest())"""

"""
MD5 encoding
a="admin123"
ah=hashlib.md5(a.encode())
print(ah.hexdigest())
"""


#one line hashing
a=hashlib.sha256("admin123".encode()).hexdigest()
print(a)