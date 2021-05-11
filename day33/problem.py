import collections
# Create a deque
deque_colors = collections.deque(["Red","Green","White"])
print(deque_colors)
# Append to the left
print("\nAdding to the left: ")
deque_colors.appendleft("Pink")
print(deque_colors)
# Append to the right
print("\nAdding to the right: ")
deque_colors.append("Orange")
print(deque_colors)
# Remove from the right
print("\nRemoving from the right: ")
deque_colors.pop()
print(deque_colors)
# Remove from the left
print("\nRemoving from the left: ")
deque_colors.popleft()
print(deque_colors)
# Reverse the dequeue
print("\nReversing the deque: ")
deque_colors.reverse()
print(deque_colors)
