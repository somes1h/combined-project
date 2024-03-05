import matplotlib.pyplot as plt
import numpy as np
import math as mt
import streamlit as st

st.header('Mechanical opposing force and Laws of Thermodynamics')
add_selectbox = st.sidebar.selectbox("Select the Topic",
option1=st.checkbox('Drag force proportional to $v^2$')
option2=st.checkbox('Drag force proportional to $v$')
option3=st.checkbox('Thermodynamics')
option4=st.checkbox('Heat Engine'))
if option1:
    st.title('DRAG FORCE ON A FALLING BODY FOR $v^2$')
    st.header('',divider='rainbow')
    st.subheader('Drag force is a mechanical force that acts opposite to the relative motion of any object moving with respect to a surrounding fluid.')
    
    #DRAG FORCE
    D = st.number_input('Enter the Drag Coefficient',min_value=0.001,key="1")
    m = st.number_input('Enter the mass',min_value=0.001,key="2")
    g = st.number_input('Enter the gravitational accleration value',min_value=0.001,key="3")
    Y=[0]
    t1=0
    t2=10
    n = 10000
    h = (t2-t1)/n
    A=st.number_input('Enter area of cross section of object',min_value=0.001,key="4")

    t = [t1]
    Vy = [0]
    def f1(v):
        value =g-(A*D*v**2)/(2*m)
        return value
    i = 0
    while i<=n:
        t.append(t[i]+h)
        Vy.append(Vy[i]+h*f1(Vy[i]))
        i+=1

    plt.plot(t,Vy)
    plt.xlabel('t')
    plt.ylabel('v')
    plt.grid()
    plt.title('Velocity vs Time')
    plt.savefig('drag1.jpg')
    st.image('drag1.jpg')

if option2:
    st.title('DRAG FORCE ON A FALLING BODY FOR $v$')
    st.header('', divider='rainbow')
    st.subheader('Drag force is a mechanical force that acts opposite to the relative motion of any object moving with respect to a surrounding fluid.')

    # DRAG FORCE
    D1 = st.number_input('Enter the Drag Coefficient', min_value=0.001)
    m1 = st.number_input('Enter the mass', min_value=0.001)
    g1 = st.number_input('Enter the gravitational accleration value', min_value=0.001)
    Y = [0]
    t1 = 0
    t2 = 10
    n = 10000
    h = (t2 - t1) / n
    A1 = st.number_input('Enter area of cross section of object', min_value=0.001)

    t = [t1]
    Vy = [0]


    def f1(v):
        value=g1-(A1*D1*v)/(2*m1)
        return value


    i = 0
    while i <= n:
        t.append(t[i] + h)
        Vy.append(Vy[i] + h * f1(Vy[i]))
        i += 1

    plt.plot(t, Vy)
    plt.xlabel('t')
    plt.ylabel('v')
    plt.grid()
    plt.title('Velocity vs Time')
    plt.savefig('drag2.jpg')
    st.image('drag2.jpg')
#plt.show()

#==================================================================================

#PROJECTILE MOTION


