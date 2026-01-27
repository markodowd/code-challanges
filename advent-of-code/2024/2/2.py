from typing import List

safe_reports = 0
safe_reports_dampened = 0


def validate_safe_report(numbers: List[int]) -> bool:
    is_increasing = None

    for index in range(1, len(numbers)):
        diff = numbers[index] - numbers[index-1]

        if abs(diff) not in range(1,4):
            return False

        if diff > 0:
            if is_increasing is None:
                is_increasing = True
            elif is_increasing is False:
                return False
        elif diff < 0:
            if is_increasing is None:
                is_increasing = False
            elif is_increasing is True:
                return False

    return True

def validate_safe_report_dampened(numbers: List[int]) -> bool:
    is_increasing = None
    rule_breaks = 0

    for index in range(1, len(numbers)):
        diff = numbers[index] - numbers[index-1]

        if abs(diff) not in range(1,4):
            return False

        if diff > 0:
            if is_increasing is None:
                is_increasing = True
            elif is_increasing is False:
                rule_breaks += 1

                if rule_breaks > 1:
                    return False
        elif diff < 0:
            if is_increasing is None:
                is_increasing = False
            elif is_increasing is True:
                rule_breaks += 1

                if rule_breaks > 1:
                    return False


    return True


with open("input.txt", "r") as file:
    for line in file:
        line_numbers = list(map(int, line.split()))

        is_safe_report = validate_safe_report(line_numbers)

        if is_safe_report:
            safe_reports += 1

        is_safe_report_dampened = validate_safe_report_dampened(line_numbers)

        if is_safe_report_dampened:
            safe_reports_dampened += 1



print("Safe Reports: ", safe_reports)
print("Safe Dampened Reports: ", safe_reports_dampened)

