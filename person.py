from osv import osv
from osv import fields

class ascs_person(osv.osv):
 
    _name = 'ascs.person'
    _description = 'ascs.person'
 
    _columns = {
            'name':fields.char('Person Name', size=64, required=True, readonly=False),
            'id_proof':fields.char('Identification Proof', size=64, required=False, readonly=False),
            'id_no':fields.char('Identification Number', size=64, required=False, readonly=False),
            'cat_id':fields.many2one('ascs.frontdesk','facility',required=False,ondelete='set null')
                            
        }
ascs_person()