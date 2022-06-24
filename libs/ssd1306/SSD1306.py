############    Display informations    #############################
SSD1306_LCDWIDTH                    = 128
SSD1306_LCDHEIGHT                   = 64

############    Fundamental Commands    #############################
#set contrast control register
SSD1306_SETCONTRAST                 = 0x81
#Turn on the OLED panel resuming from previous display data or not
SSD1306_DISPLAYALLON_RESUME         = 0xA4
SSD1306_DISPLAYALLON                = 0xA5
#Set normal/inverse mode
SSD1306_NORMALDISPLAY               = 0xA6
SSD1306_INVERTDISPLAY               = 0xA7
#Set display ON/OFF(Sleep Mode)
SSD1306_DISPLAYON                   = 0xAF
SSD1306_DISPLAYOFF                  = 0xAE

#############   Scroll Command          #############################
#Set horizontal scrolling
SSD1306_SETSCROLL_HORIZONTAL_RIGHT  = 0x26
SSD1306_SETSCROLL_HORIZONTAL_LEFT   = 0x27
#Set vertical and horizontal scrolling
SSD1306_SETSCROLL_RIGHT             = 0x29
SSD1306_SETSCROLL_LEFT              = 0x2A
#Activate/Deactivate scroll
SSD1306_ACTIVATE_SCROLL             = 0x2E
SSD1306_DEACTIVATE_SCROLL           = 0x2F
#Set vertical scroll area
SSD1306_SET_VERTICAL_SCROLL_AREA    = 0xA3

#############   Addressing Setting Commands ########################
#Set memory addressing mode
SSD1306_MEMORYMODE                  = 0x20
#Set column address (only for horizontal or vertical addressing mode)
SSD1306_COLUMNADDR                  = 0x21
#Set page address (only for horizontal or vertical addressing mode)
SSD1306_PAGEADDR                    = 0x22

#############   Hardware Configuration Commands ####################
#Set Segment Remap
SSD1306_SEGREMAP                    = 0xA0
SSD1306_SEGREMAP_LAST               = 0xA1
#Set multiplex ratio
SSD1306_SET_MULTIPLEX               = 0xA8
#Set COM Output Scan Direction
SSD1306_COMSCANDEC                  = 0xC8
SSD1306_COMSCANINC                  = 0xC0
#Set display offset
SSD1306_SET_DISPLAY_OFFSET          = 0xD3
#Set COM Pins Hardware Configuration
SSD1306_SETCOMPINS                  = 0xDA
#Charge Pump Setting
SSD1306_CHARGEPUMP                  = 0x8D
#Set stert line to 0, you can set it from 0x40 to 0x7F to set it wherever you want
SSD1306_SETSTARTLINE_ZERO           = 0x40

#############   Timing & Driving Scheme Setting Command ############
#Set Display Clock Divide Ratio/oscillator frequency
SSD1306_SETDISPLAYCLOCKDIV          = 0xD5
#Set Pre-charge Period
SSD1306_SETPRECHARGE                = 0xD9
#Set VCOMH Deselect Level
SSD1306_SETVCOMDETECT               = 0xDB
#No Operation
SSD1306_NOP                         = 0xE3

SSD1306_SETLOWCOLUMN                = 0x00
SSD1306_SETHIGHCOLUMN               = 0x10

