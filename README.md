# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--23_23:02:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **323,959 measurements** from **39** stations.
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
| 2026-11-23 23:02:46 | Norwood (Kelani Ganga) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-11-23 23:02:44 | Glencourse (Kelani Ganga) | 9.76 | 🟢 Normal | 0.706 | 🔺 Rising |
| 2026-11-23 23:02:42 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-11-23 23:02:30 | Nawalapitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | -0.045 |  |
| 2026-11-23 23:02:21 | Badalgama (Maha Oya) | 2.57 | 🟢 Normal | 0.000 |  |
| 2026-11-23 23:01:54 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.183 | 🔺 Rising |
| 2026-11-23 23:01:50 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-23 23:01:44 | Giriulla (Maha Oya) | 1.79 | 🟢 Normal | 0.250 | 🔺 Rising |
| 2026-11-23 23:01:35 | Magura (Kalu Ganga) | 2.20 | 🟢 Normal | 216.000 | 🔺 Rising |
| 2026-11-23 23:01:34 | Magura (Kalu Ganga) | 2.14 | 🟢 Normal | 216.000 | 🔺 Rising |
| 2026-11-23 23:01:31 | Manampitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-11-23 23:01:30 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-11-23 23:01:25 | Moragaswewa (Deduru Oya) | 0.76 | 🟢 Normal | -0.020 |  |
| 2026-11-23 23:01:12 | Moraketiya (Walawe Ganga) | 2.20 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-11-23 23:01:06 | Rathnapura (Kalu Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-11-23 23:01:05 | Peradeniya (Mahaweli Ganga) | 3.12 | 🟢 Normal | -0.021 |  |
| 2026-11-23 23:00:15 | Wellawaya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-23 23:00:12 | Rathnapura (Kalu Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-11-23 22:40:01 | Thalgahagoda (Nilwala Ganga) | 0.76 | 🟢 Normal | -0.031 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-23 23:01:35 | Magura (Kalu Ganga) | 2.20 | 🟢 Normal | 216.000 | 🔺 Rising |
| 2026-11-23 22:07:08 | Holombuwa (Kelani Ganga) | 1.45 | 🟢 Normal | 0.894 | 🔺 Rising |
| 2026-11-23 23:02:44 | Glencourse (Kelani Ganga) | 9.76 | 🟢 Normal | 0.706 | 🔺 Rising |
| 2026-11-23 22:17:21 | Urawa (Nilwala Ganga) | 1.32 | 🟢 Normal | 0.301 | 🔺 Rising |
| 2026-11-23 23:01:44 | Giriulla (Maha Oya) | 1.79 | 🟢 Normal | 0.250 | 🔺 Rising |
| 2026-11-23 23:01:54 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.183 | 🔺 Rising |
| 2026-11-23 22:04:57 | Deraniyagala (Kelani Ganga) | 1.64 | 🟢 Normal | 0.141 | 🔺 Rising |
| 2026-11-23 23:01:12 | Moraketiya (Walawe Ganga) | 2.20 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-11-23 22:11:35 | Baddegama (Gin Ganga) | 1.66 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-11-23 22:09:10 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-11-23 22:04:37 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-11-23 22:12:14 | Pitabeddara (Nilwala Ganga) | 1.19 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-11-23 23:00:15 | Wellawaya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-23 23:01:30 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-11-23 23:01:50 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-23 22:01:37 | Horowpothana (Yan Oya) | 2.18 | 🟢 Normal | 0.000 |  |
| 2026-11-23 18:05:14 | Galgamuwa (Mee Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-11-23 22:19:03 | Ellagawa (Kalu Ganga) | 5.10 | 🟢 Normal | 0.000 |  |
| 2026-11-23 22:02:46 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-11-23 22:02:55 | Dunamale (Aththanagalu Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-11-23 23:02:21 | Badalgama (Maha Oya) | 2.57 | 🟢 Normal | 0.000 |  |
| 2026-11-23 23:01:31 | Manampitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-11-23 23:01:06 | Rathnapura (Kalu Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-11-23 22:06:01 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | -0.010 |  |
| 2026-11-23 22:03:34 | Kuda Oya (Kirindi Oya) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-11-23 23:02:42 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-11-23 23:02:46 | Norwood (Kelani Ganga) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-11-23 23:01:25 | Moragaswewa (Deduru Oya) | 0.76 | 🟢 Normal | -0.020 |  |
| 2026-11-23 18:02:13 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | -0.020 |  |
| 2026-11-23 22:01:10 | Panadugama (Nilwala Ganga) | 3.53 | 🟢 Normal | -0.021 |  |
| 2026-11-23 23:01:05 | Peradeniya (Mahaweli Ganga) | 3.12 | 🟢 Normal | -0.021 |  |
| 2026-11-22 17:02:02⌛ | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | -0.022 |  |
| 2026-11-23 22:03:52 | Hanwella (Kelani Ganga) | 1.00 | 🟢 Normal | -0.031 |  |
| 2026-11-23 22:40:01 | Thalgahagoda (Nilwala Ganga) | 0.76 | 🟢 Normal | -0.031 |  |
| 2026-11-23 22:05:57 | Thawalama (Gin Ganga) | 2.12 | 🟢 Normal | -0.040 |  |
| 2026-11-23 23:02:30 | Nawalapitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | -0.045 |  |
| 2026-11-23 18:00:35 | Weraganthota (Mahaweli Ganga) | -2.49 | 🟢 Normal | -0.050 |  |
| 2026-11-23 22:02:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.08 | 🟢 Normal | -0.061 |  |
| 2026-11-23 22:05:39 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | -0.133 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)