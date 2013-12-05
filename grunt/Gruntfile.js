module.exports = function(grunt) {

  require('matchdep').filterDev('grunt-*').forEach(grunt.loadNpmTasks);

  // Project configuration.
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    uglify: {
      options: {
        banner: '/*! <%= pkg.name %> <%= grunt.template.today("yyyy-mm-dd") %> */\n'
      },
      build: {
        src: 'src/<%= pkg.name %>.js',
        dest: 'build/<%= pkg.name %>.min.js'
      }
    },

   compass: {
      dev: {
        options: {
          config: 'config.rb',
          force: true,
        }
      },
      forcecompile: true
    },

  concat: {
    options: {
      stripBanners: true,
      banner: '/*! <%= pkg.name %> - v<%= pkg.version %> - ' +
        '<%= grunt.template.today("yyyy-mm-dd") %> */',
    },
    css_main: {
      src: ['app/**/*.css'],
      dest: '../static/css/main.css',
    },
    css_vendor: {
      src: ['vendor/**/*.css'],
      dest: '../static/css/vendor.css',
    },

    js_vendor: {
      src: ['vendor/**/jquery.linkify.js', 'vendor/**/jquery.form.js'],
      dest: '../static/js/vendor.js'
    },

    js_main: {
      src: ['app/**/*.js'],
      dest: '../static/js/main.js'
    }
  },


  watch: {
      sass: {
        files: ['app/**/css/**/*.scss', 'vendor/**/css/**/*.scss', 'vendor/**/js/*.js'],
        tasks: ['compass:dev', 'concat']
      },
      options: {
         livereload: true
      }
    },


  });


  // Default task(s).
  grunt.registerTask('default', 'watch');
  grunt.registerTask('build', 'compass:dev');
  grunt.registerTask('combine', 'concat');

};
