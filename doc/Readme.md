https://discourse.zynthian.org/t/custom-ui-ambitions-or-maybe-some-day-the-controller-grid-page/5191

I got the core UI design concepts done and also some of the data structures, let’s start with the UI:

![UI Design](/doc/media/Ui.png)

There is a main grid with an X/Y grid of values (i find that for the official 3.2 inch screen 4x4 works, but it’s already the max) and Z pages (this can be arranged manually) that keeps each parameter binding in it’s own dict, and organizes them.

For each parameter there are 4 control types:

* Slider: a normal slider, akin to what we have today
* Pan slider: same, but with the 0 value in the center
* Switch: pretty self explanatory, defaults to on/off but can be changed
* List: Has a list of values that you choose from, I’m still debating if this should be shown in the screen in the order you scroll through as a popup with all the options or keep it simple and tiny.

Also for each parameter there is the following data:

* label (defaults to lv2-label)
* ctrl_label (user defined label, optional, helps with weird controller layouts)
* lv2_parameter_out (still researching about this)
* cc_in
* channel_in
* type (the ones listed above)
* options (if type = list or type=switch)

Now for the BIG question:

Should I build this as a separate application that would fit into the midi effects category, with it’s own UI and maybe set a new standard for “modules” or “plugins” for zynthian that have their own UI (this would also allow this “virtual midi controller” to run on any system that uses linux) using Kivy or tkinter (still deciding on this)?

**OR**

Should I build on top of what we already have, creating an option within the layers to show this interface if there is the json file for it?

Either of those would require me to write an editor application, which I would love to be able to have integrated in the webconf tool or run as a web app since that means cross compatibility (and then you copy your json file over to a certain folder.


# Next post

This turned out to be the way I keep notes in this proyect, so a lil update, mostly about decisions taken and some clarifications.

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

> Also for each parameter there is the following data:
>
>
>
> * label (defaults to lv2-label)
> * ctrl_label (user defined label, optional, helps with weird controller layouts)
> * lv2_parameter_out (still researching about this)
> * cc_in
> * channel_in
> * type (the ones listed above)
> * options (if type = list or type=switch)

Regarding how the tecnical details it would be a 3 dimension array (x/y/page) of the parameter data structure explained above, and that would act as the midi routing matrix. The idea is to use only one midi channel in for each instance of the control grid( be able to use current layer for example) so you could have 2 of the same hardware midi controller controlling 2 different synths by using 2 different midi channels

> Now for the BIG question:
>
>
>
> Should I build this as a separate application that would fit into the midi effects category, with it’s own UI and maybe set a new standard for “modules” or “plugins” for zynthian that have their own UI (this would also allow this “virtual midi controller” to run on any system that uses linux) using Kivy or tkinter (still deciding on this)?
>
>
>
> **OR**
>
>
>
> Should I build on top of what we already have, creating an option within the layers to show this interface if there is the json file for it?

I’ve settled on the following:
Developing a portable python app, and, when it’s functional, try to either make it into an lv2 plugin and integrate the interface with zynthian OR keep it standalone and integrate it with zynthian (yes, aswering a EITHER/OR with another EITHER/OR, I’m sure that’ll go well) In a way, zynthian already does this, but with the four encoders, so I don’t know if that’ll help with the integration efforts.

> Either of those would require me to write an editor application, which I would love to be able to have integrated in the webconf tool or run as a web app since that means cross compatibility (and then you copy your json file over to a certain folder.

This would make so if you have a bigger controller or screen and want more/less parameters on view, you are able to control that and the order in wich parameters appear, and also make it possible to arrange the parameters in pages with titles like FILTER, OSC, LFO, ENV etc so that they make more sense and are grouped together in a more meaningful way.

All this to say, I’ve been thinking a lot on this but not developing much. I hope I can bring you some :face_with_monocle: from this interface sooner rather than later.
