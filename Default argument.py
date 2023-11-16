# illustrating Default arguments

def id(name, course="CPE"):
    print("Name is " + name)
    print("Course is " + course)

id("James", "Agric")

#so basically, if you don't give it a parament, the function uses the default argument. it prints agric on the first call and on the second call it prints the default argument, which is CPE

id("James")
