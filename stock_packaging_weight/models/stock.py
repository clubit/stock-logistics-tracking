from openerp import models, fields, api, _
import openerp.addons.decimal_precision as dp


class stock_package(models.Model):
    _inherit = "stock.quant.package"

    weight = fields.Float('Gross Weight', digits_compute=dp.get_precision('Stock Weight'), help="The gross weight of the products in the package in kg.")
    weight_net = fields.Float('Net Weight', digits_compute=dp.get_precision('Stock Weight'), help="The gross weight plus the weight of the package in kg.")
