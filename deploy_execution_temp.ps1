$connectionString = "Server=127.0.0.1,1433;Database=master;Integrated Security=True;TrustServerCertificate=True;"
$folderName = "TimesheetDeployments"

$projectPath = "C:\sc_ShriyaHariparsad_2026\Timesheet_Project\TimesheetMigration\TimesheetMigration\bin\Development\TimesheetMigration.ispac"
$projectName = [System.IO.Path]::GetFileNameWithoutExtension($projectPath)

$fileBytes = [System.IO.File]::ReadAllBytes($projectPath)
$hexString = "0x" + [System.BitConverter]::ToString($fileBytes).Replace("-", "")

$deployQuery = "
SET NOCOUNT ON;
IF NOT EXISTS (SELECT 1 FROM [SSISDB].[catalog].[folders] WHERE name = '$folderName')
BEGIN
    EXEC [SSISDB].[catalog].[create_folder] @folder_name = '$folderName';
END
DECLARE @project_binary VARBINARY(MAX) = $hexString;
EXEC [SSISDB].[catalog].[deploy_project]
    @folder_name = '$folderName',
    @project_name = '$projectName',
    @project_stream = @project_binary;
"

$connection = New-Object System.Data.SqlClient.SqlConnection($connectionString)
$command = New-Object System.Data.SqlClient.SqlCommand($deployQuery, $connection)

try {
    $connection.Open()
    $command.ExecuteNonQuery() | Out-Null
    Write-Host "SUCCESS: Deployment completed! Your SSIS project is now live in SSMS."
} catch {
    Write-Error "Database connection crashed: $_"
    exit 1
} finally {
    $connection.Close()
}
