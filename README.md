# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--21_17:02:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **321,973 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Moraketiya — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **12** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-21 17:02:27 | Glencourse (Kelani Ganga) | 9.87 | 🟢 Normal | -0.135 |  |
| 2026-11-21 17:01:43 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-21 17:01:41 | Thanamalwila (Kirindi Oya) | 1.88 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-21 17:01:36 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-21 17:01:16 | Moragaswewa (Deduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-11-21 17:00:59 | Magura (Kalu Ganga) | 2.03 | 🟢 Normal | -0.094 |  |
| 2026-11-21 17:00:44 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-11-21 17:00:41 | Manampitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-11-21 16:27:09 | Pitabeddara (Nilwala Ganga) | 1.62 | 🟢 Normal | -0.015 |  |
| 2026-11-21 16:17:31 | Baddegama (Gin Ganga) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-11-21 16:14:45 | Horowpothana (Yan Oya) | 1.96 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-11-21 16:13:52 | Rathnapura (Kalu Ganga) | 2.35 | 🟢 Normal | -0.090 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-21 16:01:53 | Moraketiya (Walawe Ganga) | 3.00 | 🟡 Alert | 0.000 |  |
| 2026-11-21 16:01:51 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | 0.330 | 🔺 Rising |
| 2026-11-21 16:05:57 | Thawalama (Gin Ganga) | 1.87 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-11-21 17:01:41 | Thanamalwila (Kirindi Oya) | 1.88 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-21 16:02:47 | Hanwella (Kelani Ganga) | 1.82 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-21 16:02:11 | Thanthirimale (Malwathu Oya) | 1.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-21 16:14:45 | Horowpothana (Yan Oya) | 1.96 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-11-21 17:01:16 | Moragaswewa (Deduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-11-21 17:01:43 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-21 16:04:45 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-11-21 16:17:31 | Baddegama (Gin Ganga) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-11-19 14:01:52⌛ | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-11-21 17:01:36 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-21 17:00:44 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-11-21 16:03:42 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-11-21 17:00:41 | Manampitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-11-21 16:03:36 | Peradeniya (Mahaweli Ganga) | 2.76 | 🟢 Normal | 0.000 |  |
| 2026-11-21 16:09:22 | Urawa (Nilwala Ganga) | 1.03 | 🟢 Normal | -0.009 |  |
| 2026-11-21 16:10:41 | Thalgahagoda (Nilwala Ganga) | 1.14 | 🟢 Normal | -0.009 |  |
| 2026-11-21 16:06:42 | Badalgama (Maha Oya) | 4.55 | 🟢 Normal | -0.009 |  |
| 2026-11-21 16:03:06 | Nawalapitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-11-21 16:03:09 | Ellagawa (Kalu Ganga) | 6.10 | 🟢 Normal | -0.010 |  |
| 2026-11-21 16:00:34 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-11-21 16:08:25 | Norwood (Kelani Ganga) | 0.86 | 🟢 Normal | -0.011 |  |
| 2026-11-21 16:27:09 | Pitabeddara (Nilwala Ganga) | 1.62 | 🟢 Normal | -0.015 |  |
| 2026-11-21 16:01:41 | Wellawaya (Kirindi Oya) | 1.23 | 🟢 Normal | -0.020 |  |
| 2026-11-21 16:04:00 | Holombuwa (Kelani Ganga) | 0.88 | 🟢 Normal | -0.032 |  |
| 2026-11-21 16:03:51 | Deraniyagala (Kelani Ganga) | 0.56 | 🟢 Normal | -0.039 |  |
| 2026-11-21 16:00:45 | Weraganthota (Mahaweli Ganga) | -2.42 | 🟢 Normal | -0.041 |  |
| 2026-11-21 16:04:03 | Putupaula (Kalu Ganga) | 0.96 | 🟢 Normal | -0.041 |  |
| 2026-11-21 16:06:26 | Dunamale (Aththanagalu Oya) | 1.76 | 🟢 Normal | -0.048 |  |
| 2026-11-21 16:10:58 | Panadugama (Nilwala Ganga) | 4.88 | 🟢 Normal | -0.061 |  |
| 2026-11-21 16:04:52 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.061 |  |
| 2026-11-21 16:00:45 | Kuda Oya (Kirindi Oya) | 2.32 | 🟢 Normal | -0.061 |  |
| 2026-11-21 16:03:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.68 | 🟢 Normal | -0.061 |  |
| 2026-11-21 16:13:52 | Rathnapura (Kalu Ganga) | 2.35 | 🟢 Normal | -0.090 |  |
| 2026-11-21 17:00:59 | Magura (Kalu Ganga) | 2.03 | 🟢 Normal | -0.094 |  |
| 2026-11-21 17:02:27 | Glencourse (Kelani Ganga) | 9.87 | 🟢 Normal | -0.135 |  |
| 2026-11-21 16:02:42 | Giriulla (Maha Oya) | 3.36 | 🟢 Normal | -0.244 |  |

## River Water Level Charts by Station

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)