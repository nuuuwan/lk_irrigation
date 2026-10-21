# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--21_05:36:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **293,702 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thalgahagoda — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-21 05:36:13 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-10-21 05:26:00 | Urawa (Nilwala Ganga) | 0.77 | 🟢 Normal | -0.030 |  |
| 2026-10-21 05:24:42 | Magura (Kalu Ganga) | 1.65 | 🟢 Normal | -0.007 |  |
| 2026-10-21 05:17:10 | Manampitiya (Mahaweli Ganga) | 0.49 | 🟢 Normal | -0.008 |  |
| 2026-10-21 05:12:39 | Deraniyagala (Kelani Ganga) | 0.97 | 🟢 Normal | -0.013 |  |
| 2026-10-21 05:11:32 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-10-21 05:10:38 | Baddegama (Gin Ganga) | 1.63 | 🟢 Normal | -0.099 |  |
| 2026-10-21 05:09:08 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-21 05:07:18 | Moraketiya (Walawe Ganga) | 1.15 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-21 05:07:15 | Horowpothana (Yan Oya) | 2.17 | 🟢 Normal | -0.028 |  |
| 2026-10-21 05:06:39 | Dunamale (Aththanagalu Oya) | 1.92 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-10-21 05:06:35 | Putupaula (Kalu Ganga) | 0.76 | 🟢 Normal | -0.048 |  |
| 2026-10-21 05:06:23 | Wellawaya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-21 05:06:03 | Panadugama (Nilwala Ganga) | 4.17 | 🟢 Normal | -0.131 |  |
| 2026-10-21 05:05:10 | Glencourse (Kelani Ganga) | 10.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-21 05:04:50 | Giriulla (Maha Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-10-21 05:04:20 | Hanwella (Kelani Ganga) | 2.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-21 05:04:09 | Padiyathalawa (Maduru Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-21 05:03:51 | Peradeniya (Mahaweli Ganga) | 2.94 | 🟢 Normal | -0.057 |  |
| 2026-10-21 05:03:16 | Badalgama (Maha Oya) | 2.55 | 🟢 Normal | -0.010 |  |
| 2026-10-21 05:03:15 | Norwood (Kelani Ganga) | 1.18 | 🟢 Normal | -0.030 |  |
| 2026-10-21 05:02:51 | Rathnapura (Kalu Ganga) | 1.97 | 🟢 Normal | -0.021 |  |
| 2026-10-21 05:02:15 | Holombuwa (Kelani Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-10-21 05:02:14 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-10-21 05:02:07 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.031 |  |
| 2026-10-21 05:01:59 | Moragaswewa (Deduru Oya) | 1.10 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-21 05:01:57 | Nawalapitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | -0.021 |  |
| 2026-10-21 05:01:55 | Thaldena (Mahaweli Ganga) | 0.64 | 🟢 Normal | -0.030 |  |
| 2026-10-21 05:01:45 | Pitabeddara (Nilwala Ganga) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-10-21 05:01:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.10 | 🟢 Normal | 0.084 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-21 05:00:30 | Thalgahagoda (Nilwala Ganga) | 1.47 | 🟡 Alert | -0.005 |  |
| 2026-10-20 18:02:39 | Galgamuwa (Mee Oya) | 0.61 | 🟢 Normal | 9.000 | 🔺 Rising |
| 2026-10-21 05:01:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.10 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-10-21 05:01:59 | Moragaswewa (Deduru Oya) | 1.10 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-21 05:36:13 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-10-21 05:06:39 | Dunamale (Aththanagalu Oya) | 1.92 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-10-21 05:09:08 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-20 18:04:50 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-21 05:04:20 | Hanwella (Kelani Ganga) | 2.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-21 05:06:23 | Wellawaya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-21 05:05:10 | Glencourse (Kelani Ganga) | 10.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-21 05:07:18 | Moraketiya (Walawe Ganga) | 1.15 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-21 05:11:32 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-10-21 05:04:50 | Giriulla (Maha Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-10-21 05:04:09 | Padiyathalawa (Maduru Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-20 18:01:22 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-10-21 05:00:48 | Thawalama (Gin Ganga) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-10-21 05:24:42 | Magura (Kalu Ganga) | 1.65 | 🟢 Normal | -0.007 |  |
| 2026-10-21 05:17:10 | Manampitiya (Mahaweli Ganga) | 0.49 | 🟢 Normal | -0.008 |  |
| 2026-10-21 04:13:47 | Thanamalwila (Kirindi Oya) | 1.18 | 🟢 Normal | -0.009 |  |
| 2026-10-21 05:01:45 | Pitabeddara (Nilwala Ganga) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-10-21 05:02:14 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-10-21 05:02:15 | Holombuwa (Kelani Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-10-21 05:03:16 | Badalgama (Maha Oya) | 2.55 | 🟢 Normal | -0.010 |  |
| 2026-10-21 05:12:39 | Deraniyagala (Kelani Ganga) | 0.97 | 🟢 Normal | -0.013 |  |
| 2026-10-21 05:01:41 | Ellagawa (Kalu Ganga) | 5.62 | 🟢 Normal | -0.020 |  |
| 2026-10-21 05:02:51 | Rathnapura (Kalu Ganga) | 1.97 | 🟢 Normal | -0.021 |  |
| 2026-10-21 05:01:57 | Nawalapitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | -0.021 |  |
| 2026-10-21 05:07:15 | Horowpothana (Yan Oya) | 2.17 | 🟢 Normal | -0.028 |  |
| 2026-10-21 05:03:15 | Norwood (Kelani Ganga) | 1.18 | 🟢 Normal | -0.030 |  |
| 2026-10-21 05:01:55 | Thaldena (Mahaweli Ganga) | 0.64 | 🟢 Normal | -0.030 |  |
| 2026-10-21 05:26:00 | Urawa (Nilwala Ganga) | 0.77 | 🟢 Normal | -0.030 |  |
| 2026-10-21 05:02:07 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.031 |  |
| 2026-10-21 05:06:35 | Putupaula (Kalu Ganga) | 0.76 | 🟢 Normal | -0.048 |  |
| 2026-10-21 05:00:08 | Siyambalanduwa (Heda Oya) | 0.93 | 🟢 Normal | -0.050 |  |
| 2026-10-21 05:03:51 | Peradeniya (Mahaweli Ganga) | 2.94 | 🟢 Normal | -0.057 |  |
| 2026-10-21 05:10:38 | Baddegama (Gin Ganga) | 1.63 | 🟢 Normal | -0.099 |  |
| 2026-10-21 05:06:03 | Panadugama (Nilwala Ganga) | 4.17 | 🟢 Normal | -0.131 |  |
| 2026-10-21 05:01:06 | Nakkala (Kumbukkan Oya) | 1.15 | 🟢 Normal | -0.149 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)