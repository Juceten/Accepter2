from PIL import Image
import keyboard, pyautogui, time, math, logging, json

class Accepter():
    __confidence = 0.7
    
    def __init__(self):
        with open("app/settings.json", "r") as f:
            settings = json.load(f)
        self.__r_buttons = ['app/assets/resized-one.png', 'app/assets/resized-two.png']
        self.__settings = settings
        self.__scale = {
            '4:3' : [(1280,960) , ('app/assets/f1.png','app/assets/f2.png')],
            '16:9' : [(3840, 2160) , ('app/assets/s1.png','app/assets/s2.png')],
            '16:10' : [(1680,1050) , ('app/assets/t1.png','app/assets/t2.png')],
            '5:4' : [(1280,1024) , ('app/assets/b1.png','app/assets/b2.png')]
        }
        self.__override_list=[1280,1360,1366,1600,1920,2715,3840]
        self.__resolution = []
        self.__aspect_ratio = ""
        self.__prop = None
        self.__getInfo()
            
    def __getInfo(self):
            resolution = list(pyautogui.size())
            if resolution != self.__resolution:
                gcd = math.gcd(resolution[0], resolution[1])
                self.__resolution, self.__aspect_ratio = resolution, f"{int(resolution[0]/gcd)}:{int(resolution[1]/gcd)}"
                logging.debug(f"real aspect:{self.__aspect_ratio}")
                if resolution[0] in self.__override_list:
                    self.__aspect_ratio = "16:9"
                elif self.__aspect_ratio not in self.__scale.keys():
                    self.__aspect_ratio = "16:10"
                self.__prop = resolution[0]/self.__scale[self.__aspect_ratio][0][0]
                logging.debug("info updated...")
                self.__updateButtons()
    
    def __updateButtons(self):
        buttons = [Image.open(self.__scale[self.__aspect_ratio][1][0]), Image.open(self.__scale[self.__aspect_ratio][1][1])]
        for i in range(2):
            resized_button = buttons[i].resize((math.floor(buttons[i].size[0] * self.__prop), math.floor(buttons[i].size[1] * self.__prop)))
            resized_button.save(self.__r_buttons[i])
        logging.debug("buttons updated...")

    def __checkForAccept(self):
        for i in self.__r_buttons:
            if pyautogui.locateOnScreen(i, grayscale=True,confidence=self.__confidence) != None:
                return True, i
        return False, None

    def __acceptMatch(self, button):
        pixel = pyautogui.locateCenterOnScreen(button,grayscale=True,confidence=self.__confidence)
        pyautogui.moveTo(x=pixel[0],y=pixel[1])
        pyautogui.click()
        logging.info("Match accepted...")
        time.sleep(1)

    def start(self):
        logging.info(f'You can exit this script at any time by holding the "{self.__settings["quit_key"]}" key...')
        if self.__settings["close_on_accept"]:
            logging.info("This script will close automatically after accepting a match...")
        else:
            logging.info("This script must be manually closed...")
        on = 1
        while on and keyboard.is_pressed(self.__settings["quit_key"]) == False:
            self.__getInfo()
            self.__debugMsgs()
            check, button = self.__checkForAccept()
            if check == True:
                self.__acceptMatch(button)
                logging.debug("I see the button...")
                if self.__settings["close_on_accept"]:
                    on = 0
            time.sleep(1)

    def __debugMsgs(self):
        logging.debug(self.__resolution)
        logging.debug(self.__aspect_ratio)
        logging.debug(self.__prop)

if __name__ == "__main__":
    logging.basicConfig(format="%(asctime)s:%(levelname)s:%(message)s", datefmt="%D %T", level=logging.DEBUG)
    auto = Accepter()
    auto.start()
    