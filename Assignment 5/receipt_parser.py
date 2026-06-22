import re
import json

def parse_price(price_str):
    return float(price_str.replace('\xa0', '').replace(' ', '').replace(',', '.'))

def parse_receipt(filename="raw.txt"):
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()

    # [Item Number]. \n [Product Name] \n [Qty] x [Unit Price] \n [Total Price] \n Стоимость \n [Repeated Total Price]
    item_pattern = re.compile(
        r'^\d+\.\s*\n'                       # Line 1: Item number (e.g., 1.) at the start of a line
        r'(.+?)\s*\n'                        # Line 2: Group 1 -> Product Name (lazy match until newline)
        r'([\d\s,]+)\s*x\s*([\d\s,]+)\n'     # Line 3: Group 2 -> Qty, Group 3 -> Unit Price
        r'([\d\s,]+)\n'                      # Line 4: Group 4 -> Total Price for this item
        r'Стоимость\s*\n'                    # Line 5: Literal keyword "Стоимость"
        r'[\d\s,]+\n',                       # Line 6: Repeated total price string
        re.MULTILINE
    )

    items = []
    total_calculated = 0.0

    # Find all item matches using the regex pattern
    for match in item_pattern.finditer(content):
        name = match.group(1).strip()
        qty = parse_price(match.group(2))
        unit_price = parse_price(match.group(3))
        total_price = parse_price(match.group(4))

        total_calculated += total_price

        items.append({
            "product_name": name,
            "quantity": qty,
            "unit_price": unit_price,
            "total_price": total_price
        })

    # Extract Date and Time information
    datetime_match = re.search(r'Время:\s*([\d.]+)\s+([\d:]+)', content)
    date_str, time_str = datetime_match.groups() if datetime_match else ("Not Found", "Not Found")

    # Extract Payment Method
    payment_match = re.search(r'(Банковская карта|Наличные):', content, re.IGNORECASE)
    payment_method = payment_match.group(1).strip() if payment_match else "Not Specified"

    # Extract the total amount stated in the receipt
    total_match = re.search(r'ИТОГО:\s*\n([\d\s,]+)', content)
    stated_total = parse_price(total_match.group(1)) if total_match else 0.0

    # Construct the structured dictionary output
    parsed_data = {
        "metadata": {
            "date": date_str,
            "time": time_str,
            "payment_method": "Card" if "карта" in payment_method.lower() else "Cash",
            "total_stated_in_receipt": stated_total,
            "total_calculated": round(total_calculated, 2)
        },
        "items": items
    }

    return parsed_data

if __name__ == "__main__":
    result = parse_receipt()
    # Print the beautifully formatted JSON structure to the console
    print(json.dumps(result, indent=4, ensure_ascii=False))

    # Save the final structured output to a JSON file
    with open("parsed_receipt.json", "w", encoding="utf-8") as out_f:
        json.dump(result, out_f, indent=4, ensure_ascii=False)
