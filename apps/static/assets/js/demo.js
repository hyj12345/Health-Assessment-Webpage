"use strict";
// Cicle Chart
Circles.create({
	id:           'task-complete',
	radius:       50,
	value:        80,
	maxValue:     100,
	width:        5,
	text:         function(value){return value + '%';},
	colors:       ['#36a3f7', '#fff'],
	duration:     400,
	wrpClass:     'circles-wrp',
	textClass:    'circles-text',
	styleWrapper: true,
	styleText:    true
})

//Notify
$.notify({
	icon: 'flaticon-alarm-1',
	title: 'Hi! Dear User',
	message: 'Welcome to the Health Assessment Webpage',
},{
	type: 'info',
	placement: {
		from: "bottom",
		align: "right"
	},
	time: 1000,
});




// JQVmap
var dataColor = {
	'mo': 150,
	'fl': 35,
	'or': 45
}
$('#map-example').vectorMap(
{
	    map: 'usa_en',
	backgroundColor: 'transparent',
          enableZoom: true,
          showTooltip: true,
          selectedColor: null,
          hoverColor: null,
          colors: {
			  wy: '#87d36f',
wv: '#77cf7b',
wi: '#91d467',
wa: '#e0d92e',
vt: '#83d271',
ut: '#eebb3c',
tx: '#d7d934',
tn: '#74ce7d',
sd: '#94d564',
sc: '#d3d937',
ri: '#8dd469',
pa: '#e5d130',
or: '#7ad079',
ok: '#aed851',
oh: '#ecc237',
ny: '#c2d943',
nv: '#64ca8a',
nm: '#c6d940',
nj: '#ee9f50',
nh: '#80d174',
ne: '#e58e5e',
nd: '#a3d759',
nc: '#bed946',
mt: '#cbd93d',
ms: '#9bd65f',
mo: '#98d562',
mn: '#ec9955',
mi: '#f0b341',
me: '#b2d84e',
md: '#f0ac46',
ma: '#e9945a',
la: '#69cb86',
ky: '#dcd931',
ks: '#e08962',
in: '#cfd93a',
il: '#71ce80',
id: '#6ecd82',
ia: '#aad754',
hi: '#a7d757',
ga: '#bad948',
fl: '#db8566',
de: '#66ca88',
dc: '#61c98c',
ct: '#9fd65c',
co: '#efa64b',
ca: '#e9ca33',
az: '#5dc790',
ar: '#6bcc84',
al: '#8ad36c',
ak: '#5fc88e',},
	// map: 'world_en',
	// backgroundColor: 'transparent',
	// borderColor: '#fff',
	// borderWidth: 2,
	// color: '#e4e4e4',
	// enableZoom: true,
	// hoverColor: '#35cd3a',
	// hoverOpacity: null,
	// normalizeFunction: 'linear',
	// scaleColors: ['#b6d6ff', '#005ace'],
	// selectedColor: '#35cd3a',
	// selectedRegions: ['mo', 'fl', 'or'],
	// showTooltip: true,
	onRegionClick: function(element, code, region)
	{
		return false;
	}
});

//Chart


var ctx = document.getElementById('statisticsChart').getContext('2d');

var statisticsChart = new Chart(ctx, {
	type: 'line',
	data: {
		labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
		datasets: [ {
			label: "Subscribers",
			borderColor: '#f3545d',
			pointBackgroundColor: 'rgba(243, 84, 93, 0.6)',
			pointRadius: 0,
			backgroundColor: 'rgba(243, 84, 93, 0.4)',
			legendColor: '#f3545d',
			fill: true,
			borderWidth: 2,
			data: [154, 184, 175, 203, 210, 231, 240, 278, 252, 312, 320, 374]
		}, {
			label: "New Visitors",
			borderColor: '#fdaf4b',
			pointBackgroundColor: 'rgba(253, 175, 75, 0.6)',
			pointRadius: 0,
			backgroundColor: 'rgba(253, 175, 75, 0.4)',
			legendColor: '#fdaf4b',
			fill: true,
			borderWidth: 2,
			data: [256, 230, 245, 287, 240, 250, 230, 295, 331, 431, 456, 521]
		}, {
			label: "Active Users",
			borderColor: '#177dff',
			pointBackgroundColor: 'rgba(23, 125, 255, 0.6)',
			pointRadius: 0,
			backgroundColor: 'rgba(23, 125, 255, 0.4)',
			legendColor: '#177dff',
			fill: true,
			borderWidth: 2,
			data: [542, 480, 430, 550, 530, 453, 380, 434, 568, 610, 700, 900]
		}]
	},
	options : {
		responsive: true, 
		maintainAspectRatio: false,
		legend: {
			display: false
		},
		tooltips: {
			bodySpacing: 4,
			mode:"nearest",
			intersect: 0,
			position:"nearest",
			xPadding:10,
			yPadding:10,
			caretPadding:10
		},
		layout:{
			padding:{left:5,right:5,top:15,bottom:15}
		},
		scales: {
			yAxes: [{
				ticks: {
					fontStyle: "500",
					beginAtZero: false,
					maxTicksLimit: 5,
					padding: 10
				},
				gridLines: {
					drawTicks: false,
					display: false
				}
			}],
			xAxes: [{
				gridLines: {
					zeroLineColor: "transparent"
				},
				ticks: {
					padding: 10,
					fontStyle: "500"
				}
			}]
		}, 
		legendCallback: function(chart) { 
			var text = []; 
			text.push('<ul class="' + chart.id + '-legend html-legend">'); 
			for (var i = 0; i < chart.data.datasets.length; i++) { 
				text.push('<li><span style="background-color:' + chart.data.datasets[i].legendColor + '"></span>'); 
				if (chart.data.datasets[i].label) { 
					text.push(chart.data.datasets[i].label); 
				} 
				text.push('</li>'); 
			} 
			text.push('</ul>'); 
			return text.join(''); 
		}  
	}
});

