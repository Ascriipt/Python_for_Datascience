from give_bmi import give_bmi, apply_limit
import random

def main():
    """
    BMI func Tester
    """
    # print(give_bmi([random.randint(0, 100) for _ in range(10)], [random.randint(0, 100) for _ in range(10)]))
    height = [2.71, 1.15]
    weight = [165.3, 38.4]

    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))

if __name__ == "__main__":
    try :
        main()
    except RuntimeError as e :
        print (f"Error: {e}")
