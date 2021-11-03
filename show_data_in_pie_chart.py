import matplotlib.pyplot as plt

def show_data_in_pie_chart(data_values, data_labels):
	plt.pie(data_values, labels = data_labels, autopct='%1.1f%%',startangle=90)
	 
	# plotting legend
	plt.axis("equal")
	 
	# showing the plot
	plt.show()
