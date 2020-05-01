import re


def Bs_Magic(str):
    """
    博深魔改的部分
    :param str: 任意一个字符串（一行）
    :return: 标准ahk代码,可能会返回好几行，然后中间夹着\n进行返回
    """
    if not str.strip().startswith("bs$"):
        return str
    # 现阶段支持的语句：
    a = "bs$ Hotkey Ctrl q::"
    b = "bs$ Click, WheelDown,1"
    command = re.findall(" *bs[$] *([A-Za-z]*)[, ]", str)
    if command[0] == "Hotkey":
        temp = re.split("[, ;+\n]", str)
        while "" in temp:
            temp.remove("")
        key_num = temp.index("::") - 2
        if key_num == 1:
            return temp[2] + "::"
        elif key_num == 2:
            return temp[2] + " & " + temp[3] + "::"
    elif command[0] == "Click":
        temp = re.split("[, ;]", str)
        while "" in temp:
            temp.remove("")
        return "Loop " + temp[3] + "{\n    Click, " + temp[2] + "\n}\n"
    else:
        print("An err")