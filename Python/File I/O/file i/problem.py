with open('names.txt', 'r') as file:
    
    cleaned_name = []

    for name in file:
        cleaned = name.strip().title()
        if cleaned not in cleaned_name:
            cleaned_name.append(cleaned)
       
    print(cleaned_name)