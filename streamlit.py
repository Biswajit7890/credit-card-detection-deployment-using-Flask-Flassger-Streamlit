
import pickle
import streamlit as st

pickle_in = open("cat_model.pkl", "rb")
classifier = pickle.load(pickle_in)



def welcome():
    return "credit card Lead Detection"



def predict_credit_card_Lead(st_gen,Age,region_val,occup_val,Channel_val,Vintage,credit_val,Avg_Account_Balance,Active_value):
    prediction = classifier.predict([[st_gen,Age,region_val,occup_val,Channel_val,Vintage,credit_val,Avg_Account_Balance,Active_value]])
    return prediction

def main():

    st.title('credit card lead detection')
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Credit Card Lead Detection ML App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    Gender = st.radio("Gender", ('Female', 'Male'))
    if (Gender == 'Female'):
        st_gen = 1
    else:
        st_gen = 2
    Age = st.text_input("Age", "Type Here")
    Region_Code = st.radio("Region_Code", ('RG268', 'RG277', 'RG270'))
    if (Region_Code == 'RG268'):
        region_val = 1
    elif (Region_Code == 'RG277'):
        region_val = 2
    else:
        region_val = 3
    Occupation = st.radio("Occupation", ('Other', 'Salaried', 'Self_Employed', 'Entrepreneur'))
    if (Occupation == 'Other'):
        occup_val = 1
    elif (Occupation == 'Salaried'):
        occup_val = 2
    elif (Occupation == 'Self_Employed'):
        occup_val = 3
    else:
        occup_val = 4
    Channel_Code = st.radio("Channel_Code", ('X3', 'X1', 'X2', 'X4'))
    if (Channel_Code == 'X3'):
        Channel_val = 3
    elif (Channel_Code == 'X1'):
        Channel_val = 1
    elif (Channel_Code == 'X2'):
        Channel_val = 2
    else:
        Channel_val = 4
    Vintage = st.text_input("Vintage", "Type Here")
    Credit_Product = st.radio("Credit_Product", ('No', 'Yes'))
    if (Credit_Product == 'No'):
        credit_val = 1
    elif (Credit_Product == 'Yes'):
        credit_val = 2
    Avg_Account_Balance = st.text_input("Avg_Account_Balance", "Type Here")
    Is_Active = st.radio("Is_Active", ('No', 'Yes'))
    if (Is_Active == 'No'):
        Active_value = 1
    else:
        Active_value = 2
    result = ""
    if st.button("Predict"):
        result = predict_credit_card_Lead(st_gen, Age, region_val, occup_val, Channel_val, Vintage, credit_val,
                                          Avg_Account_Balance, Active_value)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()


