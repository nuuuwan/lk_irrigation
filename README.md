# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--09_20:10:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **283,452 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Norwood — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-09 20:10:15 | Panadugama (Nilwala Ganga) | 4.01 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-10-09 20:09:47 | Norwood (Kelani Ganga) | 1.53 | 🟡 Alert | -0.027 |  |
| 2026-10-09 20:06:40 | Holombuwa (Kelani Ganga) | 2.02 | 🟢 Normal | 0.222 | 🔺 Rising |
| 2026-10-09 20:06:27 | Moragaswewa (Deduru Oya) | 1.48 | 🟢 Normal | 0.243 | 🔺 Rising |
| 2026-10-09 20:06:05 | Peradeniya (Mahaweli Ganga) | 4.55 | 🟢 Normal | 0.481 | 🔺 Rising |
| 2026-10-09 20:05:09 | Rathnapura (Kalu Ganga) | 4.20 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-10-09 20:05:07 | Urawa (Nilwala Ganga) | 1.90 | 🟢 Normal | -0.050 |  |
| 2026-10-09 20:05:02 | Giriulla (Maha Oya) | 3.30 | 🟢 Normal | 0.237 | 🔺 Rising |
| 2026-10-09 20:04:41 | Thalgahagoda (Nilwala Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-10-09 20:04:30 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | -0.020 |  |
| 2026-10-09 20:04:28 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-09 20:04:22 | Glencourse (Kelani Ganga) | 12.57 | 🟢 Normal | 0.213 | 🔺 Rising |
| 2026-10-09 20:04:00 | Nawalapitiya (Mahaweli Ganga) | 1.51 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-10-09 20:03:39 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.064 |  |
| 2026-10-09 20:03:23 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-10-09 20:03:23 | Dunamale (Aththanagalu Oya) | 2.02 | 🟢 Normal | -0.030 |  |
| 2026-10-09 20:03:20 | Deraniyagala (Kelani Ganga) | 0.79 | 🟢 Normal | -0.090 |  |
| 2026-10-09 20:03:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.40 | 🟢 Normal | -0.077 |  |
| 2026-10-09 20:02:47 | Hanwella (Kelani Ganga) | 3.41 | 🟢 Normal | 0.228 | 🔺 Rising |
| 2026-10-09 20:02:45 | Badalgama (Maha Oya) | 3.91 | 🟢 Normal | -0.033 |  |
| 2026-10-09 20:02:44 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | -0.020 |  |
| 2026-10-09 20:02:34 | Manampitiya (Mahaweli Ganga) | -0.35 | 🟢 Normal | -0.010 |  |
| 2026-10-09 20:02:26 | Baddegama (Gin Ganga) | 2.59 | 🟢 Normal | -0.021 |  |
| 2026-10-09 20:02:02 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | 0.204 | 🔺 Rising |
| 2026-10-09 20:01:42 | Pitabeddara (Nilwala Ganga) | 1.65 | 🟢 Normal | 0.226 | 🔺 Rising |
| 2026-10-09 20:01:42 | Ellagawa (Kalu Ganga) | 6.26 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-09 20:01:41 | Moraketiya (Walawe Ganga) | 1.80 | 🟢 Normal | 0.195 | 🔺 Rising |
| 2026-10-09 20:01:40 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-09 20:01:30 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-10-09 20:01:23 | Thanamalwila (Kirindi Oya) | 1.04 | 🟢 Normal | -0.020 |  |
| 2026-10-09 20:00:42 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-09 20:00:41 | Thawalama (Gin Ganga) | 2.20 | 🟢 Normal | -0.068 |  |
| 2026-10-09 20:00:22 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-10-09 20:00:11 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.041 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-09 20:09:47 | Norwood (Kelani Ganga) | 1.53 | 🟡 Alert | -0.027 |  |
| 2026-10-09 20:06:05 | Peradeniya (Mahaweli Ganga) | 4.55 | 🟢 Normal | 0.481 | 🔺 Rising |
| 2026-10-09 20:06:27 | Moragaswewa (Deduru Oya) | 1.48 | 🟢 Normal | 0.243 | 🔺 Rising |
| 2026-10-09 20:05:02 | Giriulla (Maha Oya) | 3.30 | 🟢 Normal | 0.237 | 🔺 Rising |
| 2026-10-09 20:02:47 | Hanwella (Kelani Ganga) | 3.41 | 🟢 Normal | 0.228 | 🔺 Rising |
| 2026-10-09 20:01:42 | Pitabeddara (Nilwala Ganga) | 1.65 | 🟢 Normal | 0.226 | 🔺 Rising |
| 2026-10-09 20:06:40 | Holombuwa (Kelani Ganga) | 2.02 | 🟢 Normal | 0.222 | 🔺 Rising |
| 2026-10-09 20:04:22 | Glencourse (Kelani Ganga) | 12.57 | 🟢 Normal | 0.213 | 🔺 Rising |
| 2026-10-09 20:02:02 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | 0.204 | 🔺 Rising |
| 2026-10-09 20:01:41 | Moraketiya (Walawe Ganga) | 1.80 | 🟢 Normal | 0.195 | 🔺 Rising |
| 2026-10-09 20:00:22 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-10-09 20:05:09 | Rathnapura (Kalu Ganga) | 4.20 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-10-09 20:04:00 | Nawalapitiya (Mahaweli Ganga) | 1.51 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-10-09 20:00:11 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-09 20:10:15 | Panadugama (Nilwala Ganga) | 4.01 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-10-09 20:01:42 | Ellagawa (Kalu Ganga) | 6.26 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-09 18:10:37 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-09 18:01:41 | Weraganthota (Mahaweli Ganga) | -3.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-09 20:03:23 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-10-09 20:00:42 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-09 20:04:28 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-09 20:01:40 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-09 18:01:04 | Thanthirimale (Malwathu Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-10-09 20:04:41 | Thalgahagoda (Nilwala Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-10-09 20:01:30 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-10-09 20:02:34 | Manampitiya (Mahaweli Ganga) | -0.35 | 🟢 Normal | -0.010 |  |
| 2026-10-09 19:10:38 | Magura (Kalu Ganga) | 2.01 | 🟢 Normal | -0.017 |  |
| 2026-10-09 19:07:38 | Putupaula (Kalu Ganga) | 1.35 | 🟢 Normal | -0.018 |  |
| 2026-10-09 20:04:30 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | -0.020 |  |
| 2026-10-09 20:01:23 | Thanamalwila (Kirindi Oya) | 1.04 | 🟢 Normal | -0.020 |  |
| 2026-10-09 20:02:44 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | -0.020 |  |
| 2026-10-09 20:02:26 | Baddegama (Gin Ganga) | 2.59 | 🟢 Normal | -0.021 |  |
| 2026-10-09 20:03:23 | Dunamale (Aththanagalu Oya) | 2.02 | 🟢 Normal | -0.030 |  |
| 2026-10-09 20:02:45 | Badalgama (Maha Oya) | 3.91 | 🟢 Normal | -0.033 |  |
| 2026-10-09 20:05:07 | Urawa (Nilwala Ganga) | 1.90 | 🟢 Normal | -0.050 |  |
| 2026-10-09 20:03:39 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.064 |  |
| 2026-10-09 20:00:41 | Thawalama (Gin Ganga) | 2.20 | 🟢 Normal | -0.068 |  |
| 2026-10-09 20:03:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.40 | 🟢 Normal | -0.077 |  |
| 2026-10-09 20:03:20 | Deraniyagala (Kelani Ganga) | 0.79 | 🟢 Normal | -0.090 |  |

## River Water Level Charts by Station

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)