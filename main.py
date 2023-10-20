import streamlit as st
import random

st.set_page_config( "Free Palestine", page_icon="✊")
def new_line(n=1):
    st.markdown(("<br>" * n),unsafe_allow_html=True)


st.markdown("<h1 align='center'> Free Palestine ❤️ </h1>", unsafe_allow_html=True)
new_line()

col1, col2, col3 = st.columns([1,2,1])
col2.image("assets/logo.jpg")
new_line()

st.write("This app is for encrypting your words that's defending and sharing about what happening in Palestine in a fast and easy way. This encryption because our words offends their public modesty. **Pray for Gaza, Pray for Palestine** 🙏")
new_line(1)

st.markdown("<h2 align='center'> Enter Your Text Here </h2>", unsafe_allow_html=True)
text = st.text_area("", placeholder="Enter Your Text Here...", height=50, )
new_line()

mystyle = '''
    <style>
        textarea {
            text-align: right;
        }
    </style>
    '''
mystylespan = '''
    <style>
        pre {
            text-align: right;
        }
    </style>
    '''

st.markdown(mystyle, unsafe_allow_html=True)
st.markdown(mystylespan, unsafe_allow_html=True)


def check_let_lang(char):
    
    english_letters_small = "abcdefghijklmnopqrstuvwxyz"
    english_letters_capital = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    arabic_letters = "ابتثجحخدذرزسشصضطظعغفقكلمنهوي"

    if char in english_letters_small or char in english_letters_capital:
        return "eng"
    
    elif char in arabic_letters:
        return "arab"
    
    else:
        return 0

def arab_to_eng(char):

    eng_let = "DFGRZ"
    arab_let = "دفغرز"

    if char in arab_let:
        return eng_let[arab_let.index(char)]
    
    return char

def eng_to_arab(char):

    eng_let = "ADFGKLMNRSTZ"
    arab_let = "ادفغكلمنرستز"

    if char in eng_let:
        return arab_let[eng_let.index(char)]
    
    return char


def add_spec(word, num_letters):

    spec_let = ['/','.','_','*', "~" , "|", "-" ]
    word = list(word)
    
    for i in range(num_letters):
        word.insert(random.randint(1, len(word)-1), f"ـ{random.choice(spec_let)}ـ")
    
    word = "".join(word)
    return word

special_let = ["a", "ل", "ا", "س"]
def replace_spec(word):

    letters = [let for let in ["a", "ل", "ا", "س"] if let in word]
    rep = random.choice(letters) if letters else None

    if rep:
        
        if rep == 'a':
            word = word.replace(rep, "@")
        
        elif rep == "ل":
            final_res += "l"
        
        elif rep == "ا":
            word = word.replace(rep, "١")
        
        elif rep == "س":
            word = word.replace(rep, "w")   

    return word 

def rand_let_nums(word, important=False):

    word_len = len(word)
    nums_letters = word_len // 2 if important else word_len // 4

    if nums_letters == 0:
        nums_letters = 1

    return nums_letters

def add_rand_chars(word, num_letters):

    random_chars = ['ى', "," , "|"]
    
    for i in range(num_letters):
        word = list(word).insert(random.randint(1, len(word)-1), random.choice(random_chars))

    return word


def encrypt_word(word, important=False):
    encrypted_word = ""
    if important:
        
        # Replace Letters
        for char in word:
            if check_let_lang(char) == "arab":
                pass
                # encrypted_word += arab_to_eng(char)
            
            elif check_let_lang(char) == "eng" and char.upper() in "ADFGKLMNRSTZ":
                encrypted_word += eng_to_arab(char.upper())

            else:
                encrypted_word += char
        
        # Add Random Characters
        nums_letters = rand_let_nums(word, True)
        encrypted_word = add_spec(encrypted_word, nums_letters)

        # # Add Special Characters
        # encrypted_word = replace_spec(encrypted_word)

    else:
        nums_letters = rand_let_nums(word, False)
        encrypted_word = add_spec(word, nums_letters)

    
    return encrypted_word

def encrypt(text, importance_words):
    encrypted_text = ""
    if importance_words:
        for word in text.split():
            encrypted_word = encrypt_word(word, False) if word in importance_words else word
            encrypted_text += encrypted_word + " "

    else:
        for word in text.split():

            encrypted_word = encrypt_word(word, True) if word in importance_words else encrypt_word(word, False)
            encrypted_text += encrypted_word + " "
    
    return encrypted_text


if text:
    importance_words = st.multiselect("Select The Importance Words", options=text.split(),)


new_line(1)
col1, col2, col3 = st.columns([1,1,1])
if col2.button("Encrypt Your Text 🔑", use_container_width=True):
    if text:
        encrypted_text = encrypt(text, importance_words)

        new_line()
        st.subheader("🔐 Your Encrypted Text:")
        st.code(encrypted_text, language="text")
        new_line()
        st.info("**Note 1:** Copy Your Text by Clicking on the Copy Button in the **Top Right Corner** of the Code Box!")
        st.info("**Note 2:** You can Re-Encrypt Your Text Again by Clicking on the Button Again! ")

    else:
        st.error("Please Enter Your Text First!", )
