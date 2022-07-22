##########################################################################################
#                                                                                        #
#                              一言机器人 TG:@hitoko_yiyanbot                             #
#                                   by 咸鱼味的鸽子g2nnyS                                 #
#                                                                                        #
#     一言机器人是一个简单的机器人，它可以定时向你的Telegram群组发送一言。也可以通过指令获取    #
#                                                                                        #
##########################################################################################
# -*- coding:utf-8 -*-
# 首先需要引入需要的库
import logging
import telegram
from telegram import Update
from telegram.ext import Updater, CallbackContext, CommandHandler
from telegram.error import NetworkError, Unauthorized
from time import sleep
import time
import requests as r

token = 'TOKEN' #在此填入你的Token

#发送/yiyan指令，向用户发送从一言API获取的内容
def yiyan(update: Update, context: CallbackContext):
        if update.message:  # 如果Bot收到消息
            # 从一言API获取一言
            yiyan = r.get('https://v1.hitokoto.cn/').json()
            # 发送消息, 提取hitokoto、from、from_who
            update.message.reply_text(update.message.chat_id, '一言: ' + yiyan['hitokoto'] + '\n' + '出处: ' + yiyan['from'] + yiyan['from_who'])
            print('指令:/yiyan 发送时间:',time.strftime("%H:%M:%S", time.localtime()), '类型:reply_text')
            # 发送消息后，更新update_id
            update_id = update.update_id + 1

#发送/start指令
def start(update: Update, context: CallbackContext):
        if update.message:  # 如果Bot收到消息
            # 发送消息, 携带变量message、from_who、from_who_who
            update.message.reply_text(update.message.chat_id, '欢迎使用一言机器人！\n'
                                                     '请输入/help查看指令！')
            print('指令:/start 发送时间:',time.strftime("%H:%M:%S", time.localtime()), '类型:reply_text')
            # 发送消息后，更新update_id
            update_id = update.update_id + 1

#发送/help指令
def help(update: Update, context: CallbackContext):
        if update.message:  # 如果Bot收到消息
            # 发送消息, 携带变量message、from_who、from_who_who
            update.message.reply_text(update.message.chat_id, '指令如下：\n'
                                                     '/start: 开始使用机器人\n'
                                                     '/help: 查看帮助\n'
                                                     '/yiyan: 获取一言\n')
            print('指令:/help 发送时间:',time.strftime("%H:%M:%S", time.localtime()), '类型:reply_text')

# 定义程序的入口
if __name__ == '__main__':
    updater = Updater(token=token, use_context=True)
    # 注册指令
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('help', help))
    updater.dispatcher.add_handler(CommandHandler('yiyan', yiyan))
    # 启动程序
    updater.start_polling()

        