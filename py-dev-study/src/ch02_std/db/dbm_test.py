import dbm

"""
测试dbm 
"""
with dbm.open("cache", "c") as db:

    # Record some values
    db[b"hello"] = b"there"
    db["py"] = "Python lang"
    db["java"] = "Java lang"
    db["erl"] = "Erlang lang"
    assert db[b"erl"] == b"Erlang lang"

    print(db.get("python", b"not present"))

    db["www.yahoo.com"] = b"4"

# db is automatically closed when leaving the with statement.
