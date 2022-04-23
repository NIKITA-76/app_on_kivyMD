from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

Window.size = (710, 500)


class ContainerBX(BoxLayout):
    size_font = 0
    Stopdot = False
    all_simbols = []
    int_simbols = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    plus_AndOther = ["+", "-", "*", "/"]
    plus_AndOtherStop = False
    stop_sizeFont = True

    def metricsAss(self,
                   Bin=False, Octal=False,
                   Hex=False, default=False,
                   BinTo=False, OctalTo=False,
                   HexTo=False, defaultTo=False):

        if BinTo == True:
            try:
                txt = str(self.input.text)
                main_result = int(txt, 2)
                print(main_result)
            except:
                self.output.text = "Error. Please check your details "

        if OctalTo == True:
            try:
                txt = str(self.input.text)
                main_result = int(txt, 8)
                print(main_result)
            except:
                self.output.text = "Error. Please check your details "

        if defaultTo == True:
            try:
                txt = str(self.input.text)
                main_result = int(txt)
                print(main_result)
            except:
                self.output.text = "Error. Please check your details "

        if HexTo == True:
            try:
                txt = str(self.input.text)
                main_result = int(txt, 16)
                print(main_result)
            except:
                self.output.text = "Error. Please check your details "

        if Bin == True:
            try:
                x = main_result
                n = ""
                while x > 0:
                    y = str(x % 2)
                    n = y + n
                    x = int(x / 2)
                self.output.text = n
            except:
                self.output.text = "Error. Please check your details "

        if Octal == True:
            try:
                num = int(main_result)
                base = 8

                newNum = ''

                while num > 0:
                    newNum = str(num % base) + newNum
                    num //= base

                self.output.text = newNum
            except:
                self.output.text = "Error. Please check your details "

        if default == True:
            try:
                num = int(main_result)
                base = 10

                newNum = ''

                while num > 0:
                    newNum = str(num % base) + newNum
                    num //= base

                self.output.text = newNum
            except:
                self.output.text = "Error. Please check your details "

        if Hex == True:
            try:
                num = int(main_result)
                base = 16

                newNum = ''

                while num > 0:

                    _num = str(num % base)
                    if _num == "10":
                        _num = "A"
                    if _num == "11":
                        _num = "B"
                    if _num == "12":
                        _num = "C"
                    if _num == "13":
                        _num = "D"
                    if _num == "14":
                        _num = "E"
                    if _num == "15":
                        _num = "F"
                    if _num == "16":
                        _num = "10"

                    newNum = _num + newNum

                    num //= base

                self.output.text = newNum
            except:
                self.output.text = "Error. Please check your details "

    def add_numbers(self, numbers, x=1, y=1):

        self.all_simbols.append(numbers)

        """Scale font_size"""
        # if len(self.display.text) % 9 <= 1 and self.stop_sizeFont == True:
        #    self.display.font_size -= 5
        #    self.size_font += 1
        #    if self.size_font >= 10:
        #        self.stop_sizeFont = False
        #        self.s = 1  # stoped write after MinSize

        if y == 0:
            self.display.text = self.display.text[:-1]

        if x == 0:
            self.display.font_size = 75
            self.stop_sizeFont = True
            self.size_font = 0
            self.s = 0

        if ((self.plus_AndOtherStop != True) or (self.all_simbols[-1] not in self.plus_AndOther)):
            self.plus_AndOtherStop = False

            if ((self.all_simbols[-1] != ".") or (
                    self.Stopdot == False and self.display.text != "Error")):
                self.display.text += str(numbers)

                print(self.all_simbols)

            if self.all_simbols[-1] not in self.int_simbols:

                if (self.all_simbols[-1] == "."):
                    self.Stopdot = True
                else:
                    self.Stopdot = False

            if self.all_simbols[-1] not in self.int_simbols:

                if (self.all_simbols[-1] in self.plus_AndOther):
                    self.plus_AndOtherStop = True
                else:
                    self.plus_AndOtherStop = False

        print(self.all_simbols)

    def main_operation(self, calculation, x=0):

        try:
            self.display.text = str(round((eval(calculation)), 2))
        except Exception:
            if (x == 1):
                self.display.text = ""
                x = 0
            else:
                self.display.text = "Error"


class CalculatorApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "DeepPurple"
        self.theme_cls.primary_hue = "400"
        self.theme_cls.theme_style = "Dark"

        return ContainerBX()


if __name__ == "__main__":
    CalculatorApp().run()