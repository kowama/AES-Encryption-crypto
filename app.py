from flask import Flask, render_template, request

from models.encryption import AESCipher

app = Flask(__name__, static_url_path='/static')


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_text = request.form['input_text']
        secrete_key = request.form['secret_key']
        key_size = int(request.form['key_size'])
        to_encrypt = 'to_encrypt' in request.form

        # blank or empty
        if not input_text.strip():
            # invalid input text or secret key
            message = 'invalid input text'
            return render_template('index.html', to_encrypt=to_encrypt, error_message=message)

        if not secrete_key.strip():
            # invalid input text or secret key
            message = 'invalid secret key'
            print(message)
            return render_template('index.html', to_encrypt=to_encrypt, error_message=message)

        # Adapt the key to AES Algorithm [16, 24, 32]
        adapted_secrete_key = secrete_key
        suffix = ''
        key_length = len(secrete_key)
        if key_length > 32:
            adapted_secrete_key = secrete_key[:32]
        elif key_length != 16 and key_length != 24 and key_length != 32:
            if key_length < 16:
                suffix = '*' * (16 - key_length)
            elif 16 < key_length < 24:
                suffix = '*' * (24 - key_length)
            elif 24 < key_length < 32:
                suffix = '*' * (32 - key_length)

            adapted_secrete_key = secrete_key + suffix
            print(input_text)
            print(secrete_key)
            print(adapted_secrete_key)
            print(key_size)
            print(to_encrypt)

        output_text = ''
        try:
            output_text = AESCipher.encrypt(input_text,
                                            adapted_secrete_key, key_size
                                            ) if to_encrypt else AESCipher.decrypt(input_text,
                                                                                   adapted_secrete_key, key_size)
        except Exception as error:
            print(error)
            return render_template('index.html', input_text=input_text, secrete_key=secrete_key, key_size=key_size,
                                   output_text=output_text,
                                   to_encrypt=to_encrypt,
                                   error_message=str(error) if to_encrypt else 'invalid encrypted key or text')

        return render_template('index.html', input_text=input_text, secrete_key=secrete_key, key_size=key_size,
                               output_text=output_text,
                               to_encrypt=to_encrypt,
                               success_message='Successfully ' + 'encrypted' if to_encrypt else 'decrypted')

    return render_template('index.html', to_encrypt=True)


@app.route('/more')
def more():
    return render_template('more.html')


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True)
