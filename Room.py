from osv import osv
from osv import fields

class ASCS_room(osv.osv):
 
    _name = 'ascs.room'
    _description = 'ascs.room'
 
    _columns = {
            'Block_id':fields.many2one('ascs.block','Block',required=True,ondelete='set null'),
            'Number_id':fields.many2one('ascs.no','Room No.',required=True,ondelete='set null'),
            'rtyp': fields.selection([('senior', 'Senior'),('junior','Junior'),('labour','Labour'),('vip','VIP')],'Room Type'),
            'name':fields.char('capaciy', size=64, required=False, readonly=False),
            'pno':fields.char('Phone No', size=64, required=False, readonly=False),
            'add':fields.text('Additional Details', size=64, required=False, readonly=False),
        
        }
ASCS_room()