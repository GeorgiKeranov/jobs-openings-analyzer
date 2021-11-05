import matplotlib.pyplot as plt
import numpy as np

def visualize_data_in_pie_chart(labels, values):
	plt.pie(values, labels = labels, autopct = '%1.1f%%', startangle = 90)
	 
	# plotting legend
	plt.axis("equal")
	 
	# showing the plot
	plt.show()

def visualize_data_in_grouped_bar_chart(labels, on_site_jobs_count, remote_jobs_count, chart_title):
	labels_indexes = np.arange(len(labels))
	bars_width = 0.40

	fig, ax = plt.subplots()
	rects1 = ax.bar(labels_indexes - bars_width/2, on_site_jobs_count, bars_width, label='Worldwide On-Site Jobs')
	rects2 = ax.bar(labels_indexes + bars_width/2, remote_jobs_count, bars_width, label='Worldwide Remote Jobs')

	# Add some text for labels, title and custom x-axis tick labels, etc.
	ax.set_ylabel(chart_title)
	ax.set_title('Job Openings')
	ax.set_xticks(labels_indexes)
	ax.set_xticklabels(labels)
	ax.legend()

	ax.bar_label(rects1, padding=0)
	ax.bar_label(rects2, padding=0)

	fig.tight_layout()

	plt.show()

def visualize_data_in_bar_chart(labels, values, chart_title):
	labels_indexes = np.arange(len(labels))
	bars_width = 0.40

	fig, ax = plt.subplots()
	rect = ax.bar(labels_indexes, values, bars_width)

	# Add some text for labels, title and custom x-axis tick labels, etc.
	ax.set_ylabel('Job Openings')
	ax.set_title(chart_title)
	ax.set_xticks(labels_indexes)
	ax.set_xticklabels(labels)
	ax.legend()

	ax.bar_label(rect, padding=0)

	fig.tight_layout()

	plt.show()
