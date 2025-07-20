import sys
from commands.create_table import CreateTableCommand
from commands.add_employee import AddEmployeeCommand
from commands.unique import UniqueCommand
from commands.generate_data import GenerateDataCommand
from commands.prefiltered import PrefilteredCommand
from commands.optimize_query import OptimizeQueryCommand
from commands.drop_table import DropTableCommand


def main():
    mode = sys.argv[1]
    
    # Сценарии CLI
    match mode:
        case "1":
            CreateTableCommand().run()
        case "2":
            AddEmployeeCommand().run(sys.argv[2:])
        case "3":
            UniqueCommand().run()
        case "4":
            GenerateDataCommand().run()
        case "5":
            PrefilteredCommand().run()
        case "6":
            OptimizeQueryCommand().run()
        case "0":
            DropTableCommand().run()
        case _:
            print("Unknown mode")

# Точка входа
if __name__ == "__main__":
    main()