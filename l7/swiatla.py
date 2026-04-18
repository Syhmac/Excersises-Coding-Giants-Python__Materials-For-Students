kolor = "żółty"

if kolor == "czerwony":
	print("Zatrzymaj się!")
elif kolor == "żółty":
	print("Przygotuj się!")
else: # w domyśle kolor zielony
	print("Jedź!")

match kolor:
	case "czerwony":
		print("Zatrzymaj się!")
	case "żółty":
		print("Przygotuj sie!")
	case _:
		print("Jedź!")