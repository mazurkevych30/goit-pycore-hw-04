
def total_salary(path):
    try:
        with open(path) as f:
            total = 0
            lines = [line.strip() for line in f.readlines()]
            for line in lines:
                _, salary = line.split(",")
                total += int(salary)
            
            return (total, int(total / len(lines)))

    except FileNotFoundError: 
        return "Файл не знайдено."
    except Exception as e:
        print(f"Сталася помилка: {e}")

total, average = total_salary("./salary.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")