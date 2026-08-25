# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--25_10:13:38-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **242,976 measurements** from **39** stations.
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
| 2026-08-25 10:13:38 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-25 10:11:54 | Panadugama (Nilwala Ganga) | 2.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-25 10:10:30 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-25 10:07:58 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | -0.009 |  |
| 2026-08-25 10:07:50 | Magura (Kalu Ganga) | 1.73 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-25 10:07:08 | Peradeniya (Mahaweli Ganga) | 2.75 | 🟢 Normal | -0.053 |  |
| 2026-08-25 10:07:00 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-08-25 10:06:44 | Rathnapura (Kalu Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-08-25 10:06:40 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-08-25 10:06:15 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-25 10:06:07 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-08-25 10:05:21 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-25 10:05:13 | Moragaswewa (Deduru Oya) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-25 10:05:12 | Dunamale (Aththanagalu Oya) | 0.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-25 10:05:08 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-08-25 10:04:20 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-08-25 10:03:47 | Glencourse (Kelani Ganga) | 9.53 | 🟢 Normal | 0.000 |  |
| 2026-08-25 10:03:45 | Glencourse (Kelani Ganga) | 9.53 | 🟢 Normal | 0.000 |  |
| 2026-08-25 10:03:25 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-25 10:03:25 | Galgamuwa (Mee Oya) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-25 10:03:06 | Thanthirimale (Malwathu Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-08-25 10:02:47 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-25 10:02:41 | Ellagawa (Kalu Ganga) | 4.94 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-08-25 10:02:40 | Wellawaya (Kirindi Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-08-25 10:02:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.51 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-08-25 10:02:18 | Hanwella (Kelani Ganga) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-08-25 10:02:14 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-08-25 10:01:46 | Manampitiya (Mahaweli Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-25 10:01:40 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-25 10:01:37 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-08-25 10:01:31 | Thawalama (Gin Ganga) | 1.44 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-08-25 10:01:27 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-25 10:01:20 | Moraketiya (Walawe Ganga) | 0.63 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-25 10:01:07 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-25 10:00:41 | Horowpothana (Yan Oya) | 1.89 | 🟢 Normal | -0.010 |  |
| 2026-08-25 10:00:29 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-08-25 10:00:21 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-25 10:00:15 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | 0.600 | 🔺 Rising |
| 2026-08-25 09:59:15 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | 0.600 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-25 10:00:15 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | 0.600 | 🔺 Rising |
| 2026-08-25 10:06:07 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-08-25 10:02:14 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-08-25 10:02:41 | Ellagawa (Kalu Ganga) | 4.94 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-08-25 10:02:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.51 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-08-25 10:07:50 | Magura (Kalu Ganga) | 1.73 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-25 10:01:31 | Thawalama (Gin Ganga) | 1.44 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-08-25 10:05:21 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-25 10:06:15 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-25 10:01:20 | Moraketiya (Walawe Ganga) | 0.63 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-25 10:11:54 | Panadugama (Nilwala Ganga) | 2.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-25 10:05:12 | Dunamale (Aththanagalu Oya) | 0.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-25 10:02:40 | Wellawaya (Kirindi Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-08-25 10:00:21 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-25 10:05:13 | Moragaswewa (Deduru Oya) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-25 10:05:08 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-08-25 10:01:40 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-25 10:01:37 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-08-25 10:03:25 | Galgamuwa (Mee Oya) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-25 10:13:38 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-25 10:07:00 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-08-25 10:10:30 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-25 10:03:47 | Glencourse (Kelani Ganga) | 9.53 | 🟢 Normal | 0.000 |  |
| 2026-08-25 10:02:47 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-25 10:01:07 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-25 10:03:25 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-25 10:06:40 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-08-25 10:01:46 | Manampitiya (Mahaweli Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-25 10:06:44 | Rathnapura (Kalu Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-08-25 10:03:06 | Thanthirimale (Malwathu Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-08-25 10:01:27 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-25 10:07:58 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | -0.009 |  |
| 2026-08-25 09:05:38 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-08-25 10:00:29 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-08-25 10:04:20 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-08-25 10:00:41 | Horowpothana (Yan Oya) | 1.89 | 🟢 Normal | -0.010 |  |
| 2026-08-25 10:02:18 | Hanwella (Kelani Ganga) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-08-25 09:16:39 | Thalgahagoda (Nilwala Ganga) | 0.18 | 🟢 Normal | -0.039 |  |
| 2026-08-25 10:07:08 | Peradeniya (Mahaweli Ganga) | 2.75 | 🟢 Normal | -0.053 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)