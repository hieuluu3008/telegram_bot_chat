import os
import subprocess
import asyncio
import logging
from datetime import datetime
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Thiết lập logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Bot Token
BOT_TOKEN = "81xxxxxx09:AAG-iOxxxxxxxxxxxWO-SBxxxxxxxxxxWg"

# PATH FILE
ALLOWED_DIRECTORY = r"C:\Users\TS-1352.LAPTOP-9R6P8INJ\Desktop\test"

## Xử lý lệnh /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    start_text = """
    Happiness! Em là Irene-ssi. Anh cần em giúp gì ạ? Hãy gõ <b>/help</b> để xem những việc em có thể làm nhé 😉
    """
    await update.message.reply_text(start_text, parse_mode='HTML')

## Xử lý lệnh /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    help_text = """
📚 <b>Đây là một số việc mà em có thể hỗ trợ anh</b>

🔸 <b>/time</b> - Hiển thị thời gian hiện tại
🔸 <b>/calc &lt;số1&gt; &lt;số2&gt;</b> - Cộng hai số
   📝 Ví dụ: <code>/calc 10 20</code> → Kết quả: 30
🔸 <b>/echo &lt;tin nhắn&gt;</b> - Em sẽ lặp lại tin nhắn của anh
   📝 Ví dụ: <code>/echo Xin chào!</code> → kết quả trả lời: "Xin chào!"
🔸 <b>/list</b> - Em sẽ list ra các file giúp anh   
🔸 <b>/run</b> - Em sẽ run file giúp anh   
   📝 Ví dụ: <code>/run file_1</code> → Chạy file python file_1
🔸 <b>/info</b> - Xem thông tin về em

❓ <b>LƯU Ý:</b>
• Các số có thể là số thập phân (ví dụ: 3.5)
• Tin nhắn echo có thể chứa nhiều từ

Em có thể trả lời cho anh bất kỳ lúc nào 😍
    """
    await update.message.reply_text(help_text, parse_mode='HTML')

## Xử lý lệnh /time
async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    now = datetime.now()
    
    # Định dạng thời gian theo múi giờ Việt Nam
    time_str = now.strftime("%H:%M:%S")
    date_str = now.strftime("%d/%m/%Y")
    weekday = now.strftime("%A")
    
    # Chuyển tên thứ sang tiếng Việt
    weekdays = {
        "Monday": "Thứ Hai",
        "Tuesday": "Thứ Ba", 
        "Wednesday": "Thứ Tư",
        "Thursday": "Thứ Năm",
        "Friday": "Thứ Sáu",
        "Saturday": "Thứ Bảy",
        "Sunday": "Chủ Nhật"
    }
    
    vietnamese_weekday = weekdays.get(weekday, weekday)
    
    time_message = f"""
⏰ **THỜI GIAN HIỆN TẠI**

🕐 Giờ: **{time_str}**
📅 Ngày: **{date_str}**
📆 Thứ: **{vietnamese_weekday}**

🌍 Múi giờ: UTC+7 (Việt Nam)
    """
    await update.message.reply_text(time_message, parse_mode='Markdown')

## Xử lý lệnh /calc
async def calc_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    args = context.args
    
    # Kiểm tra số lượng tham số
    if len(args) < 2:
        error_message = """
❌ **THIẾU THAM SỐ!**

📝 Cách sử dụng: `/calc <số1> <số2>`

💡 **Ví dụ:**
• `/calc 10 20` → Kết quả: 30
• `/calc 3.5 2.5` → Kết quả: 6.0
• `/calc -5 10` → Kết quả: 5

⚠️ Lưu ý: Cần có đúng 2 số để tính toán!
        """
        await update.message.reply_text(error_message, parse_mode='Markdown')
        return
    
    try:
        # Chuyển đổi tham số thành số
        num1 = float(args[0])
        num2 = float(args[1])
        
        # Tính toán các phép tính cơ bản
        addition = num1 + num2
        subtraction = num1 - num2
        multiplication = num1 * num2
        division = num1 / num2 if num2 != 0 else "Không thể chia cho 0"
        
        result_message = f"""
🧮 **KẾT QUẢ TÍNH TOÁN**

