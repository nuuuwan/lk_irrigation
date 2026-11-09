# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--10_05:03:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **311,697 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Dunamale — Minor Flood; 🟡 Rathnapura — Alert; 🟡 Thawalama — Alert; 🟡 Kalawellawa (Millakanda) — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **18** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-10 05:03:25 | Hanwella (Kelani Ganga) | 6.26 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-11-10 05:03:25 | Dunamale (Aththanagalu Oya) | 4.60 | 🟠 Minor Flood | 0.030 | 🔺 Rising |
| 2026-11-10 05:03:24 | Giriulla (Maha Oya) | 3.28 | 🟢 Normal | -0.158 |  |
| 2026-11-10 05:03:17 | Norwood (Kelani Ganga) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-11-10 05:03:09 | Kithulgala (Kelani Ganga) | 2.02 | 🟢 Normal | -0.082 |  |
| 2026-11-10 05:03:05 | Glencourse (Kelani Ganga) | 14.35 | 🟢 Normal | -0.205 |  |
| 2026-11-10 05:02:54 | Thalgahagoda (Nilwala Ganga) | 1.60 | 🟡 Alert | 0.000 |  |
| 2026-11-10 05:02:46 | Moragaswewa (Deduru Oya) | 3.82 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-11-10 05:02:29 | Deraniyagala (Kelani Ganga) | 1.29 | 🟢 Normal | -0.050 |  |
| 2026-11-10 05:02:23 | Peradeniya (Mahaweli Ganga) | 4.29 | 🟢 Normal | -0.121 |  |
| 2026-11-10 05:02:05 | Thanamalwila (Kirindi Oya) | 2.45 | 🟢 Normal | -1.026 |  |
| 2026-11-10 05:01:07 | Thaldena (Mahaweli Ganga) | 0.92 | 🟢 Normal | -0.050 |  |
| 2026-11-10 05:01:07 | Putupaula (Kalu Ganga) | 2.50 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-11-10 05:00:52 | Nakkala (Kumbukkan Oya) | 1.30 | 🟢 Normal | -0.044 |  |
| 2026-11-10 05:00:35 | Manampitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-11-10 05:00:06 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-10 04:48:03 | Thanamalwila (Kirindi Oya) | 2.69 | 🟢 Normal | -1.026 |  |
| 2026-11-10 04:37:19 | Thalgahagoda (Nilwala Ganga) | 1.60 | 🟡 Alert | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-10 04:04:23 | Baddegama (Gin Ganga) | 4.05 | 🟠 Minor Flood | 0.057 | 🔺 Rising |
| 2026-11-10 05:03:25 | Dunamale (Aththanagalu Oya) | 4.60 | 🟠 Minor Flood | 0.030 | 🔺 Rising |
| 2026-11-10 04:04:12 | Rathnapura (Kalu Ganga) | 5.31 | 🟡 Alert | 0.643 | 🔺 Rising |
| 2026-11-10 04:07:51 | Thawalama (Gin Ganga) | 4.90 | 🟡 Alert | 0.055 | 🔺 Rising |
| 2026-11-10 04:00:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.36 | 🟡 Alert | 0.043 | 🔺 Rising |
| 2026-11-10 04:03:14 | Magura (Kalu Ganga) | 5.20 | 🟡 Alert | 0.000 |  |
| 2026-11-10 03:08:38 | Panadugama (Nilwala Ganga) | 5.83 | 🟡 Alert | 0.000 |  |
| 2026-11-10 05:02:54 | Thalgahagoda (Nilwala Ganga) | 1.60 | 🟡 Alert | 0.000 |  |
| 2026-11-10 04:05:06 | Moraketiya (Walawe Ganga) | 3.98 | 🟡 Alert | -0.511 |  |
| 2026-11-09 18:02:22 | Weraganthota (Mahaweli Ganga) | -2.56 | 🟢 Normal | 0.225 | 🔺 Rising |
| 2026-11-10 05:02:46 | Moragaswewa (Deduru Oya) | 3.82 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-11-10 04:06:15 | Pitabeddara (Nilwala Ganga) | 3.55 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-11-10 05:03:25 | Hanwella (Kelani Ganga) | 6.26 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-11-10 04:06:57 | Nagalagam Street (Kelani Ganga) | 1.10 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-11-10 04:02:16 | Badalgama (Maha Oya) | 3.75 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-11-10 05:01:07 | Putupaula (Kalu Ganga) | 2.50 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-11-10 04:01:59 | Horowpothana (Yan Oya) | 2.85 | 🟢 Normal | 0.000 |  |
| 2026-11-09 18:06:18 | Galgamuwa (Mee Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-11-10 04:03:44 | Ellagawa (Kalu Ganga) | 8.57 | 🟢 Normal | 0.000 |  |
| 2026-11-09 14:08:46 | Padiyathalawa (Maduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-10 05:00:06 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-10 04:02:58 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-11-10 05:00:35 | Manampitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-11-10 03:04:19 | Urawa (Nilwala Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-11-10 05:03:17 | Norwood (Kelani Ganga) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-11-09 18:01:00 | Thanthirimale (Malwathu Oya) | 1.86 | 🟢 Normal | -0.010 |  |
| 2026-11-10 04:02:10 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-11-10 03:04:30 | Kuda Oya (Kirindi Oya) | 2.83 | 🟢 Normal | -0.029 |  |
| 2026-11-10 05:00:52 | Nakkala (Kumbukkan Oya) | 1.30 | 🟢 Normal | -0.044 |  |
| 2026-11-10 05:01:07 | Thaldena (Mahaweli Ganga) | 0.92 | 🟢 Normal | -0.050 |  |
| 2026-11-10 05:02:29 | Deraniyagala (Kelani Ganga) | 1.29 | 🟢 Normal | -0.050 |  |
| 2026-11-10 04:11:29 | Holombuwa (Kelani Ganga) | 1.37 | 🟢 Normal | -0.075 |  |
| 2026-11-10 05:03:09 | Kithulgala (Kelani Ganga) | 2.02 | 🟢 Normal | -0.082 |  |
| 2026-11-10 04:02:03 | Nawalapitiya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.092 |  |
| 2026-11-10 05:02:23 | Peradeniya (Mahaweli Ganga) | 4.29 | 🟢 Normal | -0.121 |  |
| 2026-11-10 05:03:24 | Giriulla (Maha Oya) | 3.28 | 🟢 Normal | -0.158 |  |
| 2026-11-10 04:01:12 | Wellawaya (Kirindi Oya) | 2.06 | 🟢 Normal | -0.197 |  |
| 2026-11-10 05:03:05 | Glencourse (Kelani Ganga) | 14.35 | 🟢 Normal | -0.205 |  |
| 2026-11-10 05:02:05 | Thanamalwila (Kirindi Oya) | 2.45 | 🟢 Normal | -1.026 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)