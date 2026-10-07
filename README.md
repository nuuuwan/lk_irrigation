# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--07_10:11:44-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **281,274 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-07 10:11:44 | Panadugama (Nilwala Ganga) | 5.50 | 🟡 Alert | -0.100 |  |
| 2026-10-07 10:10:50 | Dunamale (Aththanagalu Oya) | 2.21 | 🟢 Normal | -0.009 |  |
| 2026-10-07 10:10:47 | Thanthirimale (Malwathu Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-10-07 10:10:46 | Thawalama (Gin Ganga) | 2.59 | 🟢 Normal | -0.083 |  |
| 2026-10-07 10:09:28 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-07 10:09:11 | Holombuwa (Kelani Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-10-07 10:08:16 | Rathnapura (Kalu Ganga) | 1.82 | 🟢 Normal | -0.019 |  |
| 2026-10-07 10:07:49 | Magura (Kalu Ganga) | 2.25 | 🟢 Normal | -0.072 |  |
| 2026-10-07 10:07:16 | Urawa (Nilwala Ganga) | 0.52 | 🟢 Normal | -0.011 |  |
| 2026-10-07 10:07:10 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-10-07 10:07:03 | Baddegama (Gin Ganga) | 2.45 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-07 10:06:46 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.037 |  |
| 2026-10-07 10:06:40 | Badalgama (Maha Oya) | 3.00 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-07 10:06:20 | Nawalapitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-10-07 10:05:56 | Pitabeddara (Nilwala Ganga) | 1.52 | 🟢 Normal | -0.030 |  |
| 2026-10-07 10:05:17 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-10-07 10:04:41 | Norwood (Kelani Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-10-07 10:04:35 | Glencourse (Kelani Ganga) | 10.86 | 🟢 Normal | -0.031 |  |
| 2026-10-07 10:04:14 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | -0.051 |  |
| 2026-10-07 10:04:12 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-07 10:03:58 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | -0.020 |  |
| 2026-10-07 10:03:48 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | -0.029 |  |
| 2026-10-07 10:03:41 | Ellagawa (Kalu Ganga) | 5.59 | 🟢 Normal | -0.010 |  |
| 2026-10-07 10:03:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.66 | 🟢 Normal | -0.118 |  |
| 2026-10-07 10:03:08 | Peradeniya (Mahaweli Ganga) | 2.65 | 🟢 Normal | -0.156 |  |
| 2026-10-07 10:02:59 | Giriulla (Maha Oya) | 1.78 | 🟢 Normal | -0.020 |  |
| 2026-10-07 10:02:48 | Kithulgala (Kelani Ganga) | 2.11 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-10-07 10:02:28 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | -0.011 |  |
| 2026-10-07 10:02:28 | Hanwella (Kelani Ganga) | 2.70 | 🟢 Normal | -0.020 |  |
| 2026-10-07 10:02:11 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-10-07 10:02:06 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | -0.030 |  |
| 2026-10-07 10:01:44 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | -0.084 |  |
| 2026-10-07 10:01:38 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-07 10:01:34 | Kuda Oya (Kirindi Oya) | 1.44 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-10-07 10:01:07 | Siyambalanduwa (Heda Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-10-07 10:01:06 | Manampitiya (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-07 10:00:47 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | -0.071 |  |
| 2026-10-07 10:00:20 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-07 10:11:44 | Panadugama (Nilwala Ganga) | 5.50 | 🟡 Alert | -0.100 |  |
| 2026-10-07 10:07:10 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-10-07 10:01:34 | Kuda Oya (Kirindi Oya) | 1.44 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-10-07 10:02:48 | Kithulgala (Kelani Ganga) | 2.11 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-10-07 10:01:06 | Manampitiya (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-07 10:06:40 | Badalgama (Maha Oya) | 3.00 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-07 10:07:03 | Baddegama (Gin Ganga) | 2.45 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-07 10:04:12 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-07 10:00:20 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-10-07 10:06:20 | Nawalapitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-10-07 10:01:38 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-07 10:02:11 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-10-07 10:09:28 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-07 10:01:07 | Siyambalanduwa (Heda Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-10-07 10:05:17 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-10-07 10:09:11 | Holombuwa (Kelani Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-10-07 10:10:47 | Thanthirimale (Malwathu Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-10-07 09:09:40 | Thalgahagoda (Nilwala Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-10-07 10:10:50 | Dunamale (Aththanagalu Oya) | 2.21 | 🟢 Normal | -0.009 |  |
| 2026-10-07 10:04:41 | Norwood (Kelani Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-10-07 10:03:41 | Ellagawa (Kalu Ganga) | 5.59 | 🟢 Normal | -0.010 |  |
| 2026-10-07 10:02:28 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | -0.011 |  |
| 2026-10-07 10:07:16 | Urawa (Nilwala Ganga) | 0.52 | 🟢 Normal | -0.011 |  |
| 2026-10-07 10:08:16 | Rathnapura (Kalu Ganga) | 1.82 | 🟢 Normal | -0.019 |  |
| 2026-10-07 10:03:58 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | -0.020 |  |
| 2026-10-07 10:02:28 | Hanwella (Kelani Ganga) | 2.70 | 🟢 Normal | -0.020 |  |
| 2026-10-07 10:02:59 | Giriulla (Maha Oya) | 1.78 | 🟢 Normal | -0.020 |  |
| 2026-10-07 10:03:48 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | -0.029 |  |
| 2026-10-07 10:02:06 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | -0.030 |  |
| 2026-10-07 10:05:56 | Pitabeddara (Nilwala Ganga) | 1.52 | 🟢 Normal | -0.030 |  |
| 2026-10-07 10:04:35 | Glencourse (Kelani Ganga) | 10.86 | 🟢 Normal | -0.031 |  |
| 2026-10-07 10:06:46 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.037 |  |
| 2026-10-07 10:04:14 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | -0.051 |  |
| 2026-10-07 10:00:47 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | -0.071 |  |
| 2026-10-07 10:07:49 | Magura (Kalu Ganga) | 2.25 | 🟢 Normal | -0.072 |  |
| 2026-10-07 10:10:46 | Thawalama (Gin Ganga) | 2.59 | 🟢 Normal | -0.083 |  |
| 2026-10-07 10:01:44 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | -0.084 |  |
| 2026-10-07 10:03:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.66 | 🟢 Normal | -0.118 |  |
| 2026-10-07 10:03:08 | Peradeniya (Mahaweli Ganga) | 2.65 | 🟢 Normal | -0.156 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)