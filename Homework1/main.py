"""
This is my first homewor for this python course.
The code has one of my favourite songs (the first one i got in mind) and some characteristics of it.
"""


#The song is Chateau from Angus & Julia Stone
#The first variables will be the String variables
Song = "Chateau"
Artist = "Angus & Julia Stone"
Producer1, Producer2 = "Angus Stone", "Julia Stone"
Album = "Snow"
Genre = "Pop"
Label = "EMI"
MonthRealized = "August"

#The next variables will be the float variables

Duration = 4.33

#The last variables will be the integers

DayRealized = 24
YearRealized = 2017

#Here I print all of the attributes from the variables
print("My favourite song is " + Song + " from " + Artist + ".")
print ("The song was written and produced by " + Producer1 + " and " + Producer2 + ".")
print("This is a " + Genre + " song featured in the album " + Album + ". Labeled by " + Label + ".")
print ("This " + str(Duration) + " minutes long song, was realized on " + str(DayRealized) + ", "+ MonthRealized + ", " + str(YearRealized) + ".")

