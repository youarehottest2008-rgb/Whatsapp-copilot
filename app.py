import streamlit as st
import datetime

st.set_page_config(page_title="WhatsApp AI Copilot", page_icon="💬", layout="centered")
st.title("💬 WhatsApp AI Copilot")
st.caption("For Vendors in Warri & Lagos - Never miss a sale")

# Init
if 'products' not in st.session_state:
    st.session_state.products = []
if 'business_name' not in st.session_state:
    st.session_state.business_name = "My Fashion Store"

with st.sidebar:
    st.header("⚙️ Your Business")
    st.session_state.business_name = st.text_input("Business Name", st.session_state.business_name)

    st.header("📦 Add Product")
    name = st.text_input("Product Name", "Black Hoodie")
    price = st.number_input("Price (₦)", value=5000, min_value=0)
    stock = st.number_input("Stock", value=10)
    sizes = st.text_input("Sizes", "M, L, XL, XXL")
    colors = st.text_input("Colors", "Black, White, Blue")
    delivery = st.text_input("Delivery Areas", "Warri, PH, Lagos, Abuja")
    pay = st.text_input("Payment", "Opay 1234567890 - John")

    if st.button("➕ Add Product", type="primary"):
        if len(st.session_state.products) >= 2:
            st.error("FREE PLAN LIMIT: 2 products max. Upgrade for ₦5000/month to add unlimited.")
        else:
            st.session_state.products.append({
                "name": name, "price": price, "stock": stock,
                "sizes": sizes, "colors": colors,
                "delivery": delivery, "pay": pay
            })
            st.success(f"Added {name}!")

st.subheader(f"📦 Products in {st.session_state.business_name}")
if not st.session_state.products:
    st.info("Add your first product from sidebar 👈")
else:
    for i, p in enumerate(st.session_state.products):
        st.write(f"**{i+1}. {p['name']}** - ₦{p['price']} (Stock: {p['stock']})")
        st.write(f"Sizes: {p['sizes']} | Colors: {p['colors']}")

st.divider()
st.subheader("🤖 AI Auto-Reply Tester")

col1, col2 = st.columns(2)
with col1:
    customer_msg = st.text_area("Paste Customer WhatsApp Message:", "Oga how much for the hoodie? Do you deliver to PH? I want size L", height=100)

with col2:
    tone = st.selectbox("Tone", ["Friendly & Professional", "Pidgin English", "Urgent Sales Closer"])

if st.button("✨ Generate Perfect Reply", type="primary", use_container_width=True):
    if not st.session_state.products:
        st.warning("Add at least 1 product first!")
    else:
        # Use first product for demo
        p = st.session_state.products[0]

        if "Pidgin" in tone:
            reply = f"""Hello boss! 👋

Yes o, {p['name']} dey available!

💰 Price: ₦{p['price']}
📏 Sizes: {p['sizes']}
🎨 Colors: {p['colors']}
🚚 Delivery: Yes we dey deliver to PH & {p['delivery']}
💳 Payment: {p['pay']}

Abeg send your size, color, full address + phone number make I reserve am for you now. Stock dey finish fast!

- {st.session_state.business_name}"""
        else:
            reply = f"""Hello 👋 Thanks for reaching out to {st.session_state.business_name}!

Yes, {p['name']} is available and in stock ✅

💰 Price: ₦{p['price']}
📏 Sizes Available: {p['sizes']}
🎨 Colors: {p['colors']}
🚚 Delivery: Yes, we deliver to PH! We cover {p['delivery']}
💳 Payment: {p['pay']}

To place your order, please send:
1. Your preferred Size & Color
2. Full Delivery Address
3. Phone Number

I will confirm your order and delivery fee immediately.

Looking forward to your order!
- {st.session_state.business_name}"""

        st.text_area("📋 COPY THIS REPLY TO WHATSAPP:", reply, height=250)
        st.balloons()
        st.success("Reply generated! Copy and paste to WhatsApp")

st.divider()
st.caption(f"Generated {datetime.datetime.now().strftime('%d %b %Y')} | Made for Warri Vendors | Upgrade to Pro for ₦5000/mo")
