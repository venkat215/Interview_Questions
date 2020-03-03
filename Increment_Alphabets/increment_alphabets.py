
ords_ = [97]
min_ord = 97
max_ord = 122

def char_return(ord_):
    return chr(ord_)

def rearrage_ords():

    carry_over = 1

    for i in range(len(ords_)-1, -1, -1):

        if carry_over:
            if ords_[i] < max_ord:
                ords_[i]+= 1
                carry_over = 0
            else:
                ords_[i] = min_ord
                carry_over = 1
        
        if carry_over and (not i):
            ords_.insert(0, min_ord)

def form_alias():

    alias = ''
    for i in range(len(ords_)):
        alias+= chr(ords_[i])
    
    rearrage_ords()
    return alias

for j in range(10000):
    if j == 27:
        stop = 1
    print(form_alias())