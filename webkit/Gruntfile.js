
module.exports = function(grunt) {
	 grunt.initConfig({
	  pkg: grunt.file.readJSON('hextris-gh-pages/package.json'),
	  nodewebkit: {
		options: {
			build_dir: './webkitbuilds', // Where the build version of my node-webkit app is saved
			mac: true, // We want to build it for mac
			win: true, // We want to build it for win
			linux32: true, // We don't need linux32
			linux64: true, // We don't need linux64
		},
		src: ['hextris-gh-pages/**'], // Your node-webkit app
	  },
	}),
	grunt.loadNpmTasks('grunt-node-webkit-builder');
	grunt.registerTask('default',["nodewebkit"]);
}
