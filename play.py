
import os

f = open('play_manim.bat', 'w')

py_file_name = 'example_scenes.py'
py_file_name = 'tutorial/9_proyect_1.py'
#demo
#py_file_name = 'manim_sandbox/demo/ThreeD_demo.py'
#py_file_name = 'manim_sandbox/demo/Updater_demo.py'

#utils/scenes
#py_file_name = 'manim_sandbox/utils/scenes/bilibili.py'
#py_file_name = 'manim_sandbox/utils/scenes/LSystem.py'
#py_file_name = 'manim_sandbox/utils/scenes/NewGraphScene.py'

#videos/2020NewYear
#py_file_name = 'manim_sandbox/videos/2020NewYear/Tony.py'

#videos
#py_file_name = 'manim_sandbox/videos/Bezier.py'
#py_file_name = 'manim_sandbox/videos/Mandelbrot.py'
#py_file_name = 'manim_sandbox/videos/Nameplate_4K.py'
#py_file_name = 'manim_sandbox/videos/SandpileModel.py'



#videos/HomeworkVol01
#py_file_name = 'manim_sandbox/videos/HomeworkVol01/DistinctWind.py'



pl = ' -pl'

str01 = 'python -m manim ' + py_file_name + pl

f.write(str01)

f.close()

os.system('play_manim.bat')


