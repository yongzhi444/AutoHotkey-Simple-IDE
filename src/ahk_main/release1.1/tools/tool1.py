
def isVar(str1):
    # todo 用于判定，当前的字符串,是否符合变量命名规范
    if "-" in str1:
        return False
    if str1[0].isdigit():
        return False
    if str1:
        return True
    else:
        return False
