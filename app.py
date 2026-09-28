import os
import asyncio
import streamlit as st
from dotenv import load_dotenv
from hindsight_client import Hindsight


# =====================================================
# SETUP
# =====================================================

load_dotenv()

API_KEY = os.getenv("HINDSIGHT_API_KEY")

if not API_KEY:
    st.error("HINDSIGHT_API_KEY is missing from your .env file.")
    st.stop()


client = Hindsight(
    base_url="https://api.hindsight.vectorize.io",
    api_key=API_KEY
)


st.set_page_config(
    page_title="CustomerSupportAgent",
    page_icon="💬",
    layout="wide"
)


# =====================================================
# CUSTOM DESIGN
# =====================================================

st.markdown("""
<style>

.main-title {
    font-size: 38px;
    font-weight: 700;
    margin-bottom: 5px;
}

.subtitle {
    font-size: 17px;
    opacity: 0.7;
    margin-bottom: 25px;
}

.memory-card {
    padding: 20px;
    border-radius: 12px;
    border: 1px solid rgba(128,128,128,0.25);
    margin-top: 10px;
    margin-bottom: 10px;
}

.section-title {
    font-size: 22px;
    font-weight: 650;
    margin-top: 10px;
}

</style>
""", unsafe_allow_html=True)


# =====================================================
# HEADER
# =====================================================

st.markdown(
    '<div class="main-title">💬 CustomerSupportAgent</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'AI customer support that remembers the customer — '
    'so they never have to repeat their story.'
    '</div>',
    unsafe_allow_html=True
)


# =====================================================
# STATUS
# =====================================================

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("🧠 Memory", "Active")

with col2:
    st.metric("🔎 Recall", "Enabled")

with col3:
    st.metric("🤖 AI Support", "Online")


st.divider()


# =====================================================
# LIVE SUPPORT CHAT
# =====================================================

st.markdown(
    '<div class="section-title">💬 Live Support Chat</div>',
    unsafe_allow_html=True
)

st.write(
    "The agent remembers previous conversations and uses "
    "them to provide context-aware support."
)


chat_col1, chat_col2 = st.columns([1, 2])


with chat_col1:

    chat_customer = st.text_input(
        "Customer",
        placeholder="e.g. Tejashwini",
        key="chat_customer"
    )


with chat_col2:

    chat_message = st.text_area(
        "Message",
        placeholder="Type the customer's message...",
        height=100,
        key="chat_message"
    )


# =====================================================
# LIVE SUPPORT FUNCTION
# =====================================================

async def live_support(name, message):

    # -------------------------------------------------
    # STEP 1: RECALL PREVIOUS CUSTOMER MEMORY
    # -------------------------------------------------

    memories = await client.arecall(
        bank_id="customer-support",
        query=(
            f"What previous support problems did "
            f"customer {name} report?"
        )
    )

    # -------------------------------------------------
    # STEP 2: GENERATE CONTEXT-AWARE RESPONSE
    # -------------------------------------------------

    response = await client.areflect(
        bank_id="customer-support",
        query=(
            f"You are CustomerSupportAgent helping "
            f"customer {name}. "

            f"Use any relevant previous memories about "
            f"this customer to understand their situation. "

            f"Answer the customer's new message: "
            f"{message}. "

            f"Be helpful, polite and empathetic. "

            f"Do not invent specific facts, dates, "
            f"order numbers, or previous actions that "
            f"are not supported by the customer's memory."
        ),
        budget="low"
    )

    return memories, response


# =====================================================
# SEND TO CUSTOMER SUPPORT AGENT
# =====================================================

if st.button(
    "🚀 Send to CustomerSupportAgent",
    type="primary"
):

    if chat_customer and chat_message:

        try:

            memories, response = asyncio.run(
                live_support(
                    chat_customer,
                    chat_message
                )
            )

            # -------------------------------------------------
            # HINDSIGHT STATUS
            # -------------------------------------------------

            st.success(
                "🧠 Hindsight memory used to generate this response."
            )


            # -------------------------------------------------
            # DISPLAY RECALLED MEMORY
            # -------------------------------------------------

            st.markdown(
                "### 🧠 Hindsight Memory Used"
            )

            if memories.results:

                for memory in memories.results:

                    st.markdown(
                        '<div class="memory-card">',
                        unsafe_allow_html=True
                    )

                    st.write(
                        memory.text
                    )

                    st.markdown(
                        '</div>',
                        unsafe_allow_html=True
                    )

            else:

                st.info(
                    "No previous memory was found for this customer."
                )


            # -------------------------------------------------
            # DISPLAY AI RESPONSE
            # -------------------------------------------------

            st.markdown(
                "### 🤖 CustomerSupportAgent"
            )

            st.info(
                response.text
            )


        except Exception as e:

            st.error(
                "Could not generate the support response."
            )

            st.code(str(e))

    else:

        st.warning(
            "Please enter both the customer name and message."
        )


st.divider()


# =====================================================
# SAVE NEW SUPPORT CONVERSATION
# =====================================================

st.markdown(
    '<div class="section-title">'
    '💬 Save New Support Conversation'
    '</div>',
    unsafe_allow_html=True
)

st.write(
    "Store a customer's message in Hindsight so it "
    "can be remembered in future conversations."
)


left, right = st.columns([1, 2])


with left:

    new_customer = st.text_input(
        "Customer Name",
        placeholder="e.g. Tejashwini",
        key="new_customer"
    )


