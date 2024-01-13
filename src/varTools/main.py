

def get_dvalue(dictionary: dict, path):
    result = None
    try:
        for obj in path:
            dictionary = dictionary[obj]
        return dictionary
    except Exception:
        return None


if __name__ == "__main__":
    print('RUN TESTS varTools.get_dvalue')
    test1 = {'one':{'two':'2', 'three': 3, 'four': {4:['four and five']}}}
    assert get_dvalue(test1, ['one', 'four', 4,0]) == 'four and five'

    test2 = {"one":[0, {'seeking':'result'}], 'two':'error'}
    assert get_dvalue(test2, ['one', 1, 'seeking']) == 'result' , f"[UnitTest] Fail. {get_dvalue(test2, ['one', 11, 'seeking'])} != 'result' "

    test3 = {"one":[0, {'seeking':'result'}], 'two':'error'}
    assert get_dvalue(test2, ['one', 11, 'seeking']) is None, f"[UnitTest] Fail. Не получили ошибку при некорректном пути в листе. "
    print('TEST COMPLETED.')