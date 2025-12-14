# global varoable and import


# getting user input
def get_user_input():
    weight = float(input("weight(kg): "))
    height = float(input("height (m): "))
    return height, weight


# calculate bmi
def calculate_bmi(height, weight):
    return weight // (height**2)


# get the bmi result
def get_bmi_result(bmi):
    if bmi < 18.5:
        print(f"bmi: {bmi}", "result: ", "under weight")
    elif 18.5 <= bmi < 25:
        print(f"bmi: {bmi}", "result: ", "normal")
    elif 25 <= bmi < 30:
        print(f"bmi: {bmi}", "result: ", "over weight")
    elif 30 <= bmi < 35:
        print(f"bmi: {bmi}", "result: ", "obese")
    else:
        print(f"bmi: {bmi}", "result: ", "extremely obese")


# main function to run
def main():
    height, weight = get_user_input()
    get_bmi_result(calculate_bmi(height, weight))


if __name__ == "__main__":
    main()
