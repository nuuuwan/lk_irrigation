# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--01_04:33:07-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **303,547 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thalgahagoda — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **28** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-01 04:33:07 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.007 |  |
| 2026-11-01 04:26:04 | Panadugama (Nilwala Ganga) | 4.73 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-11-01 04:21:38 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-11-01 04:14:34 | Holombuwa (Kelani Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-11-01 04:12:11 | Dunamale (Aththanagalu Oya) | 1.82 | 🟢 Normal | -0.018 |  |
| 2026-11-01 04:11:16 | Thawalama (Gin Ganga) | 2.27 | 🟢 Normal | 0.262 | 🔺 Rising |
| 2026-11-01 04:07:51 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-11-01 04:07:09 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-11-01 04:06:00 | Putupaula (Kalu Ganga) | 1.21 | 🟢 Normal | -0.089 |  |
| 2026-11-01 04:05:54 | Rathnapura (Kalu Ganga) | 2.08 | 🟢 Normal | -0.018 |  |
| 2026-11-01 04:05:39 | Baddegama (Gin Ganga) | 2.29 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-11-01 04:04:02 | Thalgahagoda (Nilwala Ganga) | 1.55 | 🟡 Alert | 0.000 |  |
| 2026-11-01 04:03:31 | Manampitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.049 |  |
| 2026-11-01 04:03:15 | Moragaswewa (Deduru Oya) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-11-01 04:03:08 | Glencourse (Kelani Ganga) | 10.25 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-01 04:03:06 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-01 04:03:00 | Deraniyagala (Kelani Ganga) | 0.80 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-11-01 04:02:57 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-11-01 04:02:37 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | -0.005 |  |
| 2026-11-01 04:02:33 | Ellagawa (Kalu Ganga) | 6.12 | 🟢 Normal | -0.030 |  |
| 2026-11-01 04:02:32 | Hanwella (Kelani Ganga) | 2.17 | 🟢 Normal | 0.000 |  |
| 2026-11-01 04:02:29 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-11-01 04:02:13 | Thanamalwila (Kirindi Oya) | 1.49 | 🟢 Normal | -0.068 |  |
| 2026-11-01 04:01:54 | Horowpothana (Yan Oya) | 2.30 | 🟢 Normal | 0.000 |  |
| 2026-11-01 04:01:45 | Moraketiya (Walawe Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-11-01 04:01:12 | Kuda Oya (Kirindi Oya) | 1.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-01 04:01:05 | Wellawaya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-01 04:00:55 | Peradeniya (Mahaweli Ganga) | 2.65 | 🟢 Normal | -0.022 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-01 04:04:02 | Thalgahagoda (Nilwala Ganga) | 1.55 | 🟡 Alert | 0.000 |  |
| 2026-11-01 04:11:16 | Thawalama (Gin Ganga) | 2.27 | 🟢 Normal | 0.262 | 🔺 Rising |
| 2026-11-01 04:02:57 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-11-01 04:07:09 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-11-01 04:03:00 | Deraniyagala (Kelani Ganga) | 0.80 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-11-01 04:03:08 | Glencourse (Kelani Ganga) | 10.25 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-01 04:05:39 | Baddegama (Gin Ganga) | 2.29 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-11-01 04:26:04 | Panadugama (Nilwala Ganga) | 4.73 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-11-01 04:01:05 | Wellawaya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-01 04:01:12 | Kuda Oya (Kirindi Oya) | 1.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-01 03:10:56 | Pitabeddara (Nilwala Ganga) | 1.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-01 04:21:38 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-11-01 03:01:34 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-11-01 04:03:06 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-01 04:01:54 | Horowpothana (Yan Oya) | 2.30 | 🟢 Normal | 0.000 |  |
| 2026-11-01 03:04:56 | Magura (Kalu Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-11-01 04:02:29 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-11-01 04:02:32 | Hanwella (Kelani Ganga) | 2.17 | 🟢 Normal | 0.000 |  |
| 2026-11-01 03:02:48 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-11-01 04:01:45 | Moraketiya (Walawe Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-11-01 04:07:51 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-11-01 04:14:34 | Holombuwa (Kelani Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-11-01 04:02:37 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | -0.005 |  |
| 2026-11-01 04:33:07 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.007 |  |
| 2026-11-01 03:10:02 | Urawa (Nilwala Ganga) | 0.89 | 🟢 Normal | -0.009 |  |
| 2026-11-01 03:04:43 | Giriulla (Maha Oya) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-11-01 04:03:15 | Moragaswewa (Deduru Oya) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-10-31 18:00:38 | Thanthirimale (Malwathu Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-10-31 18:01:51 | Galgamuwa (Mee Oya) | 1.09 | 🟢 Normal | -0.011 |  |
| 2026-11-01 04:05:54 | Rathnapura (Kalu Ganga) | 2.08 | 🟢 Normal | -0.018 |  |
| 2026-11-01 04:12:11 | Dunamale (Aththanagalu Oya) | 1.82 | 🟢 Normal | -0.018 |  |
| 2026-11-01 03:04:27 | Badalgama (Maha Oya) | 2.71 | 🟢 Normal | -0.020 |  |
| 2026-10-31 18:04:44 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | -0.020 |  |
| 2026-11-01 04:00:55 | Peradeniya (Mahaweli Ganga) | 2.65 | 🟢 Normal | -0.022 |  |
| 2026-11-01 04:02:33 | Ellagawa (Kalu Ganga) | 6.12 | 🟢 Normal | -0.030 |  |
| 2026-11-01 03:26:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.89 | 🟢 Normal | -0.036 |  |
| 2026-11-01 04:03:31 | Manampitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.049 |  |
| 2026-11-01 04:02:13 | Thanamalwila (Kirindi Oya) | 1.49 | 🟢 Normal | -0.068 |  |
| 2026-11-01 04:06:00 | Putupaula (Kalu Ganga) | 1.21 | 🟢 Normal | -0.089 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)