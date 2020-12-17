h,m,s = map(int, input().strip().split(':'))
if h < 12: # means its AM
    h += 12 if h==0 else 0 
    print('{:0>2d}:{:0>2d}:{:0>2d}AM'.format(h,m,s))
else:#means its PM
    h=h%12
    h += 12 if h==0 else 0 
    print('{:0>2d}:{:0>2d}:{:0>2d}PM'.format(h,m,s))
