def is_dot_in_string(text):
    return  '.' in text
print(is_dot_in_string('We are going to the moon.'))

def is_dollor_sign_string(text):
    for char in text:
        if char != '$':
            return False
    return True

print(is_dollor_sign_string('$$$$$$$$O$'))