// requiring path and fs modules
const child_process = require('child_process');
const path = require('path');
const fs = require('fs');
let tab;

function readTheDirectory(directoryName) {
  //joining path of directory
  const directoryPath = path.join(__dirname, directoryName);
  let dir = [];
  // passing directoryPath
  fileNames = fs.readdirSync(directoryPath, { withFileTypes: true });
  // listing all files using forEach

  fileNames.forEach((dirent) => {
    ch = directoryName + '/' + dirent.name;
    if (dirent.isDirectory()) {
      dir.push(...readTheDirectory(ch));
    } else dir.push(ch);
  });
  return dir;
}
function extractComments(filePath) {
  const lines = fs.readFileSync(filePath).toString().split('\n');
  let comments = [],
    blockComment = false;
  inlineComment = false;
  for (let index = 0; index < lines.length; index++) {
    if (lines[index][0] + lines[index][1] === '//') {
      inlineComment
        ? (comments[comments.length - 1] += ' ' + lines[index].substr(2))
        : comments.push(lines[index].substr(2) + '|'),
        (inlineComment = true);
    } else inlineComment = false;

    if (lines[index][0] + lines[index][1] === '/*')
      (blockComment = true), comments.push(lines[index].substr(3) + ' ');

    if (lines[index].includes('*/'))
      (blockComment = false),
        (comments[comments.length - 1] +=
          ' ' + lines[index].substr(0, lines[index].indexOf('*/')) + '|');

    if (
      blockComment &&
      !lines[index].includes('*/') &&
      !lines[index].includes('/*')
    )
      comments[comments.length - 1] =
        comments[comments.length - 1] + ' ' + lines[index].substr(2);
  }

  return comments;
}

function verifyComments(comments) {
  return child_process
    .execFileSync('python', ['automation.py', comments])
    .toString();
}

tab = readTheDirectory('express');
for (let i = 0; i < tab.length; i++) {
  tab[i] = { name: tab[i], comments: extractComments(tab[i]) };

  if (tab[i].comments.length) {
    tab[i].comments = verifyComments(tab[i].comments);
    console.log(tab[i].comments);
  }
}
