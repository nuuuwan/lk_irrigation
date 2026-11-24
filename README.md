# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--24_11:03:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **324,379 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **19** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-24 11:03:02 | Hanwella (Kelani Ganga) | 2.61 | 🟢 Normal | -0.122 |  |
| 2026-11-24 11:02:57 | Pitabeddara (Nilwala Ganga) | 1.54 | 🟢 Normal | -0.022 |  |
| 2026-11-24 11:02:46 | Deraniyagala (Kelani Ganga) | 0.58 | 🟢 Normal | -0.050 |  |
| 2026-11-24 11:02:36 | Nawalapitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-11-24 11:02:36 | Ellagawa (Kalu Ganga) | 5.44 | 🟢 Normal | 0.000 |  |
| 2026-11-24 11:02:10 | Thanamalwila (Kirindi Oya) | 1.28 | 🟢 Normal | -0.166 |  |
| 2026-11-24 11:01:44 | Moragaswewa (Deduru Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-11-24 11:01:24 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-24 11:01:22 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-24 11:01:20 | Giriulla (Maha Oya) | 2.89 | 🟢 Normal | -0.104 |  |
| 2026-11-24 11:01:11 | Kuda Oya (Kirindi Oya) | 1.67 | 🟢 Normal | -0.010 |  |
| 2026-11-24 11:00:56 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | -0.012 |  |
| 2026-11-24 11:00:41 | Manampitiya (Mahaweli Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-11-24 11:00:38 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-11-24 11:00:11 | Weraganthota (Mahaweli Ganga) | -3.03 | 🟢 Normal | -1.000 |  |
| 2026-11-24 10:23:47 | Baddegama (Gin Ganga) | 1.63 | 🟢 Normal | -0.025 |  |
| 2026-11-24 10:13:15 | Urawa (Nilwala Ganga) | 1.13 | 🟢 Normal | -0.043 |  |
| 2026-11-24 10:12:55 | Panadugama (Nilwala Ganga) | 3.98 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-11-24 10:12:42 | Norwood (Kelani Ganga) | 0.82 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-24 10:05:37 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-11-24 10:12:55 | Panadugama (Nilwala Ganga) | 3.98 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-11-24 10:02:18 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-24 10:07:29 | Thalgahagoda (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-24 11:00:38 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-11-24 11:01:44 | Moragaswewa (Deduru Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-11-24 11:02:36 | Nawalapitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-11-24 11:01:22 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-24 10:01:10 | Horowpothana (Yan Oya) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-11-24 10:03:17 | Galgamuwa (Mee Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-11-24 10:12:42 | Norwood (Kelani Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-11-24 11:02:36 | Ellagawa (Kalu Ganga) | 5.44 | 🟢 Normal | 0.000 |  |
| 2026-11-24 11:01:24 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-24 10:02:57 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-11-24 11:00:41 | Manampitiya (Mahaweli Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-11-24 10:03:09 | Rathnapura (Kalu Ganga) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-11-24 10:03:04 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | 0.000 |  |
| 2026-11-24 11:01:11 | Kuda Oya (Kirindi Oya) | 1.67 | 🟢 Normal | -0.010 |  |
| 2026-11-24 10:03:33 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-11-24 10:01:44 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | -0.011 |  |
| 2026-11-24 11:00:56 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | -0.012 |  |
| 2026-11-24 10:04:02 | Magura (Kalu Ganga) | 1.65 | 🟢 Normal | -0.016 |  |
| 2026-11-24 11:02:57 | Pitabeddara (Nilwala Ganga) | 1.54 | 🟢 Normal | -0.022 |  |
| 2026-11-22 17:02:02⌛ | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | -0.022 |  |
| 2026-11-24 10:23:47 | Baddegama (Gin Ganga) | 1.63 | 🟢 Normal | -0.025 |  |
| 2026-11-24 10:04:03 | Moraketiya (Walawe Ganga) | 2.61 | 🟢 Normal | -0.029 |  |
| 2026-11-24 10:03:04 | Thawalama (Gin Ganga) | 1.91 | 🟢 Normal | -0.041 |  |
| 2026-11-24 10:13:15 | Urawa (Nilwala Ganga) | 1.13 | 🟢 Normal | -0.043 |  |
| 2026-11-24 10:05:05 | Dunamale (Aththanagalu Oya) | 1.73 | 🟢 Normal | -0.044 |  |
| 2026-11-24 10:09:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.90 | 🟢 Normal | -0.047 |  |
| 2026-11-24 11:02:46 | Deraniyagala (Kelani Ganga) | 0.58 | 🟢 Normal | -0.050 |  |
| 2026-11-24 10:01:31 | Holombuwa (Kelani Ganga) | 0.92 | 🟢 Normal | -0.058 |  |
| 2026-11-24 11:01:20 | Giriulla (Maha Oya) | 2.89 | 🟢 Normal | -0.104 |  |
| 2026-11-24 11:03:02 | Hanwella (Kelani Ganga) | 2.61 | 🟢 Normal | -0.122 |  |
| 2026-11-24 10:02:56 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | -0.162 |  |
| 2026-11-24 11:02:10 | Thanamalwila (Kirindi Oya) | 1.28 | 🟢 Normal | -0.166 |  |
| 2026-11-24 10:05:49 | Badalgama (Maha Oya) | 4.40 | 🟢 Normal | -0.171 |  |
| 2026-11-24 10:05:00 | Glencourse (Kelani Ganga) | 10.45 | 🟢 Normal | -0.190 |  |
| 2026-11-24 11:00:11 | Weraganthota (Mahaweli Ganga) | -3.03 | 🟢 Normal | -1.000 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)