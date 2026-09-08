# list of alphabets
alphabets = ['a', 'b', 'd', 'e', 'i', 'j', 'o']
filteredVowels = filter(lambda x: x in ['a', 'e', 'i', 'o', 'u'], alphabets)
print('The filtered vowels are: {}'.format(list(filteredVowels)))

seq = [1,2,3,4,5]
x= list(filter(lambda num: num%2== 0, seq))
print(f"Only even number list: {x}")
