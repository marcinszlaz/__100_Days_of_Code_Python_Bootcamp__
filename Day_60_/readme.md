eng/pl

fast way click here -> https://myaccount.google.com/apppasswords
                    -> and type your password
or -> enter to your google account / security and log / 2FA / END / passwords do app / click `>`


# Google App Passwords - Setup Guide

1. **Prerequisite:** **2-Step Verification (2FA)** must be enabled on your Google Account. If it's off, the App Passwords option will not be visible.
2. **Direct Link:** [myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)
3. **Manual Path:**
   - Go to [myaccount.google.com](https://myaccount.google.com).
   - Select the **Security** tab on the left sidebar.
   - Under the "How you sign in to Google" section, click on **2-Step Verification**.
   - Scroll to the very bottom of the page to find **App Passwords**.
4. **Generation Process:**
   - Enter a custom name (e.g., "Python Flask Blog - Project 60").
   - Click **Create**.
   - Copy the generated 16-character code (ignore the spaces).
5. **Developer Best Practice:** Never hardcode this password in `main.py`. Store it in your `.env` file as `MAIL_PASSWORD=your_16_char_code`.

# Generowanie Haseł do Aplikacji (Google App Passwords)

1. **Wymaganie:** Na koncie Google musi być włączona **Weryfikacja dwuetapowa** (2FA). Bez tego opcja haseł do aplikacji w ogóle się nie pojawi.
2. **Link bezpośredni:** [myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)
3. **Ścieżka ręczna (gdyby link padł):**
   - Wejdź na [myaccount.google.com](https://myaccount.google.com).
   - Wybierz zakładkę **Bezpieczeństwo** (Security) po lewej.
   - W sekcji "Jak logujesz się w Google" kliknij w **Weryfikacja dwuetapowa**.
   - Zjedź na sam dół strony – tam jest sekcja **Hasła do aplikacji**.
4. **Procedura:**
   - Wpisz nazwę (np. "Flask Blog Project 60").
   - Kliknij **Utwórz**.
   - Skopiuj 16-znakowy kod (bez spacji).
5. **Zasada rzemieślnika:** Nigdy nie wrzucaj tego kodu do `main.py`. Wklej go do pliku `.env` jako `MAIL_PASSWORD=twoj_kod_tutaj`.

