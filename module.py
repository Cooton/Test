import study50 as const
const.NAME='FishC'
print(const.NAME)
try :
    const.NAME='FishC.com'
except TypeError as Err:
    print(Err)
    
