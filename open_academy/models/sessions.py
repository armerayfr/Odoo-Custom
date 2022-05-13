from odoo import api, fields, models
from datetime import date
from odoo.exceptions import ValidationError

class Session(models.Model):
    _name = 'courses.session'
    _description = 'tracking the session of student courses'

    name = fields.Char(string='Name')
    start_date = fields.Date(string='Start Date', default=date.today())
    duration = fields.Integer(string='Duration in Minutes')

    number_of_seats = fields.Integer(string='Number of Seats')

    # active = fields.Char(string='Status', default='deactive')

    # complex domain
    instructor_id = fields.Many2one('res.partner', string = 'Instructor', domain = "['|', ('instructor', '=', 'True'), '|', ('teacher', '=', 'Teacher / Level 1'), ('teacher', '=', 'Teacher / Level 2') ]")
    
    # course_ids = fields.One2many('openacademy.course', 'session_id')
    course_ids = fields.Many2one('openacademy.course', string = 'Course')

    attendees_ids = fields.Many2many('res.partner', string='Attendees')

    percentage_of_taken_seats = fields.Char(compute = '_compute_percentage', string = 'Percentage of Taken Seats')
    days_left = fields.Integer(compute = '_compute_days_left', string = 'Days Left')

    def _compute_percentage(self):
        for record in self:
            record.percentage_of_taken_seats = float(round((len(record.attendees_ids) / record.number_of_seats) * 100))

    def _compute_days_left(self):
        for record in self:
            record.days_left = (int(date.today().strftime("%Y%m%d%H%M%S")) - int(record.start_date.strftime("%Y%m%d%H%M%S"))) / 1000000

    @api.onchange('number_of_seats', 'attendees_ids')
    def _onchange_taken_seats(self):
        
        return {
        'warning': {
            'title': "Something bad happened",
            'message': "Type a negative number of seats, or more participants than seats is not allowed!!!",
            }
        }


    @api.constrains('number_of_seats')
    def _check_is_full_capacity(self):

        for record in self:
            if record.number_of_seats > 1000:
                raise ValidationError('Out of capacity, < 1000 is allowed!!!')


    @api.constrains('duration')
    def _check_too_long_duration(self):

        for record in self:
            if record.duration > 180 :
                raise ValidationError('Too long duration, < 180 minutes is allowed!!!')



    @api.constrains('instructor_id')
    def _check_is_same_instructor_attendees(self):

        for record in self:
            if record.instructor_id in record.attendees_ids:
              raise ValidationError('Instructor and attendees are not allowed to be same in the session')


class Instructor(models.Model):
    _inherit = 'res.partner'

    instructor = fields.Boolean(string='Instructor')
    teacher = fields.Char(string='Teacher')

    instructor_ids = fields.Many2many('courses.session', string='instructor')


