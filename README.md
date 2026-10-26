# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--26_20:17:23-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **298,750 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Holombuwa — Minor Flood; 🟠 Rathnapura — Minor Flood; 🟡 Thawalama — Alert; 🟡 Panadugama — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-26 20:17:23 | Panadugama (Nilwala Ganga) | 5.97 | 🟡 Alert | 0.101 | 🔺 Rising |
| 2026-10-26 20:13:17 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-10-26 20:10:10 | Rathnapura (Kalu Ganga) | 8.43 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-26 20:09:01 | Manampitiya (Mahaweli Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-10-26 20:08:51 | Baddegama (Gin Ganga) | 3.26 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-10-26 20:08:20 | Manampitiya (Mahaweli Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-10-26 20:08:13 | Magura (Kalu Ganga) | 4.90 | 🟡 Alert | 0.091 | 🔺 Rising |
| 2026-10-26 20:07:54 | Putupaula (Kalu Ganga) | 2.82 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-26 20:07:15 | Kithulgala (Kelani Ganga) | 2.71 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-10-26 20:06:48 | Ellagawa (Kalu Ganga) | 9.45 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-10-26 20:05:50 | Peradeniya (Mahaweli Ganga) | 5.25 | 🟡 Alert | -0.079 |  |
| 2026-10-26 20:05:33 | Thawalama (Gin Ganga) | 4.70 | 🟡 Alert | 0.217 | 🔺 Rising |
| 2026-10-26 20:05:14 | Rathnapura (Kalu Ganga) | 8.43 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-26 20:05:07 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | -0.021 |  |
| 2026-10-26 20:04:52 | Urawa (Nilwala Ganga) | 2.40 | 🟢 Normal | 0.000 |  |
| 2026-10-26 20:04:37 | Giriulla (Maha Oya) | 5.11 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-10-26 20:04:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.66 | 🟠 Minor Flood | 0.090 | 🔺 Rising |
| 2026-10-26 20:04:03 | Holombuwa (Kelani Ganga) | 3.70 | 🟠 Minor Flood | 0.073 | 🔺 Rising |
| 2026-10-26 20:03:56 | Moraketiya (Walawe Ganga) | 2.32 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-26 20:03:50 | Deraniyagala (Kelani Ganga) | 2.16 | 🟢 Normal | -0.021 |  |
| 2026-10-26 20:03:41 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-10-26 20:03:38 | Glencourse (Kelani Ganga) | 15.29 | 🟡 Alert | 0.051 | 🔺 Rising |
| 2026-10-26 20:03:13 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-10-26 20:03:09 | Moragaswewa (Deduru Oya) | 4.53 | 🟢 Normal | -0.012 |  |
| 2026-10-26 20:03:08 | Kuda Oya (Kirindi Oya) | 1.42 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-10-26 20:02:57 | Badalgama (Maha Oya) | 4.91 | 🟢 Normal | 0.194 | 🔺 Rising |
| 2026-10-26 20:02:50 | Nawalapitiya (Mahaweli Ganga) | 2.50 | 🟢 Normal | -0.165 |  |
| 2026-10-26 20:02:49 | Thalgahagoda (Nilwala Ganga) | 1.36 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-10-26 20:02:31 | Dunamale (Aththanagalu Oya) | 4.28 | 🟡 Alert | 0.080 | 🔺 Rising |
| 2026-10-26 20:02:27 | Norwood (Kelani Ganga) | 2.03 | 🟡 Alert | -0.070 |  |
| 2026-10-26 20:02:16 | Hanwella (Kelani Ganga) | 6.26 | 🟢 Normal | 0.212 | 🔺 Rising |
| 2026-10-26 20:02:05 | Horowpothana (Yan Oya) | 2.33 | 🟢 Normal | -0.031 |  |
| 2026-10-26 20:01:55 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-10-26 20:01:40 | Padiyathalawa (Maduru Oya) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-10-26 20:01:35 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-10-26 20:01:31 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-26 20:01:29 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-10-26 20:00:51 | Wellawaya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.030 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-26 20:04:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.66 | 🟠 Minor Flood | 0.090 | 🔺 Rising |
| 2026-10-26 20:04:03 | Holombuwa (Kelani Ganga) | 3.70 | 🟠 Minor Flood | 0.073 | 🔺 Rising |
| 2026-10-26 20:10:10 | Rathnapura (Kalu Ganga) | 8.43 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-26 20:05:33 | Thawalama (Gin Ganga) | 4.70 | 🟡 Alert | 0.217 | 🔺 Rising |
| 2026-10-26 20:17:23 | Panadugama (Nilwala Ganga) | 5.97 | 🟡 Alert | 0.101 | 🔺 Rising |
| 2026-10-26 20:08:13 | Magura (Kalu Ganga) | 4.90 | 🟡 Alert | 0.091 | 🔺 Rising |
| 2026-10-26 20:02:31 | Dunamale (Aththanagalu Oya) | 4.28 | 🟡 Alert | 0.080 | 🔺 Rising |
| 2026-10-26 20:03:38 | Glencourse (Kelani Ganga) | 15.29 | 🟡 Alert | 0.051 | 🔺 Rising |
| 2026-10-26 20:02:27 | Norwood (Kelani Ganga) | 2.03 | 🟡 Alert | -0.070 |  |
| 2026-10-26 20:05:50 | Peradeniya (Mahaweli Ganga) | 5.25 | 🟡 Alert | -0.079 |  |
| 2026-10-26 20:02:16 | Hanwella (Kelani Ganga) | 6.26 | 🟢 Normal | 0.212 | 🔺 Rising |
| 2026-10-26 20:02:57 | Badalgama (Maha Oya) | 4.91 | 🟢 Normal | 0.194 | 🔺 Rising |
| 2026-10-26 18:02:01 | Thanthirimale (Malwathu Oya) | 2.50 | 🟢 Normal | 0.162 | 🔺 Rising |
| 2026-10-26 20:04:37 | Giriulla (Maha Oya) | 5.11 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-10-26 20:03:08 | Kuda Oya (Kirindi Oya) | 1.42 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-10-26 20:08:51 | Baddegama (Gin Ganga) | 3.26 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-10-26 20:07:15 | Kithulgala (Kelani Ganga) | 2.71 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-10-26 18:05:52 | Galgamuwa (Mee Oya) | 4.21 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-10-26 20:02:49 | Thalgahagoda (Nilwala Ganga) | 1.36 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-10-26 20:06:48 | Ellagawa (Kalu Ganga) | 9.45 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-10-26 20:00:51 | Wellawaya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-26 20:07:54 | Putupaula (Kalu Ganga) | 2.82 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-26 20:01:31 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-26 20:03:56 | Moraketiya (Walawe Ganga) | 2.32 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-26 20:01:55 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-10-26 20:01:29 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-10-26 20:03:41 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-10-26 20:13:17 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-10-26 20:09:01 | Manampitiya (Mahaweli Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-10-26 20:04:52 | Urawa (Nilwala Ganga) | 2.40 | 🟢 Normal | 0.000 |  |
| 2026-10-26 20:01:35 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-10-26 20:01:40 | Padiyathalawa (Maduru Oya) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-10-26 20:03:09 | Moragaswewa (Deduru Oya) | 4.53 | 🟢 Normal | -0.012 |  |
| 2026-10-26 20:03:50 | Deraniyagala (Kelani Ganga) | 2.16 | 🟢 Normal | -0.021 |  |
| 2026-10-26 20:05:07 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | -0.021 |  |
| 2026-10-26 20:02:05 | Horowpothana (Yan Oya) | 2.33 | 🟢 Normal | -0.031 |  |
| 2026-10-26 18:07:46 | Pitabeddara (Nilwala Ganga) | 3.43 | 🟢 Normal | -0.057 |  |
| 2026-10-26 18:02:45 | Weraganthota (Mahaweli Ganga) | -2.38 | 🟢 Normal | -0.058 |  |
| 2026-10-26 20:02:50 | Nawalapitiya (Mahaweli Ganga) | 2.50 | 🟢 Normal | -0.165 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)