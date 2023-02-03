# Add:
import maviruhInfo

WATER_BUTTONS_HEIGHT = 265

# Search:
	"height" : 25*11+8,

# Change:
	"height" : 25*11+8+25,

# Search:
		"height" : 25*11+8,

# Change:
		"height" : 25*11+8+25,

# Search:
				{
					"name" : "salestext_off_button",
					"type" : "radio_button",

					"x" : LINE_DATA_X+MIDDLE_BUTTON_WIDTH,
					"y" : 240,

					"text" : uiScriptLocale.OPTION_SALESTEXT_VIEW_OFF,

					"default_image" : ROOT_PATH + "middle_button_01.sub",
					"over_image" : ROOT_PATH + "middle_button_02.sub",
					"down_image" : ROOT_PATH + "middle_button_03.sub",
				},

# Add:
				#--------------------------------------------------------------------
				{"name" : "Deniz_Suyu","type" : "text","x" : LINE_LABEL_X,"y" : WATER_BUTTONS_HEIGHT+2,"text" : maviruhInfo.DENIZ_SUYU,},
				{"name" : "maviruh_water_0","type" : "radio_button","x" : LINE_DATA_X,"y" : WATER_BUTTONS_HEIGHT,"text" : maviruhInfo.DENIZ_1,"default_image" : ROOT_PATH + "minimize_empty_button_01.sub","over_image" : ROOT_PATH + "minimize_empty_button_02.sub","down_image" : ROOT_PATH + "minimize_empty_button_03.sub",},
				{"name" : "maviruh_water_1","type" : "radio_button","x" : LINE_DATA_X+XSMALL_BUTTON_WIDTH,"y" : WATER_BUTTONS_HEIGHT,"text" : maviruhInfo.DENIZ_2,"default_image" : ROOT_PATH + "minimize_empty_button_01.sub","over_image" : ROOT_PATH + "minimize_empty_button_02.sub","down_image" : ROOT_PATH + "minimize_empty_button_03.sub",},
				{"name" : "maviruh_water_2","type" : "radio_button","x" : LINE_DATA_X+XSMALL_BUTTON_WIDTH*2,"y" : WATER_BUTTONS_HEIGHT,"text" : maviruhInfo.DENIZ_3,"default_image" : ROOT_PATH + "minimize_empty_button_01.sub","over_image" : ROOT_PATH + "minimize_empty_button_02.sub","down_image" : ROOT_PATH + "minimize_empty_button_03.sub",},
				{"name" : "maviruh_water_3","type" : "radio_button","x" : LINE_DATA_X+XSMALL_BUTTON_WIDTH*3,"y" : WATER_BUTTONS_HEIGHT,"text" : maviruhInfo.DENIZ_4,"default_image" : ROOT_PATH + "minimize_empty_button_01.sub","over_image" : ROOT_PATH + "minimize_empty_button_02.sub","down_image" : ROOT_PATH + "minimize_empty_button_03.sub",},
				{"name" : "maviruh_water_4","type" : "radio_button","x" : LINE_DATA_X+XSMALL_BUTTON_WIDTH*4,"y" : WATER_BUTTONS_HEIGHT,"text" : maviruhInfo.DENIZ_5,"default_image" : ROOT_PATH + "minimize_empty_button_01.sub","over_image" : ROOT_PATH + "minimize_empty_button_02.sub","down_image" : ROOT_PATH + "minimize_empty_button_03.sub",},
				{"name" : "maviruh_water_5","type" : "radio_button","x" : LINE_DATA_X+XSMALL_BUTTON_WIDTH*5,"y" : WATER_BUTTONS_HEIGHT,"text" : maviruhInfo.DENIZ_6,"default_image" : ROOT_PATH + "minimize_empty_button_01.sub","over_image" : ROOT_PATH + "minimize_empty_button_02.sub","down_image" : ROOT_PATH + "minimize_empty_button_03.sub",},
				{"name" : "maviruh_water_6","type" : "radio_button","x" : LINE_DATA_X+XSMALL_BUTTON_WIDTH*6,"y" : WATER_BUTTONS_HEIGHT,"text" : maviruhInfo.DENIZ_7,"default_image" : ROOT_PATH + "minimize_empty_button_01.sub","over_image" : ROOT_PATH + "minimize_empty_button_02.sub","down_image" : ROOT_PATH + "minimize_empty_button_03.sub",},
				{"name" : "maviruh_water_7","type" : "radio_button","x" : LINE_DATA_X+XSMALL_BUTTON_WIDTH*7,"y" : WATER_BUTTONS_HEIGHT,"text" : maviruhInfo.DENIZ_8,"default_image" : ROOT_PATH + "minimize_empty_button_01.sub","over_image" : ROOT_PATH + "minimize_empty_button_02.sub","down_image" : ROOT_PATH + "minimize_empty_button_03.sub",},
