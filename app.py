import streamlit as st
import datetime
import urllib.parse

st.set_page_config(page_title="WhatsApp AI Copilot by Allen", layout="centered")
st.title("WhatsApp AI Copilot")
st.caption("Built by Allen - Warri, Delta")

if 'products' not in st.session_state:
    st.session_state.products = []
if 'business_name' not in st.session_state:
    st.session_state.business_name = "Allen Collections"

with st.sidebar:
    st.header("Your Business")
    st.session_state.business_name = st.text_input("Business Name", st.session_state.business_name)
    st.divider()
    st.header("Upgrade to Pro - 5000 Naira/mo")
    st.info("Free: 2 products. Pro: Unlimited")
    st.code("Bank: Palmpay\nAccount: 9029508840\nName: Allen\nAmount: 5000", language="text")
    st.write("After payment, send proof to WhatsApp")
    st.link_button("WhatsApp Allen: 09113042934", "https://wa.me/2349113042934?text=Hi%20Allen%20I%20paid%20for%20Pro", use_container_width=True)
    st.divider()
    st.header("Add Product")
    name = st.text_input("Product Name", "Black Hoodie")
    price = st.number_input("Price N", value=15000)
    stock = st.number_input("Stock", value=10)
    sizes = st.text_input("Sizes", "M,L,XL,XXL")
    colors = st.text_input("Colors", "Black, White")
    delivery = st.text_input("Delivery Areas", "Warri, Ughelli, PH, Lagos")
    pay = st.text_input("Payment Info", "Palmpay 9029508840 - Allen")

    if st.button("Add Product", type="primary"):
        if len(st.session_state.products) >= 2:
            st.error("FREE LIMIT! Pay 5000 to Palmpay 9029508840 Allen to unlock.")
        else:
            st.session_state.products.append({"name":name,"price":price,"stock":stock,"sizes":sizes,"colors":colors,"delivery":delivery,"pay":pay})
            st.success("Added!")

st.subheader(st.session_state.business_name)
if not st.session_state.products:
    st.info("Click >> top left to add your first product")
else:
    for i, p in enumerate(st.session_state.products):
        st.write(f"{i+1}. {p['name']} - N{p['price']} | {p['sizes']} | Stock:{p['stock']}")

st.divider()
st.subheader("Auto-Reply Generator")
customer_msg = st.text_area("Paste customer message:", "how much for hoodie? do you deliver to PH? size L")
tone = st.selectbox("Reply Tone", ["Professional", "Pidgin Warri"])

if st.button("Generate Perfect Reply", use_container_width=True, type="primary"):
    if not st.session_state.products:
        st.warning("Add product first - Click >> top left!")
    else:
        p = st.session_state.products[0]
        if tone == "Pidgin Warri":
            reply = f"Hello boss! Yes {p['name']} dey avail! Price N{p['price']}, Sizes {p['sizes']}, Colors {p['colors']}. Delivery: Yes we dey deliver to PH and {p['delivery']}. Payment: {p['pay']}. Oya send size + color + address + phone make I pack am now! - {st.session_state.business_name}"
        else:
            reply = f"Hello! Thanks for contacting {st.session_state.business_name}! Yes {p['name']} is available. Price: N{p['price']} | Sizes: {p['sizes']} | Colors: {p['colors']} | Stock: {p['stock']} left | Delivery: Yes to PH, we cover {p['delivery']} | Payment: {p['pay']}. Please send size, color, address & phone to order. Thanks! - Allen"

        st.text_area("Copy this reply:", reply, height=170)
        encoded = urllib.parse.quote(reply)
        wa_link = f"https://wa.me/?text={encoded}"
        st.link_button("Share to WhatsApp (1-click)", wa_link, use_container_width=True, type="primary")
        st.success("Reply ready!")
        st.balloons()

st.divider()
st.caption(f"Built by Allen | WhatsApp 09113042934 | {datetime.datetime.now().strftime('%d %b %Y')}")
