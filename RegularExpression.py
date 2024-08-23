# RegEX
# A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
# RegEx can be used to check if a string contains the specified search pattern.

# RegEx Module
# Python has a built-in package called re, which can be used to work with Regular Expressions.

#tasks
para  = '''Sarah received several emails this week. On Monday, she got an email from john_doe123@gmail.com regarding a project update. Later, she was contacted by her friend at alice@example.com about a weekend plan. She also received a promotional offer from sales@shopnow.co.uk. On Wednesday, her manager sent her an important document from manager@workplace.com. Sarah noticed that her phone number, 987-654-3210, was included in the email signature.

On Thursday, she received another email from info@business.org, inviting her to a webinar. She saved the contact numbers +44 123 456 7890 and 123-456-7890 in her phone book. Sarah’s friend, Emily, sent a reminder about their meeting, including her new phone number (456) 789-0123.

Sarah is also organizing her calendar and noticed these dates: 09/12/2023, 2023.11.23, and 11-25-2023. She is planning her tasks accordingly.'''
import re
# Questions:

# Find all email addresses in the text.

email  = re.findall(r"[a-zA-Z0-9_-]+@[a-zA-Z]+\.[a-zA-z]+",para)
print(email)

# Extract all phone numbers in the text.

number = re.findall(r"\+?\d{1,2}[-.\s]?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}", para)
print(number)


# Find all dates in the text.

dates = re.findall(r"\b\d{2}[/-]\d{2}[/-]\d{4}\b|\b\d{4}\.\d{2}\.\d{2}\b",para)
print(dates)
# Extract dates in different formats, such as dd/mm/yyyy, yyyy.mm.dd, and mm-dd-yyyy.
# Example: re.findall(r"\b\d{2}[/-]\d{2}[/-]\d{4}\b|\b\d{4}\.\d{2}\.\d{2}\b", text)
# Identify all words that start with a capital letter.

# Find all the words that start with a capital letter.

capital = re.findall(r"\b[A-Z][a-zA-Z]*\b",para)
print(capital)

# Extract all domain names from the email addresses.

domain = re.findall(r"@[a-zA-Z]+\.[a-z]+",para)
print(domain)

