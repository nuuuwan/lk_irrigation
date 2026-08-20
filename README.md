# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--20_12:13:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **238,582 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **3** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-20 12:13:42 | Magura (Kalu Ganga) | 2.90 | 🟢 Normal | 0.000 |  |
| 2026-08-20 12:13:22 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.050 |  |
| 2026-08-20 12:13:03 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | -0.009 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-20 12:02:25 | Ellagawa (Kalu Ganga) | 5.59 | 🟢 Normal | 0.134 | 🔺 Rising |
| 2026-08-20 12:03:34 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-08-20 12:02:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.18 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-08-20 12:02:06 | Glencourse (Kelani Ganga) | 9.79 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-08-20 11:05:20 | Panadugama (Nilwala Ganga) | 2.41 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-08-20 12:09:51 | Urawa (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-08-20 12:01:48 | Wellawaya (Kirindi Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-20 12:02:18 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-20 12:01:41 | Nawalapitiya (Mahaweli Ganga) | 1.59 | 🟢 Normal | 0.000 |  |
| 2026-08-20 12:01:16 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-20 12:01:34 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-08-20 12:02:13 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-08-20 12:13:42 | Magura (Kalu Ganga) | 2.90 | 🟢 Normal | 0.000 |  |
| 2026-08-20 12:02:55 | Hanwella (Kelani Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-08-20 12:01:54 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-20 12:00:24 | Moraketiya (Walawe Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-08-20 12:03:37 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-20 12:00:41 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-20 12:04:40 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-08-20 12:04:36 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-08-20 12:01:17 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-08-20 12:04:19 | Rathnapura (Kalu Ganga) | 2.92 | 🟢 Normal | 0.000 |  |
| 2026-08-20 12:01:15 | Thanthirimale (Malwathu Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-08-20 12:02:43 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-08-20 12:01:33 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-20 12:13:03 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | -0.009 |  |
| 2026-08-20 12:05:04 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | -0.009 |  |
| 2026-08-20 12:02:51 | Moragaswewa (Deduru Oya) | -0.19 | 🟢 Normal | -0.010 |  |
| 2026-08-20 12:02:48 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-08-20 12:02:45 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | -0.011 |  |
| 2026-08-20 12:01:55 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | -0.020 |  |
| 2026-08-20 12:02:14 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.031 |  |
| 2026-08-20 12:06:06 | Deraniyagala (Kelani Ganga) | 0.97 | 🟢 Normal | -0.039 |  |
| 2026-08-20 12:04:19 | Pitabeddara (Nilwala Ganga) | 0.61 | 🟢 Normal | -0.039 |  |
| 2026-08-20 12:01:18 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | -0.040 |  |
| 2026-08-20 12:13:22 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.050 |  |
| 2026-08-20 12:02:16 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.057 |  |
| 2026-08-20 12:02:33 | Thawalama (Gin Ganga) | 1.78 | 🟢 Normal | -0.084 |  |
| 2026-08-20 12:01:49 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | -0.119 |  |

## River Water Level Charts by Station

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)