bot_icon_base64 = "data:image/svg+xml;base64,<BASE64_IMAGE_STRING>"
user_icon_base64 = "data:image/png;base64,<BASE64_IMAGE_STRING>"

css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex;
}
.chat-message.user {
    background-color: rgba(240, 242, 246, 0.5); /*#f0f0f0; Subtle color for user message background */
    flex-direction: row-reverse; /* Right align user icon */
}
.chat-message.bot {
    background-color: #fff; /*#e0e0e0;  Subtle color for bot message background */
}
.chat-message .avatar {
    width: 10%; /* Reduce width to 10% */
}
.chat-message .avatar img {
    max-width: 39px; /* Reduce size by 50% */
    max-height: 39px; /* Reduce size by 50% */
    border-radius: 50%;
    object-fit: cover;
}
.chat-message .useravatar {
    margin-left: 20px;margin-right: -20px;
}
.chat-message .useravatar img {
    max-width: 35px !important; /* Reduce size by 50% */
    max-height: 35px !important; /* Reduce size by 50% */
}
.chat-message .message {
    width: 90%;
    padding: 0 1.5rem;
    color: #000; /* Black text color for readability */
    padding-left: 0px !important;
}
.chat-message.user .message {
    align-content: space-evenly;
    text-align: right; /* Right align text for user message */
    padding-right: 0px;
}
'''

bot_template = f'''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://t3.ftcdn.net/jpg/01/36/49/90/360_F_136499077_xp7bSQB4Dx13ktQp0OYJ5ricWXhiFtD2.jpg">
    </div>
    <div class="message">{{{{MSG}}}}</div>
</div>
'''

user_template = f'''
<div class="chat-message user">
    <div class="avatar useravatar">
        <img src="https://i.pinimg.com/736x/8b/16/7a/8b167af653c2399dd93b952a48740620.jpg">
    </div>    
    <div class="message">{{{{MSG}}}}</div>
</div>
'''

expander_css = '<style>[data-testid="stExpander"] div:has(>.streamlit-expanderContent) {overflow: scroll;height: 45vh;}</style>'