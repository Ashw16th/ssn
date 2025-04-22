def stable_marriage(n, men_pref, women_pref):
    free_men = list(range(n))
    women_partner = [-1] * n
    men_next_proposal = [0] * n

    while free_men:   
        man = free_men.pop(0)
        woman = men_pref[man][men_next_proposal[man]]    #selecting 
        men_next_proposal[man] += 1                   #incrementing the proposal

        if women_partner[woman] == -1:
            women_partner[woman] = man
        else:
            current_man = women_partner[woman]
            if women_pref[woman].index(man) < women_pref[woman].index(current_man):
                women_partner[woman] = man
                free_men.append(current_man)
            else:
                free_men.append(man)

    print("\nStable Marriage Pairs:")
    for woman, man in enumerate(women_partner):
        print(f"Man {man + 1} - Woman {woman + 1}")

n = int(input("Enter number of men/women: "))

print("\nEnter the preference list for each man:")
men_pref = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(n)]

print("\nEnter the preference list for each woman:")
women_pref = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(n)]

stable_marriage(n, men_pref, women_pref)
