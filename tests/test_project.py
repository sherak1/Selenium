from pages.home_page import HomePage

def test_correct_login(driver):
    home_page = HomePage(driver)
    home_page.go_to()
    home_page.login("standard_user", "secrect_sauce")
    home_page.verification()
    home_page.add_two_products()
    home_page.click_icon()
    home_page.verification_your_cart()
    home_page.products_chart()
    home_page.click_checkout()
    home_page.your_information_title()
    home_page.the_fields_filling("Sanina", "Herak", "73000")
    home_page.verification_overview()
    home_page.verification_products_overview()
    home_page.finish_button()
    home_page.complete()
    home_page.menu_button()
    home_page.logout_button()
    home_page.verification_login_page()


