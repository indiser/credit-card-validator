import random

def get_valid_card_number():
    # 1. Generate the first 15 digits randomly
    # We use a list of integers for easier math
    payload = [random.randint(0, 9) for _ in range(15)]
    
    # 2. Calculate the Luhn sum for these 15 digits
    # We work backwards because the Luhn pattern (double every second) 
    # starts from the rightmost digit.
    
    current_sum = 0
    # For the payload, the rightmost digit (index 14) will be the 
    # "2nd" digit in the final 16-digit number, so it MUST be doubled.
    is_second = True 
    
    for digit in reversed(payload):
        d = digit
        
        if is_second:
            d = d * 2
            # Handle numbers > 9 (e.g., 18 -> 1+8=9)
            if d > 9:
                d -= 9
        
        current_sum += d
        # Flip the flag for the next digit
        is_second = not is_second
        
    # 3. Calculate the Check Digit
    # The sum plus the check_digit must be divisible by 10.
    # Formula: (10 - (sum % 10)) % 10
    check_digit = (10 - (current_sum % 10)) % 10
    
    # 4. Append the check digit to the payload
    payload.append(check_digit)
    
    # 5. Convert list back to string
    return "".join(map(str, payload))

# --- Your Main Execution ---
if __name__ == "__main__":
    
    # Generate 5 valid cards instantly
    for i in range(5):
        valid_card = get_valid_card_number()
        print(f"Valid Card Generated: {valid_card}")