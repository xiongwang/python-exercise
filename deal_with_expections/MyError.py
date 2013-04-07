import MyIndexError
import MyValueError

userList = ['wangxiong', 'fengjing', 'dunmin', 'jiangge']
user_str = ' '
user_name = 0
input_selectIndex = 0

try:
    input_selectIndex = int(raw_input('Enter the Number to find: '))
    user_str = userList[input_selectIndex]
    input_selectName = raw_input('Enter the Name to find: ')
    user_name = userList.index(input_selectName)
#be careful about the except statments
except IndexError, e:
    print 'Error Number: ', MyIndexError.MyIndexError('1').value
except ValueError, e:
    print 'Error Number: ', MyValueError.MyValueError('2').value
else:
    print 'Index: ' + str(input_selectIndex) + ' User: ' + user_str
    print 'User: ' + input_selectName + ' Index: ' + str(user_name)
