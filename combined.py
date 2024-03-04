import matplotlib.pyplot as plt
import numpy as np
import math as mt
import streamlit as st

option1=st.checkbox('Drag')
#option2=st.checkbox('Projectile')
option3=st.checkbox('Thermodynamics')
option4=st.checkbox('Heat Engine')

if option1:
    st.title('DRAG FORCE ON A FALLING BODY')
    st.header('',divider='rainbow')
    #DRAG FORCE
    D = st.number_input('Enter the Drag Coefficient',min_value=0.001)
    m = st.number_input('Enter the mass',min_value=0.001)
    g = st.number_input('Enter the gravitational accleration value',min_value=0.001)
    Y=[0]
    t1=0
    t2=10
    n = 10000
    h = (t2-t1)/n
    A=st.number_input('Enter area of cross section of object',min_value=0.001)

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
    plt.savefig('drag.jpg')
    st.image('drag.jpg')
#plt.show()

#========================================================
#========================================================
#========================================================

#PROJECTILE MOTION


if option3:
    def plot_process(process_type, pressure_values, volume_values):
        plt.figure(figsize=(8, 6))

        if process_type == "Isothermal":
            plt.plot(volume_values, pressure_values, label="Isothermal Process", color="b")
        elif process_type == "Isobaric":
            plt.plot(volume_values, pressure_values, label="Isobaric Process", color="r")
        elif process_type == "Isochoric":
            plt.plot(volume_values, pressure_values, label="Isochoric Process", color="g")
        elif process_type == "Adiabatic":
            plt.plot(volume_values, pressure_values, label="Adiabatic Process", color="m")
        else:
            st.error("Invalid process type selected!")
            return

        plt.xlabel("Volume")
        plt.ylabel("Pressure")
        plt.title(f"{process_type} Process")
        plt.legend()
        plt.grid(True)
        plt.savefig('graph.jpg')
        st.image('graph.jpg')
        # st.pyplot()


    def main():
        st.title("Thermodynamic Processes Visualization")

        process_type = st.selectbox("Select process type:",
                                    ["Isothermal", "Isobaric", "Isochoric", "Adiabatic"])

        pressure_values = st.text_input("Enter pressure values (comma-separated):")
        volume_values = st.text_input("Enter volume values (comma-separated):")

        if st.button("Plot"):
            try:
                pressure_values = [float(p) for p in pressure_values.split(",")]
                volume_values = [float(v) for v in volume_values.split(",")]

                plot_process(process_type, pressure_values, volume_values)
            except ValueError:
                st.error("Please enter valid pressure and volume values!")


    if __name__ == "__main__":
        main()
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