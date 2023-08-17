import os
import sys
script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))
sys.path.append(os.path.join(script_directory, '..'))

import matplotlib.pyplot as plt
from common.plotting import Plotter
from common.evaluate import Evaluate
from DStarLite.dstar_lite import DStarLite
from DStarLite.create_dstarlite_model import CreateDstarLiteModel

# adj_type: 4adj or 8adj
# expand_method: random or heading
# dist_type: manhattan or euclidean
setting = {'adj_type': '8adj', 
           'dist_type': 'euclidean',
           'expand_method': 'heading'}

# model
model = CreateDstarLiteModel(setting, has_dynamic_obsts=True, use_rnd=False, map_id=1)


# dstar lite
pp_obj = DStarLite(model)
# -----------------------------------


# Evaluate
eval = Evaluate(pp_obj)
pp_obj.sol.proc_time = round(pp_obj.sol.proc_time, 3)

# results
print(' ----------- results ------------')
print('nodes:', pp_obj.sol.nodes)
print('dirs:', pp_obj.sol.dirs)
print('time:', pp_obj.sol.proc_time)
print('length:', eval.path_length)
print('turns:', eval.path_turns)
print('smoothness:', eval.smoothness)
print(' ---------- statistics ---------')
print('n_expanded:', eval.n_expanded)
print('n_opened:', eval.n_opened)
print('n_reopened:', eval.n_reopened)
print('n_final_open:', eval.n_final_open)


# plot
name = 'sim-2'
do_animate = False  # True - False
if not do_animate:
    plot_dyno = True
    plotter = Plotter(model, plot_dyno)
    name = name + '.png'
    pic_name = os.path.join(script_directory, 'Results/'+name) 
    plotter.plot_solution(pp_obj.sol)
    # plotter.fig.savefig(pic_name)
else:
    plot_dyno = False
    plotter = Plotter(model, plot_dyno)
    name = name + '.gif'
    pic_name = os.path.join(script_directory, 'Results/'+name) 
    plotter.plot_anim(pp_obj.sol)
    plotter.anim.save(pic_name, fps=4)
plt.show()