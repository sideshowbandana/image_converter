'use strict'

const { exec } = require('child_process');
const gm = require('gm').subClass({imageMagick: true});
const fileType = require('file-type');
require('gm-base64');

console.log('starting function');
exports.handle = function(e, ctx, cb) {
  // exec('convert -version', (err, stdout, stderr) => {
  //   if (err) {
  //     // node couldn't execute the command
  //     return;
  //   }

  //   // the *entire* stdout and stderr (buffered)
  //   console.log('convert -version');
  //   console.log(`stdout: ${stdout}`);
  //   console.log(`stderr: ${stderr}`);
  // });

  let input = Buffer.from(e.image, 'base64');
  let fileMime = fileType(input);
  let image = gm(input, 'input.svg');
  image.toBase64('jpg', function(err, base64) {
    console.log(base64);
    cb(null, base64);
  });
}
