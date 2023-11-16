#This program is to illustrate the use if variable length argument

def personnel(name, *Fav_subjects):
    print( name, "enjoys reading")
    for subjects in Fav_subjects:
        print(subjects)

personnel("Micheal", "C++", "Java", "Programming", "Web dev")

print("\t")

personnel("Nora", "UI/UX", "Fashion Designing", "Tote Bag making")