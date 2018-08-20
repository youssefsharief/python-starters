from macropy import reduce, _, f  


print(list(map(f[_[0]], ['omg', 'wtf', 'bbq'])))
# ['o', 'w', 'b']

print(list(reduce(f[_ + _], ['omg', 'wtf', 'bbq'])))
