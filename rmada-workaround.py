import gradio as gr
import os
import json

from modules import scripts, script_callbacks, shared, sd_hijack

def on_ui_tabs():       
    return

script_callbacks.on_ui_tabs(on_ui_tabs)
