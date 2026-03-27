def build_data():
    # Produce subcategories
    produce_data = {
        "fruits": {
            "bananas": {"per lb": 0.58},
            "limes": {"per each": 0.35},
            "mangoes": {"per each": 1.25},
            "hass avocados": {"per each": 1.50},
            "yellow nectarines": {"per lb": 2.99},
            "white nectarines": {"per lb": 2.99},
            "grapefruit": {"per each": 1.10},
            "pineapples": {"per each": 3.00},
            "blackberries": {"per 6 oz pack": 3.99},
            "kiwis": {"per each": 0.75},
            "coconut": {"per each": 2.50},
            "strawberries": {"per 1 lb pack": 3.99},
            "cantaloupe": {"per each": 3.25},
            "seedless lemons": {"per each": 0.55},
            "raspberries": {"per 6 oz pack": 3.99},
            "guava": {"per each": 1.80},
            "red seedless grapes": {"per lb": 2.50},
            "navel oranges": {"per 4 lb bag": 4.50},
            "green seedless grapes": {"per lb": 2.50},
            "honeydew melon": {"per each": 3.50},
            "dragon fruit": {"per each": 5.00},
            "blueberries": {"per 6 oz pack": 3.99},
            "black seedless grapes": {"per lb": 2.50},
            "red globe seeded grapes": {"per lb": 2.50},
            "mandarin oranges": {"per lb": 2.00},
            "tangerine": {"per lb": 2.00},
            "plums": {"per lb": 2.99},
            "white peach": {"per lb": 2.99},
            "pomegranate": {"per each": 3.00},
            "cara cara oranges": {"per each": 1.20},
            "apricot": {"per lb": 3.50},
            "key limes": {"per lb": 3.00},
        },
        "vegetables": {
            "cucumbers": {"per each": 0.75},
            "iceberg lettuce": {"per head": 1.50},
            "broccoli": {"per lb": 2.00},
            "green onions": {"per bunch": 1.00},
            "tomato": {"per lb": 2.25},
            "carrots": {"per lb": 1.20},
            "potatoes": {"per 5 lb bag": 3.50, "per 10 lb bag": 6.49},
            "cabbage": {"per lb": 0.85},
            "bell pepper": {"per each": 1.50},
            "celery": {"per stalk": 1.75},
            "onion": {"per lb": 1.00},
            "spinach": {"per 5 oz bag": 2.00},
            "asparagus": {"per lb": 3.99},
            "mushrooms": {"per 8 oz pack": 1.97},
            "lettuce": {"per head": 1.50},
            "green beans": {"per lb": 2.00},
            "zucchini": {"per lb": 1.50},
            "sweet potatoes": {"per lb": 1.10},
            "garlic": {"per bulb": 0.60},
            "peas": {"per lb": 2.50},
            "squash": {"per lb": 1.50},
            "cauliflower": {"per head": 2.50},
            "ginger": {"per lb": 3.00},
            "jalapeno peppers": {"per lb": 1.50},
            "corn on the cob": {"per ear": 0.75},
            "brussels sprouts": {"per lb": 3.25},
            "cole slaw": {"per 16 oz bag": 1.97},
            "white onions": {"per lb": 1.00},
            "iceberg salad": {"per 12 oz bag": 2.14},
            "sweet onions": {"per lb": 1.50},
            "medley tomatoes": {"per 12 oz pack": 3.18},
            "calabacita squash": {"per each": 1.10},
            "baby potatoes": {"per 1.5 lb bag": 3.72},
            "shredded carrots": {"per 10 oz bag": 1.87},
            "peeled garlic": {"per 6 oz pack": 3.07},
            "red radish": {"per bunch": 1.94},
            "celery hearts": {"per each": 2.97},
            "baby bella mushrooms": {"per 8 oz pack": 2.17},
            "sweet tomatoes": {"per pint pack": 2.56},
            "eggplant": {"per each": 2.61},
            "red baby potatoes": {"per 1.5 lb bag": 3.72},
            "russet potatoes": {"per 5 lb bag": 2.77},
            "butternut squash": {"per 16 oz pack": 3.28},
            "rainbow baby carrots": {"per 12 oz bag": 2.16},
            "serrano pepper": {"per 4 oz bag": 1.58},
            "kale": {"per bunch": 1.48},
            "mini sweet peppers": {"per 8 oz bag": 3.46},
            "broccoli florets": {"per 32 oz pack": 5.98},
            "red potatoes": {"per 5 lb bag": 4.34},
            "red onions": {"per 3 lb bag": 3.54},
            "whole carrots": {"per 5 lb bag": 4.77},
            "celery sticks": {"per 1.6 oz pack": 1.97},
            "green leaf lettuce": {"per 7 oz pack": 3.07},
        }
    }

    # Grains
    grains_data = {
        "rice": {"per 1 lb bag": 1.50, "per 5 lb bag": 6.00},
        "bread": {"per loaf": 2.50},
        "oatmeal": {"per 18 oz container": 3.00},
        "pasta": {"per 1 lb box": 1.20},
        "flour": {"per 5 lb bag": 4.00},
        "cereal": {"per 12 oz box": 3.50}
    }

    # Dairy
    dairy_data = {
        "milk": {"per gallon": 3.50},
        "cheese": {"per lb": 6.00},
        "yogurt": {"per 6 oz container": 1.00},
        "butter": {"per lb": 4.00},
        "cream cheese": {"per 8 oz tub": 2.50}
    }

    # Protein
    protein_data = {
        "chicken breast": {"per lb": 3.50},
        "ground beef": {"per lb": 4.00},
        "eggs": {"per dozen": 2.50},
        "tofu": {"per 14 oz pack": 2.00},
        "salmon": {"per lb": 8.00}
    }

    # Household
    household_data = {
        "laundry detergent": {"per 50 oz bottle": 7.00},
        "dish soap": {"per 16 oz bottle": 2.50},
        "paper towels": {"per 6 roll pack": 6.00},
        "toilet paper": {"per 12 roll pack": 9.00},
        "trash bags": {"per 30 count box": 8.00}
    }

    # Medicine
    medicine_data = {
        "acetaminophen": {"per 100 count bottle": 8.00},
        "ibuprofen": {"per 100 count bottle": 10.00},
        "cough syrup": {"per 8 oz bottle": 7.00},
        "antacid": {"per 50 count pack": 5.00}
    }

    # Clothing
    clothing_data = {
        "girls pants": {"per pair": 10.00},
        "girls jeans": {"per pair": 15.00},
        "womens jeans": {"per pair": 25.00},
        "womens short sleeve shirts": {"per each": 12.00},
        "mens t-shirts": {"per each": 10.00},
        "mens jeans": {"per pair": 20.00}
    }

    # Toys
    toys_data = {
        "doll": {"per each": 8.00},
        "lego set": {"per set": 30.00},
        "toy car": {"per each": 5.00},
        "board game": {"per each": 15.00}
    }

    # All categories combined
    categories = {
        "produce": produce_data,
        "grains": grains_data,
        "dairy": dairy_data,
        "protein": protein_data,
        "household": household_data,
        "medicine": medicine_data,
        "clothing": clothing_data,
        "toys": toys_data,
    }

    return categories


