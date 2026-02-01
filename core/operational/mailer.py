def disparar_email_bienvenida(user_email, status_kyc):
    if status_kyc == "VERIFICADO":
        print(f"📧 Enviando Welcome Email a {user_email}...")
        return True
    return False
