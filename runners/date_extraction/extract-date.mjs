import { readFileSync } from 'fs';
import extractDate from 'extract-date';

try {
    const filename = process.argv[2]
    const data = readFileSync(filename, 'utf8')
    const dates = extractDate.default(data);
    console.log(JSON.stringify(dates));
} catch (err) {
  console.error(err)
}

