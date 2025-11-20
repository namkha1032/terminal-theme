
# import debugpy
# debugpy.listen(("0.0.0.0", 5678))
# print("Waiting for debugger attach...")
# debugpy.wait_for_client()
# Get the current working directory
import os
current_path = os.getcwd()

# Print the result
print(f"The current working directory is: {current_path}")
current_dir = os.path.dirname(os.path.abspath(__file__))

print("The file directory is:", current_dir)
pass