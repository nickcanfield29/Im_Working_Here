import time

import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import pyautogui


############STATS VARIABLES
global time_started

global times_ran
times_ran = 0

global tabs_ran_through
tabs_ran_through = 0

global type_count
type_count = 0

global click_count
click_count = 0


#############SLEEP VARIABLES
global sleep_max_range_seconds
sleep_max_range_seconds = 15

global sleep_max_range_seconds_action
sleep_max_range_seconds_action = 2

global sleep_max_range_switch_pages
sleep_max_range_switch_pages = 5

global sleep_click_max_seconds
sleep_click_max_seconds = 2

#############LIST OF ELEMENTS TO CLICK ON
global list_of_html_elements
list_of_html_elements = [
    "h1",
    "h2",
    "h3",
    "p",
    "br"
]


global list_of_sentences
list_of_sentences = [
    "VBA work to find a job.",
    "Find me a job.",
    "Where can I find a element?",
    "Have you found the missing link?",
    "Vohn is the best.",
    "Where did my trousers go?",
    "Put another random sentence here.",
    "Find jobs",
    "Dude, where is my car?"
]

global x_screen_max
global x_screen_min

global y_screen_max
global y_screen_min



global path_chromedriver
path_chromedriver = "chromedriver.exe" #change this to be where your chrome driver is located



def move_mouse_and_click(x,y):

    try:
        print("Moving Mouse to Position | X: " + str(x) + " | Y:" + str(y))
        pyautogui.moveTo(x, y)
    except:
        print("Couldn't move mouse there")

    click_mouse()
    sleep_random_actions()

    x_cord = random.randrange(x_screen_min, x_screen_max)
    y_cord = random.randint(y_screen_min, y_screen_max)

    try:
        print("Moving Mouse to Position | X: " + str(x_cord) + " | Y:" + str(y_cord))
        pyautogui.dragRel(x_cord, y_cord)  # move mouse to this new coordinate
        sleep_random_actions()
    except:
        print("Couldn't move mouse there")

    click_mouse()


    x_cord = random.randrange(x_screen_min, x_screen_max)
    y_cord = random.randint(y_screen_min, y_screen_max)

    try:
        print("Moving Mouse to Position | X: " + str(x_cord) + " | Y:" + str(y_cord))
        pyautogui.dragTo(x_cord, y_cord)
    except:
        print("Couldn't drag mouse there")

    click_mouse()

    sleep_random_actions()


    x_cord = random.randint(0, 100)
    y_cord = random.randint(0, 100)
    try:
        print("Moving Mouse to Position | X: " + str(x_cord) + " | Y:" + str(y_cord))
        pyautogui.dragRel(x_cord, y_cord)
    except:
        print("Couldn't drag mouse there")

    click_mouse()


def click_mouse():

    try:
        print("Moving Mouse to Position | X: " + str(0) + " | Y:" + str(0))
        pyautogui.moveTo(x_screen_max/2, y_screen_max/2)
        print("Clicking on position | X: " + str(x_screen_max/2) + " | Y:" + str(y_screen_max/2))
        pyautogui.click()
    except:
        print("Big Error on Clicking Mouse!")

    number_of_clicks = random.randint(1, 5)

    if (random.randint(0, 10) >= 3):

        for num in range(0, number_of_clicks):
            print("Clicking...")
            try:
                pyautogui.click()
                time.sleep(.5)
            except:
                print("Couldn't click mouse there")


def scroll_mouse():

    try:
        go_down = random.randrange(-15, 0, 1)
        print("Scrolling mouse down # Clicks: " + str(go_down))
        pyautogui.scroll(go_down)  # scroll down
    except:
        print("Couldn't scroll down that far")

    sleep_random_actions()

    try:
        scroll_up = random.randint(0, 100)
        print("Scrolling mouse up # Clicks: " + str(scroll_up))
        pyautogui.scroll(scroll_up)  # scroll up
    except:
        print("Couldn't scroll up that far")


def get_to_your_pages():

    if len(path_chromedriver) == 0:
        print("ERROR!")
        print("Please download the Selenium Chromedriver and put the .exe filepath in the global variable spot above.")
        exit()

    global browser
    browser = webdriver.Chrome(path_chromedriver)

    # open Google as a base page
    browser.get("https://www.google.com")


def switch_pages(window):

        time_switchpages = random.randrange(3, sleep_max_range_switch_pages)
        print("Sleeping for " + str(time_switchpages) + " seconds...")
        time.sleep(time_switchpages)

        browser.switch_to.window(window)
        print("Switched to tab " + browser.current_url)


