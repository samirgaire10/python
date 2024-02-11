# import re

# # Read the JavaScript code from a file
# with open('script.js', 'r') as file:
#     js_code = file.read()

# # Define a function to replace occurrences of helloButton
# def replace_hello_buttons(match):
#     global button_count
#     button_count += 1
#     if button_count % 3 == 1:
#         return f'helloContent{button_count // 5}'
#     elif button_count % 2 == 0:
#         return f'helloContent{button_count // 3}'
#     else:
#         return f'helloContent{button_count // 1}'

# # Initialize button count
# button_count = 0

# # Replace helloButton occurrences with appropriate values
# modified_code = re.sub(r'helloContent', replace_hello_buttons, js_code)

# # Write the modified JavaScript code back to the file
# with open('modified_script.js', 'w') as file:
#     file.write(modified_code)















import re

# Read the JavaScript code from a file
with open('script.js', 'r') as file:
    js_code = file.read()

# Define a function to replace occurrences of helloButton
def replace_hello_buttons(match):
    global button_count, current_number
    button_count += 1
    if button_count % 3 == 1:
        current_number += 1
    return f'helloContent{current_number}'

# Initialize button count and current number
button_count = 0
current_number = 0

# Replace helloButton occurrences with appropriate values
modified_code = re.sub(r'helloContent', replace_hello_buttons, js_code)

# Write the modified JavaScript code back to the file
with open('modified_script.js', 'w') as file:
    file.write(modified_code)
