# -*- coding: utf-8 -*-

from odoo import models, api


class AccountMove(models.Model):
    _inherit = 'account.move'

    def action_print_payment_receipt(self):
        """
        Action to print the payment receipt report.
        Can be called from any invoice regardless of payment status.
        """
        self.ensure_one()
        return self.env.ref('comprobante_pago.action_report_payment_receipt').report_action(self)