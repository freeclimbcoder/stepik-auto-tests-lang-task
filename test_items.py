#import time


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_to_cart_button_is_displayed(browser):
    browser.get(link)
    #time.sleep(5)
    assert browser.find_element_by_class_name('btn-add-to-basket').is_displayed(), \
        'I see no btn-add-to-basket button'