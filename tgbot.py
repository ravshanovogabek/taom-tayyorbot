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

@dp.message()
async def handle_message(message: types.Message):
    user_id = message.from_user.id
    text = message.text

    if user_id not in user_data:
        await message.answer("Iltimos, /start buyrug'ini yuboring.")
        return

    state = user_data[user_id].get("state", "language_selection")
#til tanlashni yozganda
    if state == "language_selection":
        if text in ["🇺🇿 O'zbekcha", "🇷🇺 Русский", "🇬🇧 English"]:
            language_mapping = {
                "🇺🇿 O'zbekcha": "O'zbekcha",
                "🇷🇺 Русский": "Русский",
                "🇬🇧 English": "English"
            }
            selected_language = language_mapping[text]
            user_data[user_id]["language"] = selected_language
            user_data[user_id]["state"] = "main_menu"
            await message.answer(
                f"{selected_language} tili tanlandi.\nEndi menyudan tanlang:",
                reply_markup=main_menu[selected_language]
            )
        else:
            await message.answer("Iltimos, tilni tanlang:", reply_markup=language_menu) # tugmadan tanlaganda

#Holat Main Menu bo'lganda
    elif state == "main_menu":
        language = user_data[user_id]["language"]
        if text in ["📦 Buyurtma berish", "📦 Сделать заказ", "📦 Place an Order"]:#buyurtma berish tugmasi
            user_data[user_id]["state"] = "order_method"
            await message.answer(
                "Yetkazib berish turini tanlang:", reply_markup=delivery_takeaway_menu
            )
        elif text == "📝 Fikr bildirish" or text == "📝 Обратная связь" or text == "📝 Feedback":
            user_data[user_id]["state"] = "feedback"
            await message.answer(
                "Iltimos, fikringizni yozing:", reply_markup=feedback_menu
            )
        elif text == "📞 Biz bilan aloqa" or text == "📞 Связаться с нами" or text == "📞 Contact Us":
            user_data[user_id]["state"] = "contact_us"
            await message.answer(
                "Biz bilan bog'lanish uchun telefon raqamimiz: +998777777777", reply_markup=contact_menu
            )
        elif text == "👥 Jamoamizga qo'shiling" or text == "👥 Присоединяйтесь к нам" or text == "👥 Join Our Team":
            user_data[user_id]["state"] = "join_team"
            await message.answer(
                "Iltimos, jamoamizga qo'shilish uchun so'rovnomani boshlang:", reply_markup=join_team_menu
            )
        elif text == "Ortga":
            await message.answer("Ortga qaytdingiz.", reply_markup=main_menu[language])
            
            
    elif state == "feedback":
        if text in ["⭐⭐⭐⭐⭐ 5 Stars", "⭐⭐⭐⭐ 4 Stars", "⭐⭐⭐ 3 Stars", "⭐⭐ 2 Stars", "⭐ 1 Star"]:
            user_data[user_id]["rating"] = text
            await message.answer(f"Rating: {text}.\nIltimos, fikringizni yozing:", reply_markup=feedback_menu)
            user_data[user_id]["state"] = "write_feedback"
        elif text == "📋 Leave Comments":
            user_data[user_id]["state"] = "write_feedback"
            await message.answer("Iltimos, fikringizni yozib qoldiring:", reply_markup=ReplyKeyboardMarkup(resize_keyboard=True))
        elif text == "📝 Write Feedback":
            user_data[user_id]["state"] = "write_feedback"
            await message.answer("Iltimos, fikringizni yozib qoldiring:", reply_markup=ReplyKeyboardMarkup(resize_keyboard=True))

        elif text == "Ortga":
            language = user_data[user_id]["language"]
            user_data[user_id]["state"] = "main_menu"
            await message.answer("Ortga qaytdingiz.", reply_markup=main_menu[language])
            
    elif state == "write_feedback":
        user_data[user_id]["feedback"] = text
        rating = user_data[user_id].get("rating", "No rating given")
        category = user_data[user_id].get("category", "No category selected")
        
        # Send feedback to the channel with rating and category
        await bot.send_message(chat_id=tg_channel, text=f"Fikr:\n{rating}\nKategoriya: {category}\n{user_data[user_id]['feedback']}")
        
        await message.answer("Fikringiz yuborildi. Rahmat!")
        user_data[user_id]["state"] = "main_menu"
        language = user_data[user_id]["language"]
        await message.answer("Ortga qaytdingiz.", reply_markup=main_menu[language])
            
            
            
    elif state == "contact_us":
        if text == "📞 Call Us: +998777777777":
            await message.answer("Bizning telefon raqamimiz: +998777777777. Iltimos, qo'ng'iroq qiling.")
        elif text == "📧 Email Us: support@example.com":
            await message.answer("Bizning elektron pochta manzilimiz: support@example.com.")
        elif text == "🌐 Visit our Website":
            await message.answer("Bizning veb-saytimizga tashrif buyuring: https://www.example.com")
        elif text == "🗓 Business Hours: 9 AM - 6 PM":
            await message.answer("Bizning ish vaqtlari: 9:00 dan 18:00 gacha.")
        elif text == "Ortga":
            language = user_data[user_id]["language"]
            user_data[user_id]["state"] = "main_menu"
            await message.answer("Ortga qaytdingiz.", reply_markup=main_menu[language])
            
    elif state == "join_team":
        if text == "📝 Start Application":
            user_data[user_id]["state"] = "team_application_position"
            await message.answer("Qaysi pozitsiyada ishlashni istaysiz? Masalan: Delivery Driver, Waiter, etc.")
        elif text == "Ortga":
            language = user_data[user_id]["language"]
            user_data[user_id]["state"] = "main_menu"
            await message.answer("Ortga qaytdingiz.", reply_markup=main_menu[language])

    elif state == "team_application_position":
        user_data[user_id]["position"] = text
        user_data[user_id]["state"] = "team_application_availability"
        await message.answer("Ishga kirish uchun qachon bo'lishingiz mumkin? Masalan: Full-time, Part-time, etc.")

    elif state == "team_application_availability":
        user_data[user_id]["availability"] = text
        user_data[user_id]["state"] = "team_application_location"
        await message.answer("Iltimos, yashash joyingizni kiriting (shahar yoki hudud):")

    elif state == "team_application_location":
        user_data[user_id]["location"] = text
        user_data[user_id]["state"] = "team_application_submit"
        await message.answer("Arizangizni yuborishdan oldin tekshirib ko'ring:\n"
                             f"Pozitsiya: {user_data[user_id]['position']}\n"
                             f"Availability: {user_data[user_id]['availability']}\n"
                             f"Location: {user_data[user_id]['location']}\n"
                             "Agar hammasi to'g'ri bo'lsa, 'Yuborish' deb yozing.")

    elif state == "team_application_submit":
        if text.lower() == "yuborish":
            # Send application details to the Telegram channel
            application = f"Yangi ariza:\n\n" \
                          f"Pozitsiya: {user_data[user_id]['position']}\n" \
                          f"Availability: {user_data[user_id]['availability']}\n" \
                          f"Location: {user_data[user_id]['location']}"
            await bot.send_message(chat_id=tg_channel, text=application)
            await message.answer("Arizangiz yuborildi. Rahmat!")
            user_data[user_id]["state"] = "main_menu"
            language = user_data[user_id]["language"]
            await message.answer("Yana biror narsa buyurtma qilmoqchimisiz?", reply_markup=main_menu[language])

        elif text == "Ortga":
            user_data[user_id]["state"] = "main_menu"
            language = user_data[user_id]["language"]
            await message.answer("Ortga qaytdingiz.", reply_markup=main_menu[language])
                
