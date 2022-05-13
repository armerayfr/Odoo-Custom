from odoo import api, fields, models

class Course(models.Model):
    _name = 'openacademy.course'
    _description = 'track couses that taking from student'
    _rec_name = "title"

    title = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')

    # users_id = fields.Many2one('res.users', string='Users')
    responsible_id = fields.Many2one('res.users', string='Responsible')

    # session_id = fields.Many2one('courses.session', string='Session')
    
    session_ids = fields.One2many('courses.session', 'course_ids')

    _sql_constraints = [('course_title_unique', 'unique(title)', 'name course must be unique')]


    # not allowed to duplicate unique

    # _sql_constraints = [('Copy of description', 'unique(description)', 'not possible use function anymore')]
    # _sql_constraints = [('description_title_different', 'CHECK(title = description)', 'name and description course must be different')]

