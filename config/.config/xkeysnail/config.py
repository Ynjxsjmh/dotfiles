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
        K('w'): K('Shift-KEY_1'),      # !
        K('z'): K('Shift-KEY_2'),      # @
        K('g'): K('Shift-KEY_3'),      # #
        K('d'): K('Shift-KEY_4'),      # $
        K('t'): K('Shift-KEY_5'),      # %
        K('b'): K('Shift-KEY_6'),      # ^
        K('r'): K('Shift-KEY_7'),      # &
        K('a'): K('Shift-KEY_8'),      # *
        K('f'): K('Shift-MINUS'),      # _
        K('x'): K('Shift-EQUAL'),      # +
        K('v'): K('MINUS'),            # -
        K('e'): K('EQUAL'),            # =
        K('q'): K('Shift-SLASH'),      # ?
        K('s'): K('SEMICOLON'),        # ;
        K('c'): K('Shift-SEMICOLON'),  # :
    },

    # Alternative for bracket
    K('LEFT_BRACE'): {                  # [
        K('e'): K('Shift-KEY_9'),       # (
        K('r'): K('Shift-KEY_0'),       # )
        K('d'): K('LEFT_BRACE'),        # [
        K('f'): K('RIGHT_BRACE'),       # ]
        K('c'): K('Shift-LEFT_BRACE'),  # {
        K('v'): K('Shift-RIGHT_BRACE'), # }
        K('t'): K('SLASH'),             # /
        K('g'): K('Shift-SLASH'),       # |
        K('b'): K('BACKSLASH'),         # \
    },

    # Alternative for numbers
    K('APOSTROPHE'): {                  # '
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
        K('a'): K('APOSTROPHE'),        # ', Apostrophe
        K('q'): K('Shift-APOSTROPHE'),  # ",
        K('g'): K('GRAVE'),             # `, Grave
        K('t'): K('Shift-GRAVE'),       # ~, Tilde
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
