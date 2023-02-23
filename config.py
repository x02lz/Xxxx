from os import getenv
from dotenv import load_dotenv

admins = {}
load_dotenv()

# client vars
API_ID = int(getenv("API_ID", "20752871")) #لا تغير هاذة القيمة
API_HASH = getenv("API_HASH", "57681e5dfee94a798324ac5f5fb217bf")#لا تغير هاذة القيمة
BOT_TOKEN = getenv("BOT_TOKEN", "5518255795:AAGGikA5Xsk27UQCSJCMwLxlG4wdC0Qk_H4")
SESSION_NAME = getenv("SESSION_NAME", "AgBYRxJi-DNZAcIqTb7gfvj4idR4RAm4Thfvv1KdRdNvkJ7_H8X3yqNuIHSDqkPGiKidwcIecyBRivHxVEAEWzAUDVaX9GluUywm23pVVQCJ0gpZt1KYOV6OYHl69rZJpj3EVpgl5rksSW3UItuSyt91Y4_ulrZbvK4hyrBWld-KzaFt1Xws6SJZS1Aw40GGYgHLkB1urOB3ilT1WKs8vFh1Ay_luLfxMQKkOwh2ySuqhE79LyaU-HfIxZXfrUu6MP-dt_R1jP8bxtBOr42rwuscS7tmNSyhmyA4z8BTmEgEbJ7q_mmLiNLAyHGpyirjmB3m5ScV6NlB9H4L8InVqH2UAAAAAWobAkYA")

# mandatory vars
OWNER_USERNAME = getenv("OWNER_USERNAME", "HHMiD") # @ هنا ضع يوزر حسابك بدون 
ALIVE_NAME = getenv("ALIVE_NAME", "seno") # هنا ضع اسم حسابك
BOT_USERNAME = getenv("BOT_USERNAME", "mocisBot") # @ هنا ضع يوزر البوت بدون 
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/X02lx/RrRRR") 
UPSTREAM_BRANCH = getenv("UPSTREM_BRANCH", "main") #لا تغير هاذة القيمة
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60")) #لا تغير هاذة القيمة
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "HHMiDD") # @ هنا ضغ يوزر كروبك بدون 
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "SenoMusic") # @ هنا ضغ يوزر قناتك بدون

# database, decorators, handlers mandatory vars
MONGODB_URL = getenv("MONGODB_URL", "mongodb+srv://veez:mega@cluster0.heqnd.mongodb.net/veez?retryWrites=true&w=majority")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! . $").split())
OWNER_ID = list(map(int, getenv("OWNER_ID", "7933309").split()))
                                             #هنا ضع ايدي المطور فوق و الاعلئ
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "7933309").split()))

# image resources vars
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.png")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.png")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/d70bb6fa92728763c671f.png")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/430dcf25456f2bb38109f.png")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/cd5c96a3c7e8ae1913ef3.png")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
