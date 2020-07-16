/* Reading xls file */ 
<script src="https://cdnjs.cloudflare.com/ajax/libs/xlsx/0.16.2/jszip.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/xlsx/0.16.2/xlsx.js"></script>
<script>
    // Reading File xlxs.
    // step 1
    var ExcelToJSON = function () {
        this.parseExcel = function (file) {
            var reader = new FileReader();
            reader.onload = function (e) {
                var data = e.target.result;
                var workbook = XLSX.read(data, {
                    type: 'binary'
                });
                workbook.SheetNames.forEach(function (sheetName) {
                    // Here is your object
                    var XL_row_object = XLSX.utils.sheet_to_row_object_array(workbook.Sheets[sheetName]);
                    var json_object = JSON.stringify(XL_row_object); // เพื่อแปลงข้อมูลจากไฟล์ data.js ให้เป็น string
                    data_json = JSON.parse(json_object) // เพื่อแปลงข้อมูลจาก JSON string ให้เป็น JavaScript object ครับ 
                    $('#xlx_json').val(json_object); //แสดงข้อมูลใน TextArea
                    // console.log(data_json);
                })
            };
            reader.onerror = function (ex) {
                console.log(ex);
            };
            reader.readAsBinaryString(file);
        };
    };
    // step 2
    function handleFileSelect(evt) {
        var files = evt.target.files; // FileList object
        var xl2json = new ExcelToJSON();
        xl2json.parseExcel(files[0]);
    }
    // step 1
    document.getElementById('filer_input').addEventListener('change', handleFileSelect, false);
    // End Reading File xlxs.
</script>
