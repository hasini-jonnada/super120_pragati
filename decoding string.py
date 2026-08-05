def decodeString(s: str) -> str:
    stack = []
    current_num = 0
    current_str = ""

    for char in s:
        if char.isdigit():
            # Build the number (can be more than 1 digit)
            current_num = current_num * 10 + int(char)
        elif char == '[':
            # Push current state to stack
            stack.append((current_str, current_num))
            current_str = ""
            current_num = 0
        elif char == ']':
            # Pop from stack and build new string
            last_str, repeat_num = stack.pop()
            current_str = last_str + current_str * repeat_num
        else:
            # Normal character, add to current string
            current_str += char

    return current_str