📊 **Các phép tính với {num1} và {num2}:**
➕ Cộng: **{num1} + {num2} = {addition}**
➖ Trừ: **{num1} - {num2} = {subtraction}**
✖️ Nhân: **{num1} × {num2} = {multiplication}**
➗ Chia: **{num1} ÷ {num2} = {division}**

✅ Phép cộng (kết quả chính): **{addition}**
        """
        await update.message.reply_text(result_message, parse_mode='Markdown')
        
    except ValueError:
        error_message = """
❌ **LỖI ĐỊNH DẠNG SỐ!**

🚫 Vui lòng nhập số hợp lệ!

💡 **Ví dụ đúng:**
• `/calc 10 20`
• `/calc 3.14 2.86`
• `/calc -15 25`

🚫 **Ví dụ sai:**
• `/calc abc 123`
• `/calc 10 xyz`
        """
        await update.message.reply_text(error_message, parse_mode='Markdown')

## Xử lý lệnh /echo
async def echo_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    args = context.args
    
    if not args:
        error_message = """
❌ **THIẾU TIN NHẮN!**

📝 Cách sử dụng: `/echo <tin nhắn>`

💡 **Ví dụ:**
• `/echo Xin chào!`
• `/echo Hôm nay thời tiết đẹp`
• `/echo 123 ABC xyz`

🔊 Bot sẽ lặp lại chính xác tin nhắn của bạn!
        """
        await update.message.reply_text(error_message, parse_mode='Markdown')
        return
    
    # Ghép tất cả các từ lại thành câu
    echo_message = " ".join(args)
    user = update.effective_user
    
    response = f"""
🔊 **ECHO MESSAGE**

👤 **{user.first_name} đã nói:**
💬 "{echo_message}"

✨ Tin nhắn đã được lặp lại thành công!
    """
    await update.message.reply_text(response, parse_mode='Markdown')

## Xử lý lệnh info
async def info_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user = update.effective_user
    chat = update.effective_chat
    
    info_message = f"""
ℹ️ **THÔNG TIN CỦA EM**

👩 **Tên:** Bae Joohyun
😘 **Nickname:** Irene
📍 **Phiên bản:** 1.0.0
⚡ **Trạng thái:** Hoạt động
🔧 **Ngôn ngữ:** Python
📚 **Thư viện:** python-telegram-bot

👤 **Thông tin người dùng:**
• **Tên:** {user.first_name}
• **Username:** @{user.username if user.username else 'Không có'}  
• **ID:** {user.id}

💬 **Thông tin chat:**
• **Loại chat:** {chat.type}
• **Chat ID:** {chat.id}

📊 **Tính năng:**
✅ Hiển thị thời gian
✅ Tính toán cơ bản  
✅ Echo tin nhắn
✅ Hỗ trợ 24/7

🔄 **Cập nhật cuối:** {datetime.now().strftime("%d/%m/%Y")}
    """
    await update.message.reply_text(info_message, parse_mode='Markdown')

## Xử lý lệnh /run
async def run_python_file(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Lệnh /run để chạy file Python"""
    
    # Kiểm tra xem có tên file không
    if not context.args:
        await update.message.reply_text("Vui lòng cung cấp tên file!\nVí dụ: /run file1")
        return
    
    filename = context.args[0]
    
    # Thêm đuôi .py nếu chưa có
    if not filename.endswith('.py'):
        filename += '.py'
    
    # Đường dẫn đầy đủ đến file
    filepath = os.path.join(ALLOWED_DIRECTORY, filename)
    
    # Kiểm tra file có tồn tại không
    if not os.path.exists(filepath):
        await update.message.reply_text(f"File {filename} không tồn tại!")
        return
    
    # Kiểm tra file có trong thư mục được phép không
    if not os.path.abspath(filepath).startswith(os.path.abspath(ALLOWED_DIRECTORY)):
        await update.message.reply_text("Không được phép truy cập file này!")
        return
    
    try:
        await update.message.reply_text(f"Đang chạy {filename}...")
        
        # Chạy file Python
        result = subprocess.run(
            ['python', filepath],
            capture_output=True,
            text=True,
            timeout=30  # Timeout 30 giây
        )
        
        # Gửi kết quả
        if result.returncode == 0:
            output = result.stdout if result.stdout else "File chạy thành công (không có output)"
            # Giới hạn độ dài message (Telegram limit 4096 chars)
            if len(output) > 4000:
                output = output[:4000] + "\n... (output quá dài, đã cắt bớt)"
            await update.message.reply_text(f"✅ Kết quả:\n```\n{output}\n```", parse_mode='Markdown')
        else:
            error = result.stderr if result.stderr else "Có lỗi xảy ra"
            if len(error) > 4000:
                error = error[:4000] + "\n... (error quá dài, đã cắt bớt)"
            await update.message.reply_text(f"❌ Lỗi:\n```\n{error}\n```", parse_mode='Markdown')
            
    except subprocess.TimeoutExpired:
        await update.message.reply_text("❌ File chạy quá lâu (timeout 30s)")
    except Exception as e:
        await update.message.reply_text(f"❌ Lỗi không mong muốn: {str(e)}")

