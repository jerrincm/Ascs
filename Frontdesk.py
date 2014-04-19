from osv import osv
from osv import fields

class ASCS_Frontdesk(osv.osv):
 
    _name = 'ascs.frontdesk'
    _description = 'ascs.frontdesk'
 
    _columns = {
            'name':fields.boolean('Check in', size=64, required=True, readonly=False),
            'nam_id':fields.many2one('res.partner','Customer',required=False,ondelete='set null'),
            'Prod_id':fields.many2one('product.product','Project',required=False,ondelete='set null'),
            'rtyp': fields.selection([('senior', 'Senior'),('junior','Junior'),('labour','Labour'),('vip','VIP')],'Category'),
            'Number_id':fields.many2one('ascs.no','Room No.',required=False,ondelete='set null'),
            'cat':fields.text('Facilities', size=64, required=False, readonly=False),
            'in':fields.date('Check In Date', size=64, required=False, readonly=False),
            'out':fields.date('Check Out Date', size=64, required=False, readonly=True),
            'ascs_persons':fields.one2many('ascs.person','cat_id','Person Details')
            
            
        }
ASCS_Frontdesk()