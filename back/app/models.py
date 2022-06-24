from django.db import models


class Cart(models.Model):
    cartid = models.AutoField(db_column='CartID', primary_key=True)  # Field name made lowercase.
    cartuserlastname = models.CharField(db_column='CartUserLastName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cartuserfirstname = models.CharField(db_column='CartUserFirstName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cartusepatronyc = models.CharField(db_column='CartUsePatronyc', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cartuseradress = models.TextField(db_column='CartUserAdress', blank=True, null=True)  # Field name made lowercase.
    cartuseremail = models.CharField(db_column='CartUserEmail', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cartuserphone = models.CharField(db_column='CartUserPhone', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cartgoodphoto = models.CharField(db_column='CartGoodPhoto', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cartgoodname = models.TextField(db_column='CartGoodName', blank=True, null=True)  # Field name made lowercase.
    cartgoodcost = models.IntegerField(db_column='CartGoodCost', blank=True, null=True)  # Field name made lowercase.
    cartgoodquantity = models.IntegerField(db_column='CartGoodQuantity', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Cart'


class Good(models.Model):
    goodid = models.AutoField(db_column='GoodID', primary_key=True)  # Field name made lowercase.
    goodname = models.TextField(db_column='GoodName')  # Field name made lowercase.
    goodcategory = models.ForeignKey('Goodcategory', models.DO_NOTHING, db_column='GoodCategory')  # Field name made lowercase.
    goodtheme = models.ForeignKey('Goodtheme', models.DO_NOTHING, db_column='GoodTheme', blank=True, null=True)  # Field name made lowercase.
    goodamount = models.FloatField(db_column='GoodAmount', blank=True, null=True)  # Field name made lowercase.
    goodcountry = models.ForeignKey('Goodcounty', models.DO_NOTHING, db_column='GoodCountry', blank=True, null=True)  # Field name made lowercase.
    goodcost = models.FloatField(db_column='GoodCost')  # Field name made lowercase.
    gooddiscount = models.FloatField(db_column='GoodDiscount')  # Field name made lowercase.
    goodstatus = models.CharField(db_column='GoodStatus', max_length=50, blank=True, null=True)  # Field name made lowercase.
    goodsubcategory = models.CharField(db_column='GoodSubcategory', max_length=50, blank=True, null=True)  # Field name made lowercase.
    goodpopularity = models.FloatField(db_column='GoodPopularity', blank=True, null=True)  # Field name made lowercase.
    goodphoto = models.CharField(db_column='GoodPhoto', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Good'


class Goodcategory(models.Model):
    goodcategoryid = models.IntegerField(db_column='GoodCategoryID', primary_key=True)  # Field name made lowercase.
    goodcategoryname = models.CharField(db_column='GoodCategoryName', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GoodCategory'


class Goodcounty(models.Model):
    goodcountryid = models.IntegerField(db_column='GoodCountryID', primary_key=True)  # Field name made lowercase.
    goodcountryname = models.CharField(db_column='GoodCountryName', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GoodCounty'


class Goodparameter(models.Model):
    goodparameterid = models.AutoField(db_column='GoodParameterID', primary_key=True)  # Field name made lowercase.
    goodparametername = models.CharField(db_column='GoodParameterName', max_length=50)  # Field name made lowercase.
    goodparametervalue = models.TextField(db_column='GoodParameterValue')  # Field name made lowercase.
    goodparametergood = models.ForeignKey(Good, models.DO_NOTHING, db_column='GoodParameterGood')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GoodParameter'


class Goodtheme(models.Model):
    goodthemeid = models.IntegerField(db_column='GoodThemeID', primary_key=True)  # Field name made lowercase.
    goodthemename = models.TextField(db_column='GoodThemeName', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GoodTheme'


class Newscolibri(models.Model):
    newsid = models.AutoField(db_column='NewsID', primary_key=True)  # Field name made lowercase.
    newname = models.CharField(db_column='NewName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    newvalue = models.TextField(db_column='NewValue', blank=True, null=True)  # Field name made lowercase.
    newdata = models.CharField(db_column='NewData', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NewsColibri'


class Review(models.Model):
    reviewid = models.AutoField(db_column='ReviewID', primary_key=True)  # Field name made lowercase.
    reviewvalue = models.TextField(db_column='ReviewValue', blank=True, null=True)  # Field name made lowercase.
    reviewuser = models.TextField(db_column='ReviewUser', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Review'


class Sell(models.Model):
    sellid = models.AutoField(db_column='SellID', primary_key=True)  # Field name made lowercase.
    selluserlastname = models.CharField(db_column='SellUserLastName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    selluserfirstname = models.CharField(db_column='SellUserFirstName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sellusepatronyc = models.CharField(db_column='SellUsePatronyc', max_length=50, blank=True, null=True)  # Field name made lowercase.
    selluseradress = models.TextField(db_column='SellUserAdress', blank=True, null=True)  # Field name made lowercase.
    selluseremail = models.CharField(db_column='SellUserEmail', max_length=50, blank=True, null=True)  # Field name made lowercase.
    selluserphone = models.CharField(db_column='SellUserPhone', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sellgoodphoto = models.CharField(db_column='SellGoodPhoto', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sellgoodname = models.TextField(db_column='SellGoodName', blank=True, null=True)  # Field name made lowercase.
    sellgoodcost = models.IntegerField(db_column='SellGoodCost', blank=True, null=True)  # Field name made lowercase.
    sellgoodquantity = models.IntegerField(db_column='SellGoodQuantity', blank=True, null=True)  # Field name made lowercase.
    selladresspoint = models.TextField(db_column='SellAdressPoint')  # Field name made lowercase.
    sellstatus = models.ForeignKey('Sellstatus', models.DO_NOTHING, db_column='SellStatus', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Sell'


class Sellstatus(models.Model):
    sellstatusid = models.IntegerField(db_column='SellStatusID', primary_key=True)  # Field name made lowercase.
    sellstatusvalue = models.CharField(db_column='SellStatusValue', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SellStatus'


class User(models.Model):
    userid = models.AutoField(db_column='UserID', primary_key=True)  # Field name made lowercase.
    userlastname = models.CharField(db_column='UserLastname', max_length=50)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=50)  # Field name made lowercase.
    userpatronimys = models.CharField(db_column='UserPatronimys', max_length=50)  # Field name made lowercase.
    userbaseadress = models.TextField(db_column='UserBaseAdress')  # Field name made lowercase.
    useremail = models.TextField(db_column='UserEmail')  # Field name made lowercase.
    userphone = models.CharField(db_column='UserPhone', max_length=50)  # Field name made lowercase.
    userpassword = models.TextField(db_column='UserPassword')  # Field name made lowercase.
    userdiscountpoints = models.IntegerField(db_column='UserDiscountPoints', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'User'


class AuthGroup(models.Model):
    name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Sysdiagrams(models.Model):
    name = models.CharField(max_length=128)
    principal_id = models.IntegerField()
    diagram_id = models.AutoField(primary_key=True)
    version = models.IntegerField(blank=True, null=True)
    definition = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sysdiagrams'
        unique_together = (('principal_id', 'name'),)
