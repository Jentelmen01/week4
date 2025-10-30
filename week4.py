def calculate_revenue_generated(product_category, units_sold, price_tier):
    revenue_per_unit = 0    
    if product_category == "electronics":
        if price_tier == "low":
            revenue_per_unit = 45
        elif price_tier == "medium":
            revenue_per_unit = 75
        elif price_tier == "high":
            revenue_per_unit = 120
    elif product_category == "clothing":
        if price_tier == "low":
            revenue_per_unit = 25
        elif price_tier == "medium":
            revenue_per_unit = 40
        elif price_tier == "high":
            revenue_per_unit = 65
    elif product_category == "accessories":
        if price_tier == "low":
            revenue_per_unit = 15
        elif price_tier == "medium":
            revenue_per_unit = 25
        elif price_tier == "high":
            revenue_per_unit = 35
    
    total_revenue = units_sold * revenue_per_unit
    return total_revenue


def calculate_performance_ratio(experience_years, baseline_sales, actual_sales):
        expected_sales = 1000 + (experience_years * 100)
        sales_capacity = expected_sales - baseline_sales
        performance_percentage = (actual_sales - baseline_sales) / sales_capacity * 100
        return performance_percentage

def determine_achievement_level(performance_percent):
    if performance_percent < 50:
        return "Developing Level"
    elif performance_percent < 60:
        return "Competent Level"
    elif performance_percent < 70:
        return "Proficient Level"
    elif performance_percent < 85:
        return "Advanced Level"
    else:
        return "Expert Level"
    

def calculate_commission_earned(revenue, units, level_multiplier):
    base_commission = revenue * 0.05 + units * 2
    if level_multiplier == "Developing":
        multiplier = 0.5
    elif level_multiplier == "Competent":
        multiplier = 1.0
    elif level_multiplier == "Proficient":
        multiplier = 1.2
    elif level_multiplier == "Advanced":
        multiplier = 1.5
    elif level_multiplier == "Expert":
        multiplier = 1.8 
    final_commission = base_commission * multiplier
    return round(final_commission, 1)


def needs_training_support(consecutive_months, total_units, avg_performance):
    if consecutive_months >= 6 and avg_performance < 50:
        return True
    if total_units < 100 and avg_performance < 60:
        return True
    if consecutive_months >= 4 and avg_performance < 40:
        return True
    return False



def generate_sales_report(employee, product_category, units, price_tier, experience_years, baseline_sales, actual_sales, consecutive_months):
    revenue = calculate_revenue_generated(product_category, units, price_tier)
    performance = calculate_performance_ratio(experience_years, baseline_sales, actual_sales)
    level = determine_achievement_level(performance)
    level_name = level.split()[0] 
    commission = calculate_commission_earned(revenue, units, level_name)
    training_needed = needs_training_support(consecutive_months, units, performance)

    print("=" * 50)
    print(f"Sales Performance Report for {employee}")
    print("=" * 50)
    print(f"Product Category     : {product_category.capitalize()}")
    print(f"Units Sold            : {units}")
    print(f"Price Tier            : {price_tier.capitalize()}")
    print(f"Experience (Years)    : {experience_years}")
    print(f"Baseline Sales        : ${baseline_sales}")
    print(f"Actual Sales          : ${actual_sales}")
    print(f"Revenue Generated     : ${revenue}")
    print(f"Performance (%)       : {performance:.2f}%")
    print(f"Achievement Level     : {level}")
    print(f"Commission Earned     : ${commission}")
    print(f"Training Support Needed: {'Yes' if training_needed else 'No'}")
    print("=" * 50)
    print()

