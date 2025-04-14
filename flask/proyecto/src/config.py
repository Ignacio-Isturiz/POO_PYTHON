import os 

class Config:
    SECRET_KEY = os.urandom(24)
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "postgresql://Login_owner:npg_wyeWF2SkX5EA@ep-young-river-a5upb5w7-pooler.us-east-2.aws.neon.tech/Login?sslmode=require"
    SQLALCHEMY_TRACK_MODIFICATION = False