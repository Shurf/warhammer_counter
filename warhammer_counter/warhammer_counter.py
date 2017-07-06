__author__ = 'schrecknetuser'

import targets
import tau_models

def make_bgcolor_depending_on_average(ordered_values, value):
    min_value = min(ordered_values)
    max_value = max(ordered_values)
    average = (min_value + max_value) / 2

    if value >= average:
        green_component = 255
        red_component = 255 - ((value - average)/(max_value - average)) * 255
        blue_component = red_component
    else:
        red_component = 255
        green_component = 255 - ((average - value)/(max_value - average)) * 255
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

    green_component = 255 * percent
    red_component = (255 * (1 - percent))
    blue_component = 0
    bgcolor = "#%02x%02x%02x" % (int(red_component), int(green_component), int(blue_component))

    return bgcolor

def make_bgcolor(ordered_values, value):
    #return make_bgcolor_for_min_and_max(ordered_values, value)
    #return make_bgcolor_scaled(ordered_values, value)
    return make_bgcolor_depending_on_average(ordered_values, value)




def main():

    targets_list = targets.default_targets
    models = tau_models.tau_models_list



    ranges = [8, 20, 30, 36, 72]

    with open('output.html', 'w') as f:
        f.write('<html>')
        f.write('<body>')

        for range_value in ranges:

            targets_dict = {}
            for target in targets_list:
                targets_dict[target] = []
                for model in models:
                    targets_dict[target].append(model.divided_result(target, range_value))
                targets_dict[target] = sorted(targets_dict[target])



            f.write('<h3>Range %d</h3>' % range_value)

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
                    result = model.divided_result(target, range_value)
                    bgcolor = make_bgcolor(targets_dict[target], result)
                    f.write('<td bgcolor=\'%s\'>%.2f</td>' % (bgcolor, result))
                f.write('</tr>')

            f.write('</table>')
        f.write('</body>')
        f.write('</html>')


if __name__ == '__main__':
    main()