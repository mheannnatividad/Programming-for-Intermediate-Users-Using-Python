class ClubMembers:
    def __init__(self, name, birthday, age, favoriteFood, goal):
        self.name = name
        self.birthday = birthday
        self.age = age
        self.favoriteFood = favoriteFood
        self.goal = goal
    
    def displayMember(self):
        print("Parent/Member Information:")
        print("Name: " + self.name)
        print("Birthdate: " + self.birthday)
        print("Age: " + str(self.age))
        print("Favorite Food: " + self.favoriteFood)
        print("Goal: " + self.goal)

class ClubOfficers(ClubMembers):
    def __init__(self, name, birthday, age, favoriteFood, goal, position):
        self.position = position
        ClubMembers.__init__(self, name, birthday, age, favoriteFood, goal)
    
    def displayOfficer(self):
        print("Child/Officer Information:")
        print("Name: " + self.name)
        print("Birthdate: " + self.birthday)
        print("Age: " + str(self.age))
        print("Favorite Food: " + self.favoriteFood)
        print("Goal: " + self.goal)
        print("Position: " + self.position)
        
m_1 = ClubMembers("Tom", "January 16", 14, "Ice Cream", "To be Happy")
m_1.displayMember()
o_4 = ClubOfficers("Vera", "June 22", 16, "Beef Stroganoff", "To be the World's greatest Chef", "Treasurer")
o_4.displayOfficer()
    