#order type Delivery
    elif state == "order_method":
        if text == "🚚 Delivery":
            user_data[user_id]["state"] = "enter_contact"
            await message.answer(
                "Iltimos, raqamingizni kiriting yoki ulashing:", reply_markup=share_contact_keyboard
            )
        elif text == "🏃 Take Away":#Take away
            user_data[user_id]["state"] = "share_location_takeaway"
            await message.answer(
                "Joylashuvingizni jo'nating, yaqin filialni aniqlaymiz:", reply_markup=share_location_keyboard
            )
        elif text == "Ortga":
            language = user_data[user_id]["language"]
            user_data[user_id]["state"] = "main_menu"
            await message.answer("Ortga qaytdingiz.", reply_markup=main_menu[language])

    elif state == "enter_contact":#Kontaktni kiritish
        if message.contact:
            phone = message.contact.phone_number
            user_data[user_id]["contact"] = phone
            user_data[user_id]["state"] = "verify_code"
            verification_code = random.randint(10000, 99999) #kod
            user_data[user_id]["verification_code"] = verification_code
            try:
                token = get_eskiz_token(email,password)
                send_sms(phone, token)
                await message.answer(f"Tasdiqlash kodi: {verification_code}. Iltimos, ushbu kodni kiriting:")
            except Exception as ex:
                await message.answer(f"{ex}")
                
                
            
        elif text == "Ortga": #Ortga
            user_data[user_id]["state"] = "order_method"
            await message.answer(
                "Yetkazib berish turini tanlang:", reply_markup=delivery_takeaway_menu
            )
        else:
            await message.answer(
                "Iltimos, raqamingizni to'g'ri kiriting yoki ulashing:"
            )

    elif state == "verify_code": #Kod to'g'ri bo'lsa
        if text.isdigit() and int(text) == user_data[user_id].get("verification_code"):
            user_data[user_id]["state"] = "share_location_delivery"
            await message.answer(
                "Kod tasdiqlandi! Endi joylashuvingizni jo'nating:", reply_markup=share_location_keyboard
            )
        else:
            await message.answer("Kod noto'g'ri, qayta urinib ko'ring:")#kod noto'g'ri bo'lsa

    elif state == "share_location_delivery":
        if message.location:
            user_data[user_id]["location"] = (message.location.latitude, message.location.longitude)
            user_data[user_id]["state"] = "extended_menu" #Extended menuni ko'rsatadi
            language = user_data[user_id]["language"]
            await message.answer(
                "Siz ro'yxatdan o'tdingiz! Endi buyurtma qilishingiz mumkin.",
                reply_markup=get_extended_menu(language)
            )
        elif text == "Ortga":
            user_data[user_id]["state"] = "order_method"
            await message.answer(
                "Yetkazib berish turini tanlang:", reply_markup=delivery_takeaway_menu
            )
        else:
            await message.answer("Iltimos, joylashuvingizni ulashing.")

    elif state == "share_location_takeaway": #takeaway holat
        if message.location:
            user_data[user_id]["location"] = (message.location.latitude, message.location.longitude)
            user_data[user_id]["state"] = "extended_menu"
            language = user_data[user_id]["language"]
            await message.answer(
                "Siz ro'yxatdan o'tdingiz! Endi buyurtma qilishingiz mumkin.",
                reply_markup=get_extended_menu(language)
            )
        elif text == "Ortga":
            user_data[user_id]["state"] = "order_method"
            await message.answer(
                "Yetkazib berish turini tanlang:", reply_markup=delivery_takeaway_menu
            )
        else:
            await message.answer("Iltimos, joylashuvingizni ulashing.")

