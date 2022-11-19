from flask import Flask, request, render_template


app = Flask(__name__)


@app.route('/',)
def page_index():

    page_content = """ 
    <h1>Бурлаков Степан Евгеньевич</h1>
    <img src="https://skitanie.com/wp-content/uploads/2022/01/obuchenie-it-spetsialnostyam.jpg" width=30%>
    <div><p><a href="https://minobr.75.ru/deyatel-nost/informaciya-dlya-postupayuschih/napravleniya-podgotovki/129116-programmist">Что слышно в имени твоем, Степан?:</a></p>
    <p><em>Степенность, степь, ступенчатость успеха.</em></p>
    <p><strong>Характер твой не даст попасть в «капкан».</strong></p>
    <p><mark>Твоя «степанность» в жизни — не помеха!</mark></p>
    <p>Ты запрягаешь медленно, но скачешь во всю прыть.</p>
    <p>Ты крайне редко делаешь ошибки.</p>
    <p>С тобой, Степан, в семье спокойно жить.</p>
    <p>А для жены твоей ты — «Золотая Рыбка»!</p>
    <p>Ее желанья для тебя — закон!</p>
    <p>С тех пор, как ты решил на ней жениться!</p>
    <p>То даришь ей манто, то купишь ей кулон,</p>
    <p>То в ломе сделаешь жену своей царицей!</p>
    <p>Таких, как ты в России очень мало!</p>
    <p>Ты просто клад для русских «степанид».</p>
    <p>Мы поднимаем за тебя бокалы:</p>
    <p>За твой успех и твой «степанный» вид!</p></div>
    """

    return page_content


app.run()
