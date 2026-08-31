# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--31_17:03:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **248,206 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **17** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-31 17:03:03 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-08-31 17:02:30 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-08-31 17:02:09 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-31 17:01:57 | Moraketiya (Walawe Ganga) | 0.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-31 17:01:56 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-31 17:01:43 | Dunamale (Aththanagalu Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-08-31 17:01:13 | Glencourse (Kelani Ganga) | 9.54 | 🟢 Normal | -0.040 |  |
| 2026-08-31 17:01:10 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-31 17:01:10 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-08-31 17:01:09 | Peradeniya (Mahaweli Ganga) | 2.28 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-08-31 17:01:07 | Nawalapitiya (Mahaweli Ganga) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-08-31 17:00:53 | Manampitiya (Mahaweli Ganga) | -0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-31 17:00:19 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-31 17:00:07 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-08-31 16:29:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.44 | 🟢 Normal | -0.007 |  |
| 2026-08-31 16:20:50 | Magura (Kalu Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-08-31 16:17:52 | Ellagawa (Kalu Ganga) | 4.76 | 🟢 Normal | 0.008 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-31 17:03:03 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-08-31 17:01:09 | Peradeniya (Mahaweli Ganga) | 2.28 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-08-31 16:04:07 | Putupaula (Kalu Ganga) | 0.83 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-08-31 17:00:07 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-08-31 16:03:55 | Baddegama (Gin Ganga) | 1.49 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-31 17:01:57 | Moraketiya (Walawe Ganga) | 0.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-31 16:17:52 | Ellagawa (Kalu Ganga) | 4.76 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-08-31 16:00:19 | Weraganthota (Mahaweli Ganga) | -3.46 | 🟢 Normal | 0.000 |  |
| 2026-08-31 17:01:56 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-31 17:00:19 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-31 17:01:10 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-08-31 16:04:11 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-31 17:02:30 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-08-31 16:02:38 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-08-31 16:03:36 | Galgamuwa (Mee Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-31 16:20:50 | Magura (Kalu Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-08-31 16:01:17 | Pitabeddara (Nilwala Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-08-31 16:03:19 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-31 16:04:34 | Hanwella (Kelani Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-08-31 16:02:41 | Deraniyagala (Kelani Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-08-31 16:04:50 | Panadugama (Nilwala Ganga) | 2.92 | 🟢 Normal | 0.000 |  |
| 2026-08-31 17:01:10 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-31 16:03:36 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-08-31 16:06:21 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-08-31 17:01:43 | Dunamale (Aththanagalu Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-08-31 16:03:15 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-31 17:02:09 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-31 16:07:18 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-08-31 17:00:53 | Manampitiya (Mahaweli Ganga) | -0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-31 16:00:52 | Thanthirimale (Malwathu Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-31 16:02:33 | Kuda Oya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-08-31 16:01:40 | Thanamalwila (Kirindi Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-31 16:07:07 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | -0.005 |  |
| 2026-08-31 16:29:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.44 | 🟢 Normal | -0.007 |  |
| 2026-08-31 17:01:07 | Nawalapitiya (Mahaweli Ganga) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-08-31 16:03:10 | Rathnapura (Kalu Ganga) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-08-31 16:05:45 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | -0.031 |  |
| 2026-08-31 17:01:13 | Glencourse (Kelani Ganga) | 9.54 | 🟢 Normal | -0.040 |  |
| 2026-08-31 15:11:57 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | -0.048 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)