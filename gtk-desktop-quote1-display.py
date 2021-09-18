import gi
import json
import random
import threading
import time

gi.require_version("Gdk", "3.0")
gi.require_version("Gtk", "3.0")

from gi.repository import Gdk
from gi.repository import Gtk

# Display time in seconds (rough)
DISPLAY_TIME = 5
# Full path to the quotes dataset  https://www.kaggle.com/akmittal/quotes-dataset Download, unzip and refer to the location
#QUOTES_JSON_PATH = "/home/desktop-notifications/quotes.json" 

CSS = b"""
#toplevel {
    background-color: rgba(0, 0, 0, 0.1);
}
#mybox {
    margin: 20px;    
}
#main_content {
    color: white;
    font-size: 20px;
    font-weight:bold;
}
#other_content {
    color: white;
    font-size: 14px;
    font-style: italic;
}
"""



def load_quotes(quotes_json_path):
    with open(quotes_json_path) as f:
        return json.loads(f.read())

quotes = load_quotes('quotes1.json')

#print(quotes[0])
#print(quotes)
#Output: 
# {
#    'Quote': "Don't cry because it's over, smile because it happened.", 
#    'Author': 'Dr. Seuss',
#    'Tags': ['attributed-no-source', 'cry', 'crying', 'experience', 'happiness', 'joy', 'life', 'misattributed-dr-seuss', 'optimism', 'sadness', 'smile', 'smiling '], 
#    'Popularity': 0.15566615566615566,
#    'Category': 'life'
# }

random_quote_idx = random.randint(0, len(quotes))

quote_content = quotes[random_quote_idx]["quote"]
quote_author = quotes[random_quote_idx]["author"]

style_provider = Gtk.CssProvider()
style_provider.load_from_data(CSS)

Gtk.StyleContext.add_provider_for_screen(
    Gdk.Screen.get_default(),
    style_provider,
    Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
)

content_label = Gtk.Label(name="main_content")
content_label.set_text(quote_content)
content_label.set_justify(Gtk.Justification.CENTER)
content_label.set_max_width_chars(50)
content_label.set_line_wrap(True)

author_label = Gtk.Label(name="other_content")
author_label.set_text(quote_author)
author_label.set_justify(Gtk.Justification.CENTER)
author_label.set_max_width_chars(50)
author_label.set_line_wrap(True)
# author_label.set_size_request(250, -1)
box = Gtk.Box(name="mybox", orientation=Gtk.Orientation.VERTICAL)
box.pack_start(content_label, False, False, 0)
box.pack_end(author_label, False, False, 0)

window = Gtk.Window(title="", name="toplevel")
screen = window.get_screen()
visual = screen.get_rgba_visual()
window.set_visual(visual)
window.set_decorated(False)
window.add(box)

window.set_position(Gtk.WindowPosition.CENTER)
window.set_resizable(False)
window.connect("destroy", Gtk.main_quit)
window.show_all()

#def thread_function(name):
#   time.sleep(DISPLAY_TIME)
#    Gtk.main_quit()
#x = threading.Thread(target=thread_function, args=(1,))
#x.start()

Gtk.main()

x.join()
