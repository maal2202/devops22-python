# Lektion 5 - Övning 4

salary1 = int(3000)

print(f'Your current monthly salary is {salary1} \u20AC')

raise1 = int(input("How much more do you think you're worth?\n"))
percent1 = (raise1 / salary1) * 100

print(f"That is a {percent1}% increase, that's way too much \U0001F928")

raise1 = int(input(f'Do you have another offer?\n'))
percent1 = (raise1 / salary1) * 100

attempts = 0

while attempts < 4:
    if percent1 > 3.5:
        percent1 = (raise1 / salary1) * 100
        print(f'That is a {percent1}% increase, still a little too much \U0001F634')
        raise1 = int(input(f'Try me again!\n'))
        attempts += 1
    else:
        print(f"{percent1}%, that's acceptable, we have deal! \U0001F911")
        break

if attempts == 4:
    print(f"You're fired go home! \U0001F611")