FONT_STANDARD={
    #-> LETTERS
    'A':[0X7E,0X09,0X09,0X7E,0X00],
    'B':[0X7F,0X49,0X49,0X36,0X00],
    'C':[0X3E,0X41,0X41,0X22,0X00],
    'D':[0X7F,0X41,0X41,0X3E,0X00],
    'E':[0X7F,0X49,0X49,0X41,0X00],
    'F':[0X7F,0X09,0X09,0X01,0X00],
    'G':[0X3E,0X41,0X51,0X32,0X00],
    'H':[0X7F,0X08,0X08,0X7F,0X00],
    'I':[0X41,0X7F,0X41,0X00],
    'J':[0X30,0X40,0X40,0X3F,0X00],
    'K':[0X7F,0X08,0X14,0X63,0X00],
    'L':[0X7F,0X40,0X40,0X40,0X00],
    'M':[0X7F,0X02,0X04,0X02,0X7F,0X00],
    'N':[0X7F,0X04,0X08,0X7F,0X00],
    'O':[0X3E,0X41,0X41,0X3E,0X00],
    'P':[0X7F,0X09,0X09,0X06,0X00],
    'Q':[0X3E,0X41,0X21,0X5E,0X00],
    'R':[0X7F,0X09,0X09,0X76,0X00],
    'S':[0X26,0X49,0X49,0X32,0X00],
    'T':[0X01,0X01,0X7F,0X01,0X01,0X00],
    'U':[0X3F,0X40,0X40,0X3F,0X00],
    'V':[0X1F,0X20,0X40,0X20,0X1F,0X00],
    'W':[0X7F,0X20,0X18,0X20,0X7F,0X00],
    'X':[0X77,0X08,0X08,0X77,0X00],
    'Y':[0X2F,0X48,0X48,0X3F,0X00],
    'Z':[0X71,0X49,0X49,0X47,0X00],
    #-> NUMBERS
    '1':[0x42,0x7F,0x40,0x00],
    '2':[0x62,0x51,0x49,0x46,0x00],
    '3':[0x22,0x49,0x49,0x36,0x00],
    '4':[0x0C,0x0A,0x09,0x7F,0x00],
    '5':[0x47,0x45,0x45,0x39,0x00],
    '6':[0x3C,0x4A,0x49,0x30,0x00],
    '7':[0x01,0x71,0x09,0x07,0x00],
    '8':[0x36,0x49,0x49,0x36,0x00],
    '9':[0x06,0x49,0x29,0x1E,0x00],
    '0':[0x3E,0x51,0x49,0x3E,0x00],
    #-> PUNCTUATION
    '.':[0x40,0x00],
    ',':[0x60,0x00],
    ';':[0x64,0x00],
    ':':[0x44,0x00],
    '*':[0x05,0x02,0x05,0x00],
    '+':[0x08,0x08,0x3E,0x08,0x08,0x00],
    '-':[0x08,0x08,0x08,0x08,0x08,0x00],
    '?':[0x02,0x51,0x09,0x06,0x00],
    '!':[0x5F,0x00],
    '&':[0x54,0x23,0x55,0x29,0x36,0x00],
    '(':[0X1C,0x22,0x41,0x00],
    ')':[0x41,0x22,0x1C,0X00],
    '[':[0X7F,0x41,0x41,0x00],
    ']':[0x41,0x41,0x7F,0X00],
    '{':[0X08,0x77,0x41,0x41,0x00],
    '}':[0x41,0x41,0x77,0x08,0X00],
    ' ':[0X00,0x00],
    '=':[0X14,0X14,0X14,0X00],
    '>':[0x41,0x22,0x14,0x08,0x00],
    '<':[0x08,0x14,0x22,0x41,0x00],
    '^':[0x04,0x02,0x09,0x25,0x95,0x25,0x09,0x02,0x04,0x00], #wifi acceso
    '@':[0x00,0x00,0x00,0x00,0xBF,0x00,0x00,0x00,0x00,0x00]  #wifi spento
}

import i2c