elif state == "extended_menu": #Extended Menu uchun
        if text in menu:
            category = text
            user_data[user_id]["state"] = category
            await message.answer(
                f"{category} menyusi:",
                reply_markup=get_items_menu(category)
            )
            
        elif text == "🛒 Order Basket":  # Handle Order Basket here
            await show_order_basket(user_id, message)
        elif text == "Ortga":
            user_data[user_id]["state"] = "main_menu"
            language = user_data[user_id]["language"]
            await message.answer("Ortga qaytdingiz.", reply_markup=main_menu[language])

    elif state in menu:
        category = state
        if text == "Ortga":
            user_data[user_id]["state"] = "extended_menu"
            language = user_data[user_id]["language"]
            await message.answer("Ortga qaytdingiz.", reply_markup=get_extended_menu(language))

        elif text == "Buyurtmani yakunlash":
            await total_info(message)

        else:
        # Handle adding items to the order
            for item, price in menu[category].items():
                if text == f"{item} - {price} so'm":
                    if category not in user_data[user_id]:
                        user_data[user_id][category] = []
                    user_data[user_id][category].append(item)

                # Send item photo if available and show inline menu for that specific item
                    if item in item_photos:
                        await bot.send_photo(
                            chat_id=message.chat.id,
                            photo=item_photos[item],
                            caption=f"{item} qo'shildi. Narxi: {price} so'm",
                            reply_markup=get_item_inline_menu(category, item, price, 1)  # Show the inline keyboard for this item
                        )

                        
def get_item_inline_menu(category, item, price, quantity):
    """Generate an inline keyboard for an item."""
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="➖", callback_data=f"decrease:{category}:{item}"),
                InlineKeyboardButton(text=f"{quantity}", callback_data="noop"),
                InlineKeyboardButton(text="➕", callback_data=f"increase:{category}:{item}"),
            ],
            [InlineKeyboardButton(text="✅ Add to Order", callback_data=f"add_to_order:{category}:{item}:{price}")]
        ]
    )
    
