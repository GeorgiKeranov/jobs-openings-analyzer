import matplotlib.pyplot as plt
import numpy as np

def visualize_data_in_pie_chart(labels, values):
	plt.style.use('seaborn')

	plt.pie(values, labels = labels, autopct = '%1.1f%%', startangle = 90)
	 
	# plotting legend
	plt.axis("equal")
	 
	# showing the plot
	plt.show()

def visualize_data_in_grouped_bar_chart(labels, on_site_jobs_count, remote_jobs_count, chart_title):
	plt.style.use('seaborn')

	labels_indexes = np.arange(len(labels))
	bars_width = 0.40

	fig, ax = plt.subplots()
	rects1 = ax.bar(labels_indexes - bars_width/2, on_site_jobs_count, bars_width, label='Worldwide On-Site Jobs')
	rects2 = ax.bar(labels_indexes + bars_width/2, remote_jobs_count, bars_width, label='Worldwide Remote Jobs')

	# Add some text for labels, title and custom x-axis tick labels, etc.
	ax.set_title(chart_title)
	ax.set_ylabel('Job Openings')
	ax.set_xticks(labels_indexes)
	ax.set_xticklabels(labels)
	ax.legend()

	ax.bar_label(rects1, padding=3)
	ax.bar_label(rects2, padding=3)

	plt.show()

def visualize_data_in_bar_chart(labels, values, chart_title):
	plt.style.use('seaborn')

	plt.bar(labels, values)
	plt.title(chart_title)
	plt.ylabel("Job Openings")

	for index in range(len(labels)):
		plt.text(index, values[index], values[index], ha='center', va='bottom')

	plt.show()
