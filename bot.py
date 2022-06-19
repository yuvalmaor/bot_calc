import logging
import data

from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

files=[]
d=data.Data()
# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')


def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')

def filesfunc(update: Update, context: CallbackContext) -> None:
    global files
    for i in files:
                update.message.reply_document(i)

def getdata(m):
    global files
    files.append(m)


    print("***")
    print(m)


def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    global files
    global d
    try:

        update.message.reply_document(update.message.document)
        
        getdata(update.message.document)
    except:
        t=str(update.message.text)
        if(update.message.text=='file'):
            for i in files:
                update.message.reply_document(i)
        else:
            if(t[:2]=="pc"):
                update.message.reply_text("calculating value")
                update.message.reply_text(d.handel_msg(t))
            else:
                update.message.reply_text(t[:2])

    
    print(update.message.text)
    print("")
    print(update.message.contact)
    print("")
    print(update.message)
    print("")
    print(update)
    print("")

    pass
def echo2(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    
    try:
        t=str(update.message.text)
        if(t[:2]=="pc"):
            update.message.reply_text("calculating value")
            update.message.reply_text("calculating value")
        else:
            update.message.reply_text(t[:2])
    except:
        pass
        """
    try:

        update.message.reply_document(update.message.document)
        
        getdata(update.message.document)
    except:
        t=str(update.message.text)
        if(update.message.text=='file'):
            for i in files:
                update.message.reply_document(i)
        else:
            if(t[:2]=="pc"):
                update.message.reply_text("calculating value")
            else:
                update.message.reply_text(t[:2])

    
    print(update.message.text)
    print("")
    print(update.message.contact)
    print("")
    print(update.message)
    print("")
    print(update)
    print("")
    """


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("5564814911:AAGolfu4Ertp7xE-QgNhl7mWrZvQIa87H3U", use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    #dispatcher.add_handler(CommandHandler("start", start))
    #dispatcher.add_handler(CommandHandler("help", help_command))
    #dispatcher.add_handler(CommandHandler("files", filesfunc))

    # on noncommand i.e message - echo the message on Telegram
    dispatcher.add_handler(MessageHandler(~Filters.command, echo))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()