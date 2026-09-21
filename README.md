# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--21_15:09:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **267,051 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Baddegama — Minor Flood; 🟡 Thalgahagoda — Alert; 🟡 Magura — Alert; 🟡 Rathnapura — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-21 15:09:02 | Magura (Kalu Ganga) | 5.43 | 🟡 Alert | -0.043 |  |
| 2026-09-21 15:07:37 | Ellagawa (Kalu Ganga) | 9.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-21 15:06:30 | Kithulgala (Kelani Ganga) | 2.18 | 🟢 Normal | -0.069 |  |
| 2026-09-21 15:06:26 | Moragaswewa (Deduru Oya) | 0.10 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-09-21 15:05:59 | Holombuwa (Kelani Ganga) | 1.26 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-09-21 15:05:48 | Nagalagam Street (Kelani Ganga) | 0.99 | 🟢 Normal | -0.042 |  |
| 2026-09-21 15:05:36 | Baddegama (Gin Ganga) | 4.01 | 🟠 Minor Flood | 0.019 | 🔺 Rising |
| 2026-09-21 15:05:20 | Peradeniya (Mahaweli Ganga) | 3.20 | 🟢 Normal | 0.274 | 🔺 Rising |
| 2026-09-21 15:05:06 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-21 15:04:55 | Urawa (Nilwala Ganga) | 0.61 | 🟢 Normal | -0.020 |  |
| 2026-09-21 15:04:54 | Nawalapitiya (Mahaweli Ganga) | 2.41 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2026-09-21 15:04:52 | Galgamuwa (Mee Oya) | 0.40 | 🟢 Normal | -0.011 |  |
| 2026-09-21 15:04:43 | Badalgama (Maha Oya) | 3.27 | 🟢 Normal | -0.082 |  |
| 2026-09-21 15:04:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.97 | 🟠 Minor Flood | 0.029 | 🔺 Rising |
| 2026-09-21 15:04:27 | Thanamalwila (Kirindi Oya) | 1.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-21 15:04:20 | Putupaula (Kalu Ganga) | 2.67 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-21 15:04:02 | Glencourse (Kelani Ganga) | 12.95 | 🟢 Normal | -0.091 |  |
| 2026-09-21 15:03:25 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-09-21 15:03:13 | Weraganthota (Mahaweli Ganga) | -2.89 | 🟢 Normal | 0.000 |  |
| 2026-09-21 15:03:09 | Thawalama (Gin Ganga) | 2.88 | 🟢 Normal | 0.000 |  |
| 2026-09-21 15:03:03 | Panadugama (Nilwala Ganga) | 5.57 | 🟡 Alert | -0.054 |  |
| 2026-09-21 15:03:01 | Hanwella (Kelani Ganga) | 5.80 | 🟢 Normal | -0.123 |  |
| 2026-09-21 15:02:53 | Deraniyagala (Kelani Ganga) | 2.25 | 🟢 Normal | 0.161 | 🔺 Rising |
| 2026-09-21 15:02:51 | Giriulla (Maha Oya) | 1.95 | 🟢 Normal | -0.020 |  |
| 2026-09-21 15:02:50 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | -0.020 |  |
| 2026-09-21 15:02:36 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-09-21 15:02:30 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-09-21 15:02:00 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-21 15:02:00 | Wellawaya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-09-21 15:01:57 | Pitabeddara (Nilwala Ganga) | 1.43 | 🟢 Normal | -0.020 |  |
| 2026-09-21 15:01:57 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-21 15:01:36 | Thanthirimale (Malwathu Oya) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-09-21 15:01:33 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-09-21 15:01:13 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | -0.040 |  |
| 2026-09-21 15:01:10 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-21 15:01:07 | Thalgahagoda (Nilwala Ganga) | 1.50 | 🟡 Alert | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-21 15:04:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.97 | 🟠 Minor Flood | 0.029 | 🔺 Rising |
| 2026-09-21 15:05:36 | Baddegama (Gin Ganga) | 4.01 | 🟠 Minor Flood | 0.019 | 🔺 Rising |
| 2026-09-21 15:01:07 | Thalgahagoda (Nilwala Ganga) | 1.50 | 🟡 Alert | 0.000 |  |
| 2026-09-21 15:09:02 | Magura (Kalu Ganga) | 5.43 | 🟡 Alert | -0.043 |  |
| 2026-09-21 14:09:04 | Rathnapura (Kalu Ganga) | 5.62 | 🟡 Alert | -0.047 |  |
| 2026-09-21 15:03:03 | Panadugama (Nilwala Ganga) | 5.57 | 🟡 Alert | -0.054 |  |
| 2026-09-21 15:05:20 | Peradeniya (Mahaweli Ganga) | 3.20 | 🟢 Normal | 0.274 | 🔺 Rising |
| 2026-09-21 15:02:53 | Deraniyagala (Kelani Ganga) | 2.25 | 🟢 Normal | 0.161 | 🔺 Rising |
| 2026-09-21 15:04:54 | Nawalapitiya (Mahaweli Ganga) | 2.41 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2026-09-21 15:05:59 | Holombuwa (Kelani Ganga) | 1.26 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-09-21 15:06:26 | Moragaswewa (Deduru Oya) | 0.10 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-09-21 15:04:20 | Putupaula (Kalu Ganga) | 2.67 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-21 14:09:28 | Norwood (Kelani Ganga) | 1.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-21 15:07:37 | Ellagawa (Kalu Ganga) | 9.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-21 15:04:27 | Thanamalwila (Kirindi Oya) | 1.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-21 15:03:13 | Weraganthota (Mahaweli Ganga) | -2.89 | 🟢 Normal | 0.000 |  |
| 2026-09-21 15:02:00 | Wellawaya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-09-21 15:01:57 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-21 15:01:10 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-21 15:01:33 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-09-21 15:05:06 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-21 15:02:36 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-09-21 15:02:00 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-21 15:03:25 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-09-21 15:03:09 | Thawalama (Gin Ganga) | 2.88 | 🟢 Normal | 0.000 |  |
| 2026-09-21 15:01:36 | Thanthirimale (Malwathu Oya) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-09-21 15:02:30 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-09-21 15:04:52 | Galgamuwa (Mee Oya) | 0.40 | 🟢 Normal | -0.011 |  |
| 2026-09-21 15:01:57 | Pitabeddara (Nilwala Ganga) | 1.43 | 🟢 Normal | -0.020 |  |
| 2026-09-21 15:02:51 | Giriulla (Maha Oya) | 1.95 | 🟢 Normal | -0.020 |  |
| 2026-09-21 15:04:55 | Urawa (Nilwala Ganga) | 0.61 | 🟢 Normal | -0.020 |  |
| 2026-09-21 15:02:50 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | -0.020 |  |
| 2026-09-21 15:01:13 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | -0.040 |  |
| 2026-09-21 15:05:48 | Nagalagam Street (Kelani Ganga) | 0.99 | 🟢 Normal | -0.042 |  |
| 2026-09-21 14:00:45 | Dunamale (Aththanagalu Oya) | 3.10 | 🟢 Normal | -0.056 |  |
| 2026-09-21 15:06:30 | Kithulgala (Kelani Ganga) | 2.18 | 🟢 Normal | -0.069 |  |
| 2026-09-21 15:04:43 | Badalgama (Maha Oya) | 3.27 | 🟢 Normal | -0.082 |  |
| 2026-09-21 15:04:02 | Glencourse (Kelani Ganga) | 12.95 | 🟢 Normal | -0.091 |  |
| 2026-09-21 15:03:01 | Hanwella (Kelani Ganga) | 5.80 | 🟢 Normal | -0.123 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)