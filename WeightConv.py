#1 lb = 0.453592 kg
weight = float(input('Enter Weight: '))
lbkg = input('Is that in (L)bs or (K)gs? ')
if lbkg.upper() == 'L':
    print('That is ',str(weight * .45) + 'in kg')
   
elif lbkg.upper() == 'K':
    print('That is ',str(weight / .45) + 'in lbs')