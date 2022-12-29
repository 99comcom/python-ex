def merge_string(*params):
    print(type(params))
    for text in params:
        print(text)
        
        
merge_string("홍길동","심청이","강감찬")

def print_words(**params):
    print(type(params))
    for key in params:
        print("{0}의 값은 {1}입니다.".format(key,params[key]))
        
        
print_words(고양이="cat",강아지="dog",소녀="girl")
