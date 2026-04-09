import keyword
print(keyword.kwlist)

#length of keywords
print(len(keyword.kwlist))

# Check kw is valid or not
print(keyword.iskeyword('and'))
print(keyword.iskeyword('AND'))
print(keyword.iskeyword('else'))
print(keyword.iskeyword('class'))
print(keyword.iskeyword('Else'))