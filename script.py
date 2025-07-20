import sys
from commands import unique, optimize_query
from commands.generate_data import GenerateDataCommand
from commands.create_table import CreateTableCommand
from commands.add_employee import AddEmployeeCommand
from commands.drop_table import DropTableCommand
from commands.prefiltered import PrefilteredCommand

def main():
    mode = sys.argv[1]
    
    # Сценарии CLI
    match mode:
        case "1":
            CreateTableCommand().run()
        case "2":
            AddEmployeeCommand().run(sys.argv[2:])
        case "3":
            unique.run()
        case "4":
            GenerateDataCommand().run()
        case "5":
            PrefilteredCommand().run()
        case "6":
            optimize_query.run()
        case "0":
            DropTableCommand().run()
        case _:
            print("Unknown mode")

# Точка входа
if __name__ == "__main__":
    main()