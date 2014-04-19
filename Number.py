from osv import osv
from osv import fields

class ASCS_no(osv.osv):
 
    _name = 'ascs.no'
    _description = 'ascs.no'
 
    _columns = {
            'name':fields.char('Room No.', size=64, required=True, readonly=False)
        }
ASCS_no()
