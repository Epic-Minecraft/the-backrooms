def New_Game2():
    global the_menu, New_Game
    has_name = 0
    the_menu = 2
    New_Game = miniMenu.create_menu(miniMenu.create_menu_item("Player look",
            img("""
                2 2 2 2 2 . . . . . . 2 2 2 2 2
                2 2 2 2 2 2 . . . . 2 2 2 2 2 2
                2 2 2 2 2 2 2 . . 2 2 2 2 2 2 2
                2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
                2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
                . 2 2 2 2 2 2 2 2 2 2 2 2 2 2 .
                . . 2 2 2 2 2 2 2 2 2 2 2 2 . .
                . . . 2 2 2 2 2 2 2 2 2 2 . . .
                . . . 2 2 2 2 2 2 2 2 2 2 . . .
                . . 2 2 2 2 2 2 2 2 2 2 2 2 . .
                . 2 2 2 2 2 2 2 2 2 2 2 2 2 2 .
                2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
                2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
                2 2 2 2 2 2 2 . . 2 2 2 2 2 2 2
                2 2 2 2 2 2 . . . . 2 2 2 2 2 2
                2 2 2 2 2 . . . . . . 2 2 2 2 2
                """)),
        miniMenu.create_menu_item("Name",
            img("""
                2 2 2 2 2 . . . . . . 2 2 2 2 2
                2 2 2 2 2 2 . . . . 2 2 2 2 2 2
                2 2 2 2 2 2 2 . . 2 2 2 2 2 2 2
                2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
                2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
                . 2 2 2 2 2 2 2 2 2 2 2 2 2 2 .
                . . 2 2 2 2 2 2 2 2 2 2 2 2 . .
                . . . 2 2 2 2 2 2 2 2 2 2 . . .
                . . . 2 2 2 2 2 2 2 2 2 2 . . .
                . . 2 2 2 2 2 2 2 2 2 2 2 2 . .
                . 2 2 2 2 2 2 2 2 2 2 2 2 2 2 .
                2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
                2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
                2 2 2 2 2 2 2 . . 2 2 2 2 2 2 2
                2 2 2 2 2 2 . . . . 2 2 2 2 2 2
                2 2 2 2 2 . . . . . . 2 2 2 2 2
                """)),
        miniMenu.create_menu_item("Game Start"))
    miniMenu.set_frame(New_Game,
        img("""
            3 3 3 3 3 5 5 5 5 5 9 9 9 9 9
            3 3 3 3 3 5 5 5 5 5 9 9 9 9 9
            3 3 3 3 3 5 5 5 5 5 9 9 9 9 9
            3 3 3 3 3 5 5 5 5 5 9 9 9 9 9
            3 3 3 3 3 5 5 5 5 5 9 9 9 9 9
            3 3 3 3 3 5 5 5 5 5 9 9 9 9 9
            3 3 3 3 3 5 5 5 5 5 9 9 9 9 9
            3 3 3 3 3 5 5 5 5 5 9 9 9 9 9
            3 3 3 3 3 5 5 5 5 5 9 9 9 9 9
            3 3 3 3 3 5 5 5 5 5 9 9 9 9 9
            3 3 3 3 3 5 5 5 5 5 9 9 9 9 9
            3 3 3 3 3 5 5 5 5 5 9 9 9 9 9
            3 3 3 3 3 5 5 5 5 5 9 9 9 9 9
            3 3 3 3 3 5 5 5 5 5 9 9 9 9 9
            3 3 3 3 3 5 5 5 5 5 9 9 9 9 9
            """))
    
    def on_button_pressed_a(selection, selectedIndex):
        if selectedIndex == 0:
            miniMenu.close(New_Game)
            Player_look_P1()
        elif selectedIndex == 1:
            miniMenu.close(New_Game)
            Name2()
        elif selectedIndex == 2:
            miniMenu.close(New_Game)
            new_Game_start()
    miniMenu.on_button_pressed(New_Game, miniMenu.Button.A, on_button_pressed_a)
    
    if Figur == 1:
        miniMenu.get_menu_item(New_Game, 0).set_icon(img("""
            . . . . . . f f f f . . . . . .
            . . . . f f f 2 2 f f f . . . .
            . . . f f f 2 2 2 2 f f f . . .
            . . f f f e e e e e e f f f . .
            . . f f e 2 2 2 2 2 2 e e f . .
            . . f e 2 f f f f f f 2 e f . .
            . . f f f f e e e e f f f f . .
            . f f e f b f 4 4 f b f e f f .
            . f e e 4 1 f d d f 1 4 e e f .
            . . f e e d d d d d d e e f . .
            . . . f e e 4 4 4 4 e e f . . .
            . . e 4 f 2 2 2 2 2 2 f 4 e . .
            . . 4 d f 2 2 2 2 2 2 f d 4 . .
            . . 4 4 f 4 4 5 5 4 4 f 4 4 . .
            . . . . . f f f f f f . . . . .
            . . . . . f f . . f f . . . . .
            """))
    elif Figur == 2:
        miniMenu.get_menu_item(New_Game, 0).set_icon(img("""
            . . . . . f f 4 4 f f . . . . .
            . . . . f 5 4 5 5 4 5 f . . . .
            . . . f e 4 5 5 5 5 4 e f . . .
            . . f b 3 e 4 4 4 4 e 3 b f . .
            . . f 3 3 3 3 3 3 3 3 3 3 f . .
            . f 3 3 e b 3 e e 3 b e 3 3 f .
            . f 3 3 f f e e e e f f 3 3 f .
            . f b b f b f e e f b f b b f .
            . f b b e 1 f 4 4 f 1 e b b f .
            f f b b f 4 4 4 4 4 4 f b b f f
            f b b f f f e e e e f f f b b f
            . f e e f b d d d d b f e e f .
            . . e 4 c d d d d d d c 4 e . .
            . . e f b d b d b d b b f e . .
            . . . f f 1 d 1 d 1 d f f . . .
            . . . . . f f b b f f . . . . .
            """))
    elif Figur == 3:
        miniMenu.get_menu_item(New_Game, 0).set_icon(img("""
            . f f f . f f f f . f f f .
            f f f f f c c c c f f f f f
            f f f f b c c c c b f f f f
            f f f c 3 c c c c 3 c f f f
            . f 3 3 c c c c c c 3 3 f .
            . f c c c c 4 4 c c c c f .
            . f f c c 4 4 4 4 c c f f .
            . f f f b f 4 4 f b f f f .
            . f f 4 1 f d d f 1 4 f f .
            . . f f d d d d d d f f . .
            . . e f e 4 4 4 4 e f e . .
            . e 4 f b 3 3 3 3 b f 4 e .
            . 4 d f 3 3 3 3 3 3 c d 4 .
            . 4 4 f 6 6 6 6 6 6 f 4 4 .
            . . . . f f f f f f . . . .
            . . . . f f . . f f . . . .
            """))
    elif Figur == 4:
        miniMenu.get_menu_item(New_Game, 0).set_icon(img("""
            . . . . f f f f . . . . .
            . . f f f f f f f f . . .
            . f f f f f f c f f f . .
            f f f f f f c c f f f c .
            f f f c f f f f f f f c .
            c c c f f f e e f f c c .
            f f f f f e e f f c c f .
            f f f b f e e f b f f f .
            . f 4 1 f 4 4 f 1 4 f . .
            . f e 4 4 4 4 4 4 e f . .
            . f f f e e e e f f f . .
            f e f b 7 7 7 7 b f e f .
            e 4 f 7 7 7 7 7 7 f 4 e .
            e e f 6 6 6 6 6 6 f e e .
            . . . f f f f f f . . . .
            . . . f f . . f f . . . .
            """))
    elif Figur == 5:
        miniMenu.get_menu_item(New_Game, 0).set_icon(img("""
            . . . . f f f f . . . .
            . . f f e e e e f f . .
            . f f e e e e e e f f .
            f f f f 4 e e e f f f f
            f f f 4 4 4 e e f f f f
            f f f 4 4 4 4 e e f f f
            f 4 e 4 4 4 4 4 4 e 4 f
            f 4 4 f f 4 4 f f 4 4 f
            f e 4 d d d d d d 4 e f
            . f e d d b b d d e f .
            . f f e 4 4 4 4 e f f .
            e 4 f b 1 1 1 1 b f 4 e
            4 d f 1 1 1 1 1 1 f d 4
            4 4 f 6 6 6 6 6 6 f 4 4
            . . . f f f f f f . . .
            . . . f f . . f f . . .
            """))
    elif Figur == 6:
        miniMenu.get_menu_item(New_Game, 0).set_icon(img("""
            . . . . . f f f f . . . . .
            . . . f f 5 5 5 5 f f . . .
            . . f 5 5 5 5 5 5 5 5 f . .
            . f 5 5 5 5 5 5 5 5 5 5 f .
            . f 5 5 5 d b b d 5 5 5 f .
            f 5 5 5 b 4 4 4 4 b 5 5 5 f
            f 5 5 c c 4 4 4 4 c c 5 5 f
            f b b f b f 4 4 f b f b b f
            f b b 4 1 f d d f 1 4 b b f
            . f b f d d d d d d f b f .
            . f e f e 4 4 4 4 e f e f .
            . e 4 f 6 9 9 9 9 6 f 4 e .
            . 4 d c 9 9 9 9 9 9 c d 4 .
            . 4 f b 3 b 3 b 3 b b f 4 .
            . . f f 3 b 3 b 3 3 f f . .
            . . . . f f b b f f . . . .
            """))
    elif Figur == 7:
        miniMenu.get_menu_item(New_Game, 0).set_icon(img("""
            . . . . . . . c c c . . . . . .
            . . . . . . c b 5 c . . . . . .
            . . . . c c c 5 5 c c c . . . .
            . . c c b c 5 5 5 5 c c c c . .
            . c b b 5 b 5 5 5 5 b 5 b b c .
            . c b 5 5 b b 5 5 b b 5 5 b c .
            . . f 5 5 5 b b b b 5 5 5 c . .
            . . f f 5 5 5 5 5 5 5 5 f f . .
            . . f f f b f e e f b f f f . .
            . . f f f 1 f b b f 1 f f f . .
            . . . f f b b b b b b f f . . .
            . . . e e f e e e e f e e . . .
            . . e b c b 5 b b 5 b f b e . .
            . . e e f 5 5 5 5 5 5 f e e . .
            . . . . c b 5 5 5 5 b c . . . .
            . . . . . f f f f f f . . . . .
            """))
    elif Figur == 0:
        miniMenu.get_menu_item(New_Game, 0).set_icon(img("""
            2 2 2 2 2 . . . . . . 2 2 2 2 2
            2 2 2 2 2 2 . . . . 2 2 2 2 2 2
            2 2 2 2 2 2 2 . . 2 2 2 2 2 2 2
            2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
            2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
            . 2 2 2 2 2 2 2 2 2 2 2 2 2 2 .
            . . 2 2 2 2 2 2 2 2 2 2 2 2 . .
            . . . 2 2 2 2 2 2 2 2 2 2 . . .
            . . . 2 2 2 2 2 2 2 2 2 2 . . .
            . . 2 2 2 2 2 2 2 2 2 2 2 2 . .
            . 2 2 2 2 2 2 2 2 2 2 2 2 2 2 .
            2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
            2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
            2 2 2 2 2 2 2 . . 2 2 2 2 2 2 2
            2 2 2 2 2 2 . . . . 2 2 2 2 2 2
            2 2 2 2 2 . . . . . . 2 2 2 2 2
            """))
    elif has_name == 0:
        miniMenu.get_menu_item(New_Game, 1).set_icon(assets.image("""
            Cross
            """))
    elif has_name == 1:
        miniMenu.get_menu_item(New_Game, 1).set_icon(assets.image("""
            Tick
            """))
