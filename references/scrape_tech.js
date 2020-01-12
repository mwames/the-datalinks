var nodes = document.querySelectorAll('font');
var name = nodes[0].innerText;
var track = nodes[2].innerText;
var description = nodes[3].innerText;

var nodes = document.querySelectorAll('tr');
var technologies = nodes[10].cells[1]
                            .innerText
                            .split('\n')
                            .slice(1)
                            .map(s => s.trim());

var base_facilities

var x = {
    name: name,
    track: track,
    level: "",
    base_facilities: base_facilities,
    technologies: technologies,
    unit_advances: unit_advances,
    miscellaneous: miscellaneous,
    quote: {
        text: "",
        by: "",
        work: "\"\""
    },
    description: description
};