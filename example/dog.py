import machine
import ssd1306
import framebuf

i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4))
i2c.scan()
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

with open("dog.pbm", 'rb') as f:
    f.readline()
    f.readline()
    data = bytearray(f.read())
fbuf = framebuf.FrameBuffer(data, 64, 64, framebuf.MONO_HLSB)
oled.blit(fbuf,0, 0)
    
oled.show()