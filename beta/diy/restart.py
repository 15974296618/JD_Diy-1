#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
import sys

from telethon import events

from .. import chat_id, jdbot, logger, ch_name, BOT_SET


@jdbot.on(events.NewMessage(from_users=chat_id, pattern=r'^/restart$'))
async def myrestart(event):
    try:
        await jdbot.send_message(chat_id, "重启程序")
        cmdtext = 'if [ -d "/jd" ]; then root=/jd; else root=/ql; fi;' \
                  'cd $root/jbot; pm2 restart jbot'
        os.system(cmdtext)
    except Exception as e:
        title = "【💥错误💥】"
        name = "文件名：" + os.path.split(__file__)[-1].split(".")[0]
        function = "函数名：" + sys._getframe().f_code.co_name
        tip = '建议百度/谷歌进行查询'
        await jdbot.send_message(chat_id, f"{title}\n\n{name}\n{function}\n错误原因：{str(e)}\n\n{tip}")
        logger.error(f"错误--->{str(e)}")


if ch_name:
    jdbot.add_event_handler(myrestart, events.NewMessage(from_users=chat_id, pattern=BOT_SET['命令别名']['cron']))

