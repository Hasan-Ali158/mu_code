total_eggs = int(input('Enter the eggs you want to buy:'))
total_packs= total_eggs // 6

if total_eggs % 6!=0:
    total_packs += 1

print(f"Minimum total_packs required:", {total_packs} )
