from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from pynput.keyboard import Key, Controller
from imagens import imgs, descricao
from horarios import horarios, data_atual, data_amanha
from send2trash import send2trash

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_experimental_option("detach", True)
nav = webdriver.Chrome(options=options,service=ChromeService(ChromeDriverManager().install()))




## Passos Automação Mlabs ##

#1 Entrar no site do Mlabs ( https://appsocial.mlabs.io/ )

nav.get("https://appsocial.mlabs.io/")
sleep(3)

## LOGIN E SENHA

#2 Fazer Login ( Email / Senha / Submit Button )

nav.find_element(By.XPATH, '//*[@id="email"]').send_keys(input('Email do Mlabs: '))
sleep(2)
nav.find_element(By.XPATH, '//*[@id="password"]').send_keys(input('Senha do Mlabs: '))
sleep(2)
nav.find_element(By.XPATH,'//*[@id="btnSubmit"]/p/div').click()
sleep(5)

#3 Após Logado, Efetuar um click em "Agendar Post" dentro da Plataforma Mlabs

nav.get("https://appsocial.mlabs.io//schedules/new")
sleep(5)

keyboard = Controller()

def uploadingPost():
    #4 Efetuar click no Logo do Instagram(Cinza)
    nav.find_element(By.XPATH, "(//*[contains(@class, 'fa-instagram-rounded') and contains(@class, 'fa-social-icon-disabled') ])[last()]").click()
    sleep(1.5)

    #5 ALTERANDO DATA DA PUBLICAÇÃO
    nav.find_element(By.XPATH, "(//input[@placeholder='Data'])[last()]").send_keys(Keys.CONTROL,"a")
    sleep(2)
    nav.find_element(By.XPATH, "(//input[@placeholder='Data'])[last()]").send_keys(Keys.BACKSPACE)
    sleep(2)
    nav.find_element(By.XPATH, "(//input[@placeholder='Data'])[last()]").send_keys(data_amanha)
    sleep(1)

    #6 ALTERANDO HORÁRIO DA PUBLICAÇÃO
    nav.find_element(By.XPATH, "(//input[@placeholder='Hora'])[last()]").send_keys(Keys.CONTROL,"a")
    sleep(2)
    nav.find_element(By.XPATH, "(//input[@placeholder='Hora'])[last()]").send_keys(Keys.BACKSPACE)
    sleep(2)
    nav.find_element(By.XPATH, "(//input[@placeholder='Hora'])[last()]").send_keys(horarios[0])
    horarios.pop(0)
    sleep(1)

    #7 FAZENDO UPLOAD DA IMAGEM PARA O MLABS
    nav.find_element(By.XPATH, "(//label[contains(@for,'upload-photo')])[last()]").click()
    sleep(1.5)
    keyboard.type(imgs[0])
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    sleep(7)



        #8 PEGANDO A DESCRIÇÃO DA IMAGEM

    with open(imgs[0], 'r') as fp:
        fp = imgs[0].replace('.jpg', '.txt')
        with open(fp, 'r') as cd:
            a = cd.read(50)
            a = a.replace('@PsychedelicPicture', '@Psypicz')
            with open(fp, 'w') as cd:
                cd.write(a)
                imgs.pop(0)



    sleep(2)
    nav.find_element(By.XPATH, "(//div[@placeholder='Digite o seu texto'])[last()]").send_keys(Keys.CONTROL,"a")
    sleep(1.5)
    nav.find_element(By.XPATH, "(//div[@placeholder='Digite o seu texto'])[last()]").send_keys(Keys.ARROW_LEFT)
    sleep(1.5)
    nav.find_element(By.XPATH, "(//div[@placeholder='Digite o seu texto'])[last()]").send_keys(Keys.ENTER)
    sleep(1.5)
    nav.find_element(By.XPATH, "(//div[@placeholder='Digite o seu texto'])[last()]").send_keys(Keys.ARROW_UP)
    sleep(1.5)
    nav.find_element(By.XPATH, "(//div[@placeholder='Digite o seu texto'])[last()]").send_keys(a)
    sleep(4)


    #CONFIRMANDO AGENDAMENTO DE POST
    nav.find_element(By.XPATH, "(//i[contains(@class,'fa-calendar-check-o')])[last()]").click()
    sleep(6)
    nav.find_element(By.XPATH, "(//button[contains(@class,'confirm')])[last()]").click()
    sleep(6)
    nav.find_element(By.XPATH, "(//button[contains(@class,'confirm')])[last()]").click()
    sleep(6)



def addPost():
    #9 ADICIONANDO MAIS UM POST PARA COMEÇAR O LOOP
    qntdPost = int(input('Quantos posts irá agendar: '))
    sleep(2)
    for i in range(qntdPost):
        sleep(2)
        uploadingPost()


addPost()