def Name2():
    global the_menu, Player_name
    miniMenu.close(New_Game)
    the_menu = 4
    Player_name = miniMenu.create_menu(miniMenu.create_menu_item("Jack"),
        miniMenu.create_menu_item("Oliver"),
        miniMenu.create_menu_item("Timon"),
        miniMenu.create_menu_item("Olivia"),
        miniMenu.create_menu_item("Lily"))
    miniMenu.set_frame(Player_name,
        img("""
            3 3 3 3 3 5 5 5 5 5 9 9 9 9 9
            3 3 3 3 3 5 5 5 5 5 9 9 9 9 9
            3 3 3 3 3 5 5 5 5 5 9 9 9 9 9
            3 3 3 3 3 5 5 5 5 5 9 9 9 9 9
            3 3 3 3 3 5 5 5 5 5 9 9 9 9 9
            3 3 3 3 3 5 5 5 5 5 9 9 9 9 9
            3 3 3 3 3 5 5 5 5 5 9 9 9 9 9
            3 3 3 3 3 5 5 5 5 5 9 9 9 9 9
            3 3 3 3 3 5 5 5 5 5 9 9 9 9 9
            3 3 3 3 3 5 5 5 5 5 9 9 9 9 9
            3 3 3 3 3 5 5 5 5 5 9 9 9 9 9
            3 3 3 3 3 5 5 5 5 5 9 9 9 9 9
            3 3 3 3 3 5 5 5 5 5 9 9 9 9 9
            3 3 3 3 3 5 5 5 5 5 9 9 9 9 9
            3 3 3 3 3 5 5 5 5 5 9 9 9 9 9
            """))
    
    def on_button_pressed_a2(selection2, selectedIndex2):
        global fig_name
        if selectedIndex2 == 0:
            fig_name = 1
        elif selectedIndex2 == 1:
            fig_name = 2
        elif selectedIndex2 == 2:
            fig_name = 3
        elif selectedIndex2 == 3:
            fig_name = 4
        elif selectedIndex2 == 4:
            fig_name = 5
    miniMenu.on_button_pressed(Player_name, miniMenu.Button.A, on_button_pressed_a2)
    