if option3:
    import numpy as np
    import matplotlib.pyplot as plt
    import streamlit as st
    
    process=st.sidebar.radio("Select the process",["Isothermal","Adiabatic","Isobaric","Isochoric","All"])
    
    #isothermal
    
    if process=="Isothermal":
        vol1=st.number_input('Enter the value of Volume')
        v1=np.linspace(1,vol1,500)
        p1=[]
        k=st.number_input('Enter the value of pressure')
    
        for i in range(0,500):
            p1.append(k/v1[i])
    
        plt.plot(v1,p1)
        plt.title('ISOTHERMAL')
        plt.xlabel('volume')
        plt.ylabel('pressure')
        plt.savefig('graph.jpg')
        st.image('graph.jpg')
    #======================================================
    
    #adiabatic
    if process=="Adiabatic":
        gamma=st.number_input('Enter the value of Gamma')
        vol2 = st.number_input('Enter the value of Volume',key="1")
        v2=np.linspace(1,vol2,500)
        p2=[]
        k=st.number_input('Enter the value of pressure')
        for i in range(0,500):
            p2.append((k/v2[i])**(gamma))
    
        plt.plot(v2,p2)
        plt.title('ADIABATIC')
        plt.xlabel('volume')
        plt.ylabel('pressure')
        plt.savefig('graph.jpg')
        st.image('graph.jpg')
    
    #======================================================
    
    #isobaric
    if process=="Isobaric":
        vol3 = st.number_input('Enter the value of Volume',key="2")
        v3=np.linspace(1,vol3,500)
        p3=st.number_input('Enter the value of pressure')
        P3=[]
        for i in range(0,500):
            P3.append(p3)
    
        plt.plot(v3,P3)
        plt.title('ISOBARIC')
        plt.xlabel('volume')
        plt.ylabel('pressure')
        plt.savefig('graph.jpg')
        st.image('graph.jpg')
    
    
    #========================================
    #isochoric
    if process=="Isochoric":
        V4=[]
        v4=st.number_input('Enter the value of Volume',key="3")
        for i in range(0,500):
            V4.append(v4)
        pres4 = st.number_input('Enter the value of Pressure')
        p4=np.linspace(1,pres4,500)
        plt.plot(V4,p4)
        plt.title('ISOCHORIC')
        plt.xlabel('volume')
        plt.ylabel('pressure')
        plt.savefig('graph.jpg')
        st.image('graph.jpg')
    #p=k*v   isobaric  isochoric
    
    if process=="All":
    
        #==================================================================================
        col1, col2 = st.columns(2)
        with col1:
            vol1 = st.number_input('Enter the value of Volume')
        with col2:
            k = st.number_input('Enter the value of pressure')
        st.text("===========================================================================")
        v1 = np.linspace(1, vol1, 500)
        p1 = []
    
        print(len(v1))
    
        for i in range(0, 500):
            p1.append(k * (1 / v1[i]))
        print(len(p1))
        plt.subplot(2, 2, 1)
        plt.plot(v1, p1)
        plt.title('ISOTHERMAL')
        plt.xlabel('volume')
        plt.ylabel('pressure')
        #====================================================================
        col1,col2,col3=st.columns(3)
        with col1:
            gamma = st.number_input('Enter the value of Gamma')
        with col2:
            vol2 = st.number_input('Enter the value of Volume', key="1")
        with col3:
            k = st.number_input('Enter the value of pressure',key="2")
        st.text("===========================================================================")
        v2 = np.linspace(1, vol2, 500)
        p2 = []
    
        for i in range(0, 500):
            p2.append(k * (1 / v2[i]) ** (gamma))
    
        plt.subplot(2, 2, 2)
        plt.plot(v2, p2)
        plt.title('ADIABATIC')
        plt.xlabel('volume')
        plt.ylabel('pressure')
    
        #======================================================================
        col1, col2 = st.columns(2)
        with col1:
            vol3 = st.number_input('Enter the value of Volume', key="3")
        with col2:
            p3 = st.number_input('Enter the value of pressure',key="4")
        v3 = np.linspace(1, vol3, 500)
        st.text("===========================================================================")
        P3 = []
        for i in range(0, 500):
            P3.append(p3)
    
        plt.subplot(2, 2, 3)
        plt.plot(v3, P3)
        plt.title('ISOBARIC')
        plt.xlabel('volume')
        plt.ylabel('pressure')
    
        #==========================================================================
    
        V4 = []
        col1, col2 = st.columns(2)
        with col1:
            v4 = st.number_input('Enter the value of Volume', key="5")
        with col2:
            pres4 = st.number_input('Enter the value of Pressure')
        for i in range(0, 500):
            V4.append(v4)
        st.text("===========================================================================")
        p4 = np.linspace(1, pres4, 500)
        plt.subplot(2, 2, 4)
        plt.plot(V4, p4)
        plt.title('ISOCHORIC')
        plt.xlabel('volume')
        plt.ylabel('pressure')
    
        plt.subplot(2, 2, 4)
        plt.plot(V4, p4)
        plt.tight_layout()
        plt.savefig('graph.jpg')
        st.image('graph.jpg')
if option4:
    def efficiency_of_heat_engine(source_temp, sink_temp):
        efficiency = 1 - (sink_temp / source_temp)
        return efficiency * 100  # Convert to percentage


    def coefficient_of_performance(source_temp, sink_temp):
        cop = source_temp / (source_temp - sink_temp)
        return cop


    def main():
        st.title("Heat Engine Efficiency & Refrigerator Coefficient of Performance Calculator")

        st.write(" Please note that temperature of (SOURCE) > (SINK)")

        source_temp = st.number_input("Enter source temperature (in Kelvin):", min_value=0.1, step=0.1)
        sink_temp = st.number_input("Enter sink temperature (in Kelvin):", min_value=0.1, step=0.1)

        if st.button("Calculate"):
            st.write("### Heat Engine Efficiency:")
            efficiency = efficiency_of_heat_engine(source_temp, sink_temp)
            st.write(f"The efficiency of the heat engine is {efficiency:.2f}%")

            st.write("### Refrigerator Coefficient of Performance:")
            cop = coefficient_of_performance(source_temp, sink_temp)
            st.write(f"The coefficient of performance of the refrigerator is {cop:.2f}")


    if __name__ == "__main__":
        main()
