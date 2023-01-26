from pymonad.reader import Pipe
from pymonad.tools import curry
from collections import namedtuple

Contact = namedtuple('Contact', 'fname lname age')

@curry(4)
def make_contact(fname, lname, age, coll):
    return [contact for contact in coll] + [Contact(fname, lname, age)]

def update_contacts(coll):
    return [Contact(contact.fname.upper(), contact.lname, contact.age) for contact in coll]

def get_fnames(coll):
    return [contact.fname for contact in coll]

make_ted = make_contact('ted', 'bell', 90)
make_jason = make_contact( 'jason', 'dodson', 12)

res = (Pipe([])
        .then(make_ted)
        .then(make_jason)
        .then(update_contacts)
        .then(get_fnames)
        .flush())
print(res)