from telethon import TelegramClient, events
from random import choice as ch
from asyncio import sleep as sl
from datetime import datetime

shabl = ["ти голозадий син шалави закрий рило нахуй своє я ж тобі тут сраку єбав",
"слабак блядоруснявий я тобі тут ні шансу не залишу нахуй ",
"не вихрюкуй тут син шалави криворукий",
"я тобі тут мати шлюху єбашу голими руками ару",
"нахуй ти руснявий син шлюхи помер тут",
"свиня блядорила я тебе тут нахуй в жопу єбу",
"завали єбало своє свиня кривозуба нахуй і не пиши сюди взагалі",
"ти труслива сволота русняворила я тобі зараз твоє свинне рило переломаю",
"не помирай тут слабак єбаний",
"на хую ти відкинув копита русняві ару",
"який тобі нон стоп слабий син шлюхи котрий получає піздонів весь час",
"не бійся мене свинорус обриганий я ж лише тобі матір шлюху в рило виєбав",
"мовчи давай косоглазий синяра шлюхи я тобі рило рвав нахуй",
"береш мій хуй замість памперсу собі ару",
"антихрист твою русоблядську матір шлюху в сраку єбав во славу України",
"один хуй ти циган єбаний обожнюєш українські пеніси",
"нахуй ти сосеш мій хуй віслюк єбаний відірвись вже від нього",
"один хуй ти слабак котрий мого хуйця заглотне",
"русоблядь твою матір шлюху в рило хохли єбуть ",
"як тобі на смак український хуй син шалави",
"ти нахуй мені тут відсосав слабак блядський",
"циганку єбану трахаємо як не в себе хєхє",
"син шлюхози криволапий відсоси мені",
"ну і нахуй ти помер на хуї тут",
"ні нащо не здатний синяра шлюхи не помирай прям тут",
"один хуй слабак єбаний ти",
"твою маму хуями єбали",
"чого ти так бігаєш від мого хуя слабачок блядоруснявосвинотний я тобі тут кривозубу циганськоподібну матір шлюху поєбу",
"буду тебе принижувати поки остаточно не помреш від хуя",
"вічніть буду твою мати шлюху терирозувати своїм хуйом українським",
"нахуй ти тут свій відсос показав ару",
"не помирай син шалави руснявий я ж твої копита відпилю за таке",
"твою матір шлюху з балкону хуйом скинув ару",
"так та закрий нахуй своє чорне рило і відсоси мені тут",
"хуячим тебе синка блядорилої шиншили нахуй",
"ти чого вже відсосав єбаний блядорус",
"зніму з тебе шкіру син хуйні ти",
"і так і так відсосеш мій хуй",
"як би ти не старався все одно залишешся терпнем єбаним",
"все твоє життя в тебе харкати будемо синчело шалави котре відбилося від стада"]
shabl2 = ["ᴛᥙ ᴦ᧐᧘᧐ᤋᥲдᥙᥔ ᥴᥙн ɯᥲ᧘ᥲʙᥙ ᤋᥲκρᥙᥔ ρᥙ᧘᧐ нᥲ᥊уᥔ ᥴʙ᧐є я ж ᴛ᧐δі ᴛуᴛ ᥴρᥲκу єδᥲʙ",

"ᥴ᧘ᥲδᥲκ δ᧘яд᧐ρуᥴняʙᥙᥔ я ᴛ᧐δі ᴛуᴛ ні ɯᥲнᥴу нᥱ ᤋᥲ᧘ᥙɯу нᥲ᥊уᥔ ",

"нᥱ ʙᥙ᥊ρюκуᥔ ᴛуᴛ ᥴᥙн ɯᥲ᧘ᥲʙᥙ κρᥙʙ᧐ρуκᥙᥔ",
"я ᴛ᧐δі ᴛуᴛ ⲙᥲᴛᥙ ɯ᧘ю᥊у єδᥲɯу ᴦ᧐᧘ᥙⲙᥙ ρуκᥲⲙᥙ ᥲρу",
"нᥲ᥊уᥔ ᴛᥙ ρуᥴняʙᥙᥔ ᥴᥙн ɯ᧘ю᥊ᥙ ᥰ᧐ⲙᥱρ ᴛуᴛ",
"ᥴʙᥙня δ᧘яд᧐ρᥙ᧘ᥲ я ᴛᥱδᥱ ᴛуᴛ нᥲ᥊уᥔ ʙ ж᧐ᥰу єδу",
"ᤋᥲʙᥲ᧘ᥙ єδᥲ᧘᧐ ᥴʙ᧐є ᥴʙᥙня κρᥙʙ᧐ᤋуδᥲ нᥲ᥊уᥔ і нᥱ ᥰᥙɯᥙ ᥴюдᥙ ʙᤋᥲᴦᥲ᧘і",
"ᴛᥙ ᴛρуᥴ᧘ᥙʙᥲ ᥴʙ᧐᧘᧐ᴛᥲ ρуᥴняʙ᧐ρᥙ᧘ᥲ я ᴛ᧐δі ᤋᥲρᥲᤋ ᴛʙ᧐є ᥴʙᥙннᥱ ρᥙ᧘᧐ ᥰᥱρᥱ᧘᧐ⲙᥲю",
"нᥱ ᥰ᧐ⲙᥙρᥲᥔ ᴛуᴛ ᥴ᧘ᥲδᥲκ єδᥲнᥙᥔ",
"нᥲ ᥊ую ᴛᥙ ʙідκᥙнуʙ κ᧐ᥰᥙᴛᥲ ρуᥴняʙі ᥲρу",
"яκᥙᥔ ᴛ᧐δі н᧐н ᥴᴛ᧐ᥰ ᥴ᧘ᥲδᥙᥔ ᥴᥙн ɯ᧘ю᥊ᥙ κ᧐ᴛρᥙᥔ ᥰ᧐᧘учᥲє ᥰіᤋд᧐ніʙ ʙᥱᥴь чᥲᥴ",
"нᥱ δіᥔᥴя ⲙᥱнᥱ ᥴʙᥙн᧐ρуᥴ ᧐δρᥙᴦᥲнᥙᥔ я ж ᧘ᥙɯᥱ ᴛ᧐δі ⲙᥲᴛіρ ɯ᧘ю᥊у ʙ ρᥙ᧘᧐ ʙᥙєδᥲʙ",
"ⲙ᧐ʙчᥙ дᥲʙᥲᥔ κ᧐ᥴ᧐ᴦ᧘ᥲᤋᥙᥔ ᥴᥙняρᥲ ɯ᧘ю᥊ᥙ я ᴛ᧐δі ρᥙ᧘᧐ ρʙᥲʙ нᥲ᥊уᥔ",
"δᥱρᥱɯ ⲙіᥔ ᥊уᥔ ᤋᥲⲙіᥴᴛь ᥰᥲⲙᥰᥱρᥴу ᥴ᧐δі ᥲρу",
"ᥲнᴛᥙ᥊ρᥙᥴᴛ ᴛʙ᧐ю ρуᥴ᧐δ᧘ядᥴьκу ⲙᥲᴛіρ ɯ᧘ю᥊у ʙ ᥴρᥲκу єδᥲʙ ʙ᧐ ᥴ᧘ᥲʙу Уκρᥲїнᥙ",
"᧐дᥙн ᥊уᥔ ᴛᥙ цᥙᴦᥲн єδᥲнᥙᥔ ᧐δ᧐жнюєɯ уκρᥲїнᥴьκі ᥰᥱніᥴᥙ",
"нᥲ᥊уᥔ ᴛᥙ ᥴ᧐ᥴᥱɯ ⲙіᥔ ᥊уᥔ ʙіᥴ᧘юκ єδᥲнᥙᥔ ʙідіρʙᥙᥴь ʙжᥱ ʙід нь᧐ᴦ᧐",
"᧐дᥙн ᥊уᥔ ᴛᥙ ᥴ᧘ᥲδᥲκ κ᧐ᴛρᥙᥔ ⲙ᧐ᴦ᧐ ᥊уᥔця ᤋᥲᴦ᧘᧐ᴛнᥱ",
"ρуᥴ᧐δ᧘ядь ᴛʙ᧐ю ⲙᥲᴛіρ ɯ᧘ю᥊у ʙ ρᥙ᧘᧐ ᥊᧐᥊᧘ᥙ єδуᴛь ",
"яκ ᴛ᧐δі нᥲ ᥴⲙᥲκ уκρᥲїнᥴьκᥙᥔ ᥊уᥔ ᥴᥙн ɯᥲ᧘ᥲʙᥙ",
"ᴛᥙ нᥲ᥊уᥔ ⲙᥱні ᴛуᴛ ʙідᥴ᧐ᥴᥲʙ ᥴ᧘ᥲδᥲκ δ᧘ядᥴьκᥙᥔ",
"цᥙᴦᥲнκу єδᥲну ᴛρᥲ᥊ᥲєⲙ᧐ яκ нᥱ ʙ ᥴᥱδᥱ ᥊є᥊є",
"ᥴᥙн ɯ᧘ю᥊᧐ᤋᥙ κρᥙʙ᧐᧘ᥲᥰᥙᥔ ʙідᥴ᧐ᥴᥙ ⲙᥱні",
"ну і нᥲ᥊уᥔ ᴛᥙ ᥰ᧐ⲙᥱρ нᥲ ᥊уї ᴛуᴛ",
"ні нᥲщ᧐ нᥱ ᤋдᥲᴛнᥙᥔ ᥴᥙняρᥲ ɯ᧘ю᥊ᥙ нᥱ ᥰ᧐ⲙᥙρᥲᥔ ᥰρяⲙ ᴛуᴛ",
"᧐дᥙн ᥊уᥔ ᥴ᧘ᥲδᥲκ єδᥲнᥙᥔ ᴛᥙ",
"ᴛʙ᧐ю ⲙᥲⲙу ᥊уяⲙᥙ єδᥲ᧘ᥙ",
"ч᧐ᴦ᧐ ᴛᥙ ᴛᥲκ δіᴦᥲєɯ ʙід ⲙ᧐ᴦ᧐ ᥊уя ᥴ᧘ᥲδᥲч᧐κ δ᧘яд᧐ρуᥴняʙ᧐ᥴʙᥙн᧐ᴛнᥙᥔ я ᴛ᧐δі ᴛуᴛ κρᥙʙ᧐ᤋуδу цᥙᴦᥲнᥴьκ᧐ᥰ᧐діδну ⲙᥲᴛіρ ɯ᧘ю᥊у ᥰ᧐єδу",
"δуду ᴛᥱδᥱ ᥰρᥙнᥙжуʙᥲᴛᥙ ᥰ᧐κᥙ ᧐ᥴᴛᥲᴛ᧐чн᧐ нᥱ ᥰ᧐ⲙρᥱɯ ʙід ᥊уя",
"ʙічніᴛь δуду ᴛʙ᧐ю ⲙᥲᴛᥙ ɯ᧘ю᥊у ᴛᥱρᥙρ᧐ᤋуʙᥲᴛᥙ ᥴʙ᧐їⲙ ᥊уᥔ᧐ⲙ уκρᥲїнᥴьκᥙⲙ",
"нᥲ᥊уᥔ ᴛᥙ ᴛуᴛ ᥴʙіᥔ ʙідᥴ᧐ᥴ ᥰ᧐κᥲᤋᥲʙ ᥲρу",
"нᥱ ᥰ᧐ⲙᥙρᥲᥔ ᥴᥙн ɯᥲ᧘ᥲʙᥙ ρуᥴняʙᥙᥔ я ж ᴛʙ᧐ї κ᧐ᥰᥙᴛᥲ ʙідᥰᥙ᧘ю ᤋᥲ ᴛᥲκᥱ",
"ᴛʙ᧐ю ⲙᥲᴛіρ ɯ᧘ю᥊у ᤋ δᥲ᧘κ᧐ну ᥊уᥔ᧐ⲙ ᥴκᥙнуʙ ᥲρу",
"ᴛᥲκ ᴛᥲ ᤋᥲκρᥙᥔ нᥲ᥊уᥔ ᥴʙ᧐є ч᧐ρнᥱ ρᥙ᧘᧐ і ʙідᥴ᧐ᥴᥙ ⲙᥱні ᴛуᴛ",
"᥊уячᥙⲙ ᴛᥱδᥱ ᥴᥙнκᥲ δ᧘яд᧐ρᥙ᧘᧐ї ɯᥙнɯᥙ᧘ᥙ нᥲ᥊уᥔ",
"ᴛᥙ ч᧐ᴦ᧐ ʙжᥱ ʙідᥴ᧐ᥴᥲʙ єδᥲнᥙᥔ δ᧘яд᧐ρуᥴ",
"ᤋніⲙу ᤋ ᴛᥱδᥱ ɯκіρу ᥴᥙн ᥊уᥔні ᴛᥙ",
"і ᴛᥲκ і ᴛᥲκ ʙідᥴ᧐ᥴᥱɯ ⲙіᥔ ᥊уᥔ",
"яκ δᥙ ᴛᥙ нᥱ ᥴᴛᥲρᥲʙᥴя ʙᥴᥱ ᧐дн᧐ ᤋᥲ᧘ᥙɯᥱɯᥴя ᴛᥱρᥰнᥱⲙ єδᥲнᥙⲙ",
"ʙᥴᥱ ᴛʙ᧐є жᥙᴛᴛя ʙ ᴛᥱδᥱ ᥊ᥲρκᥲᴛᥙ δудᥱⲙ᧐ ᥴᥙнчᥱ᧘᧐ ɯᥲ᧘ᥲʙᥙ κ᧐ᴛρᥱ ʙідδᥙ᧘᧐ᥴя ʙід ᥴᴛᥲдᥲ"]
state = True
state1 = True
start = datetime.now()
time = 300
ph = ""
shapka = ""
media_file = ""
admin_id = "5944819766"

