from models.bills import Bill

_controller = Bill('http://127.0.0.1:5000')


def create_bill(title, amount, date, regular):
    _controller.create(title, amount, date, regular)


def read_all_bills():
    return _controller.read_all()


def delete_bill(id):
    _controller.delete(id)
