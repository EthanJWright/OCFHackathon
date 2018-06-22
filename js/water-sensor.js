// Copyright 2016 Intel Corporation
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

// This mock sensor implementation triggers an event with some data every once in a while

// Return a random integer between 0 and @upperLimit


var _ = {
	extend: require( "lodash.assignin" ),
	bind: require( "lodash.bind" )
};

var net = require('net'),
      fs = require('fs'),
      connections = {},
      server;

const SOCKETFILE = '/var/iotivity/toOCFWater';



var properties = {
  "value" : true
}



var bound;
var MockSensor = function MockSensor() {
    function trigger() {
      this.emit( "change", this.currentData() );
      bound = _.bind( trigger, this);
//        setTimeout( _.bind( trigger, this ), randomInteger( 1000 ) + 1000 );
    }
    if ( !this._isMockSensor ) {
        return new MockSensor();
    }
  bound = _.bind( trigger, this);
//    setTimeout( _.bind( trigger, this ), randomInteger( 1000 ) + 1000 );
};
/*
var MockSensor = function MockSensor() {
	function trigger() {
		this.emit( "change", this.currentData() );
		setTimeout( _.bind( trigger, this ), randomInteger( 1000 ) + 1000 );
	}
	if ( !this._isMockSensor ) {
		return new MockSensor();
	}
	setTimeout( _.bind( trigger, this ), randomInteger( 1000 ) + 1000 );
};
*/
require( "util" ).inherits( MockSensor, require( "events" ).EventEmitter );



_.extend( MockSensor.prototype, {
	_isMockSensor: true,
	currentData: function() {
		return {
          properties
		};
	}
} );

function createServer(socket){
    console.log('Creating server.');
    var server = net.createServer(function(stream) {
        console.log('Connection acknowledged.');

        // Store all connections so we can terminate them if the server closes
        // An object is better than an array for these.
        var self = Date.now();
        connections[self] = (stream);
        stream.on('end', function() {
            console.log('Client disconnected.');
            delete connections[self];
        });

        // Messages are buffers. use toString
        stream.on('data', function(msg) {
            var obj = JSON.parse(msg);
            console.log("OBJ IS: " + JSON.stringify(obj));
            
            if (obj.value == "True") {
                console.log("Running Low on Water");
            }

            else if (obj.value == "False") {

              console.log("Water level normal");

            }

            properties['value'] = msg['value'];
            bound();

        });
    })
    .listen(socket)
    .on('connection', function(socket){
        console.log('Client connected.');
    })
    ;
    return server;
}


// check for failed cleanup
console.log('Checking for leftover socket.');
fs.stat(SOCKETFILE, function (err, stats) {
    if (err) {
        // start server
        console.log('No leftover socket found.');
        server = createServer(SOCKETFILE); return;
    }
    // remove file then start server
    console.log('Removing leftover socket.')
    fs.unlink(SOCKETFILE, function(err){
        if(err){
            // This should never happen.
            console.error(err); process.exit(0);
        }
        server = createServer(SOCKETFILE); return;
    });
});



module.exports = MockSensor;
