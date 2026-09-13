# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--13_22:20:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **260,121 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-13 22:20:27 | Panadugama (Nilwala Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-09-13 22:16:34 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-09-13 22:13:50 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-09-13 22:12:59 | Rathnapura (Kalu Ganga) | 1.13 | 🟢 Normal | -0.020 |  |
| 2026-09-13 22:09:28 | Baddegama (Gin Ganga) | 1.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-13 22:08:05 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | -0.010 |  |
| 2026-09-13 22:07:42 | Glencourse (Kelani Ganga) | 9.65 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-09-13 22:06:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.87 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-13 22:06:44 | Thaldena (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-09-13 22:06:36 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-13 22:06:30 | Putupaula (Kalu Ganga) | 0.69 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-09-13 22:06:03 | Nawalapitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-09-13 22:06:03 | Thawalama (Gin Ganga) | 2.20 | 🟢 Normal | -0.068 |  |
| 2026-09-13 22:05:51 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-13 22:05:15 | Deraniyagala (Kelani Ganga) | 0.71 | 🟢 Normal | -0.019 |  |
| 2026-09-13 22:05:14 | Badalgama (Maha Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-09-13 22:05:07 | Pitabeddara (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-09-13 22:04:39 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.039 |  |
| 2026-09-13 22:04:16 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-13 22:04:02 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-13 22:03:49 | Magura (Kalu Ganga) | 2.67 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-13 22:03:42 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.030 |  |
| 2026-09-13 22:03:38 | Moraketiya (Walawe Ganga) | 0.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-13 22:03:20 | Ellagawa (Kalu Ganga) | 5.41 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-09-13 22:03:10 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-13 22:03:07 | Wellawaya (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-09-13 22:02:46 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-09-13 22:02:26 | Dunamale (Aththanagalu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-09-13 22:02:17 | Manampitiya (Mahaweli Ganga) | -0.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-13 22:02:10 | Hanwella (Kelani Ganga) | 1.40 | 🟢 Normal | -0.047 |  |
| 2026-09-13 22:02:05 | Moragaswewa (Deduru Oya) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-13 22:01:50 | Thanamalwila (Kirindi Oya) | 0.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-13 22:01:12 | Kuda Oya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-09-13 22:00:46 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-13 22:00:39 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-09-13 22:00:33 | Nakkala (Kumbukkan Oya) | 0.50 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-13 22:00:39 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-09-13 22:03:20 | Ellagawa (Kalu Ganga) | 5.41 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-09-13 22:06:44 | Thaldena (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-09-13 22:06:30 | Putupaula (Kalu Ganga) | 0.69 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-09-13 22:07:42 | Glencourse (Kelani Ganga) | 9.65 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-09-13 22:03:49 | Magura (Kalu Ganga) | 2.67 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-13 22:01:50 | Thanamalwila (Kirindi Oya) | 0.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-13 22:00:33 | Nakkala (Kumbukkan Oya) | 0.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-13 22:09:28 | Baddegama (Gin Ganga) | 1.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-13 22:02:17 | Manampitiya (Mahaweli Ganga) | -0.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-13 22:03:38 | Moraketiya (Walawe Ganga) | 0.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-13 22:06:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.87 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-13 18:02:39 | Weraganthota (Mahaweli Ganga) | -3.60 | 🟢 Normal | 0.000 |  |
| 2026-09-13 22:03:07 | Wellawaya (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-09-13 22:02:05 | Moragaswewa (Deduru Oya) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-13 22:06:03 | Nawalapitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-09-13 22:03:10 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-13 22:16:34 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-09-13 22:00:46 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-13 18:13:03 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-13 22:05:07 | Pitabeddara (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-09-13 22:02:46 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-09-13 22:20:27 | Panadugama (Nilwala Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-09-13 22:04:02 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-13 22:05:51 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-13 22:02:26 | Dunamale (Aththanagalu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-09-13 22:06:36 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-13 22:05:14 | Badalgama (Maha Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-09-13 22:04:16 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-13 18:04:05 | Thanthirimale (Malwathu Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-13 22:13:50 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-09-13 22:01:12 | Kuda Oya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-09-13 22:08:05 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | -0.010 |  |
| 2026-09-13 22:05:15 | Deraniyagala (Kelani Ganga) | 0.71 | 🟢 Normal | -0.019 |  |
| 2026-09-13 22:12:59 | Rathnapura (Kalu Ganga) | 1.13 | 🟢 Normal | -0.020 |  |
| 2026-09-13 22:03:42 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.030 |  |
| 2026-09-13 22:04:39 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.039 |  |
| 2026-09-13 22:02:10 | Hanwella (Kelani Ganga) | 1.40 | 🟢 Normal | -0.047 |  |
| 2026-09-13 22:06:03 | Thawalama (Gin Ganga) | 2.20 | 🟢 Normal | -0.068 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

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

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)