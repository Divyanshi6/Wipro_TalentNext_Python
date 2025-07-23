#        **************** MINI PROJECT ****************

# Through command line arguments three strings separated by space are given to you. Each string is a series of numbers separated by hyphen (-).
# You like all the numbers in string 1.
# You dislike all the numbers in string 2.
# Third string contains the numbers given to you. Your initial happiness is 0.
# When you encounter a number in string 1, add +1 to happiness.
# If it is in string 2, subtract -1 from happiness.
# Otherwise, no change.
# Output your final happiness at the end.
import sys
if len(sys.argv) != 4:
    print("Usage: python script.py <likes> <dislikes> <numbers>")
    print("Example: python script.py 3-1 5-7 1-5-3-8")
    sys.exit()

likes_string = sys.argv[1]
dislikes_string = sys.argv[2]
numbers_string = sys.argv[3]

likes = set(map(int, likes_string.split('-')))
dislikes = set(map(int, dislikes_string.split('-')))
numbers = list(map(int, numbers_string.split('-')))

happiness = 0

for num in numbers:
    if num in likes:
        happiness += 1
    elif num in dislikes:
        happiness -= 1

print(happiness)