async def show_order_basket(user_id, message):
    """Display the current order basket."""
    if user_id not in user_data or not any(category in menu and user_data[user_id].get(category) for category in menu):
        await message.answer("Your basket is empty!")
        return

    order_details = []
    total_price = 0

    for category, items in user_data[user_id].items():
        if category in menu:
            for item in items:
                if isinstance(item, tuple) and len(item) == 3:  # Ensure tuple structure
                    item_name, quantity, cost = item
                    order_details.append(f"{item_name} x {quantity} = {cost} so'm")
                    total_price += cost

    if not order_details:
        await message.answer("Your basket is empty!")
    else:
        order_summary = "\n".join(order_details)
        order_summary += f"\n\nTotal: {total_price} so'm"
        await message.answer(order_summary)




@dp.callback_query()
async def handle_callback_query(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    data = callback_query.data
    action, category, item = data.split(":")[:3]  # Extract action, category, item

    if action in ["increase", "decrease"]:
        # Ensure the category exists in user_data
        if "quantities" not in user_data[user_id]:
            user_data[user_id]["quantities"] = {}

        if category not in user_data[user_id]["quantities"]:
            user_data[user_id]["quantities"][category] = {}

        quantities = user_data[user_id]["quantities"][category]
        current_quantity = quantities.get(item, 1)

        # Increase or decrease the quantity
        if action == "increase":
            quantities[item] = current_quantity + 1
        elif action == "decrease" and current_quantity > 1:
            quantities[item] = current_quantity - 1

        # Ensure no negative quantities
        quantities[item] = max(0, quantities[item])

        # Update the inline keyboard with the new quantity
        if current_quantity != quantities[item]:
            await callback_query.message.edit_reply_markup(
                reply_markup=get_item_inline_menu(
                    category, item, menu[category][item], quantities[item]
                )
            )

    elif action == "add_to_order":
        price = int(data.split(":")[3])
        quantity = user_data[user_id]["quantities"].get(category, {}).get(item, 1)
        total_cost = price * quantity

        # Track in the order
        if category not in user_data[user_id]:
            user_data[user_id][category] = []
        user_data[user_id][category].append((item, quantity, total_cost))

        await callback_query.message.answer(f"{item} added to order: {quantity} x {price} so'm")
        await callback_query.message.delete()

async def total_info(message: types.Message):
    user_id = message.from_user.id
    phone = user_data[user_id].get("contact", "No phone provided")
    location = user_data[user_id].get("location", "No location provided")
    order_method = "Delivery" if user_data[user_id]["state"] == "share_location_delivery" else "Take Away"
    
    # Collect selected items and calculate total cost
    total_cost = 0
    ordered_items = []
    for category, items in user_data[user_id].get("quantities", {}).items():
        for item, quantity in items.items():
            if quantity > 0:
                price = menu[category][item]
                cost = price * quantity
                ordered_items.append(f"{item} x {quantity} - {cost} so'm")
                total_cost += cost

    # Format the order details
    order_details = "\n".join(ordered_items)
    order_summary = (
        f"Buyurtma yakunlandi!\n\n"
        f"Telefon: {phone}\n"
        f"Joylashuv: {location}\n"
        f"Buyurtma turi: {order_method}\n\n"
        f"Buyurtgan taomlar:\n{order_details}\n\n"
        f"Jami: {total_cost} so'm\n"
        f"Sizni yana kutamiz!"
    )

    # Send the order summary to the user
    await message.answer(order_summary)
    user_data[user_id]["state"] = "main_menu"
    language = user_data[user_id]["language"]
    await message.answer(
        "Buyurtmangiz tez orada tayyor bo'ladi. Yana biror narsa buyurtma qilmoqchimisiz?",
        reply_markup=main_menu[language]
    )
    
    # Send the order summary to the Telegram channel
    channel_message = (
        f"Yangi buyurtma!\n\n"
        f"Telefon: {phone}\n"
        f"Joylashuv: {location}\n"
        f"Buyurtma turi: {order_method}\n\n"
        f"Buyurtgan taomlar:\n{order_details}\n\n"
        f"Jami: {total_cost} so'm"
    )
    await bot.send_message(chat_id=tg_channel, text=channel_message)



if __name__ == '__main__':
    asyncio.run(dp.start_polling(bot)) 


  # keep the code original and make the code compact by removing unnecessary stuff




