##############################################################################
#
# Copyright (c) 2005-2006 TINY SPRL. (http://tiny.be) All Rights Reserved.
#
# WARNING: This program as such is intended to be used by professional
# programmers who take the whole responsability of assessing all potential
# consequences resulting from its eventual inadequacies and bugs
# End users who are looking for a ready-to-use solution with commercial
# garantees and support are strongly adviced to contract a Free Software
# Service Company
#
# This program is Free Software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
#
##############################################################################

import time
from report import report_sxw
from osv import osv


class pos_invoice(report_sxw.rml_parse):
	def __init__(self, cr, uid, name, context):
		super(pos_invoice, self).__init__(cr, uid, name, context)
		self.localcontext.update({
			'time': time,
		})

	def preprocess(self, objects, data, ids):
		super(pos_invoice, self).preprocess(objects, data, ids)
		iids = []
		nids = []

		for order in objects:
			order.write(self.cr,self.uid,[order.id],{'nb_print':order.nb_print + 1  })

			if order.invoice_id and order.invoice_id not in iids:
				if not order.invoice_id:
					raise osv.except_osv('Error !','Please create an invoice for this sale.')
				iids.append(order.invoice_id)
				nids.append(order.invoice_id.id)
		self.cr.commit()
		data['ids'] = nids
		self.datas = data
		self.ids = nids
		self.objects = iids
		self.localcontext['data'] = data
		self.localcontext['objects'] = iids

report_sxw.report_sxw('report.pos.invoice', 'pos.order', 'addons/libeurop/report/invoice.rml', parser= pos_invoice)

