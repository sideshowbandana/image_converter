'use strict'

const repl = require('repl');
const { exec } = require('child_process');
const gm = require('gm').subClass({imageMagick: true});
const fileType = require('file-type');
require('gm-base64');


repl.start('> ');
