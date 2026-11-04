price = 13000
paid = 50000
change = paid-price
ten = change // 10000
five = change % 10000 // 5000
one = change % 10000 % 5000 // 1000
print(f"Change: {change} = 10k: {ten} 5k: {five} 1k: {one}")