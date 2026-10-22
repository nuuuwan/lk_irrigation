# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--22_12:17:17-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **294,865 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-22 12:17:17 | Urawa (Nilwala Ganga) | 0.92 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-10-22 12:14:45 | Giriulla (Maha Oya) | 2.42 | 🟢 Normal | -0.125 |  |
| 2026-10-22 12:10:47 | Thawalama (Gin Ganga) | 2.11 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-10-22 12:10:30 | Thalgahagoda (Nilwala Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-10-22 12:10:12 | Glencourse (Kelani Ganga) | 12.12 | 🟢 Normal | -0.123 |  |
| 2026-10-22 12:08:28 | Rathnapura (Kalu Ganga) | 4.52 | 🟢 Normal | -0.154 |  |
| 2026-10-22 12:08:05 | Baddegama (Gin Ganga) | 2.12 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-22 12:08:03 | Holombuwa (Kelani Ganga) | 1.25 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-22 12:07:38 | Badalgama (Maha Oya) | 3.76 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-10-22 12:06:24 | Kithulgala (Kelani Ganga) | 2.20 | 🟢 Normal | 0.264 | 🔺 Rising |
| 2026-10-22 12:05:49 | Deraniyagala (Kelani Ganga) | 1.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-22 12:05:44 | Nagalagam Street (Kelani Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-10-22 12:05:37 | Magura (Kalu Ganga) | 1.84 | 🟢 Normal | -0.010 |  |
| 2026-10-22 12:05:11 | Ellagawa (Kalu Ganga) | 7.47 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-22 12:05:05 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-22 12:04:55 | Hanwella (Kelani Ganga) | 4.47 | 🟢 Normal | -0.089 |  |
| 2026-10-22 12:04:07 | Putupaula (Kalu Ganga) | 1.33 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-10-22 12:03:50 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-22 12:03:46 | Thaldena (Mahaweli Ganga) | 0.53 | 🟢 Normal | -0.041 |  |
| 2026-10-22 12:03:42 | Dunamale (Aththanagalu Oya) | 2.23 | 🟢 Normal | -0.010 |  |
| 2026-10-22 12:03:23 | Panadugama (Nilwala Ganga) | 4.33 | 🟢 Normal | -0.040 |  |
| 2026-10-22 12:03:04 | Norwood (Kelani Ganga) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-10-22 12:03:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-22 12:03:02 | Thanamalwila (Kirindi Oya) | 1.42 | 🟢 Normal | -0.030 |  |
| 2026-10-22 12:02:40 | Galgamuwa (Mee Oya) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-10-22 12:02:23 | Weraganthota (Mahaweli Ganga) | -2.41 | 🟢 Normal | -0.030 |  |
| 2026-10-22 12:02:18 | Nakkala (Kumbukkan Oya) | 0.93 | 🟢 Normal | -0.029 |  |
| 2026-10-22 12:02:16 | Moraketiya (Walawe Ganga) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-10-22 12:02:07 | Moragaswewa (Deduru Oya) | 4.14 | 🟢 Normal | 1.376 | 🔺 Rising |
| 2026-10-22 12:01:56 | Wellawaya (Kirindi Oya) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-10-22 12:01:55 | Thanthirimale (Malwathu Oya) | 2.07 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-22 12:01:40 | Peradeniya (Mahaweli Ganga) | 3.05 | 🟢 Normal | 0.000 |  |
| 2026-10-22 12:01:35 | Manampitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-10-22 12:01:27 | Pitabeddara (Nilwala Ganga) | 1.48 | 🟢 Normal | -0.082 |  |
| 2026-10-22 12:01:25 | Yaka Wewa (Ma Oya) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-10-22 12:01:15 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-10-22 12:00:57 | Kuda Oya (Kirindi Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-10-22 12:00:54 | Siyambalanduwa (Heda Oya) | 0.89 | 🟢 Normal | -0.030 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-22 12:02:07 | Moragaswewa (Deduru Oya) | 4.14 | 🟢 Normal | 1.376 | 🔺 Rising |
| 2026-10-22 12:06:24 | Kithulgala (Kelani Ganga) | 2.20 | 🟢 Normal | 0.264 | 🔺 Rising |
| 2026-10-22 12:07:38 | Badalgama (Maha Oya) | 3.76 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-10-22 12:01:35 | Manampitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-10-22 12:17:17 | Urawa (Nilwala Ganga) | 0.92 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-10-22 12:10:47 | Thawalama (Gin Ganga) | 2.11 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-10-22 12:04:07 | Putupaula (Kalu Ganga) | 1.33 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-10-22 12:05:11 | Ellagawa (Kalu Ganga) | 7.47 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-22 12:08:03 | Holombuwa (Kelani Ganga) | 1.25 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-22 12:01:55 | Thanthirimale (Malwathu Oya) | 2.07 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-22 12:08:05 | Baddegama (Gin Ganga) | 2.12 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-22 12:03:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-22 12:05:49 | Deraniyagala (Kelani Ganga) | 1.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-22 11:00:29 | Horowpothana (Yan Oya) | 3.20 | 🟢 Normal | 0.000 |  |
| 2026-10-22 12:02:40 | Galgamuwa (Mee Oya) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-10-22 12:05:05 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-22 12:05:44 | Nagalagam Street (Kelani Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-10-22 12:03:50 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-22 12:01:40 | Peradeniya (Mahaweli Ganga) | 3.05 | 🟢 Normal | 0.000 |  |
| 2026-10-22 12:10:30 | Thalgahagoda (Nilwala Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-10-22 12:00:57 | Kuda Oya (Kirindi Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-10-22 12:03:42 | Dunamale (Aththanagalu Oya) | 2.23 | 🟢 Normal | -0.010 |  |
| 2026-10-22 12:03:04 | Norwood (Kelani Ganga) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-10-22 12:05:37 | Magura (Kalu Ganga) | 1.84 | 🟢 Normal | -0.010 |  |
| 2026-10-22 12:01:56 | Wellawaya (Kirindi Oya) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-10-22 12:01:15 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-10-22 12:01:25 | Yaka Wewa (Ma Oya) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-10-22 12:02:16 | Moraketiya (Walawe Ganga) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-10-22 12:02:18 | Nakkala (Kumbukkan Oya) | 0.93 | 🟢 Normal | -0.029 |  |
| 2026-10-22 12:02:23 | Weraganthota (Mahaweli Ganga) | -2.41 | 🟢 Normal | -0.030 |  |
| 2026-10-22 12:00:54 | Siyambalanduwa (Heda Oya) | 0.89 | 🟢 Normal | -0.030 |  |
| 2026-10-22 12:03:02 | Thanamalwila (Kirindi Oya) | 1.42 | 🟢 Normal | -0.030 |  |
| 2026-10-22 12:03:23 | Panadugama (Nilwala Ganga) | 4.33 | 🟢 Normal | -0.040 |  |
| 2026-10-22 12:03:46 | Thaldena (Mahaweli Ganga) | 0.53 | 🟢 Normal | -0.041 |  |
| 2026-10-22 12:01:27 | Pitabeddara (Nilwala Ganga) | 1.48 | 🟢 Normal | -0.082 |  |
| 2026-10-22 12:04:55 | Hanwella (Kelani Ganga) | 4.47 | 🟢 Normal | -0.089 |  |
| 2026-10-22 12:10:12 | Glencourse (Kelani Ganga) | 12.12 | 🟢 Normal | -0.123 |  |
| 2026-10-22 12:14:45 | Giriulla (Maha Oya) | 2.42 | 🟢 Normal | -0.125 |  |
| 2026-10-22 12:08:28 | Rathnapura (Kalu Ganga) | 4.52 | 🟢 Normal | -0.154 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)