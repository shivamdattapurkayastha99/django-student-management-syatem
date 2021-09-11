from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Admin)
admin.site.register(Staffs)
admin.site.register(Courses)
admin.site.register(Subjects)
admin.site.register(Student)
admin.site.register(Attendance)
admin.site.register(AttendanceReport)
admin.site.register(LeaveReportStaff)
admin.site.register(LeaveReportStudent)
admin.site.register(FeedBackStudent)
admin.site.register(FeedbackStaffs)
admin.site.register(NotificationStaffs)
admin.site.register(NotificationStudent)