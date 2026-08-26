# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--26_15:13:11-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **244,062 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-26 15:13:11 | Dunamale (Aththanagalu Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-08-26 15:09:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.41 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-26 15:08:33 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-26 15:08:28 | Glencourse (Kelani Ganga) | 10.05 | 🟢 Normal | -0.099 |  |
| 2026-08-26 15:07:23 | Putupaula (Kalu Ganga) | 1.21 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-08-26 15:06:14 | Panadugama (Nilwala Ganga) | 3.25 | 🟢 Normal | 0.000 |  |
| 2026-08-26 15:05:51 | Magura (Kalu Ganga) | 2.73 | 🟢 Normal | -0.069 |  |
| 2026-08-26 15:05:49 | Pitabeddara (Nilwala Ganga) | 0.94 | 🟢 Normal | -0.121 |  |
| 2026-08-26 15:05:40 | Thanamalwila (Kirindi Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-26 15:05:20 | Rathnapura (Kalu Ganga) | 3.11 | 🟢 Normal | -0.132 |  |
| 2026-08-26 15:05:03 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.030 |  |
| 2026-08-26 15:04:47 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-26 15:04:45 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-26 15:04:34 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-26 15:04:08 | Giriulla (Maha Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-26 15:04:05 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-26 15:03:56 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | -0.011 |  |
| 2026-08-26 15:03:45 | Thawalama (Gin Ganga) | 1.84 | 🟢 Normal | -0.010 |  |
| 2026-08-26 15:03:34 | Urawa (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.050 |  |
| 2026-08-26 15:03:12 | Ellagawa (Kalu Ganga) | 6.78 | 🟢 Normal | 0.000 |  |
| 2026-08-26 15:02:55 | Deraniyagala (Kelani Ganga) | 1.02 | 🟢 Normal | -0.020 |  |
| 2026-08-26 15:02:52 | Baddegama (Gin Ganga) | 1.90 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-08-26 15:02:47 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-08-26 15:02:35 | Hanwella (Kelani Ganga) | 1.83 | 🟢 Normal | -0.020 |  |
| 2026-08-26 15:02:22 | Badalgama (Maha Oya) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-08-26 15:02:07 | Thanthirimale (Malwathu Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-26 15:02:06 | Wellawaya (Kirindi Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-26 15:01:57 | Horowpothana (Yan Oya) | 1.76 | 🟢 Normal | -0.010 |  |
| 2026-08-26 15:01:57 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-08-26 15:01:30 | Nawalapitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.020 |  |
| 2026-08-26 15:01:18 | Weraganthota (Mahaweli Ganga) | -3.11 | 🟢 Normal | -0.072 |  |
| 2026-08-26 15:01:17 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-26 15:01:15 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-26 15:01:11 | Manampitiya (Mahaweli Ganga) | -0.24 | 🟢 Normal | -0.010 |  |
| 2026-08-26 15:01:10 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-26 15:01:09 | Peradeniya (Mahaweli Ganga) | 2.98 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-26 15:00:58 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-26 15:00:56 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-26 15:00:21 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-26 14:17:30 | Thalgahagoda (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-08-26 15:01:09 | Peradeniya (Mahaweli Ganga) | 2.98 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-26 15:07:23 | Putupaula (Kalu Ganga) | 1.21 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-08-26 15:02:52 | Baddegama (Gin Ganga) | 1.90 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-08-26 15:01:10 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-26 15:09:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.41 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-26 15:01:57 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-08-26 15:02:06 | Wellawaya (Kirindi Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-26 15:00:21 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-26 15:01:17 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-26 15:04:08 | Giriulla (Maha Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-26 15:04:05 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-26 15:02:47 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-08-26 15:03:12 | Ellagawa (Kalu Ganga) | 6.78 | 🟢 Normal | 0.000 |  |
| 2026-08-26 15:06:14 | Panadugama (Nilwala Ganga) | 3.25 | 🟢 Normal | 0.000 |  |
| 2026-08-26 15:00:58 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-26 15:04:34 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-26 15:13:11 | Dunamale (Aththanagalu Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-08-26 15:00:56 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-26 15:04:47 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-26 15:02:22 | Badalgama (Maha Oya) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-08-26 15:08:33 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-26 15:02:07 | Thanthirimale (Malwathu Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-26 15:04:45 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-26 15:05:40 | Thanamalwila (Kirindi Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-26 15:01:57 | Horowpothana (Yan Oya) | 1.76 | 🟢 Normal | -0.010 |  |
| 2026-08-26 15:03:45 | Thawalama (Gin Ganga) | 1.84 | 🟢 Normal | -0.010 |  |
| 2026-08-26 15:01:11 | Manampitiya (Mahaweli Ganga) | -0.24 | 🟢 Normal | -0.010 |  |
| 2026-08-26 15:03:56 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | -0.011 |  |
| 2026-08-26 15:01:30 | Nawalapitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.020 |  |
| 2026-08-26 15:02:35 | Hanwella (Kelani Ganga) | 1.83 | 🟢 Normal | -0.020 |  |
| 2026-08-26 15:02:55 | Deraniyagala (Kelani Ganga) | 1.02 | 🟢 Normal | -0.020 |  |
| 2026-08-26 15:05:03 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.030 |  |
| 2026-08-26 15:03:34 | Urawa (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.050 |  |
| 2026-08-26 15:05:51 | Magura (Kalu Ganga) | 2.73 | 🟢 Normal | -0.069 |  |
| 2026-08-26 15:01:18 | Weraganthota (Mahaweli Ganga) | -3.11 | 🟢 Normal | -0.072 |  |
| 2026-08-26 15:08:28 | Glencourse (Kelani Ganga) | 10.05 | 🟢 Normal | -0.099 |  |
| 2026-08-26 15:05:49 | Pitabeddara (Nilwala Ganga) | 0.94 | 🟢 Normal | -0.121 |  |
| 2026-08-26 15:05:20 | Rathnapura (Kalu Ganga) | 3.11 | 🟢 Normal | -0.132 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)