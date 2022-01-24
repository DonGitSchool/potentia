let nyooom = 0
let strip = neopixel.create(DigitalPin.P1, 15, NeoPixelMode.RGB)
strip.setPixelColor(0, neopixel.colors(NeoPixelColors.Red))
strip.show()
basic.forever(function () {
    basic.showNumber(pins.analogReadPin(AnalogPin.P0))
})
basic.forever(function () {
    nyooom = pins.map(
    pins.analogReadPin(AnalogPin.P0),
    0,
    100000,
    0,
    100000
    )
    basic.pause(nyooom)
    strip.rotate(1)
    strip.show()
})
