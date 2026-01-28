from models.bills import Bill

_controller = Bill('http://127.0.0.1:5000')


def create_bill(title, amount, date, regular):

    # check if its null
    if not title:
        print('Title cannot be null.')
        return
    
    if not amount:
        print('Amount cannot be null.')
        return
    
    if not regular:
        print('Regular cannot be null.')
        return
    
    if not date:
        print('Date cannot be null')
        return

    # check type of var
    if not isinstance(title, str):
        print('Title must be a String.')
        return
    
    try:
        amount = float(amount)
    except (TypeError, ValueError):
        print('Amount must be a Number.')
        return
    
    if not isinstance(date, str):
        print('Date must be String.')
        return
    
    if not isinstance(regular, bool):
        print('Regular must be Boolean.')
        return
    
    _controller.create(title, amount, date, regular)


def read_all_bills():
    return _controller.read_all()


def delete_bill(id):
    if not id:
        print('ID cannot be null.')
        return

    try:
        id = int(id)
    except (TypeError, ValueError):
        print('ID must be a number.')
        return

    _controller.delete(id)
