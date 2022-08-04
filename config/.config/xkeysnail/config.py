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

    K('APOSTROPHE'): {                  # '
        # Alternative for bracket
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
    }
})



    # Alternative for numbers
    K("/-w"): K("1"),
    K("/-e"): K("2"),
    K("/-r"): K("3"),
    K("/-s"): K("4"),
    K("/-d"): K("5"),
    K("/-f"): K("6"),
    K("/-x"): K("7"),
    K("/-c"): K("8"),
    K("/-v"): K("9"),
    K("/-g"): K("0"),
})

# [Conditional modmap] Change modifier keys in certain applications
define_conditional_modmap(re.compile(r'Emacs'), {
    Key.RIGHT_CTRL: Key.ESC,
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

# Emacs-like keybindings in non-Emacs applications
define_keymap(lambda wm_class: wm_class not in ("Emacs", "URxvt"), {
    # Cursor
    K("C-b"): with_mark(K("left")),
    K("C-f"): with_mark(K("right")),
    K("C-p"): with_mark(K("up")),
    K("C-n"): with_mark(K("down")),
    K("C-h"): with_mark(K("backspace")),
    # Forward/Backward word
    K("M-b"): with_mark(K("C-left")),
    K("M-f"): with_mark(K("C-right")),
    # Beginning/End of line
    K("C-a"): with_mark(K("home")),
    K("C-e"): with_mark(K("end")),
    # Page up/down
    K("M-v"): with_mark(K("page_up")),
    K("C-v"): with_mark(K("page_down")),
    # Beginning/End of file
    K("M-Shift-comma"): with_mark(K("C-home")),
    K("M-Shift-dot"): with_mark(K("C-end")),
    # Newline
    K("C-m"): K("enter"),
    K("C-j"): K("enter"),
    K("C-o"): [K("enter"), K("left")],
    # Copy
    K("C-w"): [K("C-x"), set_mark(False)],
    K("M-w"): [K("C-c"), set_mark(False)],
    K("C-y"): [K("C-v"), set_mark(False)],
    # Delete
    K("C-d"): [K("delete"), set_mark(False)],
    K("M-d"): [K("C-delete"), set_mark(False)],
    # Kill line
    K("C-k"): [K("Shift-end"), K("C-x"), set_mark(False)],
    # Undo
    K("C-slash"): [K("C-z"), set_mark(False)],
    K("C-Shift-ro"): K("C-z"),
    # Mark
    K("C-space"): set_mark(True),
    K("C-M-space"): with_or_set_mark(K("C-right")),
    # Search
    K("C-s"): K("F3"),
    K("C-r"): K("Shift-F3"),
    K("M-Shift-key_5"): K("C-h"),
    # Cancel
    K("C-g"): [K("esc"), set_mark(False)],
    # Escape
    K("C-q"): escape_next_key,
    # C-x YYY
    K("C-x"): {
        # C-x h (select all)
        K("h"): [K("C-home"), K("C-a"), set_mark(True)],
        # C-x C-f (open)
        K("C-f"): K("C-o"),
        # C-x C-s (save)
        K("C-s"): K("C-s"),
        # C-x k (kill tab)
        K("k"): K("C-f4"),
        # C-x C-c (exit)
        K("C-c"): K("C-q"),
        # cancel
        K("C-g"): pass_through_key,
        # C-x u (undo)
        K("u"): [K("C-z"), set_mark(False)],
    }
}, "Emacs-like keys")
