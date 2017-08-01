__author__ = 'schrecknetuser'

import warhammer_counter.targets as targets
import warhammer_counter.tau_models as tau_models
import warhammer_counter.ig_models as ig_models
import warhammer_counter.ik_models as ik_models
import warhammer_counter.gk_models as gk_models
import warhammer_counter.de_models as de_models
import warhammer_counter.necron_models as necron_models
import warhammer_counter.marine_models as marine_models
import warhammer_counter.tyranid_models as tyranid_models

class Distance:
    def __init__(self, range_value:int, overwatch=False):
        self.range_value = range_value
        self.overwatch = overwatch


max_color_value = 255

def make_bgcolor_depending_on_average(ordered_values, value):
    filtered_values = [x for x in ordered_values if x > 0.0001]
    if len(filtered_values) > 0:
        min_value = min(filtered_values)
        max_value = max(filtered_values)
    else:
        min_value = 0
        max_value = 0
    average = (min_value + max_value) / 2

    if value < 0.0001:
        return "#aaaaaa"

    if value >= average:
        green_component = max_color_value
        if abs(max_value - average) < 0.0001:
            red_component = 0
        else:
            red_component = max_color_value - ((value - average)/(max_value - average)) * max_color_value
        blue_component = red_component
    else:
        red_component = max_color_value
        if abs(max_value - average) < 0.0001:
            green_component = 0
        else:
            green_component = max_color_value - ((average - value)/(max_value - average)) * max_color_value
        blue_component = green_component

    return "#%02x%02x%02x" % (int(red_component), int(green_component), int(blue_component))

def make_bgcolor_for_min_and_max(ordered_values, value):
    bgcolor = '#ffffff'
    if value == min(ordered_values):
        bgcolor = '#ff0000'
    if value == max(ordered_values):
        bgcolor = '#00ff00'
    return bgcolor


def make_bgcolor_scaled(ordered_values, value):

    total_range = max(ordered_values) - min(ordered_values)
    percent = (value - min(ordered_values))/total_range

    green_component = max_color_value * percent
    red_component = (max_color_value * (1 - percent))
    blue_component = 0
    bgcolor = "#%02x%02x%02x" % (int(red_component), int(green_component), int(blue_component))

    return bgcolor

def make_bgcolor(ordered_values, value):
    #return make_bgcolor_for_min_and_max(ordered_values, value)
    #return make_bgcolor_scaled(ordered_values, value)
    return make_bgcolor_depending_on_average(ordered_values, value)


def make_file(targets_list, models, distances, file_name):

    with open(file_name, 'w') as f:
        f.write('<html>')
        f.write('<body>')

        for distance in distances:

            all_values = []
            targets_dict = {}
            for target in targets_list:
                targets_dict[target] = []
                for model in models:
                    targets_dict[target].append(model.divided_result(target, distance.range_value, distance.overwatch))
                    all_values.append(model.divided_result(target, distance.range_value, distance.overwatch))
                targets_dict[target] = sorted(targets_dict[target])


            header = "Range %d" % distance.range_value
            if distance.overwatch:
                header += " (overwatch)"
            f.write('<h3>%s</h3>' % header)

            f.write('<table border=1>')
            f.write('<tr>')
            f.write('<td width=20%%>name</td>')
            for target in targets_list:
                f.write('<td width=%d%%>%s</td>' % (80/len(targets_list), target.name))
            f.write('</tr>')

            for model in models:
                f.write('<tr>')
                f.write('<td>%s</td>' % model.name)
                for target in targets_list:
                    result = model.divided_result(target, distance.range_value, distance.overwatch)
                    bgcolor = make_bgcolor(targets_dict[target], result)
                    #bgcolor = make_bgcolor(all_values, result)
                    f.write('<td bgcolor=\'%s\'>%.2f</td>' % (bgcolor, result))
                f.write('</tr>')

            f.write('</table>')
        f.write('</body>')
        f.write('</html>')

def main():

    targets_list = targets.default_targets
    #distances = [Distance(1, True), Distance(6), Distance(12), Distance(18), Distance(24), Distance(30), Distance(36), Distance(72)]
    distances = [Distance(6), Distance(12), Distance(18), Distance(24), Distance(30), Distance(36), Distance(72)]


    make_file(targets_list=targets_list, models=tau_models.tau_models_list, distances=distances, file_name='tau.html')
    make_file(targets_list=targets_list, models=ig_models.ig_models_list, distances=distances, file_name='ig.html')
    make_file(targets_list=targets_list, models=ik_models.ik_models_list, distances=distances, file_name='ik.html')
    make_file(targets_list=targets_list, models=ig_models.ig_leman_russ_list, distances=distances, file_name='leman russ.html')
    make_file(targets_list=targets_list, models=ig_models.ig_baneblade_list, distances=distances, file_name='baneblade.html')
    make_file(targets_list=targets_list, models=ig_models.ig_filtered_models_list + ik_models.ik_filtered_models_list + gk_models.gk_models_list, distances=distances, file_name='ig-gk-ik-filtered.html')
    make_file(targets_list=targets_list, models=ik_models.ik_filtered_models_list + gk_models.gk_models_list, distances=distances, file_name='gk-ik-filtered.html')
    make_file(targets_list=targets_list, models=de_models.de_models_list, distances=distances, file_name='de.html')
    make_file(targets_list=targets_list, models=necron_models.necron_models_list, distances=distances, file_name='nec.html')
    make_file(targets_list=targets_list, models=tyranid_models.tyranid_models_list, distances=distances, file_name='tyr.html')



if __name__ == '__main__':
    main()