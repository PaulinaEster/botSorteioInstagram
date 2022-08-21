from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time
import random

class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        firefoxProfile = webdriver.FirefoxProfile()
        firefoxProfile.set_preference("intl.accept_languages", "pt,pt-BR")
        firefoxProfile.set_preference("dom.webnotifications.enabled", False)
        self.driver = webdriver.Firefox(
            firefox_profile=firefoxProfile, executable_path="geckodriver"
        )

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com")
        time.sleep(6) 
        user_element = driver.find_element(By.NAME,"username")
        user_element.clear()
        user_element.send_keys(self.username)
        time.sleep(3)
        password_element = driver.find_element(By.NAME,"password")
        password_element.clear()
        password_element.send_keys(self.password)
        time.sleep(3)
        password_element.send_keys(Keys.RETURN)
        time.sleep(5)
        agora_nao = driver.find_element(By.CSS_SELECTOR ,".cmbtv")
        time.sleep(3)
        agora_nao.click()
        time.sleep(1)
        self.comente_nas_fotos_com_a_hashtag()

    def pega_numero_seguidores(self):
        driver = self.driver 
        driver.get("https://www.instagram.com/" + self.username + "/")
        time.sleep(3)
        infosPerfil = driver.find_element(By.CLASS_NAME, '_aa_7') #_ac2a
        time.sleep(2)
        output = infosPerfil.text.split('\n')
        output = output[1].split(' ')
        output = output[0].split(',')
        numero = int(output[0]+output[1])
        return int(numero)
    
    def pega_seguidores(self):
        users = []
        driver = self.driver
        arquivo = open("users.txt", 'a')
        arquivo = open("users.txt", "r")
        quantidade_seguidores = 0
        for line in arquivo.readlines():
            users.append(line)
        
        if(len(users) == 0):
            seguidores = []
            quantidade_seguidores = self.pega_numero_seguidores()
            driver.get("https://www.instagram.com/"+self.username+"/followers/")
            time.sleep(3)
            modal = driver.find_element(By.CSS_SELECTOR, '._aano')
            time.sleep(1)
            modal.click() 
            time.sleep(1)
            for i in range(int((quantidade_seguidores)/8)):
                driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
                time.sleep(1)
            seguidores = modal.find_elements(By.TAG_NAME, 'a')
            for i in range(len(seguidores)-1): 
                if(seguidores[i].text): 
                    users.append("@" + seguidores[i].text + " \n")
            print(len(users))
            arquivo = open("users.txt", 'a')
            arquivo.writelines(users)
            time.sleep(1)  
        print("usuarios retirados com sucesso")
        return users

    def comente_nas_fotos_com_a_hashtag(self):
        driver = self.driver  
        a = 0
        
        sorteio = 'https://www.instagram.com/p/ChZ7zdhLMj_/'     # link do sorteio
        sorteio01 = 'https://www.instagram.com/p/ChORwSJsqAQ/'
        sorteio_da_vez = sorteio #trocar aqui pro sorteio que deseja comentar
        time.sleep(1)
        
        comments = self.pega_seguidores() # pega os seus seguidores e retorna em uma lista
        time.sleep(5)
        
        driver.get(sorteio_da_vez)   #vai pro link do sorteio
        time.sleep(3) 
        
        # pega o formulario que tem a caixa para comentar
        form = driver.find_element(By.CSS_SELECTOR,'._aao9')
        time.sleep(1)
        
        # selecionar a caica input comentar
        # comment_input_box = form.find_element(By.CSS_SELECTOR,'._aaoc')
        # time.sleep(1)

        while (len(comments) >= 2):  #fazer bot rodar até comentar todos os seguidores, retirar seguidor da lista quando escolhido pro sorteio
            
            if(a == 6):
                a = 0
                driver.get("https://www.instagram.com")
                time.sleep(1)
                for i in range(random.randint(20, 60)):
                    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
                    time.sleep(random.randint(2, 5))
                driver.get(sorteio_da_vez)   #vai pro link do sorteio
                time.sleep(3) 
                
                # pega o formulario que tem a caixa para comentar
                form = driver.find_element(By.CSS_SELECTOR,'._aao9')
                time.sleep(1)
            
            
            
            time.sleep(1)
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            time.sleep(1)
            
            try: 
                
                comment_input_box = form.find_element(By.CSS_SELECTOR,'._aaoc') # selecionar a caica input comentar
                comment_input_box.clear() # limpa a caixa input
                time.sleep(1)
                
                # GERA COMENTARIOS
                pessoa_1 = random.choice(comments)    #escolhe uma pessoa aleatoria do seu perfil
                pessoa_2 = random.choice(comments)    #escolhe uma pessoa aleatoria do seu perfil
                pessoa_3 = random.choice(comments)    #escolhe uma pessoa aleatoria do seu perfil
                comments.remove(pessoa_1);            # remove a pessoa que ja foi escolhida (se n pode repetir pessoas)
                comments.remove(pessoa_2);            # remove a pessoa que ja foi escolhida (se n pode repetir pessoas)
                comments.remove(pessoa_3);            # remove a pessoa que ja foi escolhida (se n pode repetir pessoas)
                marcar_3_pessoas = pessoa_1 + " " + pessoa_2 + " " + pessoa_3 + " " # texto caso tenham 2 pessoas pra marcar
                marcar_1_pessoas = pessoa_1 + " "  # texto caso tenha 1 pessoa pra marcar

                # FAZ O COMENTARIO
                if sorteio_da_vez == sorteio:
                    comment_input_box.send_keys(marcar_3_pessoas)
                    print("Comentei: ", marcar_3_pessoas, " no post: ", sorteio_da_vez, "")
                    time.sleep(2)
                    
                elif sorteio_da_vez == sorteio01:
                    comment_input_box.send_keys("OK")
                    print("Comentei: no post: ", sorteio_da_vez, "")
                    time.sleep(2)
                    
                time.sleep(1)
                form.find_element(By.CSS_SELECTOR, '._acan').click()
                time.sleep(2)
                
                a = a + 1 
                print('Vezes comentadas:', a)      
                time.sleep(random.randint(20, 40)) #espera 30 segundos pra comentar outra vez
            except Exception as e:
                print(e)
                time.sleep(5)
    

# Entre com o usuário e senha aqui
botSorteio = InstagramBot("USER", "PASS")
botSorteio.login()
 