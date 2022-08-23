total_price = 0
card_type = "visa"
is_same_bank = True
is_expired = False

print("please insert you atm card: ")
required_amt = int(input("please enter a amount"))

def read_card():
    card_details = [1200,False,False]
    total_price = card_details [0]
    is_same_bank = card_details[1]
    is_expired = card_details [2]
    if is_expired is False:
        peform_transaction(total_price,is_same_bank,required_amt)
    else:
        return "sorry, this card is not accepted here: "

def peform_transaction(total_amt, is_same_bank, required_amt):
    charge= 0
    if not is_same_bank:
        charge = 5
        
        if required_amt > total_amt:
            print( "not enough balance")
        else:
            amt = total_amt-required_amt-charge
            print(f"remaining available balance: {amt}")
    else:
        if required_amt > total_amt:
            print( "not enough balance")
        else:
            amt = total_amt-required_amt
            print(f"remaining available balance: {amt}")

read_card()