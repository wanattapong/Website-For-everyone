<!DOCTYPE html>
<html>

<head>
    <title>ThaiCreate.Com</title>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <script src="http://code.jquery.com/jquery-latest.js"></script>
    <script type="text/javascript">
        $(document).ready(function () {

            $("#createRows").click(function () {
                var customerid = "val";
                var name = "val";
                var email = "val";
                var countrycode = "val";
                var budget = "val";
                var used = "val";
                var tr = "<tr>";
                tr = tr + "<td>" + customerid + "</td>";
                tr = tr + "<td>" + name + "</td>";
                tr = tr + "<td>" + email + "</td>";
                tr = tr + "<td>" + countrycode + "</td>";
                tr = tr + "<td>" + budget + "</td>";
                tr = tr + "<td>" + used + "</td>";
                tr = tr + "</tr>";
                $('#myTable > tbody:last').append(tr);
            });

            $("#deleteRows").click(function () {
                if ($("#myTable tr").length != 1) {
                    $("#myTable tr:last").remove();
                }
            });

            $("#clearRows").click(function () {
                //$("#myTable tbody tr:not(:first-child)").remove(); // remove all
                //$("#myBody").empty(); // remove all
                $('#myTable > tbody:last').empty(); // remove all
            });

        });
    </script>
    <meta charset=utf-8 />
</head>

<body>
    <center>
        <h1>jQuery Create table rows / tr / tbody / td</h1>

        <table width="600" border="1" id="myTable">
            <!-- head table -->
            <thead>
                <tr>
                    <td width="91">
                        <div align="center">CustomerID </div>
                    </td>
                    <td width="98">
                        <div align="center">Name </div>
                    </td>
                    <td width="198">
                        <div align="center">Email </div>
                    </td>
                    <td width="97">
                        <div align="center">CountryCode </div>
                    </td>
                    <td width="59">
                        <div align="center">Budget </div>
                    </td>
                    <td width="71">
                        <div align="center">Used </div>
                    </td>
                </tr>
            </thead>
            <!-- body dynamic rows -->
            <tbody></tbody>
        </table>
        <br />
        <input type="button" id="createRows" value="Add">
        <input type="button" id="deleteRows" value="Del">
        <input type="button" id="clearRows" value="Clear">
        <center>
</body>

</html>