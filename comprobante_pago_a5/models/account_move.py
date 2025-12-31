# -*- coding: utf-8 -*-

from odoo import models, api


class AccountMove(models.Model):
    _inherit = 'account.move'

    def action_print_payment_receipt_a5(self):
        """
        Action to print the payment receipt report in A5 format.
        Can be called from any invoice regardless of payment status.
        """
        self.ensure_one()
        return self.env.ref('comprobante_pago_a5.action_report_payment_receipt_a5').report_action(self)