class PydroidBot:
    def __init__(self):
        self.api_id = 26736366
        self.api_hash = "10a653547ac17ab466a92238755ffcec"
        self.client = TelegramClient('a4', self.api_id, self.api_hash)
        self.client.start()

    def run(self):
        @self.client.on(events.NewMessage(pattern=r'\/terror'))
        async def command_fast(event):
            user_id = event.message.sender_id
            if str(user_id) == admin_id:
                txt = event.message.message.split(maxsplit=1)[1]
                chat_id = int(txt)
                global state
                state = True
                while state:
                    text = ch(shabl)
                    await self.client.send_message(chat_id, shapka+" "+text)
                    await sl(int(time))
        
        @self.client.on(events.NewMessage(pattern=r'\/mterror'))
        async def command_fastph(event):
            user_id = event.message.sender_id
            txt = event.message.message.split(maxsplit=1)[1]
            if str(user_id) == admin_id:
                chat_id = int(txt)
                global state1
                state1 = True
                while state1:
                    text = ch(shabl2)
                    await self.client.send_file(chat_id, ph, caption=shapka+" "+text)
                    await sl(int(time))

        @self.client.on(events.NewMessage(pattern='/time'))
        async def command_set_time(event):
            if str(event.message.sender_id) == admin_id:
                text = event.message.message.split(maxsplit=1)[1]
                global time
                time = int(text)
                await event.respond("<b>ᤋᥲᴛρᥙⲙκᥲ ʙᥴᴛᥲн᧐ʙ᧘ᥱнᥲ!</b>", parse_mode='html')

        @self.client.on(events.NewMessage(pattern='/media'))
        async def command_set_file(event):
            if str(event.message.sender_id) == admin_id:
                text = event.message.message.split(maxsplit=1)[1]
                global ph
                ph = text
                await event.respond("<b>ⲙᥱдіᥲ ʙᥴᴛᥲн᧐ʙ᧘ᥱн᧐!</b>", parse_mode='html')

        @self.client.on(events.NewMessage(pattern='/text'))
        async def command_set_shapka(event):
            if str(event.message.sender_id) == admin_id:
                text = event.message.message.split(maxsplit=1)[1]
                global shapka
                shapka = str(text)
                await event.respond('<b>ɯᥲᥰκᥲ ʙᥴᴛᥲн᧐ʙ᧘ᥱнᥲ!<b>', parse_mode='html')

        @self.client.on(events.NewMessage(pattern='/uptime'))
        async def command_uptime(event):
            if str(event.message.sender_id) == admin_id:
                time_now = datetime.now()
                timing = time_now - start
                time_string = str(timing)
                time_result = time_string.split(".")[0]
                await event.respond('<b>ᥲᥰᴛᥲᥔⲙ δ᧐ᴛᥲ: <code>{}</code></b>'.format(time_result), parse_mode='html')


        @self.client.on(events.NewMessage(pattern='/stop'))
        async def command_stop(event):
            global state, state1
            stop_number = event.message.message.split(maxsplit=1)[1]
            if str(event.message.sender_id) == admin_id:
                if stop_number == "1":
                    state = False
                    await event.respond("<b>ᤋуᥰᥙнᥱн᧐</b>", parse_mode='html')
                if stop_number == "2":
                    state1 = False
                    await event.respond("<b>ᤋуᥰᥙнᥱн᧐</b>", parse_mode='html')

        @self.client.on(events.NewMessage(pattern='/menu'))
        async def command_help_commands(event):
            if str(event.message.sender_id) == admin_id:
                ph = 'https://x0.at/eJ0P.mp4'
                chat_id = event.chat_id
                me = await self.client.get_me()
                await self.client.send_file(chat_id, ph, caption='<b>ᎳᎪᏒᏒᎬN࿕ᎳᎪᏒᏒᏆᏫᏒ࿕ᏴᏫᎢ\nκ᧐ⲙᥲндᥙ д᧘я κ᧐ρᥙᥴᴛуʙᥲння δ᧐ᴛ᧐ⲙ:\n\n<code>/terror</code> + ᥲᥔді κ᧐нɸᥱρᥱнції: ʙⲙᥙκᥲє ᥴᥰᥲⲙ ᴛᥱκᥴᴛ᧐ⲙ\n<code>/mterror</code> + ᥲᥔді κ᧐нɸᥱρᥱнції: ʙⲙᥙκᥲє ᥴᥰᥲⲙ ᴛᥱκᥴᴛ + ⲙᥱдіᥲ\n<code>/time</code> ʙᥴᴛᥲн᧐ʙ᧘ює ᤋᥲᴛρᥙⲙκу\n<code>/media</code> + ᥴᥙ᧘κᥲ нᥲ ɸ᧐ᴛ᧐/ʙідᥱ᧐: ʙᥴᴛᥲн᧐ʙ᧘ює ⲙᥱдіᥲ\n<code>/text</code> ʙᥴᴛᥲн᧐ʙ᧘ює ɯᥲᥰκу\n<code>/uptime</code> ᥰ᧐κᥲᤋує ᥲᥰᴛᥲᥔⲙ δ᧐ᴛᥲ\n<code>/menu</code> ʙᥙκ᧘ᥙκᥲє ⲙᥱню δ᧐ᴛᥲ\n<code>/stop</code> ᤋуᥰᥙняє δ᧐ᴛᥲ ❲1 = ᤋʙᥙчᥲнᥙᥔ ρᥱжᥙⲙ, 2 = ⲙᥱдіᥲ ρᥱжᥙⲙ❳\n\nчᥲᴛ ᥲᥔді: <code>{}</code>\nᥲᥔді δ᧐ᴛᥲ: <code>{}</code>\nніκ: <code>{}</code>\nᴛᥱᴦ: @{}</b>'.format(chat_id, me.id, me.first_name, me.username), parse_mode='html')
    
    def start(self):
        self.client.run_until_disconnected()

if __name__ == "__main__":
    start_class = PydroidBot()
    start_class.run()
    start_class.start()