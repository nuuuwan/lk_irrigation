# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--09_12:16:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **283,149 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **3** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-09 12:16:02 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-09 12:12:12 | Urawa (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-09 12:07:38 | Glencourse (Kelani Ganga) | 11.41 | 🟢 Normal | -0.096 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-09 12:04:34 | Thawalama (Gin Ganga) | 2.19 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-10-09 12:01:25 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-10-09 12:03:32 | Putupaula (Kalu Ganga) | 1.34 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-10-09 12:12:12 | Urawa (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-09 12:02:26 | Siyambalanduwa (Heda Oya) | 0.31 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-09 12:02:05 | Thanthirimale (Malwathu Oya) | 0.83 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-10-09 12:00:45 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | 0.000 |  |
| 2026-10-09 12:01:23 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-10-09 12:05:20 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-10-09 12:03:41 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-10-09 12:02:51 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-09 12:01:11 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-10-09 12:16:02 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-09 12:00:26 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-10-09 12:02:35 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-10-09 12:03:39 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-09 12:00:42 | Manampitiya (Mahaweli Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-10-09 12:07:08 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-10-09 12:04:50 | Thanamalwila (Kirindi Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-10-09 12:04:23 | Baddegama (Gin Ganga) | 2.80 | 🟢 Normal | -0.010 |  |
| 2026-10-09 12:05:20 | Norwood (Kelani Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-10-09 12:00:19 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-10-09 12:02:27 | Pitabeddara (Nilwala Ganga) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-10-09 12:04:27 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | -0.020 |  |
| 2026-10-09 12:02:41 | Kithulgala (Kelani Ganga) | 1.95 | 🟢 Normal | -0.020 |  |
| 2026-10-09 12:06:12 | Deraniyagala (Kelani Ganga) | 0.47 | 🟢 Normal | -0.029 |  |
| 2026-10-09 12:03:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.89 | 🟢 Normal | -0.030 |  |
| 2026-10-09 12:02:09 | Ellagawa (Kalu Ganga) | 6.60 | 🟢 Normal | -0.041 |  |
| 2026-10-09 12:02:55 | Dunamale (Aththanagalu Oya) | 2.86 | 🟢 Normal | -0.041 |  |
| 2026-10-09 12:06:54 | Holombuwa (Kelani Ganga) | 1.40 | 🟢 Normal | -0.050 |  |
| 2026-10-09 12:06:40 | Magura (Kalu Ganga) | 2.22 | 🟢 Normal | -0.052 |  |
| 2026-10-09 12:01:54 | Giriulla (Maha Oya) | 3.24 | 🟢 Normal | -0.061 |  |
| 2026-10-09 12:07:38 | Glencourse (Kelani Ganga) | 11.41 | 🟢 Normal | -0.096 |  |
| 2026-10-09 12:02:49 | Panadugama (Nilwala Ganga) | 4.02 | 🟢 Normal | -0.109 |  |
| 2026-10-09 12:05:10 | Badalgama (Maha Oya) | 4.31 | 🟢 Normal | -0.110 |  |
| 2026-10-09 12:03:09 | Hanwella (Kelani Ganga) | 3.62 | 🟢 Normal | -0.110 |  |
| 2026-10-09 12:03:51 | Rathnapura (Kalu Ganga) | 2.73 | 🟢 Normal | -0.117 |  |
| 2026-10-09 12:03:24 | Moragaswewa (Deduru Oya) | 1.22 | 🟢 Normal | -0.192 |  |
| 2026-10-09 12:05:34 | Peradeniya (Mahaweli Ganga) | 2.20 | 🟢 Normal | -0.294 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)