def Player_look_P3():
    global the_menu, Look_P3
    the_menu = 3.3
    Look_P3 = miniMenu.create_menu(miniMenu.create_menu_item("Look 6",
            img("""
                . . . . . f f f f . . . . .
                . . . f f 5 5 5 5 f f . . .
                . . f 5 5 5 5 5 5 5 5 f . .
                . f 5 5 5 5 5 5 5 5 5 5 f .
                . f 5 5 5 d b b d 5 5 5 f .
                f 5 5 5 b 4 4 4 4 b 5 5 5 f
                f 5 5 c c 4 4 4 4 c c 5 5 f
                f b b f b f 4 4 f b f b b f
                f b b 4 1 f d d f 1 4 b b f
                . f b f d d d d d d f b f .
                . f e f e 4 4 4 4 e f e f .
                . e 4 f 6 9 9 9 9 6 f 4 e .
                . 4 d c 9 9 9 9 9 9 c d 4 .
                . 4 f b 3 b 3 b 3 b b f 4 .
                . . f f 3 b 3 b 3 3 f f . .
                . . . . f f b b f f . . . .
                """)),
        miniMenu.create_menu_item("Look 7",
            img("""
                . . . . . . . c c c . . . . . .
                . . . . . . c b 5 c . . . . . .
                . . . . c c c 5 5 c c c . . . .
                . . c c b c 5 5 5 5 c c c c . .
                . c b b 5 b 5 5 5 5 b 5 b b c .
                . c b 5 5 b b 5 5 b b 5 5 b c .
                . . f 5 5 5 b b b b 5 5 5 c . .
                . . f f 5 5 5 5 5 5 5 5 f f . .
                . . f f f b f e e f b f f f . .
                . . f f f 1 f b b f 1 f f f . .
                . . . f f b b b b b b f f . . .
                . . . e e f e e e e f e e . . .
                . . e b c b 5 b b 5 b f b e . .
                . . e e f 5 5 5 5 5 5 f e e . .
                . . . . c b 5 5 5 5 b c . . . .
                . . . . . f f f f f f . . . . .
                """)),
        miniMenu.create_menu_item("Backwards",
            img("""
                . . . . . . f f f . . . . . . .
                . . . . . f f f f . . . . . . .
                . . . . f f f f f . . . . . . .
                . . . f f f f f . . . . . . . .
                . . f f f f f . . . . . . . . .
                . f f f f f . . . . . . . . . .
                f f f f f f f f f f f f f f f f
                f f f f f f f f f f f f f f f f
                f f f f f f f f f f f f f f f f
                f f f f f f f f f f f f f f f f
                f f f f f f . . . . . . . . . .
                . f f f f f f . . . . . . . . .
                . . f f f f f f . . . . . . . .
                . . . . f f f f f . . . . . . .
                . . . . . f f f f . . . . . . .
                . . . . . . f f f . . . . . . .
                """)))
    miniMenu.set_frame(Look_P3,
        img("""
            3 3 3 3 3 5 5 5 5 5 9 9 9 9 9
            3 3 3 3 3 5 5 5 5 5 9 9 9 9 9
            3 3 3 3 3 5 5 5 5 5 9 9 9 9 9
            3 3 3 3 3 5 5 5 5 5 9 9 9 9 9
            3 3 3 3 3 5 5 5 5 5 9 9 9 9 9
            3 3 3 3 3 5 5 5 5 5 9 9 9 9 9
            3 3 3 3 3 5 5 5 5 5 9 9 9 9 9
            3 3 3 3 3 5 5 5 5 5 9 9 9 9 9
            3 3 3 3 3 5 5 5 5 5 9 9 9 9 9
            3 3 3 3 3 5 5 5 5 5 9 9 9 9 9
            3 3 3 3 3 5 5 5 5 5 9 9 9 9 9
            3 3 3 3 3 5 5 5 5 5 9 9 9 9 9
            3 3 3 3 3 5 5 5 5 5 9 9 9 9 9
            3 3 3 3 3 5 5 5 5 5 9 9 9 9 9
            3 3 3 3 3 5 5 5 5 5 9 9 9 9 9
            """))
    
    def on_button_pressed_a3(selection3, selectedIndex3):
        global Figur
        if selectedIndex3 == 2:
            miniMenu.close(Look_P3)
            Player_look_P2()
        elif selectedIndex3 == 0:
            Figur = 6
            miniMenu.close(Look_P3)
            New_Game2()
        elif selectedIndex3 == 1:
            Figur = 7
            miniMenu.close(Look_P3)
            New_Game2()
    miniMenu.on_button_pressed(Look_P3, miniMenu.Button.A, on_button_pressed_a3)
    
