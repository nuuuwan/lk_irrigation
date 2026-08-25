# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--26_01:14:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **243,529 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **25** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-26 01:14:57 | Magura (Kalu Ganga) | 2.33 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-08-26 01:12:42 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-26 01:11:50 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.014 |  |
| 2026-08-26 01:09:27 | Pitabeddara (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.170 | 🔺 Rising |
| 2026-08-26 01:08:46 | Rathnapura (Kalu Ganga) | 3.05 | 🟢 Normal | 0.298 | 🔺 Rising |
| 2026-08-26 01:08:27 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-26 01:05:47 | Urawa (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-08-26 01:05:44 | Panadugama (Nilwala Ganga) | 2.83 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-08-26 01:05:44 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-26 01:05:29 | Thawalama (Gin Ganga) | 1.92 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-08-26 01:05:06 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | -0.020 |  |
| 2026-08-26 01:04:55 | Baddegama (Gin Ganga) | 1.41 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-26 01:04:16 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-26 01:04:15 | Manampitiya (Mahaweli Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-26 01:04:15 | Kithulgala (Kelani Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-08-26 01:03:55 | Giriulla (Maha Oya) | 0.91 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-26 01:03:46 | Deraniyagala (Kelani Ganga) | 1.38 | 🟢 Normal | 0.322 | 🔺 Rising |
| 2026-08-26 01:03:33 | Hanwella (Kelani Ganga) | 1.18 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-08-26 01:03:22 | Ellagawa (Kalu Ganga) | 5.51 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-08-26 01:03:16 | Glencourse (Kelani Ganga) | 9.87 | 🟢 Normal | 0.228 | 🔺 Rising |
| 2026-08-26 01:02:50 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-26 01:02:06 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-26 01:01:42 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-26 01:01:39 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-26 01:01:28 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-26 01:03:46 | Deraniyagala (Kelani Ganga) | 1.38 | 🟢 Normal | 0.322 | 🔺 Rising |
| 2026-08-26 01:08:46 | Rathnapura (Kalu Ganga) | 3.05 | 🟢 Normal | 0.298 | 🔺 Rising |
| 2026-08-26 01:03:16 | Glencourse (Kelani Ganga) | 9.87 | 🟢 Normal | 0.228 | 🔺 Rising |
| 2026-08-26 01:09:27 | Pitabeddara (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.170 | 🔺 Rising |
| 2026-08-26 00:07:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.30 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-08-26 01:05:47 | Urawa (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-08-26 01:03:22 | Ellagawa (Kalu Ganga) | 5.51 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-08-26 01:05:44 | Panadugama (Nilwala Ganga) | 2.83 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-08-26 01:05:29 | Thawalama (Gin Ganga) | 1.92 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-08-26 01:14:57 | Magura (Kalu Ganga) | 2.33 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-08-26 01:03:33 | Hanwella (Kelani Ganga) | 1.18 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-08-26 00:16:31 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-08-26 00:12:25 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-08-26 01:04:55 | Baddegama (Gin Ganga) | 1.41 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-26 00:00:25 | Moraketiya (Walawe Ganga) | 0.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-26 01:02:06 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-26 01:02:50 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-26 01:03:55 | Giriulla (Maha Oya) | 0.91 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-26 01:04:15 | Kithulgala (Kelani Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-08-26 00:02:38 | Wellawaya (Kirindi Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-08-26 01:01:28 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-26 01:01:39 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-26 01:04:16 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-26 00:03:10 | Horowpothana (Yan Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-08-25 18:03:25 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-25 23:15:52 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-08-26 01:12:42 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-26 01:01:42 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-26 00:01:50 | Dunamale (Aththanagalu Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-08-26 01:08:27 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-26 01:05:44 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-26 01:04:15 | Manampitiya (Mahaweli Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-25 18:02:21 | Thanthirimale (Malwathu Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-08-26 00:07:19 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-26 01:11:50 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.014 |  |
| 2026-08-25 18:08:33 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -0.019 |  |
| 2026-08-26 01:05:06 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | -0.020 |  |
| 2026-08-26 00:04:27 | Nawalapitiya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.043 |  |
| 2026-08-26 00:01:42 | Peradeniya (Mahaweli Ganga) | 2.98 | 🟢 Normal | -0.043 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)