with right:

    new_message = st.text_area(
        "Customer Message",
        placeholder="Describe the customer's problem...",
        height=100,
        key="new_message"
    )


# =====================================================
# SAVE MEMORY FUNCTION
# =====================================================

async def save_memory(name, message):

    await client.aretain(
        bank_id="customer-support",

        content=(
            f"Customer {name} said: {message}"
        ),

        metadata={
            "customer_name": name
        }
    )


# =====================================================
# SAVE MEMORY BUTTON
# =====================================================

if st.button(
    "💾 Save Conversation to Memory",
    type="primary"
):

    if new_customer and new_message:

        try:

            asyncio.run(
                save_memory(
                    new_customer,
                    new_message
                )
            )

            st.success(
                "Conversation saved to Hindsight memory! 🧠"
            )

        except Exception as e:

            st.error(
                "Could not save the conversation."
            )

            st.code(str(e))

    else:

        st.warning(
            "Please enter both the customer name and message."
        )


st.divider()


# =====================================================
# CUSTOMER MEMORY / RECALL
# =====================================================

st.markdown(
    '<div class="section-title">'
    '🧠 Customer Memory'
    '</div>',
    unsafe_allow_html=True
)

st.write(
    "Retrieve information from the customer's "
    "previous conversations."
)


recall_customer = st.text_input(
    "Customer to Remember",
    placeholder="e.g. Tejashwini",
    key="recall_customer"
)


# =====================================================
# RECALL FUNCTION
# =====================================================

async def recall_memory(name):

    result = await client.arecall(
        bank_id="customer-support",

        query=(
            f"What previous support problems did "
            f"customer {name} report?"
        )
    )

    return result


# =====================================================
# RECALL BUTTON
# =====================================================

if st.button(
    "🔎 Recall Previous Conversations"
):

    if recall_customer:

        try:

            result = asyncio.run(
                recall_memory(
                    recall_customer
                )
            )

            if result.results:

                st.success(
                    f"Found {len(result.results)} "
                    f"relevant memories."
                )

                for memory in result.results:

                    st.markdown(
                        '<div class="memory-card">',
                        unsafe_allow_html=True
                    )

                    st.write(
                        f"**Memory Type:** {memory.type}"
                    )

                    st.write(
                        memory.text
                    )

                    st.markdown(
                        '</div>',
                        unsafe_allow_html=True
                    )

            else:

                st.info(
                    "No previous memories found."
                )

        except Exception as e:

            st.error(
                "Could not recall customer memory."
            )

            st.code(str(e))

    else:

        st.warning(
            "Enter the customer's name first."
        )


st.divider()


# =====================================================
# AI SUPPORT AGENT
# =====================================================

st.markdown(
    '<div class="section-title">'
    '🤖 AI Support Agent'
    '</div>',
    unsafe_allow_html=True
)

st.write(
    "Ask the agent to respond using the customer's "
    "remembered history."
)


support_col1, support_col2 = st.columns([1, 2])


with support_col1:

    support_customer = st.text_input(
        "Customer",
        placeholder="e.g. Tejashwini",
        key="support_customer"
    )


with support_col2:

    support_question = st.text_area(
        "Customer's New Question",
        placeholder=(
            "e.g. My order is still not here. "
            "What do you remember about my issue?"
        ),
        height=100,
        key="support_question"
    )


# =====================================================
# REFLECT FUNCTION
# =====================================================

async def generate_support_response(
    name,
    question
):

    response = await client.areflect(

        bank_id="customer-support",

        query=(

            f"You are a helpful customer support agent. "

            f"The customer is {name}. "

            f"Use the customer's previous memories "
            f"to answer this question: {question}. "

            f"Be helpful, polite and empathetic. "

            f"Do not invent specific facts, dates, "
            f"order numbers, or previous actions "
            f"that are not present in the customer's memories."
        ),

        budget="low"
    )

    return response


# =====================================================
# ASK AGENT BUTTON
# =====================================================

if st.button(
    "🤖 Ask CustomerSupportAgent",
    type="primary"
):

    if support_customer and support_question:

        try:

            response = asyncio.run(
                generate_support_response(
                    support_customer,
                    support_question
                )
            )

            st.success(
                "Response generated using customer memory! 🧠"
            )

            st.markdown(
                "### 💬 Agent Response"
            )

            st.info(
                response.text
            )

        except Exception as e:

            st.error(
                "Could not generate the support response."
            )

            st.code(str(e))

    else:

        st.warning(
            "Please enter the customer name and question."
        )


st.divider()


# =====================================================
# HOW IT WORKS
# =====================================================

st.markdown(
    '<div class="section-title">'
    '⚙️ How CustomerSupportAgent Works'
    '</div>',
    unsafe_allow_html=True
)


flow1, flow2, flow3, flow4 = st.columns(4)


with flow1:

    st.markdown(
        """
        ### 1️⃣ Customer

        Customer sends a support message.
        """
    )


with flow2:

    st.markdown(
        """
        ### 2️⃣ Hindsight

        Conversation is stored as memory.
        """
    )


with flow3:

    st.markdown(
        """
        ### 3️⃣ Recall

        Previous customer context is retrieved.
        """
    )


with flow4:

    st.markdown(
        """
        ### 4️⃣ Response

        AI responds using remembered context.
        """
    )


# =====================================================
# FOOTER
# =====================================================

st.divider()

st.caption(
    "CustomerSupportAgent • Powered by Hindsight Memory"
)