$(document).ready( function () {
    let data = $('#table_id').DataTable( function(){
        "lengthMenu": [[3, 10, 25, 50, -1], [3, 10, 25, 50, "All"]]
    });

} );
var bubble_map = new Datamap({
    element: document.getElementById('india'),
    scope: 'india',

    geographyConfig: {
        popupOnHover: true,
        highlightOnHover: true,
        borderColor: '#444',
        borderWidth: 0.5,
        dataUrl: 'https://rawgit.com/Anujarya300/bubble_maps/master/data/geography-data/india.topo.json'
        //dataJson: topoJsonData
    },
    fills: {
        'MAJOR': '#306596',
        'MEDIUM': '#0fa0fa',
        'MINOR': '#bada55',
        defaultFill: '#dddddd'
    },
    data: {
        'JH': { fillKey: 'MINOR' },
        'MH': { fillKey: 'MINOR' }
    },
    setProjection: function (element) {
        var projection = d3.geo.mercator()
            .center([78.9629, 23.5937]) // always in [East Latitude, North Longitude]
            .scale(1000);
        var path = d3.geo.path().projection(projection);
        return { path: path, projection: projection };
    }
});

let bubbles = [
    {
        centered: "MH",
        fillKey: "MAJOR",
        radius: 20,
        state: "Maharastra"
    },
    {
        centered: "AP",
        fillKey: "MAJOR",
        radius: 22,
        state: "Andhra Pradesh"
    },
    {
        centered: "TN",
        fillKey: "MAJOR",
        radius: 16,
        state: "Tamil Nadu"
    },
    {
        centered: "WB",
        fillKey: "MEDIUM",
        radius: 15,
        state: "West Bengal"
    },
    {
        centered: "MP",
        fillKey: "MEDIUM",
        radius: 15,
        state: "Madhya Pradesh",
        confirmed:"1020"
    },
    {
        centered: "UP",
        fillKey: "MINOR",
        radius: 8,
        state: "Uttar Pradesh"
    },
    {
        centered: "RJ",
        fillKey: "MINOR",
        radius: 7,
        state: "Rajasthan"
    }

]
// // ISO ID code for city or <state></state>
setTimeout(() => { // only start drawing bubbles on the map when map has rendered completely.
    bubble_map.bubbles(bubbles, {
        popupTemplate: function (geo, data) {
            console.log(data);
            return `<div class="hoverinfo">city: ${data.state}, Slums: ${data.radius}%</div>`;
        }
    });
}, 1000);