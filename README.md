# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--08_05:37:17-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **309,926 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Panadugama — Alert; 🟡 Dunamale — Alert; 🟡 Magura — Alert; 🟡 Urawa — Alert; 🟡 Moraketiya — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-08 05:37:17 | Rathnapura (Kalu Ganga) | 5.00 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-11-08 05:34:18 | Magura (Kalu Ganga) | 4.38 | 🟡 Alert | -0.131 |  |
| 2026-11-08 05:29:41 | Kuda Oya (Kirindi Oya) | 2.95 | 🟢 Normal | -0.021 |  |
| 2026-11-08 05:19:42 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-11-08 05:18:10 | Dunamale (Aththanagalu Oya) | 3.77 | 🟡 Alert | -0.012 |  |
| 2026-11-08 05:16:15 | Kithulgala (Kelani Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-11-08 05:16:14 | Kithulgala (Kelani Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-11-08 05:12:05 | Thalgahagoda (Nilwala Ganga) | 1.15 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-11-08 05:11:38 | Thanamalwila (Kirindi Oya) | 2.70 | 🟢 Normal | -0.964 |  |
| 2026-11-08 05:11:25 | Magura (Kalu Ganga) | 4.43 | 🟡 Alert | -0.131 |  |
| 2026-11-08 05:09:58 | Holombuwa (Kelani Ganga) | 1.31 | 🟢 Normal | -0.042 |  |
| 2026-11-08 05:09:51 | Urawa (Nilwala Ganga) | 2.60 | 🟡 Alert | -0.411 |  |
| 2026-11-08 05:08:27 | Deraniyagala (Kelani Ganga) | 0.82 | 🟢 Normal | -0.037 |  |
| 2026-11-08 05:08:14 | Moraketiya (Walawe Ganga) | 4.05 | 🟡 Alert | -0.641 |  |
| 2026-11-08 05:07:59 | Katharagama (Menik Ganga) | 0.11 | 🟢 Normal | -0.009 |  |
| 2026-11-08 05:07:31 | Putupaula (Kalu Ganga) | 1.63 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-11-08 05:07:11 | Norwood (Kelani Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-11-08 05:06:29 | Thawalama (Gin Ganga) | 3.22 | 🟢 Normal | -0.824 |  |
| 2026-11-08 05:06:07 | Pitabeddara (Nilwala Ganga) | 2.79 | 🟢 Normal | 1.049 | 🔺 Rising |
| 2026-11-08 05:05:37 | Thaldena (Mahaweli Ganga) | 0.90 | 🟢 Normal | -0.087 |  |
| 2026-11-08 05:05:18 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-08 05:04:09 | Padiyathalawa (Maduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-08 05:04:07 | Baddegama (Gin Ganga) | 2.83 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-11-08 05:04:00 | Manampitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | -0.030 |  |
| 2026-11-08 05:03:45 | Glencourse (Kelani Ganga) | 10.90 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-08 05:03:41 | Badalgama (Maha Oya) | 4.15 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-11-08 05:03:25 | Moragaswewa (Deduru Oya) | 2.16 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-11-08 05:03:19 | Peradeniya (Mahaweli Ganga) | 3.28 | 🟢 Normal | -0.134 |  |
| 2026-11-08 05:03:08 | Wellawaya (Kirindi Oya) | 2.32 | 🟢 Normal | -0.544 |  |
| 2026-11-08 05:02:46 | Horowpothana (Yan Oya) | 2.43 | 🟢 Normal | 0.000 |  |
| 2026-11-08 05:02:21 | Hanwella (Kelani Ganga) | 3.25 | 🟢 Normal | -0.021 |  |
| 2026-11-08 05:02:13 | Ellagawa (Kalu Ganga) | 7.08 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-11-08 05:01:39 | Giriulla (Maha Oya) | 3.40 | 🟢 Normal | -0.091 |  |
| 2026-11-08 05:01:19 | Nakkala (Kumbukkan Oya) | 1.44 | 🟢 Normal | -1.865 |  |
| 2026-11-08 05:01:09 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-11-08 05:00:53 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.031 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-08 04:01:46 | Panadugama (Nilwala Ganga) | 5.89 | 🟡 Alert | 0.457 | 🔺 Rising |
| 2026-11-08 05:18:10 | Dunamale (Aththanagalu Oya) | 3.77 | 🟡 Alert | -0.012 |  |
| 2026-11-08 05:34:18 | Magura (Kalu Ganga) | 4.38 | 🟡 Alert | -0.131 |  |
| 2026-11-08 05:09:51 | Urawa (Nilwala Ganga) | 2.60 | 🟡 Alert | -0.411 |  |
| 2026-11-08 05:08:14 | Moraketiya (Walawe Ganga) | 4.05 | 🟡 Alert | -0.641 |  |
| 2026-11-08 05:06:07 | Pitabeddara (Nilwala Ganga) | 2.79 | 🟢 Normal | 1.049 | 🔺 Rising |
| 2026-11-08 05:03:41 | Badalgama (Maha Oya) | 4.15 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-11-08 05:03:25 | Moragaswewa (Deduru Oya) | 2.16 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-11-08 05:07:31 | Putupaula (Kalu Ganga) | 1.63 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-11-08 05:02:13 | Ellagawa (Kalu Ganga) | 7.08 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-11-08 05:04:07 | Baddegama (Gin Ganga) | 2.83 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-11-08 05:12:05 | Thalgahagoda (Nilwala Ganga) | 1.15 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-11-08 05:37:17 | Rathnapura (Kalu Ganga) | 5.00 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-11-08 05:03:45 | Glencourse (Kelani Ganga) | 10.90 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-08 05:16:15 | Kithulgala (Kelani Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-11-08 05:19:42 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-11-08 05:05:18 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-08 05:02:46 | Horowpothana (Yan Oya) | 2.43 | 🟢 Normal | 0.000 |  |
| 2026-11-07 18:03:13 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-11-08 05:07:11 | Norwood (Kelani Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-11-08 05:04:09 | Padiyathalawa (Maduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-08 05:01:09 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-11-08 05:07:59 | Katharagama (Menik Ganga) | 0.11 | 🟢 Normal | -0.009 |  |
| 2026-11-07 18:01:10 | Thanthirimale (Malwathu Oya) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-11-07 18:00:15 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | -0.021 |  |
| 2026-11-08 05:29:41 | Kuda Oya (Kirindi Oya) | 2.95 | 🟢 Normal | -0.021 |  |
| 2026-11-08 05:02:21 | Hanwella (Kelani Ganga) | 3.25 | 🟢 Normal | -0.021 |  |
| 2026-11-08 04:24:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.90 | 🟢 Normal | -0.029 |  |
| 2026-11-08 05:04:00 | Manampitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | -0.030 |  |
| 2026-11-08 05:00:53 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.031 |  |
| 2026-11-08 05:08:27 | Deraniyagala (Kelani Ganga) | 0.82 | 🟢 Normal | -0.037 |  |
| 2026-11-08 05:09:58 | Holombuwa (Kelani Ganga) | 1.31 | 🟢 Normal | -0.042 |  |
| 2026-11-08 05:05:37 | Thaldena (Mahaweli Ganga) | 0.90 | 🟢 Normal | -0.087 |  |
| 2026-11-08 05:01:39 | Giriulla (Maha Oya) | 3.40 | 🟢 Normal | -0.091 |  |
| 2026-11-08 05:03:19 | Peradeniya (Mahaweli Ganga) | 3.28 | 🟢 Normal | -0.134 |  |
| 2026-11-08 05:03:08 | Wellawaya (Kirindi Oya) | 2.32 | 🟢 Normal | -0.544 |  |
| 2026-11-08 05:06:29 | Thawalama (Gin Ganga) | 3.22 | 🟢 Normal | -0.824 |  |
| 2026-11-08 05:11:38 | Thanamalwila (Kirindi Oya) | 2.70 | 🟢 Normal | -0.964 |  |
| 2026-11-08 05:01:19 | Nakkala (Kumbukkan Oya) | 1.44 | 🟢 Normal | -1.865 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)