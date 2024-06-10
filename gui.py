KV = """
<MainScreen>:

    MDBoxLayout:
        id: main_layout
        md_bg_color: self.theme_cls.backgroundColor

        orientation: 'horizontal'

        MDBoxLayout:
            id: left_column
            orientation: 'vertical'
            size_hint_y: None
            size_hint_x: None
#            width: '80dp'
            height: self.minimum_height
            padding: [0, 0]
            spacing: 10
            pos_hint: {"center_x": .5, "center_y": .5}

            MDExtendedFabButton:
                id: shot_btn
                fab_state: "collapse"
                pos_hint: {"center_x": .5, "center_y": .5}
#                size_hint_x: 0.75

                MDExtendedFabButtonIcon:
                    icon: "camera"

                MDExtendedFabButtonText:
                    text: "Shot"

            MDExtendedFabButton:
                id: rec_btn
                fab_state: "collapse"
                pos_hint: {"center_x": .5, "center_y": .5}

                MDExtendedFabButtonIcon:
                    id: rec_btn_icon
                    icon: "record"

                MDExtendedFabButtonText:
                    text: "Record"

#            MDLabel:
#                id: framerate
#                text: "SAMPLE"
#                color: "white"
#                halign: "center"
#                valign: "center"
##                pos_hint: {"center_x": .5, "center_y": .5}


        MDBoxLayout:
            id: center_column
            orientation: 'vertical'
            size_hint_x: 1

            MDLabel:
                id: placeholder
                text: "Trying to connect..."
                color: "white"
                halign: "center"
                valign: "center"

        MDBoxLayout:
            id: right_column
            orientation: 'vertical'
            size_hint_y: None
            size_hint_x: None
#            width: '80dp'
            height: self.minimum_height
            padding: [0, 0]
            spacing: 10
            pos_hint: {"center_x": .5, "center_y": .5}

            MDExtendedFabButton:
                id: color_btn
                fab_state: "collapse"
                pos_hint: {"center_x": .5, "center_y": .5}
#                size_hint_x: 0.75
#                on_enter: self.fab_state = "expand"
#                on_leave: self.fab_state = "collapse"


                MDExtendedFabButtonIcon:
                    icon: "palette"

                MDExtendedFabButtonText:
                    text: "Color mode"

            MDExtendedFabButton:
                id: agc_btn
                fab_state: "collapse"
                pos_hint: {"center_x": .5, "center_y": .5}
#                size_hint_x: 0.75
#                on_enter: self.fab_state = "expand"
#                on_leave: self.fab_state = "collapse"

                MDExtendedFabButtonIcon:
                    icon: "image"

                MDExtendedFabButtonText:
                    text: "AGC Mode"

            MDExtendedFabButton:
                id: zoom_btn
                fab_state: "collapse"
                pos_hint: {"center_x": .5, "center_y": .5}
#                size_hint_x: 0.75
#                on_enter: self.fab_state = "expand"
#                on_leave: self.fab_state = "collapse"

                MDExtendedFabButtonIcon:
                    icon: "loupe"

                MDExtendedFabButtonText:
                    text: "Zoom"

            MDExtendedFabButton:
                id: ffc_btn
                fab_state: "collapse"
                pos_hint: {"center_x": .5, "center_y": .5}
#                size_hint_x: 0.75
#                on_enter: self.fab_state = "expand"
#                on_leave: self.fab_state = "collapse"

                MDExtendedFabButtonIcon:
                    icon: "camera-iris"

                MDExtendedFabButtonText:
                    text: "Calibration"

"""