## Xử lý lệnh /list
async def list_files(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Lệnh /list để xem danh sách file có thể chạy"""
    try:
        files = [f for f in os.listdir(ALLOWED_DIRECTORY) if f.endswith('.py')]
        if files:
            file_list = "\n".join([f"• {f}" for f in files])
            await update.message.reply_text(f"📁 Danh sách file có thể chạy:\n{file_list}")
        else:
            await update.message.reply_text("Không có file Python nào trong thư mục!")
    except Exception as e:
        await update.message.reply_text(f"❌ Lỗi khi đọc thư mục: {str(e)}")

## Xử lý lệnh không tồn tại với gợi ý lệnh tương tự
async def unknown_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    command = update.message.text.split()[0][1:]  # Bỏ dấu /
    
    # Danh sách các lệnh có sẵn
    available_commands = ["start", "help", "time", "calc", "echo", "list", "run", "info"]
    
    # Tìm lệnh tương tự (đơn giản)
    suggestions = []
    for cmd in available_commands:
        if command.lower() in cmd or cmd in command.lower():
            suggestions.append(cmd)
    
    message = f"❌ Em không thể thực hiện lệnh `/{command}` 🥹\n\n"
    
    if suggestions:
        message += f"🤔 Có phải ý của anh là:\n"
        for suggestion in suggestions[:3]:  # Chỉ hiển thị tối đa 3 gợi ý
            message += f"• `/{suggestion}`\n"
        message += "\n"
    
    message += "💡 Anh có thể dùng /help để xem tất cả lệnh có sẵn."
    
    await update.message.reply_text(message, parse_mode='Markdown')

## Xử lý lỗi
async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):

    logger.warning(f'Update {update} caused error {context.error}')
    
    if update and update.message:
        await update.message.reply_text(
            "❌ Đã xảy ra lỗi! Vui lòng thử lại hoặc liên hệ admin."
        )

# Xử lý xin chào và tạm biệt
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle messages from the user"""
    user_message = update.message.text.lower()
    
    greeting_words = ["hi","hello","chào"]
    farewell_words = ["bye", "bai", "bí bi"]

    if any(word in user_message for word in greeting_words):
        await update.message.reply_text("Hi anh~ 😊")

    elif any(word in user_message for word in farewell_words):
        await update.message.reply_text("Bye bye anh~ 👋🥹")
    else:
        await update.message.reply_text("Em xin lỗi. Em chưa hiểu ý của anh")

def main():
    """Run the bot"""
    # Create the application
    application = Application.builder().token(BOT_TOKEN).build()
    
    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("time", time_command))
    application.add_handler(CommandHandler("calc", calc_command))
    application.add_handler(CommandHandler("echo", echo_command))
    application.add_handler(CommandHandler("info", info_command))
    application.add_handler(CommandHandler("run", run_python_file))
    application.add_handler(CommandHandler("list", list_files))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Handler cho lệnh không tồn tại - PHẢI ĐẶT CUỐI CÙNG
    application.add_handler(MessageHandler(filters.COMMAND, unknown_command))
    
    # Thêm error handler
    application.add_error_handler(error_handler)

    # Run the bot
    print("Bot is running...")
    application.run_polling(drop_pending_updates=True)

if __name__ == '__main__':
    main()