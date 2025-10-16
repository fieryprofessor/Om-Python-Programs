import os

def create_python_files(n):
    for i in range(1, n + 1):
        filename = f"Q{i}.py"
        if not os.path.exists(filename):
            with open(filename, "w") as f:
                f.write("# Python file {}\n".format(filename))
            print(f"Created: {filename}")
        else:
            print(f"Skipped (already exists): {filename}")

if __name__ == "__main__":
    try:
        n = int(input("Enter the number of files to create: "))
        create_python_files(n)
    except ValueError:
        print("Please enter a valid integer.")
