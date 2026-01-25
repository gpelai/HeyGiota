from models.bills import Bill

_controller = Bill("http://127.0.0.1:5000")

def create_bill(title, amount, regular):
    if not title:
        print("Title cannot be null.")
        return
    if not amount:
        print("Amount cannot be null.")
        return
    if not regular:
        print("Regular cannot be null.")
        return

    if not isinstance(title, str):
        print("Title must be a String.")
        return
    if not isinstance(regular, bool):
        print("Regular must be Boolean.")
        return
    try:
        amount = float(amount)
    except(TypeError, ValueError):
        print("Amount must be a Number.")
        return
    
    _controller.create(title, amount, regular)