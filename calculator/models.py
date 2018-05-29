from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User

# class User1 (models.Model):
#     username1=User.username


class Personal (models.Model) :
    user=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    post_apply = models.CharField(max_length = 150)
    department = models.CharField(max_length = 50)
    application_no = models.BigAutoField(db_column = 'APPLICATION_NO',  primary_key = True)
    email = models.EmailField(max_length = 254)
    category = models.CharField(max_length = 30)
    pwd_status = models.CharField(max_length = 5)
    internal_candidate = models.BooleanField()
    profile_image = models.ImageField(blank = True)
    first_name = models.CharField(max_length = 100)     
    middle_name = models.CharField(max_length = 100,blank = True)
    last_name = models.CharField(max_length = 100)
    father_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(auto_now = False)
    age = models.IntegerField()
    aadhar_card = models.BigIntegerField()
    gender = models.CharField(max_length = 10)
    nationality = models.CharField(max_length = 20)
    marital_status = models.CharField(max_length = 10)
    correspondence_address = models.CharField(max_length = 200)
    permanent_address = models.CharField(max_length = 200)
    mobile = models.CharField(max_length = 10)
    areas_of_specialization = models.TextField(max_length = 300,blank = True)
    phd_thesis_title = models.CharField(max_length = 200)
    date_of_acquiring_phd = models.DateField(auto_now = False)

    def __str__(self):
        return str(self.user)


class Qualification(models.Model):
    user=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    exam_passed = models.CharField(max_length = 20)
    year_of_passing = models.CharField(max_length = 20)
    degree_name = models.CharField(max_length = 20)
    discipline_or_subjects = models.TextField(max_length = 50)
    board_or_university_or_institution = models.CharField(max_length = 20)
    cgpa_or_marks = models.DecimalField(max_digits = 5,decimal_places = 3)
    class_or_division = models.CharField(max_length = 20)

    def __str__(self):
        return u'%s %s' % (str(self.user), self.exam_passed)