var myLegendContainer = document.getElementById("myChartLegend");

// generate HTML legend
myLegendContainer.innerHTML = statisticsChart.generateLegend();

// bind onClick event to all LI-tags of the legend
var legendItems = myLegendContainer.getElementsByTagName('li');
for (var i = 0; i < legendItems.length; i += 1) {
	legendItems[i].addEventListener("click", legendClickCallback, false);
}

var dailySalesChart = document.getElementById('dailySalesChart').getContext('2d');

var myDailySalesChart = new Chart(dailySalesChart, {
	type: 'line',
	data: {
		labels:["January",
		"February",
		"March",
		"April",
		"May",
		"June",
		"July",
		"August",
		"September"],
		datasets:[ {
			label: "Sales Analytics", fill: !0, backgroundColor: "rgba(255,255,255,0.2)", borderColor: "#fff", borderCapStyle: "butt", borderDash: [], borderDashOffset: 0, pointBorderColor: "#fff", pointBackgroundColor: "#fff", pointBorderWidth: 1, pointHoverRadius: 5, pointHoverBackgroundColor: "#fff", pointHoverBorderColor: "#fff", pointHoverBorderWidth: 1, pointRadius: 1, pointHitRadius: 5, data: [65, 59, 80, 81, 56, 55, 40, 35, 30]
		}]
	},
	options : {
		maintainAspectRatio:!1, legend: {
			display: !1
		}
		, animation: {
			easing: "easeInOutBack"
		}
		, scales: {
			yAxes:[ {
				display:!1, ticks: {
					fontColor: "rgba(0,0,0,0.5)", fontStyle: "bold", beginAtZero: !0, maxTicksLimit: 10, padding: 0
				}
				, gridLines: {
					drawTicks: !1, display: !1
				}
			}
			], xAxes:[ {
				display:!1, gridLines: {
					zeroLineColor: "transparent"
				}
				, ticks: {
					padding: -20, fontColor: "rgba(255,255,255,0.2)", fontStyle: "bold"
				}
			}
			]
		}
	}
});

$("#activeUsersChart").sparkline([112,109,120,107,110,85,87,90,102,109,120,99,110,85,87,94], {
	type: 'bar',
	height: '100',
	barWidth: 9,
	barSpacing: 10,
	barColor: 'rgba(255,255,255,.3)'
});

var topProductsChart = document.getElementById('topProductsChart').getContext('2d');

var myTopProductsChart = new Chart(topProductsChart, {
	type:"line",
	data: {
		labels:["January",
		"February",
		"March",
		"April",
		"May",
		"June",
		"July",
		"August",
		"September",
		"October",
		"January",
		"February",
		"March",
		"April",
		"May",
		"June",
		"July",
		"August",
		"September",
		"October",
		"January",
		"February",
		"March",
		"April",
		"May",
		"June",
		"July",
		"August",
		"September",
		"October",
		"January",
		"February",
		"March",
		"April"],
		datasets:[ {
			label: "Sales Analytics", fill: !0, backgroundColor: "rgba(53, 205, 58, 0.2)", borderColor: "#35cd3a", borderCapStyle: "butt", borderDash: [], borderDashOffset: 0, pointBorderColor: "#35cd3a", pointBackgroundColor: "#35cd3a", pointBorderWidth: 1, pointHoverRadius: 5, pointHoverBackgroundColor: "#35cd3a", pointHoverBorderColor: "#35cd3a", pointHoverBorderWidth: 1, pointRadius: 1, pointHitRadius: 5, data: [20, 10, 18, 14, 32, 18, 15, 22, 8, 6, 17, 12, 17, 18, 14, 25, 18, 12, 19, 21, 16, 14, 24, 21, 13, 15, 27, 29, 21, 11, 14, 19, 21, 17]
		}
		]
	},
	options : {
		maintainAspectRatio:!1, legend: {
			display: !1
		}
		, animation: {
			easing: "easeInOutBack"
		}
		, scales: {
			yAxes:[ {
				display:!1, ticks: {
					fontColor: "rgba(0,0,0,0.5)", fontStyle: "bold", beginAtZero: !0, maxTicksLimit: 10, padding: 0
				}
				, gridLines: {
					drawTicks: !1, display: !1
				}
			}
			], xAxes:[ {
				display:!1, gridLines: {
					zeroLineColor: "transparent"
				}
				, ticks: {
					padding: -20, fontColor: "rgba(255,255,255,0.2)", fontStyle: "bold"
				}
			}
			]
		}
	}
});

var radarChart = document.getElementById('radarChart').getContext('2d');
var myRadarChart = new Chart(radarChart, {
			type: 'radar',
			data: {
				labels: ['Running', 'Swimming', 'Eating', 'Cycling', 'Jumping'],
				datasets: [{
					data: [20, 10, 30, 2, 30],
					borderColor: '#1d7af3',
					backgroundColor : 'rgba(29, 122, 243, 0.25)',
					pointBackgroundColor: "#1d7af3",
					pointHoverRadius: 4,
					pointRadius: 3,
					label: 'Team 1'
				}, {
					data: [10, 20, 15, 30, 22],
					borderColor: '#716aca',
					backgroundColor: 'rgba(113, 106, 202, 0.25)',
					pointBackgroundColor: "#716aca",
					pointHoverRadius: 4,
					pointRadius: 3,
					label: 'Team 2'
				},
				]
			},
			options : {
				responsive: true,
				maintainAspectRatio: false,
				legend : {
					position: 'bottom'
				}
			}
		});
