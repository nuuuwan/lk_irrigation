# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--04_13:21:54-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **224,710 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Rathnapura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-04 13:21:54 | Dunamale (Aththanagalu Oya) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-08-04 13:14:20 | Baddegama (Gin Ganga) | 2.64 | 🟢 Normal | 0.909 | 🔺 Rising |
| 2026-08-04 13:13:55 | Panadugama (Nilwala Ganga) | 4.07 | 🟢 Normal | 0.000 |  |
| 2026-08-04 13:12:47 | Dunamale (Aththanagalu Oya) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-08-04 13:09:05 | Glencourse (Kelani Ganga) | 13.40 | 🟢 Normal | -0.199 |  |
| 2026-08-04 13:08:57 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | -0.009 |  |
| 2026-08-04 13:08:07 | Magura (Kalu Ganga) | 2.32 | 🟢 Normal | -0.009 |  |
| 2026-08-04 13:07:55 | Panadugama (Nilwala Ganga) | 4.07 | 🟢 Normal | 0.000 |  |
| 2026-08-04 13:07:35 | Holombuwa (Kelani Ganga) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-08-04 13:06:44 | Norwood (Kelani Ganga) | 1.27 | 🟢 Normal | -0.088 |  |
| 2026-08-04 13:06:18 | Giriulla (Maha Oya) | 1.61 | 🟢 Normal | -0.056 |  |
| 2026-08-04 13:05:19 | Manampitiya (Mahaweli Ganga) | 0.05 | 🟢 Normal | -0.009 |  |
| 2026-08-04 13:04:49 | Rathnapura (Kalu Ganga) | 6.65 | 🟡 Alert | -0.119 |  |
| 2026-08-04 13:04:40 | Hanwella (Kelani Ganga) | 6.12 | 🟢 Normal | -0.154 |  |
| 2026-08-04 13:04:19 | Nagalagam Street (Kelani Ganga) | 0.99 | 🟢 Normal | -0.015 |  |
| 2026-08-04 13:04:01 | Badalgama (Maha Oya) | 3.01 | 🟢 Normal | -0.078 |  |
| 2026-08-04 13:03:54 | Nawalapitiya (Mahaweli Ganga) | 2.86 | 🟢 Normal | -0.040 |  |
| 2026-08-04 13:03:53 | Urawa (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-04 13:03:35 | Peradeniya (Mahaweli Ganga) | 4.42 | 🟢 Normal | -0.077 |  |
| 2026-08-04 13:03:31 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-08-04 13:03:19 | Putupaula (Kalu Ganga) | 2.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-04 13:03:06 | Thawalama (Gin Ganga) | 2.43 | 🟢 Normal | -0.010 |  |
| 2026-08-04 13:02:53 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-04 13:02:50 | Deraniyagala (Kelani Ganga) | 1.86 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-08-04 13:02:48 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-04 13:02:44 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.003 |  |
| 2026-08-04 13:02:39 | Pitabeddara (Nilwala Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-08-04 13:02:25 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-08-04 13:02:19 | Kithulgala (Kelani Ganga) | 2.89 | 🟢 Normal | -0.031 |  |
| 2026-08-04 13:02:17 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-04 13:02:15 | Thalgahagoda (Nilwala Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-08-04 13:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.39 | 🟡 Alert | 0.000 |  |
| 2026-08-04 13:02:05 | Weraganthota (Mahaweli Ganga) | -2.88 | 🟢 Normal | -0.053 |  |
| 2026-08-04 13:02:01 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | -0.031 |  |
| 2026-08-04 13:01:57 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-04 13:01:34 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-08-04 13:01:29 | Ellagawa (Kalu Ganga) | 8.74 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-04 13:01:20 | Horowpothana (Yan Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-08-04 13:01:20 | Thanamalwila (Kirindi Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-04 13:01:02 | Thanthirimale (Malwathu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-08-04 13:00:52 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-04 13:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.39 | 🟡 Alert | 0.000 |  |
| 2026-08-04 13:04:49 | Rathnapura (Kalu Ganga) | 6.65 | 🟡 Alert | -0.119 |  |
| 2026-08-04 13:14:20 | Baddegama (Gin Ganga) | 2.64 | 🟢 Normal | 0.909 | 🔺 Rising |
| 2026-08-04 13:02:50 | Deraniyagala (Kelani Ganga) | 1.86 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-08-04 13:01:29 | Ellagawa (Kalu Ganga) | 8.74 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-04 13:03:19 | Putupaula (Kalu Ganga) | 2.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-04 13:02:44 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.003 |  |
| 2026-08-04 13:02:48 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-04 13:01:34 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-08-04 13:01:57 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-04 13:01:20 | Horowpothana (Yan Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-08-04 13:02:53 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-04 13:02:39 | Pitabeddara (Nilwala Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-08-04 13:13:55 | Panadugama (Nilwala Ganga) | 4.07 | 🟢 Normal | 0.000 |  |
| 2026-08-04 13:03:31 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-08-04 13:02:25 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-08-04 13:21:54 | Dunamale (Aththanagalu Oya) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-08-04 13:02:17 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-04 13:01:02 | Thanthirimale (Malwathu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-08-04 13:03:53 | Urawa (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-04 13:02:15 | Thalgahagoda (Nilwala Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-08-04 13:01:20 | Thanamalwila (Kirindi Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-04 13:08:57 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | -0.009 |  |
| 2026-08-04 13:05:19 | Manampitiya (Mahaweli Ganga) | 0.05 | 🟢 Normal | -0.009 |  |
| 2026-08-04 13:08:07 | Magura (Kalu Ganga) | 2.32 | 🟢 Normal | -0.009 |  |
| 2026-08-04 13:07:35 | Holombuwa (Kelani Ganga) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-08-04 13:03:06 | Thawalama (Gin Ganga) | 2.43 | 🟢 Normal | -0.010 |  |
| 2026-08-04 13:00:52 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-08-04 13:04:19 | Nagalagam Street (Kelani Ganga) | 0.99 | 🟢 Normal | -0.015 |  |
| 2026-08-04 13:02:01 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | -0.031 |  |
| 2026-08-04 13:02:19 | Kithulgala (Kelani Ganga) | 2.89 | 🟢 Normal | -0.031 |  |
| 2026-08-04 13:03:54 | Nawalapitiya (Mahaweli Ganga) | 2.86 | 🟢 Normal | -0.040 |  |
| 2026-08-04 13:02:05 | Weraganthota (Mahaweli Ganga) | -2.88 | 🟢 Normal | -0.053 |  |
| 2026-08-04 13:06:18 | Giriulla (Maha Oya) | 1.61 | 🟢 Normal | -0.056 |  |
| 2026-08-04 13:03:35 | Peradeniya (Mahaweli Ganga) | 4.42 | 🟢 Normal | -0.077 |  |
| 2026-08-04 13:04:01 | Badalgama (Maha Oya) | 3.01 | 🟢 Normal | -0.078 |  |
| 2026-08-04 13:06:44 | Norwood (Kelani Ganga) | 1.27 | 🟢 Normal | -0.088 |  |
| 2026-08-04 13:04:40 | Hanwella (Kelani Ganga) | 6.12 | 🟢 Normal | -0.154 |  |
| 2026-08-04 13:09:05 | Glencourse (Kelani Ganga) | 13.40 | 🟢 Normal | -0.199 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)