def main():
    number = int(input("Enter number"))
    list = [9, 10, 23, 15, 47, 2, 29, 36, 58, 14, 30, 16, 90, 40, 83]
    for i in range(len(list)):
        for j in range(len(list)):
            if i == j:
                break
            if list[i] + list[j] == number:
                print(f"{list[i]}, {list[j]} is a pair for number {number}")
                return
    print(f"No pair has sum equal to {number}")

main()