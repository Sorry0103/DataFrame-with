# -*- coding: utf-8 -*-
"""Untitled9.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1dSmsWn8rEumOU-StIKBWBGxJButA9_Xt
"""

"""Untitled8.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1NScZtAjMA-5TcxIukI2MvIusxzr43lef
"""

# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/16NmGMWf_6p3Ep4GT7Q5SPCNKuemur5YC
"""

import pandas as pd
baza={
    "FIISH":["Nuriddinjonov Imomali ","Abduhahharov Diyorbek " ,"Muminova Muharram","Alloberdiyeva Odina", "Musohonova Madina","Baxriddinoov Inomjan","Usmonjonov Ravshan" ],
    "Yoshi":['18','10','17','16','11','12','9'  ],
    "Maktabi":["53-maktab" ,"32-maktab","39-maktab","33-maktab","32-maktab","3-maktab","2-maktab" ],
    "Jinsi":[  "erkak","erkak","ayol","ayol","ayol","erkak","erka"],
    "Manzili":[ "Namangan shahar","Namangan shahar","Namangan shahar","Toshkent shahar","Namangan shahar","Andijon shahar","Fargona shahar" ]
}
db=pd.DataFrame(baza)
print(db)

Filtr=db[(db['Yoshi']=='7') &(db['Jinsi']=='erkak')]
print(Filtr)