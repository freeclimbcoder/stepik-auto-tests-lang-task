#import time


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_isthere_a_(browser):
    browser.get(link)
    #time.sleep(5)
    assert browser.find_element_by_class_name('btn-add-to-basket').is_displayed(), \
        'Кнопка добавления товара в корзину отсутсвует'