class MyGetitem:
    def __getitem__(self, key):
        if key == 'Thank U':
            return 'You are welcome!'
        elif key == 'Sorry':
            return 'That\'s all right!'
        elif key == 'Do you like me':
            return 'ELIF STATMENTS'
        else:
            return 'ELSE STATMENTS'

if __name__ == "__main__":
    mygetitem = MyGetitem()
    print mygetitem['i']
    print mygetitem['j']
    print mygetitem['k']
    print mygetitem['p']

