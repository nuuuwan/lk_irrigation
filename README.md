# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--16_04:12:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **317,067 measurements** from **39** stations.
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
| 2026-11-16 04:12:18 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-11-16 04:07:40 | Hanwella (Kelani Ganga) | 2.26 | 🟢 Normal | 0.000 |  |
| 2026-11-16 04:07:19 | Padiyathalawa (Maduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-11-16 04:06:56 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-11-16 04:06:27 | Pitabeddara (Nilwala Ganga) | 1.34 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-16 04:06:19 | Thaldena (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-11-16 04:06:11 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-11-16 04:05:42 | Wellawaya (Kirindi Oya) | 1.53 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-11-16 04:05:17 | Panadugama (Nilwala Ganga) | 4.60 | 🟢 Normal | -0.014 |  |
| 2026-11-16 04:04:10 | Thawalama (Gin Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-11-16 04:04:05 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-11-16 04:03:49 | Dunamale (Aththanagalu Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-11-16 04:03:47 | Urawa (Nilwala Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-11-16 04:03:24 | Glencourse (Kelani Ganga) | 10.42 | 🟢 Normal | 0.000 |  |
| 2026-11-16 04:03:20 | Giriulla (Maha Oya) | 1.43 | 🟢 Normal | -0.010 |  |
| 2026-11-16 04:02:50 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-16 04:02:35 | Manampitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-11-16 04:02:35 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-11-16 04:02:27 | Norwood (Kelani Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-11-16 04:02:19 | Badalgama (Maha Oya) | 2.73 | 🟢 Normal | -0.010 |  |
| 2026-11-16 04:02:04 | Horowpothana (Yan Oya) | 2.06 | 🟢 Normal | -0.010 |  |
| 2026-11-16 04:01:40 | Ellagawa (Kalu Ganga) | 5.41 | 🟢 Normal | -0.010 |  |
| 2026-11-16 04:01:27 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-11-16 04:01:19 | Nawalapitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-11-16 04:01:11 | Moragaswewa (Deduru Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-11-16 04:00:47 | Kuda Oya (Kirindi Oya) | 1.68 | 🟢 Normal | -0.007 |  |
| 2026-11-16 04:00:47 | Glencourse (Kelani Ganga) | 10.42 | 🟢 Normal | 0.000 |  |
| 2026-11-16 04:00:07 | Peradeniya (Mahaweli Ganga) | 2.88 | 🟢 Normal | -0.031 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-16 03:02:45 | Thalgahagoda (Nilwala Ganga) | 1.63 | 🟡 Alert | -0.012 |  |
| 2026-11-16 03:14:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.15 | 🟢 Normal | 1.047 | 🔺 Rising |
| 2026-11-16 04:06:56 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-11-16 04:05:42 | Wellawaya (Kirindi Oya) | 1.53 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-11-16 03:04:52 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-16 03:01:56 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-16 04:06:27 | Pitabeddara (Nilwala Ganga) | 1.34 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-16 04:01:27 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-11-16 04:01:11 | Moragaswewa (Deduru Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-11-16 04:01:19 | Nawalapitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-11-16 04:02:50 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-16 04:02:27 | Norwood (Kelani Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-11-16 04:07:40 | Hanwella (Kelani Ganga) | 2.26 | 🟢 Normal | 0.000 |  |
| 2026-11-16 04:04:05 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-11-16 04:07:19 | Padiyathalawa (Maduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-11-16 04:03:24 | Glencourse (Kelani Ganga) | 10.42 | 🟢 Normal | 0.000 |  |
| 2026-11-16 02:02:20 | Moraketiya (Walawe Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-11-16 04:02:35 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-11-16 04:03:49 | Dunamale (Aththanagalu Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-11-16 04:06:19 | Thaldena (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-11-16 04:06:11 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-11-16 04:12:18 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-11-16 04:02:35 | Manampitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-11-15 18:00:37 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-11-16 04:04:10 | Thawalama (Gin Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-11-16 04:03:47 | Urawa (Nilwala Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-11-16 03:05:52 | Thanamalwila (Kirindi Oya) | 1.48 | 🟢 Normal | -0.005 |  |
| 2026-11-16 04:00:47 | Kuda Oya (Kirindi Oya) | 1.68 | 🟢 Normal | -0.007 |  |
| 2026-11-16 03:04:19 | Magura (Kalu Ganga) | 1.89 | 🟢 Normal | -0.010 |  |
| 2026-11-16 04:02:04 | Horowpothana (Yan Oya) | 2.06 | 🟢 Normal | -0.010 |  |
| 2026-11-16 04:01:40 | Ellagawa (Kalu Ganga) | 5.41 | 🟢 Normal | -0.010 |  |
| 2026-11-16 04:03:20 | Giriulla (Maha Oya) | 1.43 | 🟢 Normal | -0.010 |  |
| 2026-11-16 04:02:19 | Badalgama (Maha Oya) | 2.73 | 🟢 Normal | -0.010 |  |
| 2026-11-15 18:01:22 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | -0.011 |  |
| 2026-11-16 04:05:17 | Panadugama (Nilwala Ganga) | 4.60 | 🟢 Normal | -0.014 |  |
| 2026-11-16 03:14:58 | Rathnapura (Kalu Ganga) | 1.80 | 🟢 Normal | -0.017 |  |
| 2026-11-16 04:00:07 | Peradeniya (Mahaweli Ganga) | 2.88 | 🟢 Normal | -0.031 |  |
| 2026-11-15 18:01:59 | Weraganthota (Mahaweli Ganga) | -1.94 | 🟢 Normal | -0.181 |  |
| 2026-11-16 03:05:30 | Baddegama (Gin Ganga) | 2.34 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)