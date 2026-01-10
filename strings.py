"""""
def normalize_name(name: str) -> str:

    return name.strip().title()
name = input("Enter your name: ")
print(normalize_name(name))



def is_valid_email(email: str) -> bool:

    return "@" in email and email.endswith(".com")
email = input("Enter your email: ")
print(is_valid_email(email))



def replace_strings(text: str) -> str:

    return text.replace("a", "4").replace("e", "3").replace("i", "1").replace("o", "0").replace("s", "5")
text = input("Enter a text: ")
print(replace_strings(text))

"""""


import csv
import io

def csv_line_to_dict(header_line: str, data_line: str) -> dict:
    """
    Converts a single CSV data line string into a dictionary using a separate header line string.
    """
    # Use io.StringIO to treat the string as a file
    f_header = io.StringIO(header_line)
    f_data = io.StringIO(data_line)

    # Use csv.reader to parse the lines into lists
    header = next(csv.reader(f_header))
    data = next(csv.reader(f_data))

    # Combine the header and data lists into a dictionary
    csv_dict = dict(zip(header, data))
    
    return csv_dict

# Example Usage:
header_str = "Name,Age,City"
data_str = "'John Doe',30,'New York'"

result_dict = csv_line_to_dict(header_str, data_str)
print(result_dict)
# Output: {'Name': 'John Doe', 'Age': '30', 'City': 'New York'}
