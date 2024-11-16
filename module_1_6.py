name = ('my_dict')
print(name)
phone_book = {'Denis': 1986, 'Max': 1992}
phone_book ['Denis'] = 1
phone_book ['Anton'] = 2
phone_book.update({'Igor': 1989,
                    'Pasha': 1980})
print(phone_book)
print(phone_book.get('Denis'))
print(phone_book.get('Yura'))
print(phone_book.pop('Anton'))
print(phone_book)
print(phone_book.items)
name = ('my_set')
print(name)
set = {15,'персик',20,35,20,'яблоко','персик'}
print(set)
set = {15,'персик',20,35,20,'яблоко','персик',25,'груша'}
print(set)
print(set.discard('персик'))
print(set)