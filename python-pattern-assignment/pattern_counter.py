def count_pattern(text, pattern):
    count = 0
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i+len(pattern)] == pattern:
            count += 1
    return count
string = input("Enter a string: ")
pattern = input("Enter a pattern: ")
print("Occurrences:", count_pattern(string, pattern))