def print_stats():

    print("********Stats Time************")
    print("!")
    print("Times Ran: " + str(times_ran))
    print("Tabs Shuffled: " + str(tabs_ran_through))
    print("Click Count: " + str(click_count))
    print("Type Count: " + str(type_count))
    time_ran = round(((time.time() - time_started)/60), 1)
    print("Time Ran (Min): " + str(time_ran))
    print("*****************************")



def sleep_random_actions():

    sleep_timer = random.randrange(0, sleep_max_range_seconds_action)
    print("Sleeping for " + str(sleep_timer) + " seconds before next action")
    time.sleep(sleep_timer)



def type_random_sentence():

    global list_of_sentences
    length_of_list = len(list_of_sentences)

    random_sentence = list_of_sentences[random.randrange(0, length_of_list-1)]

    try:

        print("Typing sentence" + random_sentence)
        pyautogui.write(random_sentence, interval=0.25)

        global type_count
        type_count = type_count + 1

        sleep_random_actions()

    except:
        print("Coulnd't type sentence " + random_sentence)



def click_tab():

    # Try clicking Tab
    try:
        count = 0
        click_number = random.randrange(1, 4)

        print("Tabbing...")
        while count <= click_number:

            print("Pressing tab key down")
            pyautogui.press('tab')  # press the Enter key
            print("Tab key pressed down")

            count = count + 1
            print("Tab Press # " + str(count))

            global click_count
            click_count = click_count + 1
            sleep_random_actions()


        print("Pressed the Tab button " + str(count) + " times")

    except:
        print("Couldn't press tab on keyboard")



def click_control():

    # Try clicking Control
    try:

        count = 0
        click_number = random.randrange(1, 4)

        print("Pressing Control...")

        while count <= click_number:

            pyautogui.press('control')  # press the Enter key

            count = count + 1

            global click_count
            click_count = click_count + 1
            sleep_random_actions()

        print("Pressed the Control button " + str(count) + " times")

    except:
        print("Couldn't press Control on keyboard")


def move_mouse_click_element():

    length_of_objects_list = len(list_of_html_elements)
    random_selection = random.randrange(0, length_of_objects_list - 1)

    tag_selection = list_of_html_elements[random_selection]

    global browser
    action = webdriver.ActionChains(browser)

    try:

        print("Getting the " + tag_selection + " Tags")
        tags = browser.find_elements_by_tag_name(tag_selection)

        for tag in tags:

            #Try clicking on element
            try:

                sleep_random_actions()
                print("Clicking on the " + tag_selection + " Tag")
                action.move_to_element_with_offset(tag)
                action.perform()

                count = 0
                click_number = random.randrange(1, 4)

                print("Clicking on the " + tag_selection + " tags")

                while count <= click_number:

                    action.click()
                    action.perform()

                    count = count + 1
                    click_count = click_count + 1

                print("Finished Clicking on the " + tag_selection + " tag")

            except:

                print("Couldn't click on element " + tag.text)

    except:
        print("Couldn't get the tags")



def run_program():

    global x_screen_max
    x_screen_max = .8*pyautogui.size()[0]
    global y_screen_max
    y_screen_max = .8*pyautogui.size()[1]

    global x_screen_min
    x_screen_min = .2*pyautogui.size()[0]
    global y_screen_min
    y_screen_min = .2*pyautogui.size()[1]

    #Open Chrome and open up Google.com
    get_to_your_pages()

    print("Please login to all of your pages, and then enter y.")

    x = input("Ready to start tabbing? Enter 'y' if yes\n")

    if x == 'y' or x == 'Y':
        print("Okay. Let's do this")

        keep_running = True

        global times_ran
        times_ran = 0

        global tabs_ran_through
        tabs_ran_through = 0

        global time_started
        time_started = time.time()

        #Keeps Looping Forever until you shut off the program or close out the browser
        while keep_running == True:

            for window in browser.window_handles:

                switch_pages(window)

                if random.randrange(0, 10, 1) >= 3:
                    click_tab()

                if random.randrange(0, 10, 1) >= 3:
                    click_control()

                if random.randrange(0, 10, 1) >= 0:

                    x_cord = random.randint(x_screen_min, x_screen_max)
                    y_cord = random.randint(y_screen_min, y_screen_max)
                    move_mouse_and_click(x_cord, y_cord)

                if random.randrange(0, 10, 1) >= 0:
                    scroll_mouse()

                if random.randrange(0, 10, 1) >= 3:
                    type_random_sentence()

                tabs_ran_through = tabs_ran_through + 1

            times_ran = times_ran + 1

            print_stats()

    browser.close()



print("Program: Hey, I'm Werkin Here!")
print("Author: Nick Canfield")
print("Website: https://processzip.com")
print("License: MIT")
print("************************************")

run_program()