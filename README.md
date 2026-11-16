# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--16_05:19:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **317,108 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thalgahagoda — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **24** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-16 05:19:57 | Panadugama (Nilwala Ganga) | 4.59 | 🟢 Normal | -0.008 |  |
| 2026-11-16 05:16:30 | Kuda Oya (Kirindi Oya) | 1.65 | 🟢 Normal | -0.024 |  |
| 2026-11-16 05:16:25 | Baddegama (Gin Ganga) | 2.30 | 🟢 Normal | -36.000 |  |
| 2026-11-16 05:16:23 | Baddegama (Gin Ganga) | 2.32 | 🟢 Normal | -36.000 |  |
| 2026-11-16 05:13:10 | Magura (Kalu Ganga) | 1.87 | 🟢 Normal | -0.021 |  |
| 2026-11-16 05:11:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.04 | 🟢 Normal | -0.257 |  |
| 2026-11-16 05:10:34 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-11-16 05:08:45 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-11-16 05:08:45 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-11-16 05:08:10 | Rathnapura (Kalu Ganga) | 1.79 | 🟢 Normal | -0.005 |  |
| 2026-11-16 05:07:53 | Urawa (Nilwala Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-11-16 05:07:50 | Padiyathalawa (Maduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-11-16 05:07:19 | Norwood (Kelani Ganga) | 1.02 | 🟢 Normal | -0.009 |  |
| 2026-11-16 05:06:05 | Pitabeddara (Nilwala Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-11-16 05:05:45 | Manampitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-11-16 05:05:42 | Wellawaya (Kirindi Oya) | 1.47 | 🟢 Normal | -0.060 |  |
| 2026-11-16 05:05:36 | Thawalama (Gin Ganga) | 1.98 | 🟢 Normal | -0.010 |  |
| 2026-11-16 05:04:17 | Giriulla (Maha Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-11-16 05:04:09 | Peradeniya (Mahaweli Ganga) | 2.83 | 🟢 Normal | -0.047 |  |
| 2026-11-16 05:04:07 | Dunamale (Aththanagalu Oya) | 1.80 | 🟢 Normal | -0.020 |  |
| 2026-11-16 05:04:03 | Badalgama (Maha Oya) | 2.72 | 🟢 Normal | -0.010 |  |
| 2026-11-16 05:03:57 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-11-16 05:03:51 | Holombuwa (Kelani Ganga) | 0.79 | 🟢 Normal | -0.012 |  |
| 2026-11-16 05:03:01 | Horowpothana (Yan Oya) | 2.05 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-16 05:00:09 | Thalgahagoda (Nilwala Ganga) | 1.58 | 🟡 Alert | -0.077 |  |
| 2026-11-16 05:05:45 | Manampitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-11-16 05:08:45 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-11-16 05:08:45 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-11-16 05:01:34 | Moragaswewa (Deduru Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-11-16 05:02:03 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-16 05:04:17 | Giriulla (Maha Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-11-16 05:06:05 | Pitabeddara (Nilwala Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-11-16 05:02:34 | Hanwella (Kelani Ganga) | 2.26 | 🟢 Normal | 0.000 |  |
| 2026-11-16 05:02:07 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-11-16 05:01:00 | Ellagawa (Kalu Ganga) | 5.41 | 🟢 Normal | 0.000 |  |
| 2026-11-16 05:07:50 | Padiyathalawa (Maduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-11-16 05:00:42 | Glencourse (Kelani Ganga) | 10.42 | 🟢 Normal | 0.000 |  |
| 2026-11-16 02:02:20 | Moraketiya (Walawe Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-11-16 05:10:34 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-11-16 05:01:06 | Thaldena (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-11-16 05:03:57 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-11-15 18:00:37 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-11-16 05:07:53 | Urawa (Nilwala Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-11-16 05:08:10 | Rathnapura (Kalu Ganga) | 1.79 | 🟢 Normal | -0.005 |  |
| 2026-11-16 05:19:57 | Panadugama (Nilwala Ganga) | 4.59 | 🟢 Normal | -0.008 |  |
| 2026-11-16 05:07:19 | Norwood (Kelani Ganga) | 1.02 | 🟢 Normal | -0.009 |  |
| 2026-11-16 05:04:03 | Badalgama (Maha Oya) | 2.72 | 🟢 Normal | -0.010 |  |
| 2026-11-16 05:02:47 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-11-16 05:05:36 | Thawalama (Gin Ganga) | 1.98 | 🟢 Normal | -0.010 |  |
| 2026-11-16 05:03:01 | Horowpothana (Yan Oya) | 2.05 | 🟢 Normal | -0.010 |  |
| 2026-11-16 05:02:16 | Nakkala (Kumbukkan Oya) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-11-15 18:01:22 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | -0.011 |  |
| 2026-11-16 05:03:51 | Holombuwa (Kelani Ganga) | 0.79 | 🟢 Normal | -0.012 |  |
| 2026-11-16 05:04:07 | Dunamale (Aththanagalu Oya) | 1.80 | 🟢 Normal | -0.020 |  |
| 2026-11-16 05:13:10 | Magura (Kalu Ganga) | 1.87 | 🟢 Normal | -0.021 |  |
| 2026-11-16 05:16:30 | Kuda Oya (Kirindi Oya) | 1.65 | 🟢 Normal | -0.024 |  |
| 2026-11-16 05:04:09 | Peradeniya (Mahaweli Ganga) | 2.83 | 🟢 Normal | -0.047 |  |
| 2026-11-16 05:05:42 | Wellawaya (Kirindi Oya) | 1.47 | 🟢 Normal | -0.060 |  |
| 2026-11-16 05:01:43 | Thanamalwila (Kirindi Oya) | 1.46 | 🟢 Normal | -0.113 |  |
| 2026-11-15 18:01:59 | Weraganthota (Mahaweli Ganga) | -1.94 | 🟢 Normal | -0.181 |  |
| 2026-11-16 05:11:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.04 | 🟢 Normal | -0.257 |  |
| 2026-11-16 05:02:31 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -1.104 |  |
| 2026-11-16 05:16:25 | Baddegama (Gin Ganga) | 2.30 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)