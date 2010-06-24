# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>). All Rights Reserved
#    $Id$
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
import time
from report import report_sxw


class account_statement(report_sxw.rml_parse):

    def __init__(self, cr, uid, name, context):
        super(account_statement, self).__init__(cr, uid, name, context)
        self.total = 0.0
        self.localcontext.update({
                'time': time,
                'get_total':self._get_total,
                })
    def _get_total(self, statement_line_ids):
        total = 0.0
        for line in statement_line_ids:
            total += line.amount
        return total
report_sxw.report_sxw('report.account.statement', 'account.bank.statement', 'addons/statement/report/account_statement.rml', parser=account_statement)
