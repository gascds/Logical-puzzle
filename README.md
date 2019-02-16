## Logical puzzle (PyEDA)

### **Introduction:** 

PyEDA is a Python library designed for EDA to provide a high-level interface representation of Boolean function and a swiftly way to calculate algorithm.

**The principle behind PyEDA:** 

PyEDA allows us to create a Boolean function by creating Boolean variables using symbolic variables (char or String) and representing its logic expression using algebraic operators (NOT, OR, AND, XOR) in a single line of code. It will then calculate any given Boolean function is satisfiable and output a set or more of Boolean variables that can satisfy the function. 

> E.g. Once upon a time, there is a pair of nought identical twins, even if their family cannot distinguish them. One day, their uncle asked who the elder brother was. 
>
> Boy A said, “I am the elder one.”
>
> Boy B said, “I am the younger one.”
>
> They then smile at each other, as someone are lying. 

1. **To construct a logic expression:**

   From the above question, we are required to find out who the elder brother is (Boy A or Boy B). Using *exprvar* to expression variables A & B .We then construct a logic expression as below. 

   >A, B = map(exprvar, 'A', 'B')

2. **To create logic Expression representation**

   We use *A* to represent Boy A if he is elder one, and *~A* if he is a younger one, and similarly for boy B. Also, Boy A and B can either be the elder or the younger brother. Then, we use **OneHot** function to set the precondition(P) that one of them is elder and one of them is younger. 

   Boy A claimed that he is the older one while Boy B claimed that he is the younger one, and these two claims can be written as: 

   >P = OneHot(A, B) 
   C1 = A 
   C2 = ~B  
   //precisely one of A and B is true`

3. **To create a statement for checking**

   If there are more than a single logic expression needs to be satisfied, we need to combine all the
   expression into a statement using algebraic operators. In this question, it is assumed that at least
   one of them is lying. Therefore, we need to consider the cases that one of them is lying and both
   are lying. Therefore, we use a new variable (R) to represent the 3 cases, and also the precondition
   (P).

   >R = P & (~C1&C2 | C1&~C2 | ~C1&~C2)

4. **Generate solution using PyEDA** 

   PyEDA includes a function called satisfy_all() which can iterate through all the satisfying input variables in the statement. And now we get the answer – Boy B is the elder brother and Boy A is the younger brother. 

   > for x **in** R.satisfy_all():
   > ... print(x)
   >...
   >{B: 1, A: 0}

### Program Design for the Shannon Puzzle

> In this logic puzzle, it is given that there are two types of people. One is salesmen, the other one is engineers. It is known that the engineers always tell lies and the salesmen always tell the truth. 
>
> There are seven people in the situation and they are labelled as A, B, C, D, E, F and G respectively, and we are given the following information to deduce their roles: 
>
> 1: B and E are salesmen 
>
> 2: C states that D is an engineer 
>
> 3: A is an engineer 
>
> 4: A declares that B affirms that C asserts that D says that E insists that F denies that G is a salesman. 

> To commence with information 4, we should consider that the path of information transferring of the statement is opposite to the sentence. This means we need to consider the sentence from the end to the front. After that, we should consider the meaning and the state of the sentence one by one. We first assume G is an engineer for the demonstration. The state at G is the engineer. 
>
> When the fact passes to F, the role of F is the factor to alter the state “G is the engineer”. That means, if F is a salesman, he will not change the fact and the state at F is still “G is the engineer”. If F is an engineer, he will change the state that “G is a salesman”. 
>
> There exists one tricky point that the sentence state that “F denies G is a salesman”. If F is a salesman, “F denies G is a salesman” means that G is an engineer. Vice versa, if F is an engineer, the sentence implies that G must be a salesman. 
>
> For the information 2 “C states that D is an engineer”, we can conclude that their roles must be different. There are two cases that C is an engineer or C is a salesman. If C is a salesman, his statement must be true that D also is an engineer. For the case of C is an engineer, his statement must be false that D is not an engineer, such that D is a salesman. 

##### Now we will have 5 updated information: 

1: B and E are salesmen 

2: C and D must have different role 

3: A is an engineer 

4: F and G must have different role 

5: A declares that B affirms that C asserts that D says that E insists that F denies that G is a salesman. 

Then, we can use the programming language to implement the logic control and list out all the possible cases. 

For the program implementation part: #Assign two roles to each person first

