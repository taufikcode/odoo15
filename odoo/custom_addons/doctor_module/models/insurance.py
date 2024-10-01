from odoo import models, fields

class Insurance(models.Model):
    _name = 'master.insurance'
    _description = 'Insurance'

    code = fields.Char(string="Kode Asuransi", required=True)
    name = fields.Char(string="Nama Asuransi", required=True)

    def name_get(self):
        result = []
        for record in self:
            name = f"{record.code} - {record.name}"
            result.append((record.id, name))
        return result