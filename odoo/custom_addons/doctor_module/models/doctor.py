from odoo import models, fields

class Doctor(models.Model):
    _name = 'doctor.model'
    _description = 'Doctor Model'

    code = fields.Char(string="Kode Dokter", required=True)
    name = fields.Char(string="Nama Dokter", required=True)
    gender = fields.Selection([
        ('laki-laki', 'Laki-Laki'),
        ('perempuan', 'Perempuan')
    ], string="Jenis Kelamin", required=True)
    blood_type = fields.Selection([
        ('a', 'A'),
        ('b', 'B'),
        ('ab', 'AB'),
        ('o', 'O')
    ], string="Gol. Darah")
    place_of_birth = fields.Char(string="Tempat Lahir")
    date_of_birth = fields.Date(string="Tgl. Lahir", required=True)
    no_ijin_praktek = fields.Char(string="No. Ijin Praktik",required=True)
    religion = fields.Selection([
        ('islam', 'Islam'),
        ('kristen', 'Kristen'),
        ('protestan', 'Protestan'),
        ('katolik', 'Katolik'),
        ('hindu', 'Hindu'),
        ('budha', 'Budha'),
        ('khonghucu', 'Khonghucu')
    ], string="Agama")
    marriage = fields.Selection([
        ('belum_menikah', 'Belum Menikah'),
        ('menikah', 'Menikah'),
        ('duda', 'Duda'),
        ('janda', 'Janda')
    ], string="Status Pernikahan")
    address = fields.Text(string="Alamat")
    phone = fields.Char(string="No. HP")
    spesialist_id = fields.Many2one('doctor.spesialist', string="Spesialisasi")
    code_spesialis = fields.Char(related='spesialist_id.code_spesialis', string="Kode Spesialis", readonly=True)
    nama_spesialis = fields.Char(related='spesialist_id.nama_spesialis', string="Nama Spesialis", readonly=True)
    insurance_id = fields.Many2one('master.insurance', string="Asuransi")