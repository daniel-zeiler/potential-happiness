import re


def parse_file(file_path):
    # Read the file content
    with open(file_path, 'r') as file:
        file_content = file.read()

    # Regular expression to extract the comment (non-greedy)
    comment_pattern = re.compile(r'\"\"\"(.*?)\"\"\"', re.DOTALL)

    # Regular expression to extract the function definition
    function_pattern = re.compile(r'def\s+([a-zA-Z_][a-zA-Z_0-9]*\s*\([^)]*\)\s*:\s*[a-zA-Z_][a-zA-Z_0-9]*)',
                                  re.MULTILINE)

    # Find comment
    comment_match = comment_pattern.search(file_content)
    for result in function_pattern.findall(file_content):
        print(result)
    if comment_match:
        comment = comment_match.group(1)
        print("Comment:")
        print(comment)
    else:
        print("No comment found")

    # Find function definition
    function_match = function_pattern.search(file_content)
    if function_match:
        function_def = function_match.group(0)
        for function_def in function_match.groups():
            print(function_def)
        print("\nFunction Definition:")
        print(function_def)
    else:
        print("No function definition found")


# Replace 'example_file.txt' with the path to your actual file
file_path = r"C:\Users\danie\PycharmProjects\potential-happiness2\TakeTwo\array_problems\Problems.py"
parse_file(file_path)
