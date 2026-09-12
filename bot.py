import telebot

BOT_TOKEN = "8639260550:AAEVN4sQdff3ia_bIt-z_MI0P9D6T5InRaY"
OWNER_ID = 8993216569

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(content_types=['text', 'photo', 'video', 'document', 'sticker', 'voice', 'animation', 'video_note', 'audio', 'contact', 'location'])
def handle_all(message):
    try:
        user = message.from_user
        name = user.first_name
        if user.last_name:
            name += " " + user.last_name
        username = f"@{user.username}" if user.username else "No username"
        user_id = user.id

        # Group-லா private-லான்னு பார்க்கறோம்
        if message.chat.type in ['group', 'supergroup']:
            chat_info = f"👥 Group: {message.chat.title}"
        else:
            chat_info = "💬 Private Chat"

        header = (
            f"📥 New Message\n"
            f"{chat_info}\n"
            f"👤 From: {name}\n"
            f"🔗 {username}\n"
            f"🆔 {user_id}"
        )

        # Owner-க்கு அனுப்புறோம்
        if message.text:
            bot.send_message(OWNER_ID, f"{header}\n\n💬 Text:\n{message.text}")
        elif message.photo:
            bot.send_photo(OWNER_ID, message.photo[-1].file_id, caption=header)
        elif message.video:
            bot.send_video(OWNER_ID, message.video.file_id, caption=header)
        elif message.document:
            bot.send_document(OWNER_ID, message.document.file_id, caption=header)
        elif message.sticker:
            bot.send_message(OWNER_ID, header)
            bot.send_sticker(OWNER_ID, message.sticker.file_id)
        elif message.voice:
            bot.send_voice(OWNER_ID, message.voice.file_id, caption=header)
        elif message.animation:
            bot.send_animation(OWNER_ID, message.animation.file_id, caption=header)
        elif message.video_note:
            bot.send_message(OWNER_ID, header)
            bot.send_video_note(OWNER_ID, message.video_note.file_id)
        elif message.audio:
            bot.send_audio(OWNER_ID, message.audio.file_id, caption=header)
        else:
            bot.send_message(OWNER_ID, f"{header}\n\n⚠️ Other type message")

    except Exception as e:
        print(e)

print("Full Silent Logger Bot is running...")
bot.infinity_polling()