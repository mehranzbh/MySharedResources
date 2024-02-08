
mzabi@Mehrannn_Asus MINGW64 /c/My-files/Codes/Tableau/Superstore
$ node --version
v20.11.0

mzabi@Mehrannn_Asus MINGW64 /c/My-files/Codes/Tableau/Superstore
$ npm init
This utility will walk you through creating a package.json file.
It only covers the most common items, and tries to guess sensible defaults.

See `npm help init` for definitive documentation on these fields
and exactly what they do.

Use `npm install <pkg>` afterwards to install a package and
save it as a dependency in the package.json file.

Press ^C at any time to quit.
package name: (superstore)
version: (1.0.0)
description:
entry point: (index.js)
test command:
git repository:
keywords:
author:
license: (ISC)
About to write to C:\My-files\Codes\Tableau\Superstore\package.json:

{
  "name": "superstore",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "author": "",
  "license": "ISC"
}


Is this OK? (yes) yes
npm notice
npm notice New minor version of npm available! 10.2.4 -> 10.4.0
npm notice Changelog: <https://github.com/npm/cli/releases/tag/v10.4.0>
npm notice Run `npm install -g npm@10.4.0` to update!
npm notice

mzabi@Mehrannn_Asus MINGW64 /c/My-files/Codes/Tableau/Superstore
$ ^C

mzabi@Mehrannn_Asus MINGW64 /c/My-files/Codes/Tableau/Superstore
$ Run `npm install -g npm@10.4.0` to update
npm ERR! process terminated
npm ERR! signal SIGINT

npm ERR! A complete log of this run can be found in: C:\Users\mzabi\AppData\Local\npm-cache\_logs\2024-02-07T17_49_09_217Z-debug-0.log


mzabi@Mehrannn_Asus MINGW64 /c/My-files/Codes/Tableau/Superstore
$ npm install -g npm@10.4.0

added 1 package in 2s

24 packages are looking for funding
  run `npm fund` for details

mzabi@Mehrannn_Asus MINGW64 /c/My-files/Codes/Tableau/Superstore
$ ls
 EmbededCode.txt
'VG Contest_Super Sample Superstore_Ryan Sleeper_v2023.2.twbx'
 index.html
 package.json
 sample_-_superstore.xls

mzabi@Mehrannn_Asus MINGW64 /c/My-files/Codes/Tableau/Superstore
$ npm install express

added 63 packages, and audited 64 packages in 3s

11 packages are looking for funding
  run `npm fund` for details

found 0 vulnerabilities

mzabi@Mehrannn_Asus MINGW64 /c/My-files/Codes/Tableau/Superstore
$ touch server.js

mzabi@Mehrannn_Asus MINGW64 /c/My-files/Codes/Tableau/Superstore
$ vim server.js

## to be added to server.js
##      const express = require('express');
##      const path = require('path');
##      const app = express();
##      const PORT = 3000;
##      
##      // Serve static files from the 'public' directory
##      app.use(express.static('public'));
##      
##      app.get('/', (req, res) => {
##          res.sendFile(path.join(__dirname, '/public/index.html'));
##      });
##      
##      app.listen(PORT, () => {
##          console.log(`Server running on http://localhost:${PORT}`);
##      });
##server.js edit finish

mzabi@Mehrannn_Asus MINGW64 /c/My-files/Codes/Tableau/Superstore
$ nnode server.js
bash: $'\302\226node': command not found

mzabi@Mehrannn_Asus MINGW64 /c/My-files/Codes/Tableau/Superstore
$ node server.js
bash: $'\302\226node': command not found

mzabi@Mehrannn_Asus MINGW64 /c/My-files/Codes/Tableau/Superstore
$ node server.js
bash: $'\302\226node': command not found

mzabi@Mehrannn_Asus MINGW64 /c/My-files/Codes/Tableau/Superstore
$ ls
 EmbededCode.txt
'VG Contest_Super Sample Superstore_Ryan Sleeper_v2023.2.twbx'
 node_modules/
 package-lock.json
 package.json
 public/
 sample_-_superstore.xls
 server.js

mzabi@Mehrannn_Asus MINGW64 /c/My-files/Codes/Tableau/Superstore
$ server.js
bash: server.js: command not found

mzabi@Mehrannn_Asus MINGW64 /c/My-files/Codes/Tableau/Superstore
$ node --version
v20.11.0

mzabi@Mehrannn_Asus MINGW64 /c/My-files/Codes/Tableau/Superstore
$ ls
 EmbededCode.txt
'VG Contest_Super Sample Superstore_Ryan Sleeper_v2023.2.twbx'
 node_modules/
 package-lock.json
 package.json
 public/
 sample_-_superstore.xls
 server.js

mzabi@Mehrannn_Asus MINGW64 /c/My-files/Codes/Tableau/Superstore
$ node server.js
Server running on http://localhost:3000
