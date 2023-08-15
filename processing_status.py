from io import TextIOWrapper
from typing import Tuple, List
import sys
import textfsm

INPUT_STATUS = sys.argv[1]
TEMPLATE = "input_status_OCT.template"


class ParserFSM():
    """A class to parse status file"""

    def __init__(self, input_file: str, template_file: str) -> None:
        self.input_file = input_file
        self.template_file = template_file

    def parse_by_textfsm(self, template: TextIOWrapper,
                         status: TextIOWrapper) -> Tuple[List[str], List[str]]:
        """Parse file by textfsm module.

        Keyword arguments:
            template -- template file
            status -- status file 
        """
        re_table = textfsm.TextFSM(template)
        headers = re_table.header
        results = re_table.ParseText(status.read())
        return (headers, results)

    def get_dict_result(self) -> dict:
        """Get dict result from parsed file"""
        template = open(self.template_file)
        try:
            status = open(self.input_file)
        except FileNotFoundError:
            print("Ooops, invalid file directory.\nPlease, try again")
            return {}
        headers, results = self.parse_by_textfsm(template, status)
        dict_result = dict(zip(headers, *results))  # type: ignore
        return (dict_result)


def main():
    parser = ParserFSM(INPUT_STATUS, TEMPLATE)
    results = parser.get_dict_result()
    for status in results:
        clean_string = results[status].replace(" ", "")
        if clean_string.isalpha():
            print(f'{status}: "{results[status]}"')
        else:
            print(f'{status}: {results[status]}')


if __name__ == "__main__":
    main()
