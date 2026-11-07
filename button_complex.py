from button import Button

class ButtonComplex(Button):
    def __init__(self, pos_x = 0, pos_y = 0, text = "", method_clicked = lambda x: print("Button clicked!"), input_value = None):
        super().__init__(pos_x, pos_y, text)

        self.method_clicked = method_clicked
        self.input_value = input_value

    def click(self, pos):
        pos_x, pos_y = pos
        if self.is_selected(pos_x, pos_y):
            self.method_clicked(self.input_value)