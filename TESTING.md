# Test-Repo für den Framework-Import-Security-Scan

Dieses Repository dient als Sync-Quelle (`GITHUB_SML_SYNC_REPO=Ir0nPyr0/clamav-test`),
um den Sicherheitsscan der Framework-Importe (ClamAV-Signaturscan plus Struktur- und
Inhaltsprüfung) über den Button **„Jetzt synchronisieren“** in der Admin-UI
end-to-end zu testen.

Alle Testdaten sind **harmlos** (EICAR-Teststring, Text-Snippets) – dieses Repo
enthält keine echten Schadprogramme. Der `main`-Branch enthält den unveränderten
Datenstand der regulären SML-Dokumentation.

## Benutzung

In `backend/.env` für den Test umstellen und das Backend neu starten
(Neustart nötig, da Repo und Branch nur beim Start gelesen werden):

```dotenv
GITHUB_SML_SYNC_REPO=Ir0nPyr0/clamav-test
GITHUB_SML_SYNC_REF=test/clamav-eicar-raw   # leer lassen = main (Standard-Branch)
```

Die ClamAV-Adresse muss nur gesetzt werden, wenn das Backend ohne Compose läuft
(`FRAMEWORK_IMPORT_CLAMAV_ADDRESS=localhost:3310`); im Compose-Setup zeigt sie
bereits auf den `clamav`-Container.

Dann in der Admin-UI **Administration → Frameworks → „Jetzt synchronisieren“**
klicken. Der Sync-Verlauf zeigt Status, `check` und `threat_name`; jeder Scan
landet zusätzlich als App-Ereignis `framework_import_scan` im Audit-Log.

Nach dem Test die Werte zurücksetzen (`GITHUB_SML_SYNC_REPO=es3-sml/es3-sml`,
`GITHUB_SML_SYNC_REF` entfernen) und das Backend neu starten — der Worker
startet den Sync sonst bei jedem Start mit den Testwerten.

## Branches

| Branch                   | Inhalt von `docs/sml_data.json`                | Erwarteter Ausgang                                                      |
| ------------------------ | ---------------------------------------------- | ----------------------------------------------------------------------- |
| `main`                   | unverändertes, echtes SML-Manifest             | `success` — Import als neue Framework-Version                           |
| `test/clamav-eicar-raw`  | Datei = exakt der 68-Byte-EICAR-Teststring     | `blocked`, `check=malware`, `threat_name=Eicar-Test-Signature` (ClamAV) |
| `test/eicar-in-json`     | EICAR-String im Fragetext (schema-valide)      | `blocked`, `check=embedded_executable`, `threat_name=eicar-test-file`   |
| `test/base64-executable` | Base64-PE-Header (`MZ…`) im Fragetext          | `blocked`, `check=embedded_executable`, `threat_name=base64-windows-pe` |
| `test/script-injection`  | `<script>`-Tag im Fragetext                    | `blocked`, `check=script_injection`, `threat_name=html-script-tag`      |
| `test/ransomware-note`   | Erpresser-Text im Fragetext                    | `blocked`, `check=ransomware`, `threat_name=ransom-note-encrypted-files`|
| `test/invalid-schema`    | gültiges JSON, aber nur 3 von 9 Dimensionen    | `invalid_manifest` — Scan erlaubt, Parser lehnt ab, Admin-Alarm         |

Hinweise:

- ClamAV erkennt EICAR nur am **Dateianfang**; deshalb testet `test/clamav-eicar-raw`
  den ClamAV-Signaturscan, während `test/eicar-in-json` die eingebaute
  Inhaltsregel (Payload in JSON-Strings) demonstriert.
- Ohne laufenden clamd blockt `test/clamav-eicar-raw` mit `check=structure`
  (ungültiges JSON) statt `check=malware`; mit konfiguriertem, aber nicht
  erreichbarem clamd endet der Lauf `scan_unavailable` (fail-closed).
- Der Sync benötigt den S3-File-Store (`PUBLIC_SURVEY_UPLOAD_S3_BUCKET`, lokal
  z. B. MinIO aus dem Compose-Setup), sonst bleibt der Sync deaktiviert.
