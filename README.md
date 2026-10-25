# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--26_05:03:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **298,144 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Magura — Alert; 🟡 Norwood — Alert; 🟡 Rathnapura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **17** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-26 05:03:18 | Nawalapitiya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.051 |  |
| 2026-10-26 05:03:18 | Giriulla (Maha Oya) | 3.19 | 🟢 Normal | -0.030 |  |
| 2026-10-26 05:03:14 | Glencourse (Kelani Ganga) | 12.47 | 🟢 Normal | -0.032 |  |
| 2026-10-26 05:03:00 | Nakkala (Kumbukkan Oya) | 1.12 | 🟢 Normal | -0.059 |  |
| 2026-10-26 05:02:51 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-10-26 05:02:45 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-10-26 05:02:20 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.131 |  |
| 2026-10-26 05:01:40 | Moraketiya (Walawe Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-10-26 05:01:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.12 | 🟡 Alert | 0.317 | 🔺 Rising |
| 2026-10-26 05:01:20 | Horowpothana (Yan Oya) | 2.32 | 🟢 Normal | -0.011 |  |
| 2026-10-26 05:01:17 | Ellagawa (Kalu Ganga) | 8.21 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-10-26 05:01:10 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-10-26 05:01:03 | Peradeniya (Mahaweli Ganga) | 3.66 | 🟢 Normal | 0.000 |  |
| 2026-10-26 05:00:47 | Moragaswewa (Deduru Oya) | 3.21 | 🟢 Normal | 0.258 | 🔺 Rising |
| 2026-10-26 05:00:41 | Manampitiya (Mahaweli Ganga) | 0.40 | 🟢 Normal | -0.041 |  |
| 2026-10-26 04:47:50 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-10-26 04:21:54 | Thawalama (Gin Ganga) | 3.23 | 🟢 Normal | -0.035 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-26 05:01:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.12 | 🟡 Alert | 0.317 | 🔺 Rising |
| 2026-10-26 04:00:42 | Magura (Kalu Ganga) | 4.08 | 🟡 Alert | 0.098 | 🔺 Rising |
| 2026-10-26 04:01:51 | Norwood (Kelani Ganga) | 1.54 | 🟡 Alert | 0.000 |  |
| 2026-10-26 04:07:24 | Rathnapura (Kalu Ganga) | 5.88 | 🟡 Alert | -0.088 |  |
| 2026-10-26 05:00:47 | Moragaswewa (Deduru Oya) | 3.21 | 🟢 Normal | 0.258 | 🔺 Rising |
| 2026-10-26 05:01:17 | Ellagawa (Kalu Ganga) | 8.21 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-10-25 18:03:46 | Galgamuwa (Mee Oya) | 1.82 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-10-26 04:04:17 | Hanwella (Kelani Ganga) | 4.05 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-10-26 04:06:39 | Badalgama (Maha Oya) | 3.85 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-10-26 04:03:23 | Kithulgala (Kelani Ganga) | 2.32 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-10-26 04:04:15 | Baddegama (Gin Ganga) | 2.58 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-10-26 04:00:41 | Thalgahagoda (Nilwala Ganga) | 1.13 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-26 04:09:30 | Panadugama (Nilwala Ganga) | 4.77 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-10-26 04:04:02 | Putupaula (Kalu Ganga) | 1.69 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-26 04:47:50 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-10-26 04:07:25 | Thanamalwila (Kirindi Oya) | 0.90 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-26 05:02:45 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-10-26 04:07:07 | Pitabeddara (Nilwala Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-10-26 05:01:40 | Moraketiya (Walawe Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-10-26 04:07:01 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-10-26 04:05:48 | Dunamale (Aththanagalu Oya) | 3.10 | 🟢 Normal | 0.000 |  |
| 2026-10-26 04:03:01 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-10-26 04:09:12 | Holombuwa (Kelani Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-10-25 18:02:16 | Thanthirimale (Malwathu Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-10-26 05:01:03 | Peradeniya (Mahaweli Ganga) | 3.66 | 🟢 Normal | 0.000 |  |
| 2026-10-26 05:02:51 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-10-26 05:01:10 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-10-26 05:01:20 | Horowpothana (Yan Oya) | 2.32 | 🟢 Normal | -0.011 |  |
| 2026-10-26 04:00:50 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | -0.020 |  |
| 2026-10-26 05:03:18 | Giriulla (Maha Oya) | 3.19 | 🟢 Normal | -0.030 |  |
| 2026-10-26 05:03:14 | Glencourse (Kelani Ganga) | 12.47 | 🟢 Normal | -0.032 |  |
| 2026-10-26 04:21:54 | Thawalama (Gin Ganga) | 3.23 | 🟢 Normal | -0.035 |  |
| 2026-10-26 04:09:28 | Urawa (Nilwala Ganga) | 1.23 | 🟢 Normal | -0.038 |  |
| 2026-10-26 05:00:41 | Manampitiya (Mahaweli Ganga) | 0.40 | 🟢 Normal | -0.041 |  |
| 2026-10-26 05:03:18 | Nawalapitiya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.051 |  |
| 2026-10-26 05:03:00 | Nakkala (Kumbukkan Oya) | 1.12 | 🟢 Normal | -0.059 |  |
| 2026-10-25 18:03:32 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | -0.069 |  |
| 2026-10-26 03:05:37 | Deraniyagala (Kelani Ganga) | 1.47 | 🟢 Normal | -0.099 |  |
| 2026-10-26 05:02:20 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.131 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)