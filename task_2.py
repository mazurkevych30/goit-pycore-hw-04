
def get_cats_info(path):
    try:
        with open(path) as f:
            cats = []

            for line in [line.strip() for line in f.readlines()]:
                id, name, age = line.split(",")
                cats.append({"id": id, "name": name, "age": age})
                
            return cats
          
    except FileNotFoundError: 
        return "Файл не знайдено."
    except Exception as e:
        print(f"Сталася помилка: {e}")

cats_info = get_cats_info("./cats.txt")
print(cats_info)