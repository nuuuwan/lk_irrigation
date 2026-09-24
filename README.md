# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--25_02:16:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **270,175 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟠 Panadugama — Minor Flood; 🟡 Norwood — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-25 02:16:19 | Peradeniya (Mahaweli Ganga) | 4.86 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-09-25 02:12:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.82 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-09-25 02:12:32 | Panadugama (Nilwala Ganga) | 6.63 | 🟠 Minor Flood | -0.009 |  |
| 2026-09-25 02:10:56 | Glencourse (Kelani Ganga) | 14.77 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-09-25 02:07:37 | Kithulgala (Kelani Ganga) | 2.85 | 🟢 Normal | 0.146 | 🔺 Rising |
| 2026-09-25 02:07:17 | Holombuwa (Kelani Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-09-25 02:07:12 | Norwood (Kelani Ganga) | 1.69 | 🟡 Alert | 0.123 | 🔺 Rising |
| 2026-09-25 02:06:57 | Baddegama (Gin Ganga) | 4.60 | 🟠 Minor Flood | 0.020 | 🔺 Rising |
| 2026-09-25 02:06:56 | Holombuwa (Kelani Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-09-25 02:05:55 | Rathnapura (Kalu Ganga) | 6.44 | 🟡 Alert | -0.010 |  |
| 2026-09-25 02:05:43 | Putupaula (Kalu Ganga) | 2.69 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-25 02:05:31 | Wellawaya (Kirindi Oya) | 1.00 | 🟢 Normal | -0.020 |  |
| 2026-09-25 02:05:27 | Giriulla (Maha Oya) | 2.35 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-09-25 02:05:09 | Thawalama (Gin Ganga) | 4.31 | 🟡 Alert | -0.217 |  |
| 2026-09-25 02:05:04 | Deraniyagala (Kelani Ganga) | 2.39 | 🟢 Normal | -0.096 |  |
| 2026-09-25 02:04:32 | Badalgama (Maha Oya) | 3.36 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-25 02:04:28 | Hanwella (Kelani Ganga) | 6.11 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-09-25 02:04:01 | Urawa (Nilwala Ganga) | 1.48 | 🟢 Normal | -0.042 |  |
| 2026-09-25 02:03:53 | Nagalagam Street (Kelani Ganga) | 1.04 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-09-25 02:03:51 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-09-25 02:03:24 | Moragaswewa (Deduru Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-25 02:03:15 | Nawalapitiya (Mahaweli Ganga) | 2.93 | 🟢 Normal | -0.150 |  |
| 2026-09-25 02:02:53 | Manampitiya (Mahaweli Ganga) | -0.30 | 🟢 Normal | -0.010 |  |
| 2026-09-25 02:02:45 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-25 02:02:35 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-25 02:02:11 | Thalgahagoda (Nilwala Ganga) | 1.76 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-25 02:01:56 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-25 02:01:46 | Ellagawa (Kalu Ganga) | 8.50 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-25 02:01:42 | Dunamale (Aththanagalu Oya) | 3.24 | 🟢 Normal | 0.000 |  |
| 2026-09-25 02:01:40 | Kuda Oya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-09-25 02:01:08 | Magura (Kalu Ganga) | 5.00 | 🟡 Alert | -0.020 |  |
| 2026-09-25 02:00:47 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-09-25 01:59:53 | Moraketiya (Walawe Ganga) | 1.33 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-25 02:06:57 | Baddegama (Gin Ganga) | 4.60 | 🟠 Minor Flood | 0.020 | 🔺 Rising |
| 2026-09-25 02:12:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.82 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-09-25 02:02:11 | Thalgahagoda (Nilwala Ganga) | 1.76 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-25 02:12:32 | Panadugama (Nilwala Ganga) | 6.63 | 🟠 Minor Flood | -0.009 |  |
| 2026-09-25 02:07:12 | Norwood (Kelani Ganga) | 1.69 | 🟡 Alert | 0.123 | 🔺 Rising |
| 2026-09-25 02:05:55 | Rathnapura (Kalu Ganga) | 6.44 | 🟡 Alert | -0.010 |  |
| 2026-09-25 02:01:08 | Magura (Kalu Ganga) | 5.00 | 🟡 Alert | -0.020 |  |
| 2026-09-25 02:05:09 | Thawalama (Gin Ganga) | 4.31 | 🟡 Alert | -0.217 |  |
| 2026-09-25 02:07:37 | Kithulgala (Kelani Ganga) | 2.85 | 🟢 Normal | 0.146 | 🔺 Rising |
| 2026-09-25 02:04:28 | Hanwella (Kelani Ganga) | 6.11 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-09-25 02:03:53 | Nagalagam Street (Kelani Ganga) | 1.04 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-09-25 02:00:47 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-09-25 02:03:51 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-09-25 02:16:19 | Peradeniya (Mahaweli Ganga) | 4.86 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-09-25 02:05:27 | Giriulla (Maha Oya) | 2.35 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-09-25 02:04:32 | Badalgama (Maha Oya) | 3.36 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-25 02:01:46 | Ellagawa (Kalu Ganga) | 8.50 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-25 02:10:56 | Glencourse (Kelani Ganga) | 14.77 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-09-25 02:05:43 | Putupaula (Kalu Ganga) | 2.69 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-24 18:00:46 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | 0.000 |  |
| 2026-09-25 01:16:18 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-25 02:03:24 | Moragaswewa (Deduru Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-25 02:01:56 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-25 00:05:30 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-24 18:02:59 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-25 02:02:35 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-25 02:01:42 | Dunamale (Aththanagalu Oya) | 3.24 | 🟢 Normal | 0.000 |  |
| 2026-09-25 02:02:45 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-25 02:07:17 | Holombuwa (Kelani Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-09-24 18:04:50 | Thanthirimale (Malwathu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-25 02:01:40 | Kuda Oya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-09-25 01:02:26 | Thanamalwila (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-09-25 02:02:53 | Manampitiya (Mahaweli Ganga) | -0.30 | 🟢 Normal | -0.010 |  |
| 2026-09-25 02:05:31 | Wellawaya (Kirindi Oya) | 1.00 | 🟢 Normal | -0.020 |  |
| 2026-09-25 01:59:53 | Moraketiya (Walawe Ganga) | 1.33 | 🟢 Normal | -0.020 |  |
| 2026-09-25 02:04:01 | Urawa (Nilwala Ganga) | 1.48 | 🟢 Normal | -0.042 |  |
| 2026-09-25 02:05:04 | Deraniyagala (Kelani Ganga) | 2.39 | 🟢 Normal | -0.096 |  |
| 2026-09-25 00:13:09 | Pitabeddara (Nilwala Ganga) | 2.87 | 🟢 Normal | -0.109 |  |
| 2026-09-25 02:03:15 | Nawalapitiya (Mahaweli Ganga) | 2.93 | 🟢 Normal | -0.150 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)