def moc_herosa(siła: int, zręczność: int, inteligencja: int):
	moc = (siła * 3 + zręczność * 2 + inteligencja * 4) / 3
	return moc

poziom = round(moc_herosa(80, 60, 70))
print(f"Moc herosa: {poziom}")