def Code_Start():
    global the_menu, Start_Menu
    the_menu = 1
    scene.set_background_image(img("""
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff99d99bbbbbcfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff99ddbdd66168bcccccc9ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff999ddbbbd66888111ccccccb99fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9966ddbbbb6688811818ccccccbbc99fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffdd69dddbbb66618881888818818cccccbe9fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffddd96dd6b6dbd68888888888888888cccccc99fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffdbbd9666666dbb668886888888cccccccccccccc9ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffdbbb99666966d68866888888cccccccccccccccccc69ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffdbbb999669666666888888888ccccbbbcc8bcccccccccc9fffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffdbbb999666666666888888888cbbcbe8bbbcbcccccbbcccb9ffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffff9bbb999666666666688888888bccb888888bbbbb88888bcccccfffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffdbbb999669666666866888868bbbbb8888888ccc888b88bbc8cccffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffdbbb9d99ddd666668868888688bbcb888888888bc888bcc8bc886c9fffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffbbbbbbddd966666888688888888888888b88888888888cc8ccc886c9ffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffdbbbbbbdd6966666666868888888888bbdbbebb8888888888bcc8c86c9fffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffff9bbdbddd6666666666888688868888ddddddddde8888888888bccbbccccfffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffff9dbb9dd666666666668868888888bddddddbdbbddcccccd88b8ebccbbbbc9ffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffdd99999666666666668868888888bdddddbbbbbdbbbccccccb8bbbccc8bbb9fffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffff9dd99996696966666666668888bbbdddddbbbddbbbbbbbbbcccc8bcccbb8bbcfffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffff9d999996666966666668688888bbdddbbbbdbbbbbbbbbbbcccccc8bbccc88bc9ffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffff99999999666996696668868868bbdddddbbbdbbbbbbbbbbbbcbccc88bcccc88c6ffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffff999996696669666966d8868666bddbbbddbbdbbbbbbbbbbbbcccccc88bbccc8869fffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffff9999996699669666666d6688668bddbbdbbbbbbbbbbbbbbbbbccccccc88bcccc866fffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffff9dd999669966666666666688668bdddbbbbbbbbbbbbbbbbbbbccccccc888bbccc669ffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffff999999669d69666666666688868bddbbbdbbbbbbbbbbbbbbbbcccccccc888bbcc869ffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffff99999996ddd69666666688888868ddbddbbbbbbbbbbbbbbbbbbccccccccc888888866ffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffff999999969ddd6669666688688888bbbbbbbbbbbbbbbbbbbbbbbbccbccccc8888888869fffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffff99999966ddddd669666688888888bbbbbbbbbbbbbbbbbbbbbbbcbccccccccc88888869fffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffff999bb99666dddd6666666668886888bbbbbbbbbbbbbbbbbbbbbbcccccccccccc8888889fffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffff99bbbb966696666666666888886888bbbbbbbbbbbbbbbbbbbbbbcbccccccccccc888886fffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffff99bbdbb666969666666668888868888bbbbbbbbbbbbbbbbbbbbccbccccccccccc8888869ffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffff99dbbbbb6696966666666668886868888bbbbeb888bbbbbbbbbcccccccccccccc8888869ffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffff99bbbbbbe6969666666666888888888888888888888bbbbbbbbccccccccccccc88888869ffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffff9bbbbbccbc66966666666688888688888888888d888ebbbbbbbcccccccccccbb88888869ffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffff9bbbbbbbbcc69996666688668886888888dd88dbbd88bbbbbbbccccccccccceb88888869ffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffff9bbbbbbbbccc999966668868888888888ddddbbbbd88cbbbbbbbbccccccccc8888888869ffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffff9ebbbbcccccccc9966666688888888888888ddbbbb888bbbbbbbbccccccccc8888888869ffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffff9bbbbbccccccccc666666888866888888888dddddbdd88bbbbbbccccccccc88888888bb9ffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffbbbbbbcccccccccc6666688888888888888888d8888888bbbbbbccccccccc88888888bb9ffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffff9dbbbbccbbccccccb666688868888888888888888888888bbbbbccccccccc888888888b9ffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffff9dbbbbbbbbcccccbb66666688888888888888888888888bbbbccccccccccc88888888869ffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffff9bbbbbbbcccccccb666666688888888888888888888888bbbbcccccccccc888888888869ffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffff9bbbbbbbccccccbb666666688888888888888888888888bbbbcccccccccc88888888886fffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffff99bbbbbbbbccccb6666668888888888888888888888888bbbbcbcccccccc88888888886fffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffff99dbbbcbbccccb6666668888888888888888888888888bbbbbccccccccc888cc888869fffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffff99dbbbcccccccc6666668688688888888888888888888bbbbccccccccc8888cc888869fffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffff999bbbbbccccbc6666666688688888888888888888888bbbbcccccccc88888dd88886ffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffff969bbbbbbcccc69666666668688868888888888888888bbbbccccccc88888bd888886ffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffff99bbbbcccccc696bb668888888868888888888888888bbbcccccccc8888bbd888869ffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffff9999bbbcccc9666dbbb8888888888888888888888888ccbcccccccc8888bc888886fffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffff699bbbbccc966966bbb8888888888888888888888888bbbbccccc88888bcc88869fffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffff9999bbcccc666666dbbdd88888888688888888888888bbcccccc88888888888669fffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffff9699dbcccc66666666bb6d8888888688888888888888bbcccccc8888888888869ffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffff9696bbbcc66666666dbbd6886868888888888888888bbcbccc8888888888d669ffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffff999ebbccc666666666dbb8868888688888888888888bbbccc8888888889b69fffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffff969ccbcc66996666666bbb868888888888888888888bbbc888888888888b6ffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffff96ccccc966966666666bb8688666888888888888888b8888888888888699ffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffff99ccbc996666666666dbb6888668888888888888888888888888888869fffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffff969ccb9666666666666dbb88866888888888888888888888888888869ffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffff969ccc6696666666666dd8888668888888888888888888888888866fffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffff969cc9669666966d66dd8888868888888888888888888bb8888669fffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffff96ccc66699669dddd888868888888888888888888888be888669ffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffff96c66669966666dd88886666668888888888888888dd888669fffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffff96966669966ddd686886868888888888888888888d888669ffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffff969666696666666688686888888888888888888888669ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffff9966966966666666886888888888888886888888669fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9699996666666888888888888888888118888699ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff969996666668888881188888888881888669ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff996999666688881818888888881886669ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9961161186618811188886116699ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff99161111611118111666699fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9999661166669999ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff999999999fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        """))
    Start_Menu = miniMenu.create_menu(miniMenu.create_menu_item("New Game",
            img("""
                . f f f . . . . . . . . f f f .
                . f f f f . . . . . . . f f f .
                . f f f f . . . . . . . f f f .
                . f f f f f . . . . . . f f f .
                . f f f f f f . . . . . f f f .
                . f f f f f f f . . . . f f f .
                . f f f f f f f . . . . f f f .
                . f f f . f f f f . . . f f f .
                . f f f . f f f f f . . f f f .
                . f f f . . f f f f f . f f f .
                . f f f . . . f f f f f f f f .
                . f f f . . . . f f f f f f f .
                . f f f . . . . . f f f f f f .
                . f f f . . . . . f f f f f f .
                . f f f . . . . . . f f f f f .
                . f f f . . . . . . . f f f f .
                """)),
        miniMenu.create_menu_item("Save",
            img("""
                f f f f f f f f f f f f . . . .
                f f f f f f f f f f f f . . . .
                f f 1 1 f 1 1 1 1 f 1 1 f f . .
                f f 1 1 f 1 1 1 1 f 1 1 f f . .
                f f 1 1 f 1 1 1 1 f 1 1 1 1 f f
                f f 1 1 f f f f f f 1 1 1 1 f f
                f f 1 1 1 1 1 1 1 1 1 1 1 1 f f
                f f 1 1 1 1 1 1 1 1 1 1 1 1 f f
                f f 1 1 1 1 1 1 1 1 1 1 1 1 f f
                f f 1 1 1 1 1 1 1 1 1 1 1 1 f f
                f f 1 f f f f f f f f f 1 1 f f
                f f 1 f 1 1 1 1 1 1 1 f 1 1 f f
                f f 1 f 1 1 1 1 1 1 1 f 1 1 f f
                f f 1 f 1 1 1 1 1 1 1 f 1 1 f f
                f f f f f f f f f f f f f f f f
                f f f f f f f f f f f f f f f f
                """),
            True),
        miniMenu.create_menu_item("Load",
            img("""
                . . f f f f . . . . . . . . . .
                . . f f f f . . . . . . . . . .
                . . f f f f . . . . . . . . . .
                . . f f f f . . . . . . . . . .
                . . f f f f . . . . . . . . . .
                . . f f f f . . . . . . . . . .
                . . f f f f . . . . . . . . . .
                . . f f f f . . . . . . . . . .
                . . f f f f . . . . . . . . . .
                . . f f f f . . . . . . . . . .
                . . f f f f . . . . . . . . . .
                . . f f f f . . . . . . . . . .
                . . f f f f . . . . . . . . . .
                . . f f f f f f f f f f f f f .
                . . f f f f f f f f f f f f f .
                . . f f f f f f f f f f f f f .
                """)))
    miniMenu.set_frame(Start_Menu,
        img("""
            3 3 3 3 3 5 5 5 5 5 9 9 9 9 9
            3 3 3 3 3 5 5 5 5 5 9 9 9 9 9
            3 3 3 3 3 5 5 5 5 5 9 9 9 9 9
            3 3 3 3 3 5 5 5 5 5 9 9 9 9 9
            3 3 3 3 3 5 5 5 5 5 9 9 9 9 9
            3 3 3 3 3 5 5 5 5 5 9 9 9 9 9
            3 3 3 3 3 5 5 5 5 5 9 9 9 9 9
            3 3 3 3 3 5 5 5 5 5 9 9 9 9 9
            3 3 3 3 3 5 5 5 5 5 9 9 9 9 9
            3 3 3 3 3 5 5 5 5 5 9 9 9 9 9
            3 3 3 3 3 5 5 5 5 5 9 9 9 9 9
            3 3 3 3 3 5 5 5 5 5 9 9 9 9 9
            3 3 3 3 3 5 5 5 5 5 9 9 9 9 9
            3 3 3 3 3 5 5 5 5 5 9 9 9 9 9
            3 3 3 3 3 5 5 5 5 5 9 9 9 9 9
            """))
    
    def on_button_pressed_a4(selection4, selectedIndex4):
        if selectedIndex4 == 0:
            miniMenu.close(Start_Menu)
            New_Game2()
        elif selectedIndex4 == 2:
            miniMenu.close(Start_Menu)
    miniMenu.on_button_pressed(Start_Menu, miniMenu.Button.A, on_button_pressed_a4)
    
