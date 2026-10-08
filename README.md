# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--09_00:12:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **282,697 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-09 00:12:12 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-10-09 00:12:10 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-10-09 00:12:08 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-10-09 00:11:46 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-10-09 00:08:01 | Hanwella (Kelani Ganga) | 3.27 | 🟢 Normal | 0.269 | 🔺 Rising |
| 2026-10-09 00:07:46 | Thanamalwila (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-10-09 00:07:32 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-09 00:06:49 | Rathnapura (Kalu Ganga) | 3.98 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-10-09 00:06:41 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-10-09 00:06:28 | Thalgahagoda (Nilwala Ganga) | 0.73 | 🟢 Normal | -0.021 |  |
| 2026-10-09 00:06:27 | Norwood (Kelani Ganga) | 1.15 | 🟢 Normal | -54.000 |  |
| 2026-10-09 00:06:25 | Norwood (Kelani Ganga) | 1.18 | 🟢 Normal | -54.000 |  |
| 2026-10-09 00:05:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.40 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-10-09 00:04:41 | Panadugama (Nilwala Ganga) | 4.35 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-10-09 00:04:18 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-09 00:04:13 | Kithulgala (Kelani Ganga) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-10-09 00:04:01 | Baddegama (Gin Ganga) | 2.46 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-10-09 00:03:56 | Holombuwa (Kelani Ganga) | 2.82 | 🟢 Normal | -0.444 |  |
| 2026-10-09 00:03:53 | Deraniyagala (Kelani Ganga) | 0.89 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-09 00:03:48 | Pitabeddara (Nilwala Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-10-09 00:03:25 | Dunamale (Aththanagalu Oya) | 2.52 | 🟢 Normal | 0.166 | 🔺 Rising |
| 2026-10-09 00:03:11 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.113 |  |
| 2026-10-09 00:03:08 | Glencourse (Kelani Ganga) | 12.60 | 🟢 Normal | 0.195 | 🔺 Rising |
| 2026-10-09 00:03:04 | Manampitiya (Mahaweli Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-10-09 00:02:53 | Thawalama (Gin Ganga) | 3.75 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-10-09 00:02:35 | Badalgama (Maha Oya) | 3.52 | 🟢 Normal | 0.428 | 🔺 Rising |
| 2026-10-09 00:02:18 | Giriulla (Maha Oya) | 4.54 | 🟢 Normal | 0.337 | 🔺 Rising |
| 2026-10-09 00:01:59 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-10-09 00:01:56 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-10-09 00:01:55 | Moragaswewa (Deduru Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-10-09 00:01:47 | Nakkala (Kumbukkan Oya) | 0.99 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-09 00:01:29 | Nawalapitiya (Mahaweli Ganga) | 1.46 | 🟢 Normal | -0.024 |  |
| 2026-10-09 00:01:19 | Peradeniya (Mahaweli Ganga) | 3.40 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-09 00:01:12 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-10-09 00:00:36 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-09 00:02:35 | Badalgama (Maha Oya) | 3.52 | 🟢 Normal | 0.428 | 🔺 Rising |
| 2026-10-09 00:02:18 | Giriulla (Maha Oya) | 4.54 | 🟢 Normal | 0.337 | 🔺 Rising |
| 2026-10-09 00:08:01 | Hanwella (Kelani Ganga) | 3.27 | 🟢 Normal | 0.269 | 🔺 Rising |
| 2026-10-09 00:03:08 | Glencourse (Kelani Ganga) | 12.60 | 🟢 Normal | 0.195 | 🔺 Rising |
| 2026-10-08 23:04:29 | Magura (Kalu Ganga) | 2.89 | 🟢 Normal | 0.187 | 🔺 Rising |
| 2026-10-09 00:03:25 | Dunamale (Aththanagalu Oya) | 2.52 | 🟢 Normal | 0.166 | 🔺 Rising |
| 2026-10-08 23:01:48 | Ellagawa (Kalu Ganga) | 5.77 | 🟢 Normal | 0.161 | 🔺 Rising |
| 2026-10-08 23:07:12 | Putupaula (Kalu Ganga) | 1.02 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-10-09 00:04:41 | Panadugama (Nilwala Ganga) | 4.35 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-10-09 00:05:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.40 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-10-09 00:04:01 | Baddegama (Gin Ganga) | 2.46 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-10-09 00:11:46 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-10-09 00:06:49 | Rathnapura (Kalu Ganga) | 3.98 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-10-09 00:02:53 | Thawalama (Gin Ganga) | 3.75 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-10-09 00:03:53 | Deraniyagala (Kelani Ganga) | 0.89 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-09 00:01:19 | Peradeniya (Mahaweli Ganga) | 3.40 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-09 00:01:47 | Nakkala (Kumbukkan Oya) | 0.99 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-09 00:04:13 | Kithulgala (Kelani Ganga) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-10-08 18:01:40 | Weraganthota (Mahaweli Ganga) | -3.46 | 🟢 Normal | 0.000 |  |
| 2026-10-09 00:12:12 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-10-09 00:01:55 | Moragaswewa (Deduru Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-10-09 00:06:41 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-10-09 00:01:12 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-10-08 18:07:01 | Galgamuwa (Mee Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-09 00:03:48 | Pitabeddara (Nilwala Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-10-09 00:07:32 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-09 00:01:59 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-10-09 00:00:36 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-10-09 00:04:18 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-09 00:03:04 | Manampitiya (Mahaweli Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-10-08 18:02:32 | Thanthirimale (Malwathu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-08 23:14:10 | Urawa (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-10-09 00:01:56 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-10-09 00:07:46 | Thanamalwila (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-10-09 00:06:28 | Thalgahagoda (Nilwala Ganga) | 0.73 | 🟢 Normal | -0.021 |  |
| 2026-10-09 00:01:29 | Nawalapitiya (Mahaweli Ganga) | 1.46 | 🟢 Normal | -0.024 |  |
| 2026-10-09 00:03:11 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.113 |  |
| 2026-10-09 00:03:56 | Holombuwa (Kelani Ganga) | 2.82 | 🟢 Normal | -0.444 |  |
| 2026-10-09 00:06:27 | Norwood (Kelani Ganga) | 1.15 | 🟢 Normal | -54.000 |  |

## River Water Level Charts by Station

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)