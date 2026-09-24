import streamlit as st
import datetime

st.set_page_config(page_title="WhatsApp AI Copilot", page_icon="💬", layout="centered")
st.title("💬 WhatsApp AI Copilot")
st.caption("For Vendors in Warri & Lagos")

if 'products' not in st.session_state:
    st.session_state.products = []
if 'business_name' not in st.session_state:
    st.session_state.business_name = "My Store"

with st.sidebar:
    st.header("⚙️ Your Business")
    st.session_state.business_name = st.text_input("Business Name", st.session_state.business_name)
    st.divider()
    st.header("💳 Upgrade to Pro")
    st.write("Free: 2 products")
    st.write("Pro: Unlimited + Logo")
    st.code("palmpay: 9029508840\nName: precious\nAmount: ₦5000/mo", language="text")
    st.write("After payment, send proof to Whatsapp: 09113042934")
    

    st.divider()
    st.header("📦 Add Product")
    name = st.text_input("Product", "Black Hoodie")
    price = st.number_input("Price ₦", value=5000)
    stock = st.number_input("Stock", value=10)
    sizes = st.text_input("Sizes", "M,L,XL")
    colors = st.text_input("Colors", "Black, White")
    delivery = st.text_input("Delivery", "Warri, PH, Lagos")
    pay = st.text_input("Your Payment Info", "Opay 1234567890")

    if st.button("➕ Add Product", type="primary"):
        if len(st.session_state.products) >= 2:
            st.error("FREE LIMIT REACHED! Pay ₦5000 to Opay above to unlock unlimited.")
        else:
            st.session_state.products.append({"name":name,"price":price,"stock":stock,"sizes":sizes,"colors":colors,"delivery":delivery,"pay":pay})
            st.success("Added!")

st.subheader(f"📦 {st.session_state.business_name}")
for i, p in enumerate(st.session_state.products):
    st.write(f"**{i+1}. {p['name']}** - ₦{p['price']} | {p['sizes']}")

st.divider()
st.subheader("🤖 Auto-Reply")
customer_msg = st.text_area("Customer Message:", "how much? do you deliver to PH? size L")
tone = st.selectbox("Tone", ["Professional", "Pidgin"])

if st.button("✨ Generate Reply", use_container_width=True, type="primary"):
    if not st.session_state.products:
        st.warning("Add product first in sidebar")
    else:
        p = st.session_state.products[0]
        if tone == "Pidgin":
            reply = f"Hello boss! Yes {p['name']} dey avail! Price ₦{p['price']}, Sizes {p['sizes']}, Delivery: Yes we dey deliver to PH & {p['delivery']}. Payment: {p['pay']}. Send size+address+phone make I pack am now! - {st.session_state.business_name}"
        else:
            reply = f"Hello 👋 Thanks for contacting {st.session_state.business_name}! Yes {p['name']} is available ✅ Price: ₦{p['price']} | Sizes: {p['sizes']} | Colors: {p['colors']} | Delivery: Yes to PH, we cover {p['delivery']} | Payment: {p['pay']}. Please send size, color, address & phone to order."
        st.text_area("📋 COPY TO WHATSAPP:", reply, height=180)
        st.balloons()

st.caption(f"Made in Warri • {datetime.datetime.now().strftime('%d %b %Y')}")