def new_Game_start():
    global Var_Player
    if True:
        pass
    elif False:
        pass
    else:
        scene.set_background_image(assets.image("""
            cityscape0
            """))
        Var_Player = sprites.create(img("""
                . . . . . . f f f f . . . . . .
                . . . . f f f 2 2 f f f . . . .
                . . . f f f 2 2 2 2 f f f . . .
                . . f f f e e e e e e f f f . .
                . . f f e 2 2 2 2 2 2 e e f . .
                . . f e 2 f f f f f f 2 e f . .
                . . f f f f e e e e f f f f . .
                . f f e f b f 4 4 f b f e f f .
                . f e e 4 1 f d d f 1 4 e e f .
                . . f e e d d d d d d e e f . .
                . . . f e e 4 4 4 4 e e f . . .
                . . e 4 f 2 2 2 2 2 2 f 4 e . .
                . . 4 d f 2 2 2 2 2 2 f d 4 . .
                . . 4 4 f 4 4 5 5 4 4 f 4 4 . .
                . . . . . f f f f f f . . . . .
                . . . . . f f . . f f . . . . .
                """),
            SpriteKind.player)
        controller.move_sprite(Var_Player)
        Var_Player.set_position(8, 70)
def Player_look_P2():
    global the_menu, Look_P2
    the_menu = 3.2
    Look_P2 = miniMenu.create_menu(miniMenu.create_menu_item("Look 4",
            img("""
                . . . . f f f f . . . . .
                . . f f f f f f f f . . .
                . f f f f f f c f f f . .
                f f f f f f c c f f f c .
                f f f c f f f f f f f c .
                c c c f f f e e f f c c .
                f f f f f e e f f c c f .
                f f f b f e e f b f f f .
                . f 4 1 f 4 4 f 1 4 f . .
                . f e 4 4 4 4 4 4 e f . .
                . f f f e e e e f f f . .
                f e f b 7 7 7 7 b f e f .
                e 4 f 7 7 7 7 7 7 f 4 e .
                e e f 6 6 6 6 6 6 f e e .
                . . . f f f f f f . . . .
                . . . f f . . f f . . . .
                """)),
        miniMenu.create_menu_item("Look 5",
            img("""
                . . . . f f f f . . . .
                . . f f e e e e f f . .
                . f f e e e e e e f f .
                f f f f 4 e e e f f f f
                f f f 4 4 4 e e f f f f
                f f f 4 4 4 4 e e f f f
                f 4 e 4 4 4 4 4 4 e 4 f
                f 4 4 f f 4 4 f f 4 4 f
                f e 4 d d d d d d 4 e f
                . f e d d b b d d e f .
                . f f e 4 4 4 4 e f f .
                e 4 f b 1 1 1 1 b f 4 e
                4 d f 1 1 1 1 1 1 f d 4
                4 4 f 6 6 6 6 6 6 f 4 4
                . . . f f f f f f . . .
                . . . f f . . f f . . .
                """)),
        miniMenu.create_menu_item("Backward",
            img("""
                . . . . . . f f f . . . . . . .
                . . . . . f f f f . . . . . . .
                . . . . f f f f f . . . . . . .
                . . . f f f f f . . . . . . . .
                . . f f f f f . . . . . . . . .
                . f f f f f . . . . . . . . . .
                f f f f f f f f f f f f f f f f
                f f f f f f f f f f f f f f f f
                f f f f f f f f f f f f f f f f
                f f f f f f f f f f f f f f f f
                f f f f f f . . . . . . . . . .
                . f f f f f f . . . . . . . . .
                . . f f f f f f . . . . . . . .
                . . . . f f f f f . . . . . . .
                . . . . . f f f f . . . . . . .
                . . . . . . f f f . . . . . . .
                """)),
        miniMenu.create_menu_item("Forward",
            img("""
                . . . . . . . . f f f . . . . .
                . . . . . . . . f f f f . . . .
                . . . . . . . . f f f f f . . .
                . . . . . . . . . f f f f f . .
                . . . . . . . . . . f f f f . .
                . . . . . . . . . . . f f f f .
                f f f f f f f f f f f f f f f f
                f f f f f f f f f f f f f f f f
                f f f f f f f f f f f f f f f f
                f f f f f f f f f f f f f f f f
                . . . . . . . . . . . f f f f .
                . . . . . . . . . . f f f f . .
                . . . . . . . . . f f f f f . .
                . . . . . . . . f f f f f . . .
                . . . . . . . . f f f f . . . .
                . . . . . . . . f f f . . . . .
                """)))
    miniMenu.set_frame(Look_P2,
        img("""
            3 3 3 3 3 5 5 5 5 5 9 9 9 9 9
            3 3 3 3 3 5 5 5 5 5 9 9 9 9 9
            3 3 3 3 3 5 5 5 5 5 9 9 9 9 9
            3 3 3 3 3 5 5 5 5 5 9 9 9 9 9
            3 3 3 3 3 5 5 5 5 5 9 9 9 9 9
            3 3 3 3 3 5 5 5 5 5 9 9 9 9 9
            3 3 3 3 3 5 5 5 5 5 9 9 9 9 9
            3 3 3 3 3 5 5 5 5 5 9 9 9 9 9
            3 3 3 3 3 5 5 5 5 5 9 9 9 9 9
            3 3 3 3 3 5 5 5 5 5 9 9 9 9 9
            3 3 3 3 3 5 5 5 5 5 9 9 9 9 9
            3 3 3 3 3 5 5 5 5 5 9 9 9 9 9
            3 3 3 3 3 5 5 5 5 5 9 9 9 9 9
            3 3 3 3 3 5 5 5 5 5 9 9 9 9 9
            3 3 3 3 3 5 5 5 5 5 9 9 9 9 9
            """))
    
    def on_button_pressed_a5(selection5, selectedIndex5):
        global Figur
        if selectedIndex5 == 3:
            miniMenu.close(Look_P2)
            Player_look_P3()
        elif selectedIndex5 == 2:
            miniMenu.close(Look_P2)
            Player_look_P1()
        elif selectedIndex5 == 0:
            Figur = 4
            miniMenu.close(Look_P2)
            New_Game2()
        elif selectedIndex5 == 1:
            Figur = 5
            miniMenu.close(Look_P2)
            New_Game2()
    miniMenu.on_button_pressed(Look_P2, miniMenu.Button.A, on_button_pressed_a5)
    
