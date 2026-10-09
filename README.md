# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--09_05:37:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **282,877 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **8** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-09 05:37:10 | Rathnapura (Kalu Ganga) | 3.45 | 🟢 Normal | -0.158 |  |
| 2026-10-09 05:32:30 | Thanamalwila (Kirindi Oya) | 0.55 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-10-09 05:28:57 | Deraniyagala (Kelani Ganga) | 0.82 | 🟢 Normal | -0.138 |  |
| 2026-10-09 05:23:25 | Pitabeddara (Nilwala Ganga) | 1.34 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-10-09 05:18:01 | Magura (Kalu Ganga) | 2.73 | 🟢 Normal | -0.131 |  |
| 2026-10-09 05:17:55 | Thawalama (Gin Ganga) | 3.18 | 🟢 Normal | -0.171 |  |
| 2026-10-09 05:12:07 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | -0.025 |  |
| 2026-10-09 05:08:03 | Thaldena (Mahaweli Ganga) | 0.59 | 🟢 Normal | -0.061 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-09 05:01:37 | Dunamale (Aththanagalu Oya) | 3.00 | 🟢 Normal | 0.208 | 🔺 Rising |
| 2026-10-09 05:04:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.70 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2026-10-09 05:03:45 | Badalgama (Maha Oya) | 4.91 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-10-09 05:02:33 | Thalgahagoda (Nilwala Ganga) | 0.97 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-10-09 05:05:13 | Ellagawa (Kalu Ganga) | 6.57 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-10-09 05:05:45 | Moragaswewa (Deduru Oya) | 1.93 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-10-09 05:07:07 | Moraketiya (Walawe Ganga) | 1.09 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-10-09 05:04:58 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-09 05:05:58 | Baddegama (Gin Ganga) | 2.72 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-09 05:05:26 | Hanwella (Kelani Ganga) | 4.02 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-09 05:04:04 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-09 05:23:25 | Pitabeddara (Nilwala Ganga) | 1.34 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-10-09 05:05:35 | Panadugama (Nilwala Ganga) | 4.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-09 05:06:12 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-09 05:32:30 | Thanamalwila (Kirindi Oya) | 0.55 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-10-09 05:01:48 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-10-08 18:01:40 | Weraganthota (Mahaweli Ganga) | -3.46 | 🟢 Normal | 0.000 |  |
| 2026-10-09 05:01:33 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-10-09 05:02:24 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-10-09 05:02:37 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-10-08 18:07:01 | Galgamuwa (Mee Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-09 05:01:30 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-08 18:02:32 | Thanthirimale (Malwathu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-09 05:06:27 | Urawa (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-10-09 05:02:15 | Siyambalanduwa (Heda Oya) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-10-09 05:04:02 | Norwood (Kelani Ganga) | 1.07 | 🟢 Normal | -0.020 |  |
| 2026-10-09 05:12:07 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | -0.025 |  |
| 2026-10-09 05:05:29 | Putupaula (Kalu Ganga) | 1.29 | 🟢 Normal | -0.055 |  |
| 2026-10-09 05:08:03 | Thaldena (Mahaweli Ganga) | 0.59 | 🟢 Normal | -0.061 |  |
| 2026-10-09 05:01:20 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.065 |  |
| 2026-10-09 05:02:54 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | -0.078 |  |
| 2026-10-09 05:03:08 | Peradeniya (Mahaweli Ganga) | 3.24 | 🟢 Normal | -0.116 |  |
| 2026-10-09 05:18:01 | Magura (Kalu Ganga) | 2.73 | 🟢 Normal | -0.131 |  |
| 2026-10-09 05:05:17 | Holombuwa (Kelani Ganga) | 1.79 | 🟢 Normal | -0.132 |  |
| 2026-10-09 05:28:57 | Deraniyagala (Kelani Ganga) | 0.82 | 🟢 Normal | -0.138 |  |
| 2026-10-09 05:02:54 | Glencourse (Kelani Ganga) | 12.36 | 🟢 Normal | -0.154 |  |
| 2026-10-09 05:37:10 | Rathnapura (Kalu Ganga) | 3.45 | 🟢 Normal | -0.158 |  |
| 2026-10-09 05:17:55 | Thawalama (Gin Ganga) | 3.18 | 🟢 Normal | -0.171 |  |
| 2026-10-09 05:02:42 | Giriulla (Maha Oya) | 4.13 | 🟢 Normal | -0.270 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)