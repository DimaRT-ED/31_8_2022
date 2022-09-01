from temp_class import Tmp
if __name__ == '__main__':
    print(Tmp.counter)
    tmp1 = Tmp()
    tmp1.set_name('tmp1')
    tmp1.set_id(1)
    print(' tmp1 name = ', tmp1.get_name(),', id  ', tmp1.get_id())
    print(Tmp.counter)

    tmp2 = Tmp('tmp2', 2)
    print(' tmp2 name = ', tmp2.get_name(), ', id  ', tmp2.get_id())
    print('Counter from staticmethod ' , Tmp.get_counter())

