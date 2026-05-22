from utils import read_students
from predictor import predictor
from utils import save_predictions
def main():
    students=read_students("students.txt")
    results=[]
    for name, hours in students:
        result= predictor(hours)
        results.append(f"{name}: {result}")
        print(f"{name}: {result}")
    save_predictions("predictions.txt", results)
if __name__ == "__main__":  #It means: “Only run main() when you start this file directly, n  
    main()
