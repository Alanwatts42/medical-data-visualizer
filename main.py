# This entrypoint file to be used in development. Start by reading README.md
import medical_data_visualizer as mdv
from unittest import main

# Test your function by calling it here
mdv.draw_cat_plot()
mdv.draw_heat_map()

# Run unit tests automatically
main(module='test_module', exit=False)


if __name__ == '__main__':
    print("mask = ")
    None