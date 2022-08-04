# -*- coding: utf-8 -*-

import re
from xkeysnail.transform import *

# define timeout for multipurpose_modmap
define_timeout(1)

# [Global modemap] swap LWin and LCtrl
define_modmap({
    Key.LEFT_META: Key.LEFT_CTRL,
    Key.LEFT_CTRL: Key.LEFT_META,
})

# Alternative for punctuation
# https://web.archive.org/web/20181111222712/https://mdickens.me/typing/letter_frequency.html
# https://web.archive.org/web/20181018014801/http://mtgap.bilfo.com/theory-of-letter-frequency.html
# Punctuation Frequency: , . - " _ ' ) ( ; = : / * ! ? $ > { } [ ] \ + | & < % @ # ^ ` ~
# Exclude some keys    : - _ ; = : * ! ? $ + & % @ # ^ ` ~
define_keymap(None, {
    # Alternative for punctuation
    K('SEMICOLON'): {                  # ;
        K('q'): K('Shift-KEY_1'),      # !
        K('w'): K('Shift-KEY_2'),      # @
        K('e'): K('Shift-KEY_3'),      # #
        K('r'): K('Shift-KEY_4'),      # $
        K('t'): K('Shift-KEY_5'),      # %
        K('a'): K('Shift-KEY_6'),      # ^
        K('s'): K('Shift-KEY_7'),      # &
        K('d'): K('Shift-KEY_8'),      # *
        K('f'): K('Shift-MINUS'),      # _
        K('g'): K('Shift-EQUAL'),      # +
        K('z'): K('MINUS'),            # -
        K('x'): K('EQUAL'),            # =
        K('c'): K('Shift-BACKSLASH'),  # ?
        K('v'): K('SEMICOLON'),        # ;
        K('b'): K('Shift-SEMICOLON'),  # :
    },

    # Alternative for bracket
    K('APOSTROPHE'): {                  # '
        K('e'): K('Shift-KEY_9'),       # (
        K('r'): K('Shift-KEY_0'),       # )
        K('d'): K('Shift-LEFT_BRACE'),  # {
        K('f'): K('Shift-RIGHT_BRACE'), # }
        K('c'): K('LEFT_BRACE'),        # [
        K('v'): K('RIGHT_BRACE'),       # ]
        K('t'): K('BACKSLASH'),         # /
        K('g'): K('Shift-SLASH'),       # |
        K('b'): K('SLASH'),             # \
        K('q'): K('APOSTROPHE'),        # '
        K('w'): K('Shift-APOSTROPHE'),  # "
        K('a'): K('GRAVE'),             # `
        K('s'): K('Shift-GRAVE'),       # ~
    },

    # Alternative for numbers
    K('BACKSLASH'): {                   # /
        K('w'): Key.KEY_1,
        K('e'): Key.KEY_2,
        K('r'): Key.KEY_3,
        K('s'): Key.KEY_4,
        K('d'): Key.KEY_5,
        K('f'): Key.KEY_6,
        K('x'): Key.KEY_7,
        K('c'): Key.KEY_8,
        K('v'): Key.KEY_9,
        K('g'): Key.KEY_0,
    },
})


# Keybindings for Firefox/Chrome
define_keymap(re.compile("Firefox|Google-chrome"), {
    # Ctrl+Alt+j/k to switch next/previous tab
    K("C-M-j"): K("C-TAB"),
    K("C-M-k"): K("C-Shift-TAB"),
    # Type C-j to focus to the content
    K("C-j"): K("C-f6"),
    # very naive "Edit in editor" feature (just an example)
    K("C-o"): [K("C-a"), K("C-c"), launch(["gedit"]), sleep(0.5), K("C-v")]
}, "Firefox and Chrome")

# Keybindings for Zeal https://github.com/zealdocs/zeal/
define_keymap(re.compile("Zeal"), {
    # Ctrl+s to focus search area
    K("C-s"): K("C-k"),
}, "Zeal")
