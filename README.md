# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--07_22:12:43-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **254,729 measurements** from **39** stations.
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
| 2026-09-07 22:12:43 | Ellagawa (Kalu Ganga) | 4.31 | 🟢 Normal | 0.000 |  |
| 2026-09-07 22:11:52 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-09-07 22:11:13 | Baddegama (Gin Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-09-07 22:09:38 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-09-07 22:09:00 | Panadugama (Nilwala Ganga) | 2.21 | 🟢 Normal | 0.000 |  |
| 2026-09-07 22:08:56 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-09-07 22:08:43 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | -0.019 |  |
| 2026-09-07 22:08:41 | Magura (Kalu Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-09-07 22:07:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.48 | 🟢 Normal | -0.020 |  |
| 2026-09-07 22:07:36 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-07 22:07:23 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | -0.154 |  |
| 2026-09-07 22:05:59 | Nawalapitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-07 22:05:57 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-09-07 22:05:36 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-09-07 22:05:23 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | -0.059 |  |
| 2026-09-07 22:05:00 | Baddegama (Gin Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-09-07 22:04:18 | Hanwella (Kelani Ganga) | 0.76 | 🟢 Normal | -0.011 |  |
| 2026-09-07 22:03:56 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-09-07 22:03:55 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-09-07 22:03:35 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-07 22:02:52 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-09-07 22:02:43 | Rathnapura (Kalu Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-09-07 22:02:40 | Manampitiya (Mahaweli Ganga) | -0.09 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-09-07 22:02:34 | Thanamalwila (Kirindi Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-07 22:02:30 | Moragaswewa (Deduru Oya) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-07 22:02:22 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-07 22:02:18 | Glencourse (Kelani Ganga) | 9.09 | 🟢 Normal | 0.000 |  |
| 2026-09-07 22:02:18 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-07 22:02:11 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-07 22:02:06 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-07 22:01:58 | Peradeniya (Mahaweli Ganga) | 2.20 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-09-07 22:01:57 | Rathnapura (Kalu Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-09-07 22:01:38 | Moraketiya (Walawe Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-07 22:01:31 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-09-07 22:01:17 | Wellawaya (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-09-07 22:01:03 | Thalgahagoda (Nilwala Ganga) | 0.15 | 🟢 Normal | -0.011 |  |
| 2026-09-07 22:00:46 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-07 22:00:39 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-07 21:57:13 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-07 22:01:58 | Peradeniya (Mahaweli Ganga) | 2.20 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-09-07 22:02:40 | Manampitiya (Mahaweli Ganga) | -0.09 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-09-07 22:11:52 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-09-07 22:08:56 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-09-07 18:10:27 | Thanthirimale (Malwathu Oya) | 0.38 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-09-07 22:05:59 | Nawalapitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-07 22:01:17 | Wellawaya (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-09-07 22:00:39 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-07 22:02:30 | Moragaswewa (Deduru Oya) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-07 22:02:06 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-07 22:00:46 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-07 18:04:43 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-07 22:08:41 | Magura (Kalu Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-09-07 22:05:57 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-09-07 22:02:52 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-09-07 22:12:43 | Ellagawa (Kalu Ganga) | 4.31 | 🟢 Normal | 0.000 |  |
| 2026-09-07 22:11:13 | Baddegama (Gin Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-09-07 22:09:00 | Panadugama (Nilwala Ganga) | 2.21 | 🟢 Normal | 0.000 |  |
| 2026-09-07 22:03:35 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-07 22:02:18 | Glencourse (Kelani Ganga) | 9.09 | 🟢 Normal | 0.000 |  |
| 2026-09-07 22:01:38 | Moraketiya (Walawe Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-07 22:01:31 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-09-07 22:02:18 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-07 22:09:38 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-09-07 22:02:11 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-07 22:03:55 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-09-07 22:02:43 | Rathnapura (Kalu Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-09-07 22:05:36 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-09-07 22:07:36 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-07 22:02:22 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-07 22:02:34 | Thanamalwila (Kirindi Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-07 22:03:56 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-09-07 22:01:03 | Thalgahagoda (Nilwala Ganga) | 0.15 | 🟢 Normal | -0.011 |  |
| 2026-09-07 22:04:18 | Hanwella (Kelani Ganga) | 0.76 | 🟢 Normal | -0.011 |  |
| 2026-09-07 22:08:43 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | -0.019 |  |
| 2026-09-07 22:07:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.48 | 🟢 Normal | -0.020 |  |
| 2026-09-07 18:02:01 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | -0.050 |  |
| 2026-09-07 22:05:23 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | -0.059 |  |
| 2026-09-07 22:07:23 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | -0.154 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)