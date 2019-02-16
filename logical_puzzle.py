from pyeda.inter import *

print ("-------------------------------Logic Puzzles Solvers-------------------------------\n\n")

print ("Here, we provid the solution for three logic pussles\n")
print ("1: Cheryl's birthday\n")
print ("2: Shannon Puzzle\n")

type = input('Choose the solution from above (input a single integer): ')
if type == "1":
  print("\n---------------------------------Cheryl's birthday----------------------------------\n")
  print("Background:\n")
  print("\tAlbert and Bernard just become friends with Cheryl, and they want to know when her birthday is. Cheryl gives them a list of 10 possible dates: 15 May, 16 May, 19 May, 17 June, 18 June, 14 July, 16 July, 14 August, 15 August, 17 August.\n")
  print("Cheryl then tells Albert and Bernard separately the month and the day of her birthday respectively.\n")
  print("-----------------------------------Conversion---------------------------------------")
  print("\nAlbert: I don't know when Cheryl's birthday is, but I know that Bernard doesn't know too.\n")
  print("Bernard: At first I don't know when Cheryl's birthday is, but I know now.\n")
  print("Albert: Then I also know when Cheryl's birthday is.")
  print("\nQuestion: So when is Cheryl's birthday?\n")
  print("------------------------------------Solution----------------------------------------")
  print("\nThe answer is 16 July.")
  print("\nHint: 0 equals false, 1 equals true.\n\nOutput (Result):")
  
  d14,d15,d16,d17,d18,d19 = map(exprvar, ('d14', 'd15', 'd16', 'd17', 'd18', 'd19'))
  May,Jun = map(exprvar, ('May','Jun'))
  Aug,Jul = map(exprvar, ('Aug','Jul'))
  s1 = OneHot(May,Jun,Jul,Aug)
  s2 = OneHot(d14,d15,d16,d17,d18,d19)
  s3 = OneHot(d14,d15,d16,d17)
  s4 = OneHot(Aug,Jul)
  s5 = OneHot(d15,d16,d17)
  s6 = OneHot(d16)
  s7 = OneHot(Jul)
  result = s1&s2&s3&s4&s5&s6&s7
  for x in result.satisfy_all():
    print(x)

elif type == "2":
  print("\n-----------------------------------Shannon Puzzle-----------------------------------\n")
  print("Background:\n")
  print("\tIt is known that salesmen always tell the truth and engineers always tell lies. B and E are salesmen. C states that D is an engineer. A declares that B affirms that C asserts that D says that E insists that F denies that G is a salesman. If A is an engineer, how many engineers are there?")
  print("\n------------------------------------------------------------------------------------\n")
  As, Ae = map(exprvar, ('As', 'Ae'))
  Bs, Be = map(exprvar, ('Bs', 'Be'))
  Cs, Ce = map(exprvar, ('Cs', 'Ce'))
  Ds, De = map(exprvar, ('Ds', 'De'))
  Es, Ee = map(exprvar, ('Es', 'Ee'))
  Fs, Fe = map(exprvar, ('Fs', 'Fe'))
  Gs, Ge = map(exprvar, ('Gs', 'Ge'))

  A=OneHot(Ae)
  B=OneHot(Bs)
  C=OneHot(Ce, Cs)
  D=OneHot(De, Ds)
  E=OneHot(Es)
  F=OneHot(Fe, Fs)
  G=OneHot(Ge, Gs)

  data_given = OneHot(Ce,De)
  data_given2 = OneHot(Fe,Ge)
  result=A&B&C&D&E&F&G&data_given&data_given2


  print("Information given:\n(1) A is an engineer.\n(2) B is a salesman.\n(3) E is a salesman.\n(4) C amd D must not be the same type.\n(5) F and G must not be the same type.")
  print("\n-------------------------------------Solution---------------------------------------")
  print("\nResult: There are 3 engineers and 4 salesmans.")
  print("\nHint: 0 equals false, 1 equals true.\n\nOutput (Result):")
  for x in result.satisfy_all():
    print(x)

else:
  print("\nWrong Input\n")
