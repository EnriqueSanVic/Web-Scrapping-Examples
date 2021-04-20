# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import random
import time

option = webdriver.ChromeOptions()
option.add_experimental_option("excludeSwitches", ["enable-automation"])
option.add_experimental_option('useAutomationExtension', False)
option.add_argument('--disable-blink-features=AutomationControlled')
driver = webdriver.Chrome(executable_path='C:\Program Files (x86)\chromedriver.exe',options=option)
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

driver.execute_script("window.open()")

driver.switch_to.window(driver.window_handles[0])

class Servidor:
    
    zona=list()
    
    def __init__(self,pais,vec ):
        self.pais=pais
        self.zona=vec

cuenta = 'ejemploUsuario'
contra = 'ejemploContraseña1234'


def specific_string(length):  
    sample_string = 'qwertyuiopasdfghjklzxcvbnm' # define un ejemplo para generar cadenas random con una longitud pasada como argumento 
    # define the condition for random string  
    result = ''.join((random.choice(sample_string)) for x in range(length))    
    return result
    

def selector_paises(pais):
    
    
    if pais=='ARG': 
         driver.get("localhost/ARG.php") 
    elif pais=='BRA':
        driver.get("localhost/BRA.php") 
    elif pais=='COL':
        driver.get("localhost/COL.php") 
    elif pais=='DEU':
        driver.get("localhost/DEU.php") 
    elif pais=='ESP':
        driver.get("localhost/ESP.php") 
    elif pais=='FRA':
        driver.get("localhost/FRA.php") 
    elif pais=='ITA':
        driver.get("localhost/ITA.php")   
    elif pais=='MAG':
        driver.get("localhost/MAG.php") 
    elif pais=='MEX':
        driver.get("localhost/MEX.php") 
    elif pais=='NED':
        driver.get("localhost/NED.php")  
    elif pais=='POL':
        driver.get("localhost/POL.php") 
    elif pais=='POR':
        driver.get("localhost/POR.php") 
    elif pais=='ROM':
        driver.get("localhost/ROM.php") 
    elif pais=='SLO':
        driver.get("localhost/SLO.php") 
    elif pais=='SUO':
        driver.get("localhost/SOU.php") 
    elif pais=='SVE':
        driver.get("localhost/SVE.php") 
    elif pais=='TUR':
        driver.get("localhost/TUR.php") 
    elif pais=='USA':
        driver.get("localhost/USA.php") 
    elif pais=='UNI':
        driver.get("localhost/UNI.php") 
    elif pais=='CES':
        driver.get("localhost/CES.php") 
    elif pais=='PP1':
        driver.get("localhost/PP1.php") 
    elif pais=='PP2':
        driver.get("localhost/PP2.php") 
    elif pais=='PP3':
        driver.get("localhost/PP3.php") 
    elif pais=='PP4':
        driver.get("localhost/PP4.php") 
           

    
argentina = Servidor('ARG',['server1','server2','server3'])
brasil = Servidor('BRA',['server1','server2','server3','server4'])
deutschland = Servidor('DEU',['server1','server2'])
españa = Servidor('ESP',['server1','server2','server3','server4'])
france = Servidor('FRA',['server1','server2','server3','server4'])
italia = Servidor('ITA',['server1','server2','server3','server4'])
magyarország = Servidor('MAG',['server1','server2','brasov','server4'])
mexico = Servidor('MEX',['server1','server2','server3','server4'])
nederland = Servidor('NED',['server1'])
polska = Servidor('POL',['server1','server2','server3','server4'])
portugal = Servidor('POR',['server1','server2','server3'])
romania = Servidor('ROM',['server1','server2','server3','server4'])
slovensko = Servidor('SLO',['server1','server2'])
sverige = Servidor('SVE',['server1'])
turkiye = Servidor('TUR',['server1','server2','server3','server4'])
united = Servidor('UNI',['server1','server2'])
usa = Servidor('USA',['server1','server2','server3'])
ceska = Servidor('CES',['server1','server2','server3','server4'])
pp1 = Servidor('PP1',['server1','server2'])
pp2 = Servidor('PP2',['server1','server2','server3'])
pp3 = Servidor('PP3',['server1','server2','server3','server4'])
pp4 = Servidor('PP4',['server1'])


