import streamlit as st

def style_background_home():

    st.markdown("""
    <style>

    .stApp{
        background: linear-gradient(
            135deg,
            #5B5FEF 0%,
            #6D63F7 45%,
            #8A63F6 100%
        ) !important;
        
    .block-container{
        max-width:px;
        padding-top:2rem;
    }

    div[data-testid="stColumn"]{

        background:white !important;

        padding:2.2rem !important;

        border-radius:28px !important;

        border:1px solid rgba(255,255,255,.15);

        box-shadow:
            0 15px 40px rgba(0,0,0,.15);

        transition:all .35s ease;

        text-align:center;

    }

    div[data-testid="stColumn"]:hover{

        transform:translateY(-8px);

        box-shadow:
            0 25px 60px rgba(0,0,0,.22);

    }

    div[data-testid="stColumn"] img{

        transition:.3s;

    }

    div[data-testid="stColumn"]:hover img{

        transform:scale(1.08);

    }

    hr{
        border:none;
    }

    </style>
    """, unsafe_allow_html=True)
    

def style_background_dashboard():

    st.markdown("""
        <style>

                .stApp {

                    background: #E0E3FF !important;
                }

        </style>  

                """
            ,unsafe_allow_html=True)
    

    

def style_base_layout():
# asdasd
    st.markdown("""
        <style>
         @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&family=Roboto:ital,wght@0,100..900;1,100..900&display=swap');
         @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');
                
         /* Hide Top Bar of streamlit */
                
            #MainMenu, footer, header {
                visibility: hidden;
            }
                
            .block-container {
                padding-top:1.5rem !important;    
            }

            h1 {
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: 3.5rem !important;
                text-shadow: 2px 2px 0 #333;
                line-height:1.1 1important;
                margin-bottom:0rem !important;
            }
                

            h2 {
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: 2rem !important;
                line-height:0.9 !important;
                margin-bottom:0rem !important;
            }
                
            h3, h4, p {
                font-family: 'Outfit', sans-serif;    
            }
                

            button{
                border-radius: 1.5rem !important;
                background: linear-gradient(90deg, #4F46E5, #6366F1);
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
                }

            button[kind="secondary"]{
               background: linear-gradient(90deg, #EC4899, #DB2777);
                border-radius: 1.5rem !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
                }

            button[kind="tertiary"]{
                border-radius: 1.5rem !important;
                background-color: black !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
                }


            button:hover{
                transform :scale(1.05)}
        </style>  

                """
            ,unsafe_allow_html=True)

