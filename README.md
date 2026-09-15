# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--16_04:28:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **262,123 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-16 04:28:05 | Dunamale (Aththanagalu Oya) | 2.29 | 🟢 Normal | -0.036 |  |
| 2026-09-16 04:22:29 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-16 04:21:57 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-16 04:19:39 | Deraniyagala (Kelani Ganga) | 1.14 | 🟢 Normal | -0.027 |  |
| 2026-09-16 04:17:12 | Moragaswewa (Deduru Oya) | -0.15 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-09-16 04:15:33 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.435 | 🔺 Rising |
| 2026-09-16 04:15:02 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-09-16 04:11:25 | Thalgahagoda (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.435 | 🔺 Rising |
| 2026-09-16 04:11:14 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-09-16 04:10:50 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-09-16 04:10:49 | Putupaula (Kalu Ganga) | 1.15 | 🟢 Normal | -0.035 |  |
| 2026-09-16 04:10:30 | Ellagawa (Kalu Ganga) | 6.25 | 🟢 Normal | 0.000 |  |
| 2026-09-16 04:09:10 | Baddegama (Gin Ganga) | 3.29 | 🟢 Normal | -0.033 |  |
| 2026-09-16 04:08:26 | Rathnapura (Kalu Ganga) | 2.42 | 🟢 Normal | -0.357 |  |
| 2026-09-16 04:08:14 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-16 04:08:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.70 | 🟢 Normal | -0.139 |  |
| 2026-09-16 04:07:49 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-16 04:07:25 | Hanwella (Kelani Ganga) | 1.79 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-16 04:06:48 | Panadugama (Nilwala Ganga) | 3.15 | 🟢 Normal | -0.020 |  |
| 2026-09-16 04:06:02 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-09-16 04:05:46 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-09-16 04:05:20 | Kithulgala (Kelani Ganga) | 1.84 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-16 04:04:57 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | -0.020 |  |
| 2026-09-16 04:04:53 | Nawalapitiya (Mahaweli Ganga) | 1.02 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-16 04:03:58 | Glencourse (Kelani Ganga) | 10.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-16 04:03:49 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-16 04:03:02 | Norwood (Kelani Ganga) | 0.83 | 🟢 Normal | -0.030 |  |
| 2026-09-16 04:02:59 | Magura (Kalu Ganga) | 3.30 | 🟢 Normal | -0.084 |  |
| 2026-09-16 04:02:37 | Peradeniya (Mahaweli Ganga) | 1.86 | 🟢 Normal | -0.318 |  |
| 2026-09-16 04:02:35 | Horowpothana (Yan Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-09-16 04:01:52 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | -0.030 |  |
| 2026-09-16 04:01:08 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-16 04:00:20 | Wellawaya (Kirindi Oya) | 1.45 | 🟢 Normal | -0.020 |  |
| 2026-09-16 04:00:18 | Padiyathalawa (Maduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-16 03:06:17 | Pitabeddara (Nilwala Ganga) | 3.18 | 🟢 Normal | 1.473 | 🔺 Rising |
| 2026-09-16 04:15:33 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.435 | 🔺 Rising |
| 2026-09-16 04:05:46 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-09-16 04:07:25 | Hanwella (Kelani Ganga) | 1.79 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-16 04:11:14 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-09-16 04:17:12 | Moragaswewa (Deduru Oya) | -0.15 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-09-16 04:03:58 | Glencourse (Kelani Ganga) | 10.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-16 04:05:20 | Kithulgala (Kelani Ganga) | 1.84 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-16 04:04:53 | Nawalapitiya (Mahaweli Ganga) | 1.02 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-16 04:07:49 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-16 04:22:29 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-16 04:02:35 | Horowpothana (Yan Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-09-15 18:07:20 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-16 04:10:30 | Ellagawa (Kalu Ganga) | 6.25 | 🟢 Normal | 0.000 |  |
| 2026-09-16 04:00:18 | Padiyathalawa (Maduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-16 04:15:02 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-09-16 03:00:21 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-09-16 04:01:08 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-16 04:08:14 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-16 04:03:49 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-16 04:06:02 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-09-15 18:02:30 | Thanthirimale (Malwathu Oya) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-09-16 04:10:50 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-09-16 03:05:01 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | -0.019 |  |
| 2026-09-16 04:06:48 | Panadugama (Nilwala Ganga) | 3.15 | 🟢 Normal | -0.020 |  |
| 2026-09-16 04:00:20 | Wellawaya (Kirindi Oya) | 1.45 | 🟢 Normal | -0.020 |  |
| 2026-09-16 04:04:57 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | -0.020 |  |
| 2026-09-16 04:19:39 | Deraniyagala (Kelani Ganga) | 1.14 | 🟢 Normal | -0.027 |  |
| 2026-09-16 04:01:52 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | -0.030 |  |
| 2026-09-16 04:03:02 | Norwood (Kelani Ganga) | 0.83 | 🟢 Normal | -0.030 |  |
| 2026-09-16 04:09:10 | Baddegama (Gin Ganga) | 3.29 | 🟢 Normal | -0.033 |  |
| 2026-09-16 04:10:49 | Putupaula (Kalu Ganga) | 1.15 | 🟢 Normal | -0.035 |  |
| 2026-09-16 04:28:05 | Dunamale (Aththanagalu Oya) | 2.29 | 🟢 Normal | -0.036 |  |
| 2026-09-15 18:02:40 | Weraganthota (Mahaweli Ganga) | -3.09 | 🟢 Normal | -0.039 |  |
| 2026-09-16 04:02:59 | Magura (Kalu Ganga) | 3.30 | 🟢 Normal | -0.084 |  |
| 2026-09-16 03:04:07 | Thanamalwila (Kirindi Oya) | 1.41 | 🟢 Normal | -0.084 |  |
| 2026-09-16 04:08:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.70 | 🟢 Normal | -0.139 |  |
| 2026-09-16 04:02:37 | Peradeniya (Mahaweli Ganga) | 1.86 | 🟢 Normal | -0.318 |  |
| 2026-09-16 04:08:26 | Rathnapura (Kalu Ganga) | 2.42 | 🟢 Normal | -0.357 |  |

## River Water Level Charts by Station

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)