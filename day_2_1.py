def read_input(file_path):
    with open(file_path, 'r') as file:
        reports = []
        for line in file.readlines():
            report = [int(level) for level in line.split()]
            reports.append(report)
    return reports


def is_safe(report):
    # Generate every combination of a report
    report_vars = [report.copy() for _ in range(len(report))]
    
    
    for i in range(len(report)):
        report_var = report_vars[i]
        del report_var[i]

    report_vars.append(report)

    for report_var in report_vars:
        if diff_check(report_var) and seq_check(report_var):
            return True
    return False


def diff_check(report):
    for i in range(len(report) - 1):
        diff = abs(report[i] - report[i + 1])
        if diff > 3 or diff < 1:
            return False
    return True

def seq_check(report):
    asc = sorted(report)
    desc = sorted(report, reverse=True)

    return report == asc or report == desc


def main():
    reports = read_input("input/day_2.txt")
    safe_reports = 0

    for report in reports:
        if is_safe(report):
            safe_reports += 1
        
    return safe_reports

if __name__ == "__main__":
    print(main())
