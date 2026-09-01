# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--01_10:09:59-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **248,835 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **0** measurements in the last **1 hour**.*

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-01 10:02:12 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2026-09-01 10:07:22 | Thawalama (Gin Ganga) | 1.54 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-01 10:02:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.28 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-01 09:00:40 | Manampitiya (Mahaweli Ganga) | -0.59 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-01 10:02:50 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-01 10:01:11 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-09-01 10:08:14 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-01 10:03:03 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-09-01 10:01:50 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-01 09:01:40 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-09-01 10:02:50 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-01 10:03:23 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-01 10:03:04 | Ellagawa (Kalu Ganga) | 4.67 | 🟢 Normal | 0.000 |  |
| 2026-09-01 10:01:23 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-01 10:03:16 | Moraketiya (Walawe Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-09-01 10:01:08 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-01 10:09:59 | Dunamale (Aththanagalu Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-09-01 10:04:16 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-09-01 10:05:15 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-01 10:04:26 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-09-01 10:06:35 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-09-01 09:02:18 | Thanthirimale (Malwathu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-01 10:09:32 | Urawa (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-01 10:01:11 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-01 10:06:38 | Thanamalwila (Kirindi Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-09-01 10:04:09 | Baddegama (Gin Ganga) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-09-01 10:06:41 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | -0.010 |  |
| 2026-09-01 10:06:05 | Glencourse (Kelani Ganga) | 9.47 | 🟢 Normal | -0.010 |  |
| 2026-09-01 10:04:56 | Magura (Kalu Ganga) | 1.33 | 🟢 Normal | -0.011 |  |
| 2026-09-01 10:00:27 | Rathnapura (Kalu Ganga) | 1.07 | 🟢 Normal | -0.012 |  |
| 2026-09-01 10:07:24 | Peradeniya (Mahaweli Ganga) | 2.88 | 🟢 Normal | -0.019 |  |
| 2026-09-01 10:06:21 | Pitabeddara (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.019 |  |
| 2026-09-01 10:04:13 | Hanwella (Kelani Ganga) | 1.12 | 🟢 Normal | -0.020 |  |
| 2026-09-01 10:07:02 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.024 |  |
| 2026-09-01 10:05:37 | Panadugama (Nilwala Ganga) | 2.75 | 🟢 Normal | -0.029 |  |
| 2026-09-01 10:02:30 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | -0.050 |  |
| 2026-09-01 10:04:10 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.058 |  |
| 2026-09-01 10:02:13 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.061 |  |
| 2026-09-01 10:04:18 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | -0.077 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)