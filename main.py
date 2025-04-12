import streamlit as st 
# custom css for styling

st.markdown(
    """
    <style>
    body {
    background-color: #f4f4f4;
)
 .main {
     background-color: white;
     padding : 20px;
     border-radius : 10px;
     box-shadow : 0px 0px 10px
 rgba(0, 0, 0, 0,1);
   width :50% ;
   margin :auto;     
 }
 h1 {
     color : #2c3e50;
     text-align : center;
     font-size  : 30px;
 }
 .stButton>button {
               background-color : #3498db;
               color : white;
               border-radius: 5px;
               padding : 10px 20px;
               border : none;
               font-size : 16px;
 }
 .stButton>button : hover{
             background-color : #2980b9;
 }
 .Selectbox, .stNumberInput{
              border-radius :5px ;
              }
          </style>
          """ ,
          unsafe_allow_html = True
)
# title of the app
st.markdown('<h1>Stylish Unit Converter</h1>' , unsafe_allow_html=True)

# sidebar for selecting conversion type
conversion_type = st.sidebar.selectbox("Choose Conversion Type:" ,["Length","Weight","Temperature"])
# function for length conversion

def convert_length(value, from_unit, to_unit):
    conversion_factors = {
        "Meters": 1,
        "Kilometers":0.001,
        "Miles": 0.000621371,
        "Feet": 3.28084,
        "Inches": 39.3701
    }
    return value*(conversion_factors[to_unit]/conversion_factors[from_unit])

 # function for weight conversion

def convert_weight(value, from_unit, to_unit):
    conversion_factors = {
        "Kilograms" : 1,
        "Grams" : 1000,
        "Pounds" : 2.20462,
        "Ounces" : 35.274
    }
    return value*(conversion_factors[to_unit]/conversion_factors[from_unit])  

  # function for temperature conversion
def convert_temperature(value, from_unit, to_unit):
    if from_unit == "Celsius": 
        if to_unit == "Fahrenheit":
            return (value * 9/5) +32
    elif to_unit == "Kelvin":
        return value + 273.15
    else:
        return value     
    if from_unit == "Fahrenheit":
        if to_unit == "Celsius":    
            return (value - 32) * 5/9
        elif to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15 
        else:
            return value
    elif from_unit == "Kelvin":
         if to_unit == "Celsius":
           return value - 273.15 
         elif to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32
         else:
             return value # same unit no conversion
#styled container

with st.container ():
    st.markdown ('<div class = "main"></div>' , unsafe_allow_html =True)
# user input
    value = st.number_input("Enter Value:" , min_value=0.0 , format="%.2f") 
# conversion logic

if conversion_type == "Temperature":
    from_unit = st.selectbox("From:",["Ceisius","Fahrenheit","Kelvin"])
    to_unit = st.selectbox("To:", ["Celsius","Fahreheit","Kelvin"])
    if st.button("Convert"):
        result = convert_temperature(value, from_unit, to_unit)
        st.success(f"Converted value: {result:.2f} {to_unit}")
elif conversion_type == "Length":
    from_unit = st.selectbox("From:",["Meters","Kilometers","Centimeters","Milimeters","Inches","Feet"])
    to_unit = st.selectbox("To:",["Meters","Kilometers","Centimeters","Milimeters","Inches","Feet"])
    if st.button("Convert"):
        result = convert_length(value, from_unit, to_unit)
        st.success(f"Converted value: {result:.2f} {to_unit}")        

elif conversion_type == "Weight":
    from_unit = st.selectbox("From:" ,["Kilograms","Grams","Pounds","Ounces"])
    to_unit =st.selectbox("To:",["Kilograms","Grams","Pounds","Ounces"])
    if st.button("Convert"):
        result = convert_weight(value, from_unit, to_unit)
        st.success(f"Converted value: {result:.2f} {to_unit}")        
                                                                                                         