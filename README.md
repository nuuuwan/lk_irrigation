# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--01_19:16:54-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **304,138 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thalgahagoda — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-01 19:16:54 | Thawalama (Gin Ganga) | 2.48 | 🟢 Normal | -0.017 |  |
| 2026-11-01 19:09:21 | Putupaula (Kalu Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-11-01 19:08:27 | Thalgahagoda (Nilwala Ganga) | 1.49 | 🟡 Alert | -0.013 |  |
| 2026-11-01 19:08:04 | Kithulgala (Kelani Ganga) | 2.16 | 🟢 Normal | -0.019 |  |
| 2026-11-01 19:08:00 | Badalgama (Maha Oya) | 2.61 | 🟢 Normal | 0.000 |  |
| 2026-11-01 19:07:33 | Baddegama (Gin Ganga) | 2.55 | 🟢 Normal | -0.037 |  |
| 2026-11-01 19:07:14 | Holombuwa (Kelani Ganga) | 0.91 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-11-01 19:07:00 | Panadugama (Nilwala Ganga) | 4.66 | 🟢 Normal | 0.000 |  |
| 2026-11-01 19:06:36 | Peradeniya (Mahaweli Ganga) | 2.64 | 🟢 Normal | 0.000 |  |
| 2026-11-01 19:06:24 | Thanamalwila (Kirindi Oya) | 0.94 | 🟢 Normal | -0.020 |  |
| 2026-11-01 19:06:19 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | -0.020 |  |
| 2026-11-01 19:05:09 | Ellagawa (Kalu Ganga) | 6.09 | 🟢 Normal | -0.010 |  |
| 2026-11-01 19:05:01 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-11-01 19:04:52 | Rathnapura (Kalu Ganga) | 2.08 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-11-01 19:04:40 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.028 |  |
| 2026-11-01 19:04:35 | Giriulla (Maha Oya) | 1.33 | 🟢 Normal | -0.009 |  |
| 2026-11-01 19:04:13 | Hanwella (Kelani Ganga) | 2.20 | 🟢 Normal | -0.019 |  |
| 2026-11-01 19:04:10 | Urawa (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-11-01 19:03:40 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2026-11-01 19:03:36 | Magura (Kalu Ganga) | 2.34 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-11-01 19:03:34 | Dunamale (Aththanagalu Oya) | 1.66 | 🟢 Normal | -0.048 |  |
| 2026-11-01 19:03:29 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | -0.020 |  |
| 2026-11-01 19:03:17 | Deraniyagala (Kelani Ganga) | 1.03 | 🟢 Normal | -0.030 |  |
| 2026-11-01 19:03:12 | Manampitiya (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-11-01 19:03:12 | Glencourse (Kelani Ganga) | 10.41 | 🟢 Normal | 0.277 | 🔺 Rising |
| 2026-11-01 19:03:09 | Horowpothana (Yan Oya) | 2.25 | 🟢 Normal | -0.010 |  |
| 2026-11-01 19:02:44 | Moragaswewa (Deduru Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-11-01 19:02:18 | Norwood (Kelani Ganga) | 1.04 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-11-01 19:02:17 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-01 19:01:42 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-01 19:01:29 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-01 19:01:12 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-11-01 19:01:04 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-11-01 19:00:15 | Wellawaya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.300 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-01 19:08:27 | Thalgahagoda (Nilwala Ganga) | 1.49 | 🟡 Alert | -0.013 |  |
| 2026-11-01 19:00:15 | Wellawaya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.300 | 🔺 Rising |
| 2026-11-01 19:03:12 | Glencourse (Kelani Ganga) | 10.41 | 🟢 Normal | 0.277 | 🔺 Rising |
| 2026-11-01 19:03:40 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2026-11-01 19:03:12 | Manampitiya (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-11-01 19:07:14 | Holombuwa (Kelani Ganga) | 0.91 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-11-01 19:02:18 | Norwood (Kelani Ganga) | 1.04 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-11-01 19:03:36 | Magura (Kalu Ganga) | 2.34 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-11-01 19:04:52 | Rathnapura (Kalu Ganga) | 2.08 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-11-01 18:02:39 | Weraganthota (Mahaweli Ganga) | -2.72 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-11-01 18:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.51 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-01 19:01:04 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-11-01 19:02:44 | Moragaswewa (Deduru Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-11-01 19:01:42 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-01 19:07:00 | Panadugama (Nilwala Ganga) | 4.66 | 🟢 Normal | 0.000 |  |
| 2026-11-01 19:01:12 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-11-01 19:05:01 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-11-01 19:01:29 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-01 19:09:21 | Putupaula (Kalu Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-11-01 19:08:00 | Badalgama (Maha Oya) | 2.61 | 🟢 Normal | 0.000 |  |
| 2026-11-01 18:01:13 | Thanthirimale (Malwathu Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-01 19:06:36 | Peradeniya (Mahaweli Ganga) | 2.64 | 🟢 Normal | 0.000 |  |
| 2026-11-01 19:04:10 | Urawa (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-11-01 19:02:17 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-01 19:04:35 | Giriulla (Maha Oya) | 1.33 | 🟢 Normal | -0.009 |  |
| 2026-11-01 19:05:09 | Ellagawa (Kalu Ganga) | 6.09 | 🟢 Normal | -0.010 |  |
| 2026-11-01 19:03:09 | Horowpothana (Yan Oya) | 2.25 | 🟢 Normal | -0.010 |  |
| 2026-11-01 19:16:54 | Thawalama (Gin Ganga) | 2.48 | 🟢 Normal | -0.017 |  |
| 2026-11-01 19:04:13 | Hanwella (Kelani Ganga) | 2.20 | 🟢 Normal | -0.019 |  |
| 2026-11-01 19:08:04 | Kithulgala (Kelani Ganga) | 2.16 | 🟢 Normal | -0.019 |  |
| 2026-11-01 19:06:19 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | -0.020 |  |
| 2026-11-01 19:03:29 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | -0.020 |  |
| 2026-11-01 18:01:32 | Pitabeddara (Nilwala Ganga) | 1.34 | 🟢 Normal | -0.020 |  |
| 2026-11-01 19:06:24 | Thanamalwila (Kirindi Oya) | 0.94 | 🟢 Normal | -0.020 |  |
| 2026-11-01 19:04:40 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.028 |  |
| 2026-11-01 19:03:17 | Deraniyagala (Kelani Ganga) | 1.03 | 🟢 Normal | -0.030 |  |
| 2026-11-01 18:02:14 | Galgamuwa (Mee Oya) | 0.96 | 🟢 Normal | -0.030 |  |
| 2026-11-01 19:07:33 | Baddegama (Gin Ganga) | 2.55 | 🟢 Normal | -0.037 |  |
| 2026-11-01 19:03:34 | Dunamale (Aththanagalu Oya) | 1.66 | 🟢 Normal | -0.048 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

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

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)