#argentina,brasil,deutschland,españa,france,italia,magyarország,mexico,nederland,polska,portugal,romania,slovensko,sverige,turkiye,ceska,pp1,united,pp2,pp3,pp4,usa

serv = [argentina,brasil,deutschland,españa,france,italia,magyarország,mexico,nederland,polska,portugal,romania,slovensko,sverige,turkiye,ceska,pp1,united,pp2,pp3,pp4,usa]


#Por alguna razón no funciona para Sverigue, aunque los pasos son correctos no valida los datos de entrada en el formulario de creación

driver.switch_to.window(driver.window_handles[1])
driver.get('localhost/emulatorNewAccount.php')

intentoEnUnServidor =0

for obj in serv:
    
    
    erc=0
    
    while True:
      
        
      if intentoEnUnServidor > 2:
            erc +=1
            intentoEnUnServidor=0
            print("ha sido imposible completar el registro de la última cuenta, pasamos al siguiente servidor")
            
      print("\n\n")
      if erc>=len(obj.zona):
          break
        
      print('Pais'+str(obj.pais)+' Zona: '+str(erc))
        
      try:
        
        cuenta = specific_string(8)
        
        
        guarda = [0] * 6
        
        guarda[0] = obj.pais
        guarda[1] = obj.zona[erc]
        guarda[2] = cuenta
        guarda[3] = contra
        
       
        driver.switch_to.window(driver.window_handles[1])
        
        driver.execute_script("location.reload(true);")
    
        nuevo_correo = driver.find_element_by_id('btn_new_tmp');
        nuevo_correo.click()
    
        afirmativo = driver.find_element_by_id('btn_new');
        afirmativo.click()
    
    
        time.sleep(4)
        correo = driver.find_element_by_id('span_mail').text;
        print('Correo: '+correo)
    
        
        driver.switch_to.window(driver.window_handles[0])
        
        selector_paises(obj.pais) #la funcion no lleva a la main page del pais
        
        time.sleep(2)
        
        driver.execute_script("location.reload(true);")
        
        inpu_name = driver.find_element_by_id('registerName')     
        inpu_name.send_keys(cuenta)
        
        inpu_mail = driver.find_element_by_id('registerEmail')     
        inpu_mail.send_keys(correo)
        
        inpu_pass = driver.find_element_by_id('registerPw')   
        inpu_pass.send_keys(contra)
        
        time.sleep(3)
        
        options = driver.find_element_by_xpath('//*[@id="serverOptions"]/a')   
        options.click()
        
        #modulo para escoger los nuevos condados
        
        
        inpu_lista = driver.find_element_by_id('registerServerServersChangeToOld')
        estilo= inpu_lista.get_attribute('style')
        
        print(estilo)
        
        
        
        estilo = estilo[17:len(estilo)]
        
        indice_1=estilo.index('display: ')
        indice_2=estilo.index(';')
        inf = estilo[indice_1+9:indice_2]
        
        print(inf)
        time.sleep(2)
        
        if inf=='none': 
            print("Ha entrado en new")
            try:
                cambiar_nuevos = driver.find_element_by_id('registerServerServersChangeToNew')  
                cambiar_nuevos.click()
            except: 
                cambiar_nuevos = driver.find_element_by_id('registerServerServersChangeToOld')  
                cambiar_nuevos.click()
        elif inf=='block':
            print("Ha entrado en block")
            try:
                
                cambiar_nuevos = driver.find_element_by_id('registerServerServersChangeToNew')  
                cambiar_nuevos.click()
            except: 
                pass
                
        elegir_lista = driver.find_element_by_id('registerServer')
        elegir_lista.send_keys(obj.zona[erc])
        
        print("\t>Sitio: "+obj.zona[erc])
        
        time.sleep(2)
        
        aceptar = driver.find_element_by_id('registerButton')   
        
        hover = ActionChains(driver).move_to_element(aceptar)
        hover.perform()
        time.sleep(0.5)
        aceptar.click()
       

        time.sleep(6)
        
        intentos=0
        ok = False
        while(ok==False):
        
            try:
                sel_char = driver.find_element_by_xpath('//*[@id="chooseRace"]/div[2]/div/div/table/tbody/tr/td[3]')
                sel_char.click() 
                ok=True
            except:
                
                intentos=intentos+1

                #estos clicks no tienen utilidad como tal es solo para que reaccione la verificacion por el bug detectado v2.3
                inpu_name.click()
                time.sleep(1)
                inpu_mail.click()
                time.sleep(1)
                inpu_pass.click()
                
                if intentos >1:
                    try:
                        elegir_lista.send_keys(obj.zona[erc-1])
                    except:
                        try:
                            elegir_lista.send_keys(obj.zona[erc+1])
                        except:
                            pass
                        
                    time.sleep(1)
                    
                elegir_lista.send_keys(obj.zona[erc])
                
                hover = ActionChains(driver).move_to_element(aceptar)
                hover.perform()
                time.sleep(0.5)
                aceptar.click()
                time.sleep(6)
                
                
                
            if intentos > 3:
                    ok = True
                    
                
        if intentos > 3:
            erc-=1
            intentoEnUnServidor += 1       
 
        else:
            intentoEnUnServidor = 0
        
            time.sleep(3)
        
            driver.switch_to.window(driver.window_handles[1])
        
            time.sleep(3)
        
            refrescar = driver.find_element_by_id('btn_refresh')
            refrescar.click()
            time.sleep(2)
        
        
            nuevo_mail = driver.find_element_by_xpath('//*[@id="list_mail"]/li[2]/a')
            nuevo_mail.click()
        
            time.sleep(3)
        
            ok = False
            intentos=0
            while(ok==False):
                intentos +=1
                try:
                    enlace = nuevo_mail = driver.find_element_by_xpath('//*[@id="mail_plain_body"]/a[1]')
                    enlace.click() 
                    ok=True
                except:
                    ir_hub = driver.find_element_by_id('btn_readmail_gohome')
                    ir_hub.click()
                
                    time.sleep(3)
            
                    refrescar = driver.find_element_by_id('btn_refresh')
                    refrescar.click()
                    time.sleep(2)
                    
                    if intentos > 5:
                        ok=True
        
                    nuevo_mail = driver.find_element_by_xpath('//*[@id="list_mail"]/li[2]/a')
                    nuevo_mail.click()
        
                    time.sleep(3)
            if intentos > 5:
                print("Repetir")
                erc -=1
                
            
            driver.switch_to.window(driver.window_handles[2])
            time.sleep(3)
    
            driver.refresh()
        
            time.sleep(3)
            #vamos a clasificacion
            clasi = driver.find_element_by_xpath('//*[@id="groupCharacter"]/li[7]')
            clasi.click()
            time.sleep(3)
            guarda[4] = driver.current_url
            guarda[5] = '2'
        
        
        
        
        
        
            driver.close() 
        
            driver.switch_to.window(driver.window_handles[1])
        
            ir_hub = driver.find_element_by_id('btn_readmail_gohome')
            ir_hub.click()
        
            #guardamos archivo
            ruta = 'cuentasaux/'+str(obj.pais)+'_'+str(obj.zona[erc])+'.txt'
        
            contenido =""
        
            for x in range(0,len(guarda)):
                contenido =contenido+str(guarda[x])+'\n'
            
            arch = open(ruta,'w',encoding='utf-8')
            arch.write(contenido)
        
            arch.close()
        
      except:
            pass
      erc+=1 
        
print('Fin del proceso')    