class SSD1306(i2c.I2c):
    """
    Class for SSD1306 OLED displays.
    Creates a new instance of the SSD1306 I2C display.
    Parameters:
        drvname (optional): The I2C bus to use. (default: I2C0)
        addr (optional): The address of the display. (default: 0x3C)
        clock (optional): The clock rate of the I2C bus. (default: 100000)
    """

    def __init__(self, addr=0x3c, drvname = I2C0, clock = 1000000):
        """
        Constructor
        """
        i2c.I2c.__init__(self, addr, drvname, clock)
        self.init()
        self.clear()

    def init(self):
        """
        Initialize the OLED display.
        No parameters.
        """
        init_sequence = [
            SSD1306_DISPLAYOFF,
            SSD1306_SETDISPLAYCLOCKDIV, 0x80,
            SSD1306_SET_MULTIPLEX, 0x3F,
            SSD1306_SET_DISPLAY_OFFSET, 0x00,
            SSD1306_SETSTARTLINE_ZERO,
            SSD1306_CHARGEPUMP, 0x14,
            SSD1306_MEMORYMODE, 0x00,
            SSD1306_SEGREMAP,
            SSD1306_COMSCANINC,
            SSD1306_SETCOMPINS, 0x12,
            SSD1306_SETCONTRAST, 0xCF,
            SSD1306_SETPRECHARGE, 0xF1,
            SSD1306_SETVCOMDETECT, 0x40,
            SSD1306_DISPLAYALLON_RESUME,
            SSD1306_NORMALDISPLAY,
            SSD1306_DISPLAYON,
            SSD1306_COLUMNADDR, 0x00, 0x7F,
            SSD1306_PAGEADDR, 0x00, 0x07,
        ]
        self._commandStream(init_sequence)

    def clear(self):
        """
        Clear the display.
        No parameters.
        """
        data = bytearray()
        self._setCursor(0, 0)
        for i in range(0xB0, 0xB8):
            for j in range(0, 1024):
                data.append(0x00)
            self._pixelStream(data)

    def clearBlue(self):
        """
        Clears the first 6 rows of the display.
        No parameters.
        """
        for i in range(0xB0, 0xB6):
            data = bytearray()
            self._setCursor(0, i)
            for j in range(0, 128):
                data.append(0x00)
            self._pixelStream(data)


    def printString(self, string, x = 0, y = 0, font = FONT_STANDARD):
        """
        Print a string on the display.
        Parameters:
            string: string to print
            x (optional): x coordinate
            y (optional): y coordinate
            font (optional): font to use
        """
        data = bytearray()
        string = string.upper()

        self._setCursor(x, y)

        for char in string:
            print(char)
            self._printChar(char, font)

    def printBitmap(self, bitmap, x = 0, y = 0, width = None, height = None):
        """
        Print a bitmap on the display.
        Parameters:
            bitmap: bitmap to print
            x (optional): x coordinate
            y (optional): y coordinate
            width (optional): width of the bitmap
            height (optional): height of the bitmap
        """
        data = bytearray()
        if width is None:
            width = len(bitmap[0])
        data = bytearray()
        if width is None:
            width = len(bitmap[0])
        if height is None:
            height = len(bitmap)
        self._createFrame(x, y, width, height)
        for i in range(0, height):
            for j in range(0, width):
                data.append(bitmap[i][j])
        self._pixelStream(data)

######################### Private methods, do not use or override unless you know what you are doing! #########################

    def _createFrame(self, x, y, width, height, border = False):
        """
        ***PRIVATE***
        Create a frame on the display.
        Parameters:
            x: x coordinate
            y: y coordinate
            width: width of the frame
            height: height of the frame
            border (optional): if True, a border is drawn
        """
        data = bytearray()
        self._commandStream(bytearray([SSD1306_COLUMNADDR, x, x + width - 1]))
        self._commandStream(bytearray([SSD1306_PAGEADDR, y, y + height - 1]))
        if not border: return
        for i in range(0, height):
            for j in range(0, width):
                if i == 0 or i == height - 1 or j == 0 or j == width - 1:
                    data.append(0xFF)
                else:
                    data.append(0x00)
        self._pixelStream(data)

    def _printChar(self, char, font):
        """
        ***PRIVATE***
        Print a character on the display.
        Parameters:
            char: character to print
            font: font to use
        """
        c = font.get(char, None)
        data = bytearray(c)
        self._pixelStream(data)

    def _setCursor(self, x, y):
        """
        ***PRIVATE***
        Set the cursor position.
        Parameters:
            x: x coordinate
            y: y coordinate
        """
        self._commandStream(bytearray([SSD1306_COLUMNADDR, x, 0x7F]))
        self._commandStream(bytearray([SSD1306_PAGEADDR, y, 0x07]))

    def _pixelStream(self, data):
        """
        ***PRIVATE***
        Send a stream of pixels to the display.
        Parameters:
            data: data to send
        """
        for d in data:
            self.write(bytearray([0x40, d]))

    def _commandStream(self, data):
        """
        ***PRIVATE***
        Send a stream of commands to the display.
        Parameters:
            data: data to send
        """
        for d in data:
            self.write(bytearray([0x00, d]))
