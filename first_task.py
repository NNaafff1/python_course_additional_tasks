import re

def remove_comments(code):
    # 1) Удаляем многострочные комментарии /* ... */
    code = re.sub(r'/\*.*?\*/', '', code, flags=re.DOTALL)
    # 2) Удаляем однострочные комментарии // ...
    code = re.sub(r'//.*', '', code)
    return code

input_code = """/*
* My first ever program in Java!
*/
class Hello { // class body starts here

/* main method */
public static void main(String[] args/* we put command line arguments here*/) {
    // this line prints my first greeting to the screen
    System.out.println("Hi!"); // :)
}
// the end
// to be continued...
"""
print("Входная строка:")
print(input_code)

# Удаление комментариев
output_code = remove_comments(input_code)

print("\nВыходная строка:")
print(output_code)