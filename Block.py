from osv import osv
from osv import fields

class ASCS_block(osv.osv):
 
    _name = 'ascs.block'
    _description = 'ascs.block'
 
    _columns = {
            'name':fields.char('Block', size=64, required=True, readonly=False)
        }
ASCS_block()