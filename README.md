# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--21_11:16:04-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **321,774 measurements** from **39** stations.
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
| 2026-11-21 11:16:04 | Thalgahagoda (Nilwala Ganga) | 1.09 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-11-21 11:11:33 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-11-21 11:10:59 | Urawa (Nilwala Ganga) | 1.21 | 🟢 Normal | -0.061 |  |
| 2026-11-21 11:10:59 | Moragaswewa (Deduru Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-11-21 11:09:52 | Holombuwa (Kelani Ganga) | 1.42 | 🟢 Normal | -0.039 |  |
| 2026-11-21 11:08:25 | Dunamale (Aththanagalu Oya) | 1.78 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-11-21 11:07:19 | Peradeniya (Mahaweli Ganga) | 2.92 | 🟢 Normal | -0.180 |  |
| 2026-11-21 11:05:41 | Rathnapura (Kalu Ganga) | 2.92 | 🟢 Normal | -0.103 |  |
| 2026-11-21 11:05:33 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.049 |  |
| 2026-11-21 11:04:46 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | -0.011 |  |
| 2026-11-21 11:04:45 | Baddegama (Gin Ganga) | 1.91 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-21 11:04:42 | Glencourse (Kelani Ganga) | 10.02 | 🟢 Normal | 0.000 |  |
| 2026-11-21 11:04:32 | Thanthirimale (Malwathu Oya) | 1.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-21 11:04:24 | Thawalama (Gin Ganga) | 2.39 | 🟢 Normal | -0.078 |  |
| 2026-11-21 11:04:19 | Giriulla (Maha Oya) | 4.30 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-21 11:04:12 | Badalgama (Maha Oya) | 2.99 | 🟢 Normal | 0.492 | 🔺 Rising |
| 2026-11-21 11:03:57 | Putupaula (Kalu Ganga) | 0.91 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-11-21 11:03:51 | Pitabeddara (Nilwala Ganga) | 2.19 | 🟢 Normal | -0.094 |  |
| 2026-11-21 11:03:26 | Manampitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-11-21 11:03:14 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-11-21 11:03:10 | Magura (Kalu Ganga) | 2.55 | 🟢 Normal | 0.243 | 🔺 Rising |
| 2026-11-21 11:03:05 | Ellagawa (Kalu Ganga) | 5.92 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-11-21 11:02:43 | Hanwella (Kelani Ganga) | 1.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-21 11:02:37 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-21 11:02:30 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-11-21 11:02:28 | Moraketiya (Walawe Ganga) | 2.94 | 🟢 Normal | 0.000 |  |
| 2026-11-21 11:02:17 | Thanamalwila (Kirindi Oya) | 1.91 | 🟢 Normal | -0.050 |  |
| 2026-11-21 11:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.79 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-21 11:02:13 | Nakkala (Kumbukkan Oya) | 0.89 | 🟢 Normal | -0.021 |  |
| 2026-11-21 11:01:52 | Wellawaya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-21 11:01:43 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | -0.021 |  |
| 2026-11-21 11:01:43 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-21 11:01:26 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-11-21 11:01:20 | Kuda Oya (Kirindi Oya) | 2.10 | 🟢 Normal | 1.288 | 🔺 Rising |
| 2026-11-21 11:01:19 | Panadugama (Nilwala Ganga) | 5.22 | 🟡 Alert | -0.065 |  |
| 2026-11-21 11:01:05 | Nawalapitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | -0.030 |  |
| 2026-11-21 11:00:47 | Weraganthota (Mahaweli Ganga) | -2.02 | 🟢 Normal | -0.030 |  |
| 2026-11-21 11:00:35 | Horowpothana (Yan Oya) | 1.94 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-21 11:01:19 | Panadugama (Nilwala Ganga) | 5.22 | 🟡 Alert | -0.065 |  |
| 2026-11-21 11:01:20 | Kuda Oya (Kirindi Oya) | 2.10 | 🟢 Normal | 1.288 | 🔺 Rising |
| 2026-11-21 11:04:12 | Badalgama (Maha Oya) | 2.99 | 🟢 Normal | 0.492 | 🔺 Rising |
| 2026-11-21 11:03:10 | Magura (Kalu Ganga) | 2.55 | 🟢 Normal | 0.243 | 🔺 Rising |
| 2026-11-21 11:03:05 | Ellagawa (Kalu Ganga) | 5.92 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-11-21 11:03:57 | Putupaula (Kalu Ganga) | 0.91 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-11-21 11:01:26 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-11-21 11:08:25 | Dunamale (Aththanagalu Oya) | 1.78 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-11-21 11:16:04 | Thalgahagoda (Nilwala Ganga) | 1.09 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-11-21 11:04:19 | Giriulla (Maha Oya) | 4.30 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-21 11:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.79 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-21 11:02:37 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-21 11:04:45 | Baddegama (Gin Ganga) | 1.91 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-21 11:00:35 | Horowpothana (Yan Oya) | 1.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-21 11:02:43 | Hanwella (Kelani Ganga) | 1.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-21 11:04:32 | Thanthirimale (Malwathu Oya) | 1.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-21 11:01:52 | Wellawaya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-21 11:10:59 | Moragaswewa (Deduru Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-11-21 11:01:43 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-21 11:11:33 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-11-21 11:03:14 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-11-19 14:01:52⌛ | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-11-21 11:04:42 | Glencourse (Kelani Ganga) | 10.02 | 🟢 Normal | 0.000 |  |
| 2026-11-21 11:02:28 | Moraketiya (Walawe Ganga) | 2.94 | 🟢 Normal | 0.000 |  |
| 2026-11-21 11:02:30 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-11-21 11:03:26 | Manampitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-11-21 11:04:46 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | -0.011 |  |
| 2026-11-21 11:02:13 | Nakkala (Kumbukkan Oya) | 0.89 | 🟢 Normal | -0.021 |  |
| 2026-11-21 11:01:43 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | -0.021 |  |
| 2026-11-21 11:00:47 | Weraganthota (Mahaweli Ganga) | -2.02 | 🟢 Normal | -0.030 |  |
| 2026-11-21 11:01:05 | Nawalapitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | -0.030 |  |
| 2026-11-21 11:09:52 | Holombuwa (Kelani Ganga) | 1.42 | 🟢 Normal | -0.039 |  |
| 2026-11-21 11:05:33 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.049 |  |
| 2026-11-21 11:02:17 | Thanamalwila (Kirindi Oya) | 1.91 | 🟢 Normal | -0.050 |  |
| 2026-11-21 11:10:59 | Urawa (Nilwala Ganga) | 1.21 | 🟢 Normal | -0.061 |  |
| 2026-11-21 11:04:24 | Thawalama (Gin Ganga) | 2.39 | 🟢 Normal | -0.078 |  |
| 2026-11-21 11:03:51 | Pitabeddara (Nilwala Ganga) | 2.19 | 🟢 Normal | -0.094 |  |
| 2026-11-21 11:05:41 | Rathnapura (Kalu Ganga) | 2.92 | 🟢 Normal | -0.103 |  |
| 2026-11-21 11:07:19 | Peradeniya (Mahaweli Ganga) | 2.92 | 🟢 Normal | -0.180 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)