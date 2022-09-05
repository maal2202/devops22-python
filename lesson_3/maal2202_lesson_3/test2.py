# Uppgift B, lektion 3

# List över alla personer, vilka läggs in i listan senare med .append
persons = []

# Person_1
name1 = input("Name of person 1:\n>").lower()
age1 = input("How old is person 1:\n>").lower()
shoe1 = input("Shoe size of person 1:\n>").lower()
person1 = (name1, age1, shoe1)
persons.append(person1)

# Person_2
name2 = input("Name of person 2:\n>").lower()
age2 = input("How old is person 2:\n>").lower()
shoe2 = input("Shoe size of person 2:\n>").lower()
person2 = (name2, age2, shoe2)
persons.append(person2)

# Person_3
name3 = input("Name of person 3:\n>").lower()
age3 = input("How old is person 3:\n>").lower()
shoe3 = input("Shoe size of person 3:\n>").lower()
person3 = (name3, age3, shoe3)
persons.append(person3)

sorted_shoe = sorted(persons, key=lambda y: y[2])
sorted_age = sorted(persons, key=lambda y: y[1])

oldest = sorted_age[2]
median_shoe = sorted_shoe[1]

print(f'The oldest person is {oldest[0].title()}, with a shoe size of {oldest[2]}')
print(f'{median_shoe[0].title()} has the median shoe size and is {median_shoe[1]} years old.')

# Sökfunktion, krävs att man fyller i någon utav de tre sökvariablerna "name" "age" "shoe" följt av värdet du letar efter, 
# exempelvis "shoe 43", "age 34", eller "name martin". 
searches = {
    "name": {
        str(name1): person1,
        str(name2): person2,
        str(name3): person3
    },
    "age": {
        str(age1): person1,
        str(age2): person2,
        str(age3): person3
    },
    "shoe": {
        str(shoe1): person1,
        str(shoe2): person2,
        str(shoe3): person3
    }
}
prop, value = input("Enter prop value: ").split(" ")
print(searches[prop][value])