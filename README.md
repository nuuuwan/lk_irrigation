# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--06_12:19:07-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **226,466 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Kithulgala — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-06 12:19:07 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | -0.008 |  |
| 2026-08-06 12:09:20 | Thawalama (Gin Ganga) | 1.48 | 🟢 Normal | -0.010 |  |
| 2026-08-06 12:08:25 | Magura (Kalu Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-08-06 12:06:53 | Panadugama (Nilwala Ganga) | 2.44 | 🟢 Normal | -0.019 |  |
| 2026-08-06 12:06:33 | Glencourse (Kelani Ganga) | 11.31 | 🟢 Normal | 0.000 |  |
| 2026-08-06 12:06:32 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-08-06 12:06:09 | Badalgama (Maha Oya) | 2.28 | 🟢 Normal | -0.019 |  |
| 2026-08-06 12:06:02 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.057 |  |
| 2026-08-06 12:06:00 | Dunamale (Aththanagalu Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-08-06 12:05:59 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-06 12:05:56 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | -0.009 |  |
| 2026-08-06 12:05:28 | Rathnapura (Kalu Ganga) | 2.08 | 🟢 Normal | -0.090 |  |
| 2026-08-06 12:05:11 | Hanwella (Kelani Ganga) | 3.02 | 🟢 Normal | -0.039 |  |
| 2026-08-06 12:05:04 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-08-06 12:04:55 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-08-06 12:04:27 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-06 12:04:26 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-06 12:03:12 | Ellagawa (Kalu Ganga) | 7.15 | 🟢 Normal | -0.131 |  |
| 2026-08-06 12:03:06 | Horowpothana (Yan Oya) | 1.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-06 12:03:03 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | -0.011 |  |
| 2026-08-06 12:02:55 | Moraketiya (Walawe Ganga) | 0.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-06 12:02:53 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-06 12:02:47 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-08-06 12:02:46 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-06 12:02:45 | Thanthirimale (Malwathu Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-08-06 12:02:42 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-06 12:02:31 | Thanamalwila (Kirindi Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-06 12:02:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.36 | 🟢 Normal | -0.020 |  |
| 2026-08-06 12:02:29 | Deraniyagala (Kelani Ganga) | 1.39 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-08-06 12:02:25 | Kithulgala (Kelani Ganga) | 3.20 | 🟡 Alert | 0.608 | 🔺 Rising |
| 2026-08-06 12:02:09 | Putupaula (Kalu Ganga) | 1.56 | 🟢 Normal | -0.050 |  |
| 2026-08-06 12:02:08 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-06 12:02:06 | Peradeniya (Mahaweli Ganga) | 4.18 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-08-06 12:01:55 | Pitabeddara (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-08-06 12:01:52 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-08-06 12:01:44 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-06 12:01:15 | Giriulla (Maha Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-08-06 12:01:15 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-06 12:01:10 | Nawalapitiya (Mahaweli Ganga) | 2.30 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-08-06 12:00:34 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-08-06 12:00:30 | Weraganthota (Mahaweli Ganga) | -3.43 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-06 12:02:25 | Kithulgala (Kelani Ganga) | 3.20 | 🟡 Alert | 0.608 | 🔺 Rising |
| 2026-08-06 12:02:06 | Peradeniya (Mahaweli Ganga) | 4.18 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-08-06 12:02:29 | Deraniyagala (Kelani Ganga) | 1.39 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-08-06 12:01:10 | Nawalapitiya (Mahaweli Ganga) | 2.30 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-08-06 12:02:55 | Moraketiya (Walawe Ganga) | 0.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-06 12:03:06 | Horowpothana (Yan Oya) | 1.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-06 12:05:59 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-06 12:05:04 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-08-06 12:02:42 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-06 12:01:15 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-06 12:01:15 | Giriulla (Maha Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-08-06 12:02:53 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-06 12:08:25 | Magura (Kalu Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-08-06 12:01:55 | Pitabeddara (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-08-06 12:04:26 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-06 12:06:33 | Glencourse (Kelani Ganga) | 11.31 | 🟢 Normal | 0.000 |  |
| 2026-08-06 12:01:44 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-06 12:06:00 | Dunamale (Aththanagalu Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-08-06 12:02:46 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-06 12:04:27 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-06 12:04:55 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-08-06 12:02:08 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-06 12:01:52 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-08-06 12:06:32 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-08-06 12:02:31 | Thanamalwila (Kirindi Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-06 12:19:07 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | -0.008 |  |
| 2026-08-06 12:05:56 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | -0.009 |  |
| 2026-08-06 12:02:45 | Thanthirimale (Malwathu Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-08-06 12:09:20 | Thawalama (Gin Ganga) | 1.48 | 🟢 Normal | -0.010 |  |
| 2026-08-06 12:00:30 | Weraganthota (Mahaweli Ganga) | -3.43 | 🟢 Normal | -0.010 |  |
| 2026-08-06 12:03:03 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | -0.011 |  |
| 2026-08-06 12:06:09 | Badalgama (Maha Oya) | 2.28 | 🟢 Normal | -0.019 |  |
| 2026-08-06 12:06:53 | Panadugama (Nilwala Ganga) | 2.44 | 🟢 Normal | -0.019 |  |
| 2026-08-06 12:02:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.36 | 🟢 Normal | -0.020 |  |
| 2026-08-06 12:05:11 | Hanwella (Kelani Ganga) | 3.02 | 🟢 Normal | -0.039 |  |
| 2026-08-06 12:02:09 | Putupaula (Kalu Ganga) | 1.56 | 🟢 Normal | -0.050 |  |
| 2026-08-06 12:06:02 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.057 |  |
| 2026-08-06 12:05:28 | Rathnapura (Kalu Ganga) | 2.08 | 🟢 Normal | -0.090 |  |
| 2026-08-06 12:03:12 | Ellagawa (Kalu Ganga) | 7.15 | 🟢 Normal | -0.131 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)