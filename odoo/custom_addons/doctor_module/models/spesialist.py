from odoo import models, fields

class Spesialist(models.Model):
    _name = 'doctor.spesialist'
    _description = 'Doctor Spesialist'

    code_spesialis = fields.Char(string="Kode Spesialis", required=True)
    nama_spesialis = fields.Char(string="Nama Spesialis", required=True)

    def name_get(self):
        result = []
        for record in self:
            name = f"{record.code_spesialis} - {record.nama_spesialis}"
            result.append((record.id, name))
        return result