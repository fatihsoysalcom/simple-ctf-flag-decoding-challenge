import base64

def run_ctf_challenge():
    # This is the "flag" we want the user to find.
    # In real CTFs, flags are usually in a specific format, e.g., "flag{this_is_your_flag}".
    secret_flag = "flag{siber_guvenlik_harika!}"

    # Simulate a common CTF challenge: an encoded message.
    # Here, we use Base64 encoding, which is frequently encountered in CTF challenges
    # across categories like web, forensics, or general programming.
    encoded_message = base64.b64encode(secret_flag.encode('utf-8')).decode('utf-8')

    print("---------------------------------------------------")
    print(" BlackBoxCTF - Basit Bir Bayrak Yakalama Simülasyonu")
    print("---------------------------------------------------")
    print("\nMerhaba siber güvenlik meraklısı!")
    print("Bu, BlackBoxCTF tarzı bir meydan okumanın basit bir örneğidir.")
    print("Aşağıdaki mesajı çözerek gizli 'bayrağı' bulmanız gerekiyor.")
    print("\nİpucu: Bu, yaygın bir metin kodlama yöntemidir. Çözmek için biraz araştırma yapmanız gerekebilir!")
    print("\nKodlanmış Mesaj:")
    print(f"  {encoded_message}")
    print("\n---------------------------------------------------")

    # User attempts to decode and find the flag.
    user_guess = input("Bayrağı çözdüğünüzü düşünüyorsanız buraya yapıştırın: ")

    # Check if the user's guess matches the actual flag.
    if user_guess == secret_flag:
        print("\nTebrikler! Doğru bayrağı buldunuz!")
        print(f"Bayrak: {secret_flag}")
        print("BlackBoxCTF'te bu şekilde puan kazanırsınız.")
    else:
        print("\nYanlış tahmin. Tekrar deneyin!")
        print("Unutmayın, bayraklar genellikle belirli bir formatta olur (örn: flag{...}).")

if __name__ == "__main__":
    run_ctf_challenge()
