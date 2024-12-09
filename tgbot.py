import asyncio
import random
import requests
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton




TOKEN = '7204571458:AAHIgVj3rFVu8FMk3cuEqqcbF1Puz6RTzwk'  # Replace with your bot token
bot = Bot(token=TOKEN)
tg_channel = '@xabarchi_lar'
dp = Dispatcher()

# User data to track states and preferences
user_data = {}



email = "ravshanovogabek27@gmail.com" 
password = "uWBAxC2bRNRfoKm4qecoOPrnKj1ii5It9nv3ExOH"

def get_eskiz_token(email, password):
    url = "https://notify.eskiz.uz/api/auth/login"
    payload ={
        "email": email,
        "password": password
    }
    headers = {}
    response = requests.post(url, data=payload, headers=headers)
    if response.status_code == 200:
        return response.json().get('data', {}).get('token', {})
    
def send_sms( phone, token):
    url = "https://notify.eskiz.uz/api/message/sms/send"
    payload={
            'mobile_phone': phone,
            'message': 'Bu Eskiz dan test',
            'from': '4546',
            'callback_url': 'http://0000.uz/test.php' }
        
    headers = {
         'Authorization': f'Bearer {token}'
    }
        
    response = requests.post(url, headers=headers, data=payload)
    if response.status_code != 200:
        raise Exception("Sms yuborishda xatolik")
        
    
    
    
    
    
# Full Menu with Updated Categories
menu = {
    'Burgerlar🍔': {'Classic': 23000, 'Cesar': 23000, 'Cheese': 27000},
    'Pizzalar🍕': {'Margherita': 18000, 'Hawai': 40000, 'Oddiy': 60000},
    'Ichimliklar🥤': {'Ice tea': 17000, 'Moxito': 25000, 'Choy': 5000},
    'Lavashlar🌯': {'Chicken Lavash': 25000, 'Beef Lavash': 28000},
    'Hot Doglar🌭': {'Classic Hot Dog': 15000, 'Cheese Hot Dog': 18000},
    'Sandwichlar🥪': {'Club Sandwich': 20000, 'Veggie Sandwich': 18000},
    'Milliy taomlar🇺🇿': {'Osh': 30000, 'Somsa': 12000},
    'Shirinliklar🍰': {'Cheesecake': 25000, 'Tiramisu': 28000}
}

item_photos = {
    'Classic': 'https://thespiceway.com/cdn/shop/files/Signature_Savory_Classic_Burger.jpg?v=1712161801',
    'Cesar': 'https://legrecoriginal.com/wp-content/uploads/Caesar_Burger3810.png',
    'Cheese': 'https://www.kitchensanctuary.com/wp-content/uploads/2021/05/Double-Cheeseburger-square-FS-42.jpg',
    'Margherita': 'https://recipes.heart.org/-/media/AHA/Recipe/Recipe-Images/Classic-Margherita-Pizza-with-Whole-Wheat-Pizza-Crust.jpg?sc_lang=en&hash=8669621DF39E46A90612215CFACFE313',
    'Hawai': 'https://www.allrecipes.com/thmb/v1Xi2wtebK1sZwSJitdV4MGKl1c=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/hawaiian-pizza-ddmfs-3x2-132-450eff04ad924d9a9eae98ca44e3f988.jpg',
    'Oddiy': 'https://i0.wp.com/daddioskitchen.com/wp-content/uploads/2023/01/IMG-5299.jpg?fit=3024%2C3024&ssl=1',
    'Ice tea': 'https://eurosnab.com/storage/news/2-1658337961.png',
    'Moxito': 'https://cdn.loveandlemons.com/wp-content/uploads/2020/07/mojito.jpg',
    'Choy': 'https://brodandtaylor.com/cdn/shop/articles/dehydrated-tea-thumb_1024x.jpg?v=1639765759',
    'Chicken Lavash': 'https://www.foodfusion.com/wp-content/uploads/2021/10/Doner-Shawarma-with-Lavash-Bread-Recipe-by-Food-fusion-1.jpg',
    'Beef Lavash': 'https://i.pinimg.com/736x/11/12/90/11129069a1558d6f4e5ce01d9a5cf3b5.jpg',
    'Classic Hot Dog': 'https://thespiceway.com/cdn/shop/files/Cheesy_Classic_Hot_Dogs.jpg?v=1712164565',
    'Cheese Hot Dog': 'https://www.belbrandsfoodservice.com/wp-content/uploads/2018/05/recipe-desktop-merkts-cheesy-hot-dawg.jpg',
    'Club Sandwich': 'https://hips.hearstapps.com/hmg-prod/images/delish-200511-seo-club-sandwich-h-14383-eb-1590780714.jpg?crop=0.671xw:1.00xh;0.123xw,0&resize=1200:*',
    'Veggie Sandwich': 'https://www.rainbownourishments.com/wp-content/uploads/2018/06/roast-veg-sandwich-1.jpg',
    'Osh': 'https://www.orexca.com/img/cuisine/plov/uzbek-pilaf.jpg',
    'Somsa': 'https://img.povar.ru/mobile/d3/9d/fc/40/somsa_samosa-4902.jpg',
    'Chessecake': 'https://www.glutenfreestories.com/wp-content/uploads/2023/08/cheesecake-slice-with-straberry-sauce-Cropped.jpg',
    'Tiramisu': 'https://assets.tmecosys.com/image/upload/t_web767x639/img/recipe/ras/Assets/6BE1C69C-69FB-4957-96EA-D76159076661/Derivates/BA406212-38AE-4EA0-B4D5-591514C21C2D.jpg'
    
        # Add more mappings for other items
}



