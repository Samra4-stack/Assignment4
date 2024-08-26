                # Assignment 4
                # (using function)
# Question no 1  (Calculate age)
def age(birth_year,current_year):
    age = current_year - birth_year
    print(age)
age(2005,2024)

# Question no 2 (Calculate Area of Rectangle)
def area(height,width):
    area = height * width
    print(area)
area(20,30)

# Question no 3  (Calculate Area of Circle)
def areaofcircle( radius):
    area = 3.14*radius**2
    print(area)
areaofcircle(30)

# Question no 4 (Calculate Area of CUBE)
def areaofcube(edges):
    area = 6*edges**2
    print(area)
areaofcube(30)

# Question no 5  (Convert Celsius into fahrenheit & vice versa)
def ConvertToFahrenheit(Celsius):
    fahrenheit = (Celsius * 9/5) + 32
    print(fahrenheit)
ConvertToFahrenheit(32)
def ConvertToCelsius(fahrenheit):
    Celsius = (fahrenheit - 32) * 5/9
    print(Celsius)
ConvertToCelsius(0)
    
# Question no 6 (Convert minutes into seconds & vice versa) 
def ConvertToSeconds(minutes):
    seconds = minutes * 60
    print(seconds)
ConvertToSeconds(23)
def ConvertToMinutes(seconds):
    minutes = seconds / 60
    print(minutes)  
ConvertToMinutes(2300) 
   
# Question no 7 (Calculate Percentage)
def CalculatePercentage(obtained,total):
    percentage = (obtained / total) * 100
    print(percentage)
CalculatePercentage(80,100)

# Question no 8 (Calculate BMI)
def calculateBMI(weight,height):
    bmi = weight / (height ** 2)
    print(bmi)
calculateBMI(75, 1.75)

# Question no 9 (Volume of cylinder)
def calculateVolumeofCylinder(radius,height):
    volume = 3.14 * radius ** 2 * height
    print(volume)
calculateVolumeofCylinder(5, 10)
