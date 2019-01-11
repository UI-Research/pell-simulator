var S1_DEFAULTS = {"a": "7000"}
var S2_DEFAULTS = {"a": "5000", "b": "0.5", "c": "1"}
var CHART_LABELS = ["","First quartile, dependent","Second quartile, dependent","Third quartile, dependent","Fourth quartile, dependent","Independent students","High school diploma or less","Associate’s degree or some college","Bachelor’s degree","Master’s or higher","White students","Black or African American","Hispanic or Latino","Asian","Another race","Public 4-year","Private nonprofit 4-year","Public 2-year","Private for profit","Other","No benefits","Receiving some benefits"]
 var BAR_HEIGHT = 50;

function getScenario(){
	return "s1"
}

function getUnits(){
	var scenario = getScenario();
	return "percent"
}

function getInputs(){
	var scenario = getScenario();
	var units = getUnits();
	return {"a": d3.select(".slider.a.s1").node().value }
}

function toKeyString(s){
	return s;
}

function getKey(){
	var scenario = getScenario()
	var units = getUnits()
	var inputs = getInputs()

	if (scenario == "s1"){
		return scenario + "_" + toKeyString(inputs["a"]) + "_" + units
	}else{
		return scenario + "_" + toKeyString(inputs["a"]) + "_" + toKeyString(inputs["b"]) + "_" + toKeyString(inputs["c"]) + "_" + units
	}
}


function buildChart(allData, category, scenario){
	var chartContainer = d3.select(".barContainer." + category + "." + scenario + " .chart")

	var data = allData
		.filter(function(o){ return o.category == category })
		.reverse()

	data.forEach(function(d){
		d["label"] = CHART_LABELS[+d.subcategory]
	})

	var w = 300,
		h = data.length * (BAR_HEIGHT + 10) + 40;
	var svg = chartContainer.append("svg").attr("width", w).attr("height",h)

    var margin = {top: 20, right: 20, bottom: 30, left: 170},
    width = w - margin.left - margin.right,
    height = h - margin.top - margin.bottom;
  
  
	var x = d3.scaleLinear().range([0, width]);
	var y = d3.scaleBand().range([height, 0]);

	var g = svg.append("g")
	.attr("transform", "translate(" + margin.left + "," + margin.top + ")");


	x.domain([0, .85]);
	y.domain(data.map(function(d) { return d.label; })).padding(0.4);

	// g.append("g")
	// .attr("class", "x axis")
	// .attr("transform", "translate(0," + height + ")")
	// .call(d3.axisBottom(x).ticks(5).tickFormat(function(d) { return parseInt(d / 1000); }).tickSizeInner([-height]));

	// g.append("g")
	// .attr("class", "y axis")
	// .call(d3.axisLeft(y));

	chartContainer.selectAll(".tickLabel")
		.data(data)
		.enter().append("div")
		.attr("class", "tickLabel chartLabel")
		.style("top", function(d){ return (y(d.label) + BAR_HEIGHT * .5) + "px" })
		.text(function(d){ return d.label })


	g.selectAll(".baselineBar")
	.data(data)
	.enter().append("rect")
	.attr("class", scenario + " " + "baselineBar")
	.attr("x", 0)
	.attr("height", BAR_HEIGHT*.75)
	.attr("y", function(d) { return y(d.label); })
	.attr("width", function(d) { return x(d[scenario + "_4000_percent_baseline"]); })

	g.selectAll(".bar")
	.data(data)
	.enter().append("rect")
	.attr("class", scenario + " " + category + " " + "bar")
	.attr("x", 0)
	.attr("height", BAR_HEIGHT*.75)
	.attr("y", function(d) { return y(d.label); })
	.attr("width", function(d) { return x(d[getKey()]); })

	g.selectAll(".baselineLine")
	.data(data)
	.enter().append("line")
	.attr("class", scenario + " " + "baselineLine")
	.attr("x1", function(d) { return x(d[scenario + "_4000_percent_baseline"]); })
	.attr("x2", function(d) { return x(d[scenario + "_4000_percent_baseline"]); })
	.attr("y1", function(d) { return y(d.label); })
	.attr("y2", function(d) { return y(d.label) + BAR_HEIGHT*.75; })

	g.selectAll(".baselineDot")
	.data(data)
	.enter().append("circle")
	.attr("class", scenario + " " + "baselineDot")
	.attr("cx", function(d) { return x(d[scenario + "_4000_percent_baseline"]); })
	.attr("cy", function(d) { return y(d.label) + BAR_HEIGHT*.75*.5; })
	.attr("r", 5)

}

function buildCostData(data, scenario){

}

function buildAverageData(data, scenario){

}

function updateCharts(){
	var unit = getUnits();
	var key = getKey();

	var w = 300

    var margin = {top: 20, right: 20, bottom: 30, left: 180},
    width = w - margin.left - margin.right


	var x = d3.scaleLinear().range([0, width]);
	x.domain([0, .85]);

	d3.selectAll(".bar")
	.transition()
	.attr("width", function(d) { return x(d[key]); })

	//update baseline, since units might change too

}

function updateCostData(){

}

function updateAverageData(){

}

function updateScenario(scenario){

}


function init(data){
	buildChart(data, "income", "s1")
	buildChart(data, "parentsEd", "s1")
	buildChart(data, "race", "s1")
	buildChart(data, "instType", "s1")
	buildChart(data, "benefits", "s1")

	// buildChart("income", "s2")
	// buildChart("parentsEd", "s2")
	// buildChart("race", "s2")
	// buildChart("instType", "s2")
	// buildChart("benefits", "s2")

	buildCostData(data, "s1")
	// buildCostData("s2")

	buildAverageData(data, "s1")
	// buildAverageData("s2")


}

d3.select("body")
	.on("click", function(){
		updateCharts()
	})


d3.select(".slider.a.s1").on("input", function(){
	updateCharts();
})

function getMinDiff(data){
	// data.forEach()
	console.log(data)
}

d3.csv("data/data.csv", function(data){
	init(data)
	getMinDiff(data)
})