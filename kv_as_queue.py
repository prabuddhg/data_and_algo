

kv_store = {
    'head': None,
    'last_committed': None
}


def set(key, value):
    kv_store[key] = value
    kv_store['head'] = key
    print(f"head pointing to {kv_store['head']}")


for i in range(1, 10):
    val = 'foo' + str(i)
    set(i, val)

print(kv_store)
