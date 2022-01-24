nyooom = 0
strip = neopixel.create(DigitalPin.P1, 15, NeoPixelMode.RGB)
strip.set_pixel_color(0, neopixel.colors(NeoPixelColors.RED))
strip.show()

def on_forever():
    basic.show_number(pins.analog_read_pin(AnalogPin.P0))
basic.forever(on_forever)

def on_forever2():
    global nyooom
    nyooom = pins.map(pins.analog_read_pin(AnalogPin.P0), 0, 100000, 0, 100000)
    basic.pause(nyooom)
    strip.rotate(1)
    strip.show()
basic.forever(on_forever2)
