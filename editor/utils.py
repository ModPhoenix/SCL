def screening(string):
    string = string.replace('<script', '&lt;script')
    string = string.replace('</script>', '&lt;/script&gt;')
    string = string.replace('<link', '&lt;link')
    return string