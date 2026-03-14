class wwGadgets:
    def __init__(self, model, compactness, processor, screen):
        self.model = model
        self.compactness = compactness
        self.processor = processor
        self.screen = screen

    def take_night_photo(self):
        print(f"{self.model} снимает ночное фото!")

    def work_all_day(self):
        print(f"{self.model} работает весь день!")


class Samsung_S23(wwGadgets):
    def __init__(self):
        super().__init__(
            model="Samsung S23",
            compactness="компактный корпус",
            processor="Snapdragon 8 Gen 2",
            screen="6.1 дюйм"
        )
        self.memory = "8 ГБ"

    def take_standard_photo(self):
        print("Samsung S23 снимает стандартное фото!")

    def fast_charge(self):
        print("Samsung S23 быстро заряжается!")


class Samsung_S25(wwGadgets):
    def __init__(self):
        super().__init__(
            model="Samsung S25",
            compactness="тонкий корпус",
            processor="Snapdragon 8 Elite",
            screen="6.2 дюйм"
        )
        self.ai_power = "мощность нейросетей"
        self.memory = "12 ГБ"

    def ai_photo(self):
        print("Samsung S25 дорисовывает фото через ИИ!")

    def instant_translate(self):
        print("Samsung S25 мгновенно переводит голос!")


class Iphone_17_Pro_Max(wwGadgets):
    def __init__(self):
        super().__init__(
            model="iPhone 17 Pro Max",
            compactness="титановый корпус",
            processor="Apple A19 Pro",
            screen="6.9 дюйм"
        )
        self.zoom = "супер-зум 8х"
        self.armor = "броня из титана"

    def shoot_hollywood_video(self):
        print("iPhone 17 Pro Max снимает голливудское видео!")

    def battery_two_days(self):
        print("iPhone 17 Pro Max держит заряд 2 дня!")
