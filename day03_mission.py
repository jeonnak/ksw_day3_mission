'''
5.4, 5.5
'''

letter = '''\tDear {0} {1},\n
\tThank you for your letter. We are sorry that our {2} {3} in your
{4}. Please note that it should never be used in a {4}, especially near any
{5}.\n\n
\tSend us your receipt and {6} for shipping and handling. We will send you
another {2} that, in our tests, is {7}% less likely to have {3}. \n\n
\tThank you for your support.
\tSincerely,
\t{8}
\t{9}
'''

salutation = 'professor'
name = 'minsu'
product = 'pencil'
verbed = 'losted'
room = 'living room'
animals = 'dog'
amount = 'love'
percent = '20'
spokesman = 'mina'
job_title = 'student'

print(letter.format(salutation, name, product, verbed, room, animals, amount, percent, spokesman, job_title))

