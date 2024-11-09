#imagine youre a loyalty program for a popular store, you need to check weather a specific customer is part d this program .If they are, you should grant them the benefits of the discount
#members of the program:
#alice
#bob
#charlie
#anna

loyal_customers = {"alice","bob","charlie","anna"}
customer = "alice"

if customer in loyal_customers:
    print("You get a discount!")
else: print("You dont get a discount")