class Research_Publications(models.Model):
    user=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    score1 = models.DecimalField(max_digits=6, decimal_places=3)
    rd_onlypi = models.DecimalField(max_digits=6, decimal_places=3)
    rd_pi = models.DecimalField(max_digits=6, decimal_places=3)
    no_of_rest_pi = models.DecimalField(max_digits=6, decimal_places=3)
    rd_co_pi = models.DecimalField(max_digits=6, decimal_places=3)
            
    rd_onlyinventor = models.DecimalField(max_digits=6, decimal_places=3)
    rd_inventor = models.DecimalField(max_digits=6, decimal_places=3)
    no_of_rest_inventor = models.DecimalField(max_digits=6, decimal_places=3)
    rd_co_inventor = models.DecimalField(max_digits=6, decimal_places=3)

        
    score2 = models.DecimalField(max_digits=6, decimal_places=3)
    no_of_5lakhs = models.DecimalField(max_digits=6, decimal_places=3)
            
            
    score3 = models.DecimalField(max_digits=6, decimal_places=3)
    phd_sole_supervisor = models.DecimalField(max_digits=6, decimal_places=3)
    phd_first_supervisor = models.DecimalField(max_digits=6, decimal_places=3)
    no_of_rest_supervisor = models.DecimalField(max_digits=6, decimal_places=3)
    phd_co_supervisor = models.DecimalField(max_digits=6, decimal_places=3)

            
    score4 = models.DecimalField(max_digits=6, decimal_places=3)
    as_sole_journal_author = models.DecimalField(max_digits=6, decimal_places=3)
    as_first_journal_author = models.DecimalField(max_digits=6, decimal_places=3)
    no_of_rest_journal_author = models.DecimalField(max_digits=6, decimal_places=3)
    as_co_journal_author = models.DecimalField(max_digits=6, decimal_places=3)

            
    score5 = models.DecimalField(max_digits=6, decimal_places=3)
    as_sole_conf_author = models.DecimalField(max_digits=6, decimal_places=3)
    as_first_conf_author = models.DecimalField(max_digits=6, decimal_places=3)
    no_of_rest_conf_author = models.DecimalField(max_digits=6, decimal_places=3)
    as_co_conf_author = models.DecimalField(max_digits=6, decimal_places=3)

    score6 = models.DecimalField(max_digits=6, decimal_places=3)
    sem_hod = models.DecimalField(max_digits=6, decimal_places=3)
    sem_dean = models.DecimalField(max_digits=6, decimal_places=3)
    sem_cw = models.DecimalField(max_digits=6, decimal_places=3)
    sem_tpi = models.DecimalField(max_digits=6, decimal_places=3)
    sem_advisor = models.DecimalField(max_digits=6, decimal_places=3)
    sem_cvo = models.DecimalField(max_digits=6, decimal_places=3)
    sem_pi = models.DecimalField(max_digits=6, decimal_places=3)
    sem_teqip = models.DecimalField(max_digits=6, decimal_places=3)

    score7 = models.DecimalField(max_digits=6, decimal_places=3)
    sem_warden = models.DecimalField(max_digits=6, decimal_places=3)
    sem_asst_warden = models.DecimalField(max_digits=6, decimal_places=3)
    sem_asso_dean = models.DecimalField(max_digits=6, decimal_places=3)
    sem_chairman = models.DecimalField(max_digits=6, decimal_places=3)
    sem_fac_inch_inst_activities = models.DecimalField(max_digits=6, decimal_places=3)

    score8 = models.DecimalField(max_digits=6, decimal_places=3)
    sem_chairman_comm = models.DecimalField(max_digits=6, decimal_places=3)
    sem_fac_inch_comm = models.DecimalField(max_digits=6, decimal_places=3)

    score9 = models.DecimalField(max_digits=6, decimal_places=3)
    sem_dept_activities = models.DecimalField(max_digits=6, decimal_places=3)
    sem_dept_comm = models.DecimalField(max_digits=6, decimal_places=3)

    score10 = models.DecimalField(max_digits=6, decimal_places=3)
    workshop = models.DecimalField(max_digits=6, decimal_places=3)

    score11 = models.DecimalField(max_digits=6, decimal_places=3)
    for2week_nat_prgm = models.DecimalField(max_digits=6, decimal_places=3)
    for1week_nat_prgm = models.DecimalField(max_digits=6, decimal_places=3)

    score12 = models.DecimalField(max_digits=6, decimal_places=3)
    conf_as_chairman = models.DecimalField(max_digits=6, decimal_places=3)

    score13 = models.DecimalField(max_digits=6, decimal_places=3)
    teaching_year = models.DecimalField(max_digits=6, decimal_places=3)

    score14 = models.DecimalField(max_digits=6, decimal_places=3)
    labs = models.DecimalField(max_digits=6, decimal_places=3)

    score15 = models.DecimalField(max_digits=6, decimal_places=3)
    theory_credit_hrs = models.DecimalField(max_digits=6, decimal_places=3)

    score16 = models.DecimalField(max_digits=6, decimal_places=3)
    pg = models.DecimalField(max_digits=6, decimal_places=3)

    score17 = models.DecimalField(max_digits=6, decimal_places=3)
    ug = models.DecimalField(max_digits=6, decimal_places=3)

    score18 = models.DecimalField(max_digits=6, decimal_places=3)
    books_international = models.DecimalField(max_digits=6, decimal_places=3)

    score19 = models.DecimalField(max_digits=6, decimal_places=3)
    books_national = models.DecimalField(max_digits=6, decimal_places=3)

    score20 = models.DecimalField(max_digits=6, decimal_places=3)
    outreach_activities = models.DecimalField(max_digits=6, decimal_places=3)

    score21 = models.DecimalField(max_digits=6, decimal_places=3)
    fellowship = models.DecimalField(max_digits=6, decimal_places=3)

    
    score22 = models.DecimalField(max_digits=6, decimal_places=3)
    above85 = models.DecimalField(max_digits=6, decimal_places=3)
    above75 = models.DecimalField(max_digits=6, decimal_places=3)

    score = models.DecimalField(max_digits=6, decimal_places=3)


    
    def __str__(self):
        return str(self.user)
