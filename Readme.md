**The idea:**
A virtual midi controller - *wait, what?*

You all know the applications for configuring the controls of a midi controller, for example the Korg nanokontrol2.
I the app you specify the following for each knob/slider/button:

* midi channel
* midi cc
* range (sometimes)

The idea is, by using the screen, creating a configurable midi controller grid, like this one

> ![UI Design](/doc/media/Ui.png)
>
>
>
> For each parameter there are 4 control types:
>
>
>
> * Slider: a normal slider, akin to what we have today
> * Pan slider: same, but with the 0 value in the center
> * Switch: pretty self explanatory, defaults to on/off but can be changed
> * List: Has a list of values that you choose from, I’m still debating if this should be shown in the screen in the order you scroll through as a popup with all the options or keep it simple and tiny.

So, basically, to create a midi router with a live display of parameters that can be controlled with (in the case of the picture above) a 16 control hardware midi controller but control (16 parameters x 4 pages) 64 parameters of a synth engine.
Kinda what the encoder controllers do, in that you have 4 controls for each layer parameter page, and then you have an N number of pages for the total number of parameters of the engine, but user configurable , addressable with midi (without interfering with the navigation controls) and with the option to show more parameters.

The idea (for the default config at least) is that the hardware midi controller is configured with a static midi config (ie midi controller knob no1 is on channel 1 cc 1, knob 2 on channel 1 cc2, etc), and, by changing pages, you can change what each control does. If you where to exit the screen entirely, the controls stay mapped to the last page you had selected, so that you can edit the engine even if it’s not in sight.
