class MySetitem:
    def __setitem__(self, key, value):
        print 'key=%s, value=%s' %(key, value)

mysetitem = MySetitem()
mysetitem['abc'] = 'abc_full'
mysetitem['def'] = 'def_full'
mysetitem['zzz'] = 'zzz_full'
