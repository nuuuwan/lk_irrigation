# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--16_02:19:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **262,053 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-16 02:19:48 | Nawalapitiya (Mahaweli Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-09-16 02:14:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.86 | 🟢 Normal | -1.469 |  |
| 2026-09-16 02:14:04 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | -0.005 |  |
| 2026-09-16 02:13:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.88 | 🟢 Normal | -1.469 |  |
| 2026-09-16 02:12:06 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-09-16 02:11:52 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-09-16 02:07:03 | Thanamalwila (Kirindi Oya) | 1.49 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-09-16 02:06:33 | Rathnapura (Kalu Ganga) | 2.86 | 🟢 Normal | -0.289 |  |
| 2026-09-16 02:05:39 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-16 02:05:22 | Baddegama (Gin Ganga) | 3.35 | 🟢 Normal | -0.020 |  |
| 2026-09-16 02:05:04 | Panadugama (Nilwala Ganga) | 3.19 | 🟢 Normal | -0.020 |  |
| 2026-09-16 02:04:22 | Dunamale (Aththanagalu Oya) | 2.44 | 🟢 Normal | -0.100 |  |
| 2026-09-16 02:04:20 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.041 |  |
| 2026-09-16 02:04:17 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-16 02:04:17 | Badalgama (Maha Oya) | 2.08 | 🟢 Normal | -0.030 |  |
| 2026-09-16 02:04:17 | Glencourse (Kelani Ganga) | 10.12 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-09-16 02:03:46 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-09-16 02:03:27 | Hanwella (Kelani Ganga) | 1.73 | 🟢 Normal | -0.020 |  |
| 2026-09-16 02:03:21 | Ellagawa (Kalu Ganga) | 6.12 | 🟢 Normal | 0.196 | 🔺 Rising |
| 2026-09-16 02:03:05 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-09-16 02:02:21 | Deraniyagala (Kelani Ganga) | 1.19 | 🟢 Normal | -0.030 |  |
| 2026-09-16 02:02:02 | Wellawaya (Kirindi Oya) | 1.46 | 🟢 Normal | -0.049 |  |
| 2026-09-16 02:01:54 | Horowpothana (Yan Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-09-16 02:01:48 | Moragaswewa (Deduru Oya) | -0.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-16 02:01:40 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-16 02:01:20 | Manampitiya (Mahaweli Ganga) | -0.23 | 🟢 Normal | 0.249 | 🔺 Rising |
| 2026-09-16 02:01:13 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-09-16 02:00:51 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-09-16 02:00:47 | Thawalama (Gin Ganga) | 1.72 | 🟢 Normal | -0.041 |  |
| 2026-09-16 02:00:44 | Padiyathalawa (Maduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-16 02:00:37 | Peradeniya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -1.158 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-16 02:01:20 | Manampitiya (Mahaweli Ganga) | -0.23 | 🟢 Normal | 0.249 | 🔺 Rising |
| 2026-09-16 02:03:21 | Ellagawa (Kalu Ganga) | 6.12 | 🟢 Normal | 0.196 | 🔺 Rising |
| 2026-09-16 02:12:06 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-09-16 02:07:03 | Thanamalwila (Kirindi Oya) | 1.49 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-09-16 02:04:17 | Glencourse (Kelani Ganga) | 10.12 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-09-16 02:04:17 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-16 02:01:48 | Moragaswewa (Deduru Oya) | -0.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-16 02:00:51 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-09-16 00:11:35 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-16 02:19:48 | Nawalapitiya (Mahaweli Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-09-16 00:15:04 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-16 02:01:54 | Horowpothana (Yan Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-09-15 18:07:20 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-16 01:13:50 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-16 02:00:44 | Padiyathalawa (Maduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-16 02:01:40 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-16 02:05:39 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-16 01:05:02 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-16 02:14:04 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | -0.005 |  |
| 2026-09-15 18:02:30 | Thanthirimale (Malwathu Oya) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-09-16 02:01:13 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-09-16 02:11:52 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-09-16 02:03:05 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-09-16 02:03:46 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-09-16 02:03:27 | Hanwella (Kelani Ganga) | 1.73 | 🟢 Normal | -0.020 |  |
| 2026-09-16 02:05:04 | Panadugama (Nilwala Ganga) | 3.19 | 🟢 Normal | -0.020 |  |
| 2026-09-16 02:05:22 | Baddegama (Gin Ganga) | 3.35 | 🟢 Normal | -0.020 |  |
| 2026-09-16 02:04:17 | Badalgama (Maha Oya) | 2.08 | 🟢 Normal | -0.030 |  |
| 2026-09-16 02:02:21 | Deraniyagala (Kelani Ganga) | 1.19 | 🟢 Normal | -0.030 |  |
| 2026-09-15 18:02:40 | Weraganthota (Mahaweli Ganga) | -3.09 | 🟢 Normal | -0.039 |  |
| 2026-09-16 02:04:20 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.041 |  |
| 2026-09-16 02:00:47 | Thawalama (Gin Ganga) | 1.72 | 🟢 Normal | -0.041 |  |
| 2026-09-16 02:02:02 | Wellawaya (Kirindi Oya) | 1.46 | 🟢 Normal | -0.049 |  |
| 2026-09-16 02:04:22 | Dunamale (Aththanagalu Oya) | 2.44 | 🟢 Normal | -0.100 |  |
| 2026-09-16 01:05:30 | Magura (Kalu Ganga) | 3.52 | 🟢 Normal | -0.124 |  |
| 2026-09-16 01:06:56 | Putupaula (Kalu Ganga) | 1.37 | 🟢 Normal | -0.137 |  |
| 2026-09-16 02:06:33 | Rathnapura (Kalu Ganga) | 2.86 | 🟢 Normal | -0.289 |  |
| 2026-09-16 02:00:37 | Peradeniya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -1.158 |  |
| 2026-09-16 02:14:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.86 | 🟢 Normal | -1.469 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)