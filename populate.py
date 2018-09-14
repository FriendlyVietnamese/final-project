import mlab
mlab.connect()
from models.order import Trasua, User
mlab.connect()
# new_service = Service(
#     name = "thu",
#     yob = 1999,
#     gender = 0,
#     height = 162,
#     phone = "000999338",
#     address = "ha noi",
#     status = True
# ))
user = User(
    username = "123",
    password = "123",
    phone = "123",
    address = "123"
)
user.save()
print("Done!")