>As, Ae = map(exprvar, (‘As’, ‘Ae’))
> 
>Bs, Be = map(exprvar, (‘Bs’, ‘Be’)) 
>
>Cs, Ce = map(exprvar, (‘Cs’, ‘Ce’)) 
>
>Ds, De = map(exprvar, (‘Ds’, ‘De’)) 
>
>Es, Ee = map(exprvar, (‘Es’, ‘Ee’))
>
>Fs, Fe = map(exprvar, (‘Fs’, ‘Fe’))
>
>Gs, Ge = map(exprvar, (‘Gs’, ‘Ge’))

**#Eliminate the probability by given information** 

> A = OneHot(Ae)
> 
> B = OneHot(Bs)
> 
> C = OneHot(Ce, Cs)
> 
> D = OneHot(De, Ds)
> 
> E = OneHot(Es)
> 
> F = OneHot(Fe, Fs)
> 
> G = OneHot(Ge, Gs)
> 
> H = OneHot(Ce, De)
> 
> I = OneHot(Fe, Ge) 

**#Use AND to connect all the given information **

> result = A&B&C&D&E&F&G&H&I 

**Output all possible result:** 

> for x in result.satisfy_all():
> 	print(x)
> 
> {Ge: 0, Gs: 1, Fe: 1, Fs: 0, Es: 1, De: 0, Ds: 1, Ce: 1, Cs: 0, Bs: 1, Ae: 1}
> 
> {Ge: 1, Gs: 0, Fe: 0, Fs: 1, Es: 1, De: 0, Ds: 1, Ce: 1, Cs: 0, Bs: 1, Ae: 1}
> 
> {Ge: 0, Gs: 1, Fe: 1, Fs: 0, Es: 1, De: 1, Ds: 0, Ce: 0, Cs: 1, Bs: 1, Ae: 1}
> 
> {Ge: 1, Gs: 0, Fe: 0, Fs: 1, Es: 1, De: 1, Ds: 0, Ce: 0, Cs: 1, Bs: 1, Ae: 1

**And we finally get there are 3 engineers and 4 salesmen.**

**Sum and Product logic puzzles ----- Cheryl’s birthday** 

> In this puzzle, it involves three people, name as A, B and C. A and B want to know the birthday of C. To let A and B know C’s birthday, C give some information to A and B. For A, C tells her month of birthday. For B, C tells her date of birthday. Also, C list out a table of the day which includes her birthday for them to infer. The table is listed below: 

| **May** |      | 15   | **16** |      |      | 19   |
| ------- | ---- | ---- | :----: | ---- | ---- | ---- |
| June    |      |      |        | 17   | 18   |      |
| July    | 14   |      |   16   |      |      |      |
| August  | 14   | 15   |        | 17   |      |      |

> Then, A says “I don’t know when C’s birthday is, but I know that B doesn’t know too.” From the statement. We can know that C’s month of birthday must not be May and June because of the second part of the statement “I know that B doesn’t know too.” It implies that the day of birthday should appear in the table at least two times. Therefore, the month of the birthday should be July or August. 
>
> After getting the conclusion from A, B knows the exact birthday because he knows the day of birthday and said that he knew the c’s birthday. It implies that the day must not appear more than one time on July and August. Therefore, day 14 should not be the day of birth. 
>
> Lastly, A also know C’s birthday by getting the statement of B. It is because he knows the month of C’s birthday. 

Follow the inference procedure, we can know that 16 July is C’s birthday.

**The solution of Cheryl’s birthday** 

\#define the exist date and months  

>d14,d15,d16,d17,d18,d19 = map(exprvar, ('d14', 'd15', 'd16', 'd17', 'd18', 'd19'))
>
>May,Jun = map(exprvar, ('May','Jun'))
>
>Aug,Jul = map(exprvar, ('Aug','Jul')) 

**Eliminate the probability by given information**
>s1 = OneHot(May,Jun,Jul,Aug)
>
>s2 = OneHot(d14,d15,d16,d17,d18,d19)
>
>s3 = OneHot(d14,d15,d16,d17)
>
>s4 = OneHot(Aug,Jul)
>
>s5 = OneHot(d15,d16,d17)
>
>s6 = OneHot(d16)
>
>s7 = OneHot(Jul)

**Use AND to connect all the given information** 

> result = s1&s2&s3&s4&s5&s6&s7 

Output all possible result: 

> for x in result.satisfy_all():
> 
>   print(x)
>   
> Output: {Jul: 1, Aug: 0, Jun: 0, May: 0, d19: 0, d18: 0, d17: 0, d16: 1, d15: 0, d14: 0} 

**We figure out the answer is 16 July.** 
