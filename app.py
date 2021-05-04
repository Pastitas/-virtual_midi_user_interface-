#!/bin/python3
import tkinter
import collections

from tkinter import *
from tkinter import ttk


class Sketchpad(Canvas):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.bind("<Button-1>", self.save_posn)
        self.bind("<B1-Motion>", self.add_line)

    def save_posn(self, event):
        self.lastx, self.lasty = event.x, event.y

    def add_line(self, event):
        self.create_line((self.lastx, self.lasty, event.x, event.y))
        self.save_posn(event)


class uigridblock(Button):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

    def toggle(self, event):
        self(
            switch_frame,
            text="Off",
            variable=switch_variable,
            indicatoron=False,
            value="off",
            width=10,
        )

class midigrid:
    def __init__(self, root):

        # This is a PoC of the basic data that each grid block is gonna have in it, this particularly is a 8X2 grid of blocks.
        # TODO This data structure should be part of a grid_block object, together with initialization.
        page = collections.OrderedDict()
        page = {
            1: {
                "label": "one",
                "ctrl_label": "default",
                "lv2_parameter_out": "none",
                "cc_in": 10,
                "channel_in": 1,
                "type": "switch",
                "value": "24",
                "options": {"on": 1, "off": 0},
            },
            2: {
                "label": "two",
                "ctrl_label": "default",
                "lv2_parameter_out": "none",
                "cc_in": 11,
                "channel_in": 1,
                "type": "switch",
                "value": "24",
                "options": {"on": 1, "off": 0},
            },
            3: {
                "label": "three",
                "ctrl_label": "default",
                "lv2_parameter_out": "none",
                "cc_in": 12,
                "channel_in": 1,
                "type": "switch",
                "value": "24",
                "options": {"on": 1, "off": 0},
            },
            4: {
                "label": "four",
                "ctrl_label": "default",
                "lv2_parameter_out": "none",
                "cc_in": 13,
                "channel_in": 1,
                "type": "switch",
                "value": "24",
                "options": {"on": 1, "off": 0},
            },
            5: {
                "label": "five",
                "ctrl_label": "default",
                "lv2_parameter_out": "none",
                "cc_in": 14,
                "channel_in": 1,
                "type": "switch",
                "value": "24",
                "options": {"on": 1, "off": 0},
            },
            6: {
                "label": "six",
                "ctrl_label": "default",
                "lv2_parameter_out": "none",
                "cc_in": 15,
                "channel_in": 1,
                "type": "switch",
                "value": "24",
                "options": {"on": 1, "off": 0},
            },
            7: {
                "label": "seven",
                "ctrl_label": "default",
                "lv2_parameter_out": "none",
                "cc_in": 16,
                "channel_in": 1,
                "type": "switch",
                "value": "24",
                "options": {"on": 1, "off": 0},
            },
            8: {
                "label": "eight",
                "ctrl_label": "default",
                "lv2_parameter_out": "none",
                "cc_in": 17,
                "channel_in": 1,
                "type": "switch",
                "value": "24",
                "options": {"on": 1, "off": 0},
            },
            9: {
                "label": "nine",
                "ctrl_label": "default",
                "lv2_parameter_out": "none",
                "cc_in": 18,
                "channel_in": 1,
                "type": "switch",
                "value": "24",
                "options": {"on": 1, "off": 0},
            },
            10: {
                "label": "ten",
                "ctrl_label": "default",
                "lv2_parameter_out": "none",
                "cc_in": 19,
                "channel_in": 1,
                "type": "switch",
                "value": "24",
                "options": {"on": 1, "off": 0},
            },
            11: {
                "label": "eleven",
                "ctrl_label": "default",
                "lv2_parameter_out": "none",
                "cc_in": 20,
                "channel_in": 1,
                "type": "switch",
                "value": "24",
                "options": {"on": 1, "off": 0},
            },
            12: {
                "label": "twelve",
                "ctrl_label": "default",
                "lv2_parameter_out": "none",
                "cc_in": 21,
                "channel_in": 1,
                "type": "switch",
                "value": "24",
                "options": {"on": 1, "off": 0},
            },
            13: {
                "label": "thirteen",
                "ctrl_label": "default",
                "lv2_parameter_out": "none",
                "cc_in": 22,
                "channel_in": 1,
                "type": "switch",
                "value": "24",
                "options": {"on": 1, "off": 0},
            },
            14: {
                "label": "fourteen",
                "ctrl_label": "default",
                "lv2_parameter_out": "none",
                "cc_in": 23,
                "channel_in": 1,
                "type": "switch",
                "value": "24",
                "options": {"on": 1, "off": 0},
            },
            15: {
                "label": "fifteen",
                "ctrl_label": "default",
                "lv2_parameter_out": "none",
                "cc_in": 24,
                "channel_in": 1,
                "type": "switch",
                "value": "24",
                "options": {"on": 1, "off": 0},
            },
            16: {
                "label": "sixteen",
                "ctrl_label": "default",
                "lv2_parameter_out": "none",
                "cc_in": 25,
                "channel_in": 1,
                "type": "switch",
                "value": "24",
                "options": {"on": 1, "off": 0},
            },
        }

        root.title("midigrid")
        root.resizable(FALSE, FALSE)
        content = ttk.Frame(root)
        content.grid(column=1, row=1, rowspan=2, columnspan=8)
        ui_grid_blocks = []
        for grid_block in page:
            ui_grid_blocks.append(
                ttk.Labelframe(
                    root,
                    borderwidth=2,
                    relief="solid",
                    height=40,
                    width=40,
                    text=page[grid_block]["label"],
                )
            )
        colpos = 0
        rowpos = 0
        for ui_grid_block in ui_grid_blocks:
            ui_grid_block.grid(column=colpos, row=rowpos, sticky=(N, W, E, S))
            colpos += 1
            if colpos == ((len(ui_grid_blocks) / 2)):
                rowpos += 1
                colpos = 0
            # s = Sketchpad(ui_grid_block, borderwidth=0, height=100, width=100)
            s = uigridblock(ui_grid_block, borderwidth=0,)
            s.grid(column=colpos, row=rowpos, sticky=(N, W, E, S))

        for child in root.winfo_children():
            child.grid_configure(padx=10, pady=10)


root = Tk()
midigrid(root)
root.mainloop()