# Keyboards
language_menu = ReplyKeyboardMarkup(
    keyboard=[ 
        [KeyboardButton(text="🇺🇿 O'zbekcha"), KeyboardButton(text="🇷🇺 Русский"), KeyboardButton(text="🇬🇧 English")],
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)


#Main Menu tugmalari
main_menu = {
    "O'zbekcha": ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📦 Buyurtma berish"), KeyboardButton(text="📜 Buyurtmalar tarixi")],
            [KeyboardButton(text="📝 Fikr bildirish"), KeyboardButton(text="📞 Biz bilan aloqa")],
            [KeyboardButton(text="👥 Jamoamizga qo'shiling")],
        ],
        resize_keyboard=True
    ),
    "Русский": ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📦 Сделать заказ"), KeyboardButton(text="📜 История заказов")],
            [KeyboardButton(text="📝 Обратная связь"), KeyboardButton(text="📞 Связаться с нами")],
            [KeyboardButton(text="👥 Присоединяйтесь к нам")],
        ],
        resize_keyboard=True
    ),
    "English": ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📦 Place an Order"), KeyboardButton(text="📜 Order History")],
            [KeyboardButton(text="📝 Feedback"), KeyboardButton(text="📞 Contact Us")],
            [KeyboardButton(text="👥 Join Our Team")],
        ],
        resize_keyboard=True
    )
}

feedback_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="⭐⭐⭐⭐⭐ 5 Stars"), KeyboardButton(text="⭐⭐⭐⭐ 4 Stars")],
        [KeyboardButton(text="⭐⭐⭐ 3 Stars"), KeyboardButton(text="⭐⭐ 2 Stars"), KeyboardButton(text="⭐ 1 Star")],
        [KeyboardButton(text="📋 Leave Comments"), KeyboardButton(text="📝 Write Feedback")],
        [KeyboardButton(text="Ortga")]
    ],
    resize_keyboard=True
)

# Updated Contact Us Menu
contact_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📞 Call Us: +998777777777"), KeyboardButton(text="📧 Email Us: support@example.com")],
        [KeyboardButton(text="🌐 Visit our Website")],
        [KeyboardButton(text="🗓 Business Hours: 9 AM - 6 PM")],
        [KeyboardButton(text="Ortga")]
    ],
    resize_keyboard=True
)

# Join our team menu (with form)
join_team_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📝 Start Application")],
        [KeyboardButton(text="Ortga")]
    ],
    resize_keyboard=True
)

# Delivery va Takeaway tugmalari
delivery_takeaway_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🚚 Delivery"), KeyboardButton(text="🏃 Take Away")],
        [KeyboardButton(text="Ortga")],
    ],
    resize_keyboard=True
)

# Kontakt ulashish tugmasi
share_contact_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📱 Share Contact", request_contact=True)],
        [KeyboardButton(text="Ortga")]
    ],
    resize_keyboard=True
)

#Lokatsiya jo'natish tugmasi
share_location_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📍 Share Location", request_location=True)],
        [KeyboardButton(text="Ortga")]
    ],
    resize_keyboard=True
)

#Kategoriya
def get_items_menu(category):
    """Generate a menu for items in a category."""
    if category not in menu:
        return ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Ortga")]], resize_keyboard=True)
    
    items = menu[category]
    keyboard = [[KeyboardButton(text=f"{item} - {price} so'm")] for item, price in items.items()]
    keyboard.append([KeyboardButton(text="Buyurtmani yakunlash"), KeyboardButton(text="Ortga")])
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)

def get_extended_menu(language):
    """Generate an extended menu for additional categories."""
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Ichimliklar🥤"), KeyboardButton(text="Burgerlar🍔"),
                KeyboardButton(text="Lavashlar🌯"), KeyboardButton(text="Hot Doglar🌭"),
            ],
            [
                KeyboardButton(text="Sandwichlar🥪"), KeyboardButton(text="Milliy taomlar🇺🇿"),
                KeyboardButton(text="Shirinliklar🍰"), KeyboardButton(text='Pizzalar🍕'),
            ],
            [  KeyboardButton(text="🛒 Order Basket"),  KeyboardButton(text="Ortga")],
        ],
        resize_keyboard=True
    )


#Start bosilganda
@dp.message(Command("start"))
async def start(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id] = {"state": "language_selection"}
    await message.answer(
        "Assalomu alaykum! Taom buyurtma botimizga xush kelibsiz.\nIltimos, tilni tanlang:",
        reply_markup=language_menu
    )
