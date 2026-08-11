print("=== PERHITUNGAN JUMLAH ROTI TOKO ===")

persediaan = 100
print(f"1. Persediaan awal: {persediaan} roti")

persediaan = persediaan + 50
print(f"2. Setelah produksi pagi +50: {persediaan} roti")


persediaan = persediaan * 3
print(f"3. Setelah dikalikan 3: {persediaan} roti")


persediaan = persediaan - 120
print(f"4. Setelah dikirim 120 roti: {persediaan} roti")


jumlah_per_etalase = persediaan / 4
print(f"5. Dibagi ke 4 etalase: {jumlah_per_etalase} roti per etalase")


jumlah_per_etalase = jumlah_per_etalase + 10
print(f"6. Setelah tambahan 10 roti sore: {jumlah_per_etalase} roti per etalase")

total_akhir = jumlah_per_etalase * 4
print(f"\nTotal roti sore di semua etalase: {total_akhir} roti")