def modify_string(input_str: str, k: int):
    """
    如果一个字符在它前面k个字符中已经出现过了, 就把这个字符改成’-’
    :param input_str: 给定的输入字符串
    :param k: 需要比较前k个字符
    :return: 修改后的字符串modified_str
    """
    assert type(input_str) == str and type(k) == int
    modified_str = ''
    seen_chars = list()  # 存储前k个字符

    for i, current_char in enumerate(input_str):
        modified_char = '-' if current_char in seen_chars else current_char
        if i >= k:  # 从第(k+1)个字符开始删去之前的第k个字符
            seen_chars.pop(0)
        seen_chars.append(current_char)  # 加入当前位置出现的字符
        modified_str += modified_char

    return modified_str


if __name__ == "__main__":
    # 测试样例
    print(modify_string('abcdefaxc', 10))  # abcdef-x-
    print(modify_string('abcdefaxcqwertba', 10))  # abcdef-x-qw-rtb-
