#%%
import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
# Load environment variables from .env file

# app_password = os.getenv("Google_App_Password")git
# receiver_email = os.getenv("receiver_email")
# sender_email = os.getenv("sender_email")

# Hide default Streamlit elements (header, footer, menu)
# hide_streamlit_style = """
#     <style>
#     header {visibility: hidden;}
#     footer {visibility: hidden;}
#     </style>
# """
# st.markdown(hide_streamlit_style, unsafe_allow_html=True)


sender_email = st.secrets["sender_email"]
receiver_email = st.secrets["receiver_email"]   
app_password = st.secrets["Google_App_Password"]
# print("✅ Environment variables loaded successfully!")
# print(f"Sender Email: {sender_email}")
# print(f"Receiver Email: {receiver_email}")  
# print("✅ App Password loaded successfully!")


# Set page configuration
st.set_page_config(page_title="FA - Flower", layout="wide")

# Initialize session state for cart if not present
if "cart" not in st.session_state:
    st.session_state.cart = []

# Sidebar for navigation
page = st.sidebar.radio(" ", ["FA - Flower", "Contact Us"])

# -------------------------------
# Page 1: Flower Shop
# -------------------------------
if page == "FA - Flower":
    st.markdown(
        "<h1 style='color:#FF69B4; text-align:center;'>🌸 Welcome to Our Flower Shop! 🌸</h1>",
        unsafe_allow_html=True
    )
    
    st.markdown(
    """
    <h5 style="color:#FFB6C1; text-align:center;">Every bloom you see is real—and just the beginning of your story. 
    \n Browse our fresh flowers and feel free to customize your perfect arrangement!</h5>
    """,
    unsafe_allow_html=True
)

    # Sample flower shop items (Name, Price, Image URL)
    flowers = [
        {"name": "Blush Elegance", "price": 65, "img": "./img_trim/1.jpg"},
        {"name": "Sunlit Grace", "price": 74, "img": "./img_trim/2.jpg"},
        {"name": "Enchanted Orchids", "price": 100, "img": "./img_trim/3.jpg"},
        {"name": "Golden Sunrise", "price": 68, "img": "./img_trim/4.jpg"},
        {"name": "Blush Harmony", "price": 76, "img": "./img_trim/5.jpg"},
        {"name": "Spring Serenade", "price": 83, "img": "./img_trim/6.jpg"},
        {"name": "Whispering Love", "price": 64, "img": "./img_trim/7.jpg"},
        {"name": "Midnight Elegance", "price": 85, "img": "./img_trim/8.jpg"},
        {"name": "Frosted Grace", "price": 88, "img": "./img_trim/9.jpg"},
        {"name": "Whispering Pastels", "price": 78, "img": "./img_trim/10.jpg"},
        {"name": "Grace in Bloom", "price": 75.5, "img": "./img_trim/11.jpg"},
        {"name": "Champagne Whispers", "price": 66.5, "img": "./img_trim/12.jpg"},
    ]

    cols_per_row = 4
    for i in range(0, len(flowers), cols_per_row):
        cols = st.columns(cols_per_row)
        for idx, flower in enumerate(flowers[i:i+cols_per_row]):
            with cols[idx]:
                st.image(flower["img"], use_container_width=True)
                st.markdown(f"**{flower['name']}**")
                st.markdown(f"Price: ${flower['price']}")
                #if st.button(f"Add {flower['name']}", key=f"btn_{i+idx}"):
                #    st.session_state.cart.append(flower)
                #    st.success(f"{flower['name']} added to cart!")

    # Display Cart
    if st.session_state.cart:
        st.markdown("### 🛒 Your Cart")
        total = sum(item["price"] for item in st.session_state.cart)
        for item in st.session_state.cart:
            st.write(f"- {item['name']} (${item['price']})")
        st.markdown(f"**Total: ${total}**")

# -------------------------------
# Page 2: Contact Page
# -------------------------------
elif page == "Contact Us":
    st.title("📞 Contact Us")
    
    st.markdown("""
        Our flowers bloom with the seasons, so we do not offer online checkout.<br>
        Instead, we believe in crafting something uniquely yours!<br>
        Please allow at least 3 days for arrangement preparation.<br>
        Fill out the form below, and our florist will contact you to customize your perfect bouquet.
    """, unsafe_allow_html=True)



    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        submitted = st.form_submit_button("Send Message")

        if submitted:
            if name and email and message:
                
                # Email configuration
                sender_email = sender_email
                receiver_email = receiver_email
                app_password = app_password
                cc_email = [email]  # Optional CC to the sender

                subject = f"New Inquiry from {name}"
                body = f"Name: {name}\nEmail: {email}\nMessage:\n{message}"

                # Create the email
                msg = MIMEMultipart()
                msg['From'] = sender_email
                msg['To'] = receiver_email
                msg['Subject'] = subject
                msg['Cc'] = ', '.join(cc_email)
                msg.attach(MIMEText(body, 'plain'))

                # Send the email
                try:
                    with smtplib.SMTP('smtp.gmail.com', 587) as server:
                        server.starttls()
                        server.login(sender_email, app_password)
                        server.send_message(msg)
                    st.success(f"Thank you {name}! We will reach out to you at {email}.")
                except Exception as e:
                    st.error(f"Error sending email: {e}")

            else:
                st.error("Please fill out all fields before submitting.")