def Player_look_P1():
    global the_menu, Look_P1
    the_menu = 3.1
    Look_P1 = miniMenu.create_menu(miniMenu.create_menu_item("Look 1",
            img("""
                . . . . . . f f f f . . . . . .
                . . . . f f f 2 2 f f f . . . .
                . . . f f f 2 2 2 2 f f f . . .
                . . f f f e e e e e e f f f . .
                . . f f e 2 2 2 2 2 2 e e f . .
                . . f e 2 f f f f f f 2 e f . .
                . . f f f f e e e e f f f f . .
                . f f e f b f 4 4 f b f e f f .
                . f e e 4 1 f d d f 1 4 e e f .
                . . f e e d d d d d d e e f . .
                . . . f e e 4 4 4 4 e e f . . .
                . . e 4 f 2 2 2 2 2 2 f 4 e . .
                . . 4 d f 2 2 2 2 2 2 f d 4 . .
                . . 4 4 f 4 4 5 5 4 4 f 4 4 . .
                . . . . . f f f f f f . . . . .
                . . . . . f f . . f f . . . . .
                """)),
        miniMenu.create_menu_item("Look 2",
            img("""
                . . . . . f f 4 4 f f . . . . .
                . . . . f 5 4 5 5 4 5 f . . . .
                . . . f e 4 5 5 5 5 4 e f . . .
                . . f b 3 e 4 4 4 4 e 3 b f . .
                . . f 3 3 3 3 3 3 3 3 3 3 f . .
                . f 3 3 e b 3 e e 3 b e 3 3 f .
                . f 3 3 f f e e e e f f 3 3 f .
                . f b b f b f e e f b f b b f .
                . f b b e 1 f 4 4 f 1 e b b f .
                f f b b f 4 4 4 4 4 4 f b b f f
                f b b f f f e e e e f f f b b f
                . f e e f b d d d d b f e e f .
                . . e 4 c d d d d d d c 4 e . .
                . . e f b d b d b d b b f e . .
                . . . f f 1 d 1 d 1 d f f . . .
                . . . . . f f b b f f . . . . .
                """)),
        miniMenu.create_menu_item("Look 3",
            img("""
                . f f f . f f f f . f f f .
                f f f f f c c c c f f f f f
                f f f f b c c c c b f f f f
                f f f c 3 c c c c 3 c f f f
                . f 3 3 c c c c c c 3 3 f .
                . f c c c c 4 4 c c c c f .
                . f f c c 4 4 4 4 c c f f .
                . f f f b f 4 4 f b f f f .
                . f f 4 1 f d d f 1 4 f f .
                . . f f d d d d d d f f . .
                . . e f e 4 4 4 4 e f e . .
                . e 4 f b 3 3 3 3 b f 4 e .
                . 4 d f 3 3 3 3 3 3 c d 4 .
                . 4 4 f 6 6 6 6 6 6 f 4 4 .
                . . . . f f f f f f . . . .
                . . . . f f . . f f . . . .
                """)),
        miniMenu.create_menu_item("Forward",
            img("""
                . . . . . . . . f f f . . . . .
                . . . . . . . . f f f f . . . .
                . . . . . . . . f f f f f . . .
                . . . . . . . . . f f f f f . .
                . . . . . . . . . . f f f f . .
                . . . . . . . . . . . f f f f .
                f f f f f f f f f f f f f f f f
                f f f f f f f f f f f f f f f f
                f f f f f f f f f f f f f f f f
                f f f f f f f f f f f f f f f f
                . . . . . . . . . . . f f f f .
                . . . . . . . . . . f f f f . .
                . . . . . . . . . f f f f f . .
                . . . . . . . . f f f f f . . .
                . . . . . . . . f f f f . . . .
                . . . . . . . . f f f . . . . .
                """)))
    miniMenu.set_frame(Look_P1,
        img("""
            3 3 3 3 3 5 5 5 5 5 9 9 9 9 9
            3 3 3 3 3 5 5 5 5 5 9 9 9 9 9
            3 3 3 3 3 5 5 5 5 5 9 9 9 9 9
            3 3 3 3 3 5 5 5 5 5 9 9 9 9 9
            3 3 3 3 3 5 5 5 5 5 9 9 9 9 9
            3 3 3 3 3 5 5 5 5 5 9 9 9 9 9
            3 3 3 3 3 5 5 5 5 5 9 9 9 9 9
            3 3 3 3 3 5 5 5 5 5 9 9 9 9 9
            3 3 3 3 3 5 5 5 5 5 9 9 9 9 9
            3 3 3 3 3 5 5 5 5 5 9 9 9 9 9
            3 3 3 3 3 5 5 5 5 5 9 9 9 9 9
            3 3 3 3 3 5 5 5 5 5 9 9 9 9 9
            3 3 3 3 3 5 5 5 5 5 9 9 9 9 9
            3 3 3 3 3 5 5 5 5 5 9 9 9 9 9
            3 3 3 3 3 5 5 5 5 5 9 9 9 9 9
            """))
    
    def on_button_pressed_a6(selection6, selectedIndex6):
        global Figur
        if selectedIndex6 == 3:
            miniMenu.close(Look_P1)
            Player_look_P2()
        elif selectedIndex6 == 0:
            Figur = 1
            miniMenu.close(Look_P1)
            New_Game2()
        elif selectedIndex6 == 1:
            Figur = 2
            miniMenu.close(Look_P1)
            New_Game2()
        elif selectedIndex6 == 2:
            Figur = 3
            miniMenu.close(Look_P1)
            New_Game2()
    miniMenu.on_button_pressed(Look_P1, miniMenu.Button.A, on_button_pressed_a6)
    

def on_b_pressed():
    global Figur
    if the_menu == 2:
        miniMenu.close(New_Game)
        Figur = 0
        Code_Start()
    elif the_menu == 3.1:
        miniMenu.close(Look_P1)
        New_Game2()
    elif the_menu == 3.2:
        miniMenu.close(Look_P2)
        New_Game2()
    elif the_menu == 3.3:
        miniMenu.close(Look_P3)
        New_Game2()
    elif the_menu == 4:
        miniMenu.close(Player_name)
        New_Game2()
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

Look_P1: Sprite = None
Look_P2: Sprite = None
Var_Player: Sprite = None
Start_Menu: Sprite = None
Look_P3: Sprite = None
fig_name = 0
Player_name: Sprite = None
Figur = 0
New_Game: Sprite = None
the_menu = 0
the_menu = 0
Code_Start()
print("Code Startet")