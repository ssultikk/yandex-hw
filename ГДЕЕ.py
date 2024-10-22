city = input()

inlili = ['лилипут', 'Лилипут', 'ЛИЛИПУТ']
inveli = ['великан', 'Великан', 'ВЕЛИКАН']

found_liliput = any(variant in city for variant in inlili)
found_velikan = any(variant in city for variant in inveli)

if found_liliput and found_velikan:
    print("Я совсем запутался.")
elif found_velikan:
    print("В Великании.")
elif found_liliput:
    print("В Лилипутии.")
else:
    print("Я совсем запутался.")
