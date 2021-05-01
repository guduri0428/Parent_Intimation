from django.contrib import admin
from testapp.models import AdminTable
from testapp.models import Student_marks
from testapp.models import Student_attendance

# Register your models here
class Admin_table_t(admin.ModelAdmin):
    list_display=['admin_id','admin_name','admin_email','admin_password']

class Student_marks_t(admin.ModelAdmin):
    list_display=['student_id','student_name','parent_phone','student_year','compiler_design','unix_programming','ooad','dbms','os','os_lp_lab','dbms_lab','ooad_lab']

class Student_attendance_t(admin.ModelAdmin):
    list_display=['student_id','student_name','parent_phone','first_hour','second_hour','third_hour','fourth_hour','fifth_hour','sixth_hour','seventh_hour','total_attendace']

admin.site.register(AdminTable,Admin_table_t)
admin.site.register(Student_marks,Student_marks_t)
admin.site.register(Student_attendance,Student_attendance_t)
