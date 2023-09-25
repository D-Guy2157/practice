# module = a file containing python code. May contain functions, classes, etc.
# used with modular programming, which is to separate a program into parts

import messages as msg  # msg is an alias for less typing

msg.hello()
msg.bye()

from messages import hello, bye  # for importing specific functions, only have to type function name

hello()
bye()
