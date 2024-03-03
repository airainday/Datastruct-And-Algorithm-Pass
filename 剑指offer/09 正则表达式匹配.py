def is_match(s, p):
    if not p:
        return not s
    # 判断第一个字符是否匹配
    first_match = bool(s) and p[0] in {s[0], '.'}
    if len(p) >= 2 and p[1] == '*':
        # is_match(s, p[2:])相当于模版中当前*前面字符出现了0次
        # first_match and is_match(s[1:], p)则是出现了1次或者多次
        return is_match(s, p[2:]) or (first_match and is_match(s[1:], p))
    else:
        return first_match and is_match(s[1:], p[1:])

# 测试
print(is_match("aaa", "a*a"))   # True
print(is_match("abaca", "ab*a"))   # False
