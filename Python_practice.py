counties = ["Arapahoe", "Denver", "Jefferson"]
if counties[1]=='Denver':
    print(counties[1])


counties =["Arapahoe", "Denver", "Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the lsit of counties.")
else:
    print("El Paso is not the list of counties.")



counties = ["Arapahoe", "Denver", "Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")

if"Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties.")


if "Arapahoe" in counties and "El Paso" not in counties:
    print("Only Arapahoe is in the list of counties.")
else:
    print("Arapahoe is in the list of counties and El Paso is not in the list of counties. ")

for county in counties:
    print(county)

x=range(4)
for n in x:
    print(n)

counties_dict = {"Arapahoe":422829, "Denver":463353, "Jefferson":432438}
for county in counties_dict:
        print(county)

for county in counties_dict.keys():
    print(county)

for voters in counties_dict.values():
    print(voters)

for county in counties_dict:
    print(counties_dict[county])

for county in counties_dict:
    print(counties_dict.get(county))

counties_dict = {"Arapahoe":369237, "Denver":413229, "Jefferson":390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters)+" registered voters.")

for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

candidate_votes=int(input("How many votes did the candidate get in the election?"))
total_votes=int(input("What is the total number of votes in the election?"))
message_to_candidate = (
    f"You received {candidate_votes} number of votes."
    f"The total number of votes in the election was {total_votes}."
    f"You received {candidate_votes/total_votes * 100}% of the total votes."

)
print(message_to_candidate)


candidate_votes=int(input("How many votes did the candidate get in the election?"))
total_votes=int(input("What is the total number of votes in the election?"))
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes."
    f"The total number of votes in the election was {total_votes:,}."
    f"You received {candidate_votes/total_votes * 100:.2f}% of the total votes."

)
print(message_to_candidate)

#Import the datetime class from the datetime module.
import datetime
#Use the now() attribute on the datetime class to get the present time.
now= datetime.datetime.now()
#Print the present time.
print("The time right now is", now)