def create_item_lookup(categories):
    item_lookup = {}
    for category, subcats in categories.items():
        # For produce, subcats is dict of subcategory dicts, else a dict of items directly
        if category == "produce":
            for subcat, items in subcats.items():
                for item, units in items.items():
                    item_lookup[item] = units
        else:
            # Other categories do not have subcategories
            for item, units in subcats.items():
                item_lookup[item] = units
    return item_lookup


def find_matches(keyword, item_lookup):
    keyword_lower = keyword.lower()
    matches = {item: units for item, units in item_lookup.items() if keyword_lower in item.lower()}
    return matches


def print_fair_market_value(item, units):
    for unit, price in units.items():
        print(f"{item.title()} has fair market value of about ${price:.2f} per {unit}.")
        print(f"One {unit} of {item.title()} can be fairly traded for or towards another item with a value of ${price:.2f}.\n")


def find_trade_matches(item_name, item_lookup):
    if item_name not in item_lookup:
        return []

    base_price_list = list(item_lookup[item_name].values())
    if not base_price_list:
        return []

    base_price = base_price_list[0]  # Use first unit price for trade comparisons

    matches = []
    for other_item, units in item_lookup.items():
        if other_item == item_name:
            continue
        for unit, price in units.items():
            # Allow a small tolerance to find trade matches within +/-10%
            if abs(price - base_price) / base_price <= 0.10:
                matches.append((other_item, unit, price))
    return matches


def main():
    print("What do you want to trade?")
    categories = build_data()
    item_lookup = create_item_lookup(categories)

    while True:
        user_input = input("Enter item name or keyword (or 'exit' to quit): ").strip().lower()
        if user_input == "exit":
            print("Goodbye!")
            break

        matches = find_matches(user_input, item_lookup)

        if not matches:
            print(f"No items found matching '{user_input}'. Please try again.\n")
            continue

        for item, units in matches.items():
            print_fair_market_value(item, units)

        # If exact match, show trade matches
        if user_input in matches:
            trade_matches = find_trade_matches(user_input, item_lookup)
            if trade_matches:
                print("Possible trade matches (items with similar value):")
                for t_item, t_unit, t_price in trade_matches:
                    print(f"- {t_item.title()} for about ${t_price:.2f} per {t_unit}")
                print()
            else:
                print("No trade matches found for this item.\n")


if __name__ == "__main__":
    main()