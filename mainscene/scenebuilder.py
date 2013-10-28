# -*- coding: utf-8 -*-

mainscene_builder = {
    "statics":{
        "sol":{
            "mainscene/models/statics/socle_base":[
                [(0,0,0),(0,0,0)],[(0,1,0),(0,0,0)],[(1,0,0),(0,0,0)],[(-1,0,0),(0,0,0)]
            ]
        },
        "bords":{
            "nord":{},
            "sud":{},
            "est":{},
            "ouest":{}
        },
        "murs":{
            "nord":{},
            "sud":{},
            "est":{},
            "ouest":{}
        },
        "decors":{
            "nord":{},
            "sud":{},
            "est":{},
            "ouest":{}
        }
    },
    "dynamics":{
        "spawners":{}
    },
    "lights":[
        [1,(0,0,0),(0,-70,0),True,None,"dir_top"],[1,(0,0,0),(-30,-10,0),True,None,"dir_right"],[1,(0,0,0),(30,-10,0),True,None,"dir_left"],
        [0,(-8,0,9),(6,-0.5,-1.5),True,None,"spot_aux_menu"]
    ]
}
