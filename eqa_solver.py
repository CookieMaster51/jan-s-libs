symbles = ["=", "+", "-", "/", " "]


# ask for the equasion
print("please format as 'ax/b + c = d'")
eqa = input("What is the equasion?\n")

def solve_eqa(eqa, symbles):

    multi_bool = False
    pm_bool = False
    div_bool = False

    # making useful things

    def is_int(num):
        try:
            int(num)
            return True
        except:
            return False

    def is_flt(num):
        try:
            float(num)
            return True
        except:
            return False

    # finds the unknowns

    var = []

    for char in eqa:
        if is_int(char) or is_flt(char) or char in symbles:
            continue
        else:
            var.append(char)

    if len(var) > 1:
        # makes sure its not a simult eqa or some line or somethin
        print("WHAT HOWWWW PLS DONTTT")
    else:
        # finds location of the unknown
        var = var[0]
        place = eqa.find(var)

        # finds the multiplier
        if place != 0:
            if eqa[place - 1] != " ":
                multi = eqa[place - 1]
                multi_bool = True
                multi = int(multi)

                if eqa[0] == "-":
                    multi = - multi

        # finds the divisor
        if eqa[place + 1] != " ":
            if eqa[place + 2] == "-":
                div = eqa[place + 3]
            else:
                div = eqa[place + 2]

            div_bool = True

            div = int(div)

            if eqa[place + 2] == "-":
                div = -div


        # finds the adder
        if not eqa.find("+") < 1:
            pm_pos = eqa.find("+")
            pm_bool = True
        else:    
            if not eqa.find("-") < 1:
                pm_pos = eqa.find("-")
                pm_bool = True

        if pm_bool:
            adder = eqa[pm_pos:]
            adder = adder[:adder.find("=")]
            adder = adder.replace(" ", "")
            adder = int(adder)

        
        # finds the post = number

        equal = eqa[eqa.find("=") + 1:]
        equal = equal.replace(" ", "")
        equal = int(equal)

        # finally soves the eqaaaaa, vibes!!!!

        if pm_bool:
            equal = equal - adder

        if div_bool:
            equal = equal * div

        if multi_bool:
            equal = equal / multi

        answer = equal

        if is_int(answer):
            answer = int(answer)

        return(answer)

def form():
    print("please put the equasion in form ax/b +- c = d")

print(solve_eqa(eqa, symbles))
