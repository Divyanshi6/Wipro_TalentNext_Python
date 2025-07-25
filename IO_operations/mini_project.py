
from collections import Counter

def get_meeting_details(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    no_of_lines = len(lines)
    if no_of_lines > 12:
        meeting_time = f"{no_of_lines - 12} PM"
    else:
        meeting_time = f"{no_of_lines} AM"
    
 
    all_words = []
    for line in lines:
        words = line.strip().split()
        for word in words:
            cleaned = ''.join(char for char in word if char.isalnum())
            if cleaned:
                all_words.append(cleaned.lower())
    
    word_counts = Counter(all_words)
    most_common_word, _ = word_counts.most_common(1)[0]
    meeting_place = most_common_word.capitalize() + " Street"
    
    return meeting_time, meeting_place

file_names = ["sample1.txt", "sample2.txt"] 
for i, file in enumerate(file_names, start=1):
    time, place = get_meeting_details(file)
    print(f"Sample Output {i}:")
    print("Meeting time:", time)
    print("Meeting place:", place)
    print()
