from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest


class FunctionalTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome("C:\\Selenium\\chromedriver.exe")
        self.browser.implicitly_wait(2)

    def tearDown(self):
        self.browser.quit()

    def test_title(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Busco Ayuda', self.browser.title)

    def test_registro(self):
        self.browser.get('http://localhost:8000')
        link = self.browser.find_element_by_id('id_register')
        link.click()

        nombre = self.browser.find_element_by_id('id_nombre')
        nombre.send_keys('Juan Daniel')

        apellidos = self.browser.find_element_by_id('id_apellidos')
        apellidos.send_keys('Arevalo')

        experiencia = self.browser.find_element_by_id('id_aniosExperiencia')
        experiencia.send_keys('5')

        #self.browser.find_element_by_xpath(
        #    "//select[@id='id_tiposDeServicio']/option[text()='Desarrollador Web']").click()
        telefono = self.browser.find_element_by_id('id_telefono')
        telefono.send_keys('3173024578')

        correo = self.browser.find_element_by_id('id_correo')
        correo.send_keys('jd.patino1@uniandes.edu.co')

        imagen = self.browser.find_element_by_id('id_imagen')
        imagen.send_keys('C:\\Selenium\\developer.jpg')

        nombreUsuario = self.browser.find_element_by_id('id_username')
        nombreUsuario.send_keys('juan645')

        clave = self.browser.find_element_by_id('id_password')
        clave.send_keys('clave123')

        botonGrabar = self.browser.find_element_by_id('id_grabar')
        botonGrabar.click()
        self.browser.implicitly_wait(3)
        #span = self.browser.find_element(By.XPATH, '//span[text()="Juan Daniel Arevalo"]')

        #self.assertIn('Juan Daniel Arevalo', span.text)

    def test_ver_detalle(self):
        self.browser.get('http://localhost:8000')
        span=self.browser.find_element(By.XPATH, '//span[text()="Juan Daniel Arevalo"]')
        span.click()

        h2=self.browser.find_element(By.XPATH, '//h2[text()="Juan Daniel Arevalo"]')

        self.assertIn('Juan Daniel Arevalo', h2.text)

    def test_login(self):
        self.browser.get('http://localhost:8000')
        link = self.browser.find_element_by_id('id_login')
        link.click()

        self.browser.implicitly_wait(1)

        nombre = self.browser.find_element_by_id('id_username')
        nombre.send_keys('juan645')

        apellidos = self.browser.find_element_by_id('id_password')
        apellidos.send_keys('clave123')

        botonLogin = self.browser.find_element_by_id('id_login')
        botonLogin.click()

        self.browser.implicitly_wait(5)

        nombre = self.browser.find_element_by_id('id_name')
        self.assertIn('Juan Daniel Arevalo', nombre.text)

    def test_edit(self):
        self.browser.get('http://localhost:8000')
        link = self.browser.find_element_by_id('id_login')
        link.click()

        self.browser.implicitly_wait(1)

        nombre = self.browser.find_element_by_id('id_username')
        nombre.send_keys('juan645')

        apellidos = self.browser.find_element_by_id('id_password')
        apellidos.send_keys('clave123')

        botonLogin = self.browser.find_element_by_id('id_login')
        botonLogin.click()

        self.browser.implicitly_wait(5)

        botonEdit = self.browser.find_element_by_id('id_editar')
        botonEdit.click()

        self.browser.implicitly_wait(5)

        telefono = self.browser.find_element_by_id('id_telefono')
        telefono.send_keys('1234567')

        botonEdit = self.browser.find_element_by_id('id_save')
        botonEdit.click()

        self.browser.implicitly_wait(5)

        telefono = self.browser.find_element_by_id('id_telefono')
        self.assertIn('1234567', telefono.text)

    def test_add_comentario(self):
        self.browser.get('http://localhost:8000')
        span = self.browser.find_element(By.XPATH, '//span[text()="Juan Daniel Arevalo"]')
        span.click()

        self.browser.implicitly_wait(5)

        correo = self.browser.find_element_by_id('correo')
        correo.send_keys('prueba@prueba.com')

        comentario = self.browser.find_element_by_id('comentario')
        comentario.send_keys('Comentario de Prueba')

        botonAddComment = self.browser.find_element_by_id('id_comentario')
        botonAddComment.click()

        self.browser.implicitly_wait(2)

        mensaje_exitoso = self.browser.find_element_by_id('mensaje')
        self.assertIn('Se registró exitosamente su comentario.', mensaje_exitoso.text)


if __name__ == '__main__':
    unittest.main()
