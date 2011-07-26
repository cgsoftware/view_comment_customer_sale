# -*- encoding: utf-8 -*-

import netsvc
import pooler, tools
import math

from tools.translate import _

from osv import fields, osv


class sale_order(osv.osv):
    _inherit = 'sale.order'
    
    def onchange_partner_id(self, cr, uid, ids, part):
      res = super(sale_order, self).onchange_partner_id(cr, uid, ids, part)
      val = res['value']
      part = self.pool.get('res.partner').browse(cr, uid, part)
      if part.comment:
             warning = {
                        'title': 'ATTENZIONE !',
                        'message':part.comment,
                        }       
      else:
            warning = {}
  
      return {'value': val, 'warning':warning}
sale_order()
