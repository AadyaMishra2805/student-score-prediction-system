def read_students(filename):
    students = []
    try:
        with open(filename, 'r') as file:
            lines= file.readlines()
            for line in lines:
                name, hours = line.strip().split(',')
                students.append((name, int(hours)))
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except ValueError:
        print(f"Error: The file '{filename}' contains invalid data.")
    return students
def save_predictions(filename, predictions):
    with open(filename,"w") as file:
        for prediction in predictions:
            file.write(prediction + "\n")