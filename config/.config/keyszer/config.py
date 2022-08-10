# define timeout for multipurpose_modmap
timeouts(multipurpose = 1)

# [Global modemap] swap LWin and LCtrl
modmap('swap left win and left ctrl', {
    Key.LEFT_META: Key.LEFT_CTRL,
    Key.LEFT_CTRL: Key.LEFT_META,
})

# create a new modifier, and use the keyboard key F24
Modifier("L_HYPER", aliases = ["LHyper"], key = Key.F24)
LHyper = Key.F24


multipurpose_modmap("default",
    # Enter is enter if pressed and immediately released...
    # ...but Right Control if held down and paired with other keys.
    {Key.APOSTROPHE : [Key.APOSTROPHE, LHyper]}
)

keymap(None, {
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

    K('LHyper-w'): Key.KEY_1,
    K('LHyper-e'): Key.KEY_2,
    K('LHyper-r'): Key.KEY_3,
    K('LHyper-s'): Key.KEY_4,
    K('LHyper-d'): Key.KEY_5,
    K('LHyper-f'): Key.KEY_6,
    K('LHyper-x'): Key.KEY_7,
    K('LHyper-c'): Key.KEY_8,
    K('LHyper-v'): Key.KEY_9,
    K('LHyper-g'): Key.KEY_0,

})
