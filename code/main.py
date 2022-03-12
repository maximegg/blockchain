from account_gestion import AccountGestion


test = AccountGestion()
for i in range(40):
    test.gift("nico", 20)
test.display_chain()


