# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--01_14:20:38-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **303,946 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thalgahagoda — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-01 14:20:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.48 | 🟢 Normal | 0.000 |  |
| 2026-11-01 14:20:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.48 | 🟢 Normal | 0.000 |  |
| 2026-11-01 14:17:36 | Giriulla (Maha Oya) | 1.36 | 🟢 Normal | -0.008 |  |
| 2026-11-01 14:14:23 | Urawa (Nilwala Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-11-01 14:14:00 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-01 14:10:11 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | -0.018 |  |
| 2026-11-01 14:08:37 | Moraketiya (Walawe Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-11-01 14:07:02 | Thalgahagoda (Nilwala Ganga) | 1.53 | 🟡 Alert | 0.000 |  |
| 2026-11-01 14:06:16 | Glencourse (Kelani Ganga) | 10.35 | 🟢 Normal | -0.050 |  |
| 2026-11-01 14:06:13 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-01 14:06:02 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-11-01 14:05:57 | Peradeniya (Mahaweli Ganga) | 2.58 | 🟢 Normal | 0.000 |  |
| 2026-11-01 14:05:43 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-01 14:04:57 | Holombuwa (Kelani Ganga) | 0.65 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-11-01 14:04:44 | Panadugama (Nilwala Ganga) | 4.67 | 🟢 Normal | -0.010 |  |
| 2026-11-01 14:04:36 | Badalgama (Maha Oya) | 2.63 | 🟢 Normal | 0.000 |  |
| 2026-11-01 14:04:09 | Moragaswewa (Deduru Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-11-01 14:04:02 | Hanwella (Kelani Ganga) | 2.30 | 🟢 Normal | -0.010 |  |
| 2026-11-01 14:04:00 | Ellagawa (Kalu Ganga) | 6.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-01 14:03:45 | Magura (Kalu Ganga) | 2.08 | 🟢 Normal | -0.011 |  |
| 2026-11-01 14:03:39 | Deraniyagala (Kelani Ganga) | 0.66 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-11-01 14:03:32 | Putupaula (Kalu Ganga) | 0.98 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-01 14:03:31 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-11-01 14:03:17 | Thanamalwila (Kirindi Oya) | 0.90 | 🟢 Normal | -0.110 |  |
| 2026-11-01 14:03:12 | Moraketiya (Walawe Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-11-01 14:02:43 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-11-01 14:02:06 | Weraganthota (Mahaweli Ganga) | 2.84 | 🟢 Normal | 5.578 | 🔺 Rising |
| 2026-11-01 14:01:58 | Horowpothana (Yan Oya) | 2.29 | 🟢 Normal | 0.000 |  |
| 2026-11-01 14:01:58 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-01 14:01:51 | Manampitiya (Mahaweli Ganga) | 0.16 | 🟢 Normal | -0.021 |  |
| 2026-11-01 14:01:50 | Galgamuwa (Mee Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-11-01 14:01:38 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-11-01 14:01:33 | Baddegama (Gin Ganga) | 2.66 | 🟢 Normal | 0.000 |  |
| 2026-11-01 14:01:29 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | -0.031 |  |
| 2026-11-01 14:01:19 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-11-01 14:01:17 | Rathnapura (Kalu Ganga) | 1.95 | 🟢 Normal | -0.034 |  |
| 2026-11-01 14:00:59 | Dunamale (Aththanagalu Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-11-01 14:00:43 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-11-01 14:00:43 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-11-01 14:00:39 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-01 14:00:10 | Pitabeddara (Nilwala Ganga) | 1.42 | 🟢 Normal | -0.021 |  |
| 2026-11-01 14:00:09 | Thawalama (Gin Ganga) | 2.14 | 🟢 Normal | -0.025 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-01 14:07:02 | Thalgahagoda (Nilwala Ganga) | 1.53 | 🟡 Alert | 0.000 |  |
| 2026-11-01 14:02:06 | Weraganthota (Mahaweli Ganga) | 2.84 | 🟢 Normal | 5.578 | 🔺 Rising |
| 2026-11-01 14:03:39 | Deraniyagala (Kelani Ganga) | 0.66 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-11-01 14:04:57 | Holombuwa (Kelani Ganga) | 0.65 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-11-01 14:00:43 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-11-01 14:03:32 | Putupaula (Kalu Ganga) | 0.98 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-01 14:04:00 | Ellagawa (Kalu Ganga) | 6.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-01 14:06:13 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-01 14:01:38 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-11-01 14:04:09 | Moragaswewa (Deduru Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-11-01 14:00:43 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-11-01 14:01:58 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-01 14:01:58 | Horowpothana (Yan Oya) | 2.29 | 🟢 Normal | 0.000 |  |
| 2026-11-01 14:01:50 | Galgamuwa (Mee Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-11-01 14:01:33 | Baddegama (Gin Ganga) | 2.66 | 🟢 Normal | 0.000 |  |
| 2026-11-01 14:06:02 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-11-01 14:08:37 | Moraketiya (Walawe Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-11-01 14:00:39 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-01 14:00:59 | Dunamale (Aththanagalu Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-11-01 14:04:36 | Badalgama (Maha Oya) | 2.63 | 🟢 Normal | 0.000 |  |
| 2026-11-01 14:01:19 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-11-01 14:05:57 | Peradeniya (Mahaweli Ganga) | 2.58 | 🟢 Normal | 0.000 |  |
| 2026-11-01 14:14:23 | Urawa (Nilwala Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-11-01 14:14:00 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-01 14:20:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.48 | 🟢 Normal | 0.000 |  |
| 2026-11-01 14:17:36 | Giriulla (Maha Oya) | 1.36 | 🟢 Normal | -0.008 |  |
| 2026-11-01 14:02:43 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-11-01 14:04:02 | Hanwella (Kelani Ganga) | 2.30 | 🟢 Normal | -0.010 |  |
| 2026-11-01 14:04:44 | Panadugama (Nilwala Ganga) | 4.67 | 🟢 Normal | -0.010 |  |
| 2026-11-01 14:03:31 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-11-01 14:03:45 | Magura (Kalu Ganga) | 2.08 | 🟢 Normal | -0.011 |  |
| 2026-11-01 14:10:11 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | -0.018 |  |
| 2026-11-01 14:01:51 | Manampitiya (Mahaweli Ganga) | 0.16 | 🟢 Normal | -0.021 |  |
| 2026-11-01 14:00:10 | Pitabeddara (Nilwala Ganga) | 1.42 | 🟢 Normal | -0.021 |  |
| 2026-11-01 14:00:09 | Thawalama (Gin Ganga) | 2.14 | 🟢 Normal | -0.025 |  |
| 2026-11-01 14:01:29 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | -0.031 |  |
| 2026-11-01 14:01:17 | Rathnapura (Kalu Ganga) | 1.95 | 🟢 Normal | -0.034 |  |
| 2026-11-01 14:06:16 | Glencourse (Kelani Ganga) | 10.35 | 🟢 Normal | -0.050 |  |
| 2026-11-01 14:03:17 | Thanamalwila (Kirindi Oya) | 0.90 | 🟢 Normal | -0.110 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)