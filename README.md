# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--16_19:07:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **289,722 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Panadugama — Minor Flood; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **28** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-16 19:07:18 | Baddegama (Gin Ganga) | 3.32 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-10-16 19:07:08 | Rathnapura (Kalu Ganga) | 3.40 | 🟢 Normal | 0.201 | 🔺 Rising |
| 2026-10-16 19:06:51 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | -0.009 |  |
| 2026-10-16 19:05:52 | Glencourse (Kelani Ganga) | 10.85 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-10-16 19:05:47 | Magura (Kalu Ganga) | 3.49 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-10-16 19:05:23 | Kithulgala (Kelani Ganga) | 2.45 | 🟢 Normal | 0.469 | 🔺 Rising |
| 2026-10-16 19:05:09 | Padiyathalawa (Maduru Oya) | 0.70 | 🟢 Normal | 0.641 | 🔺 Rising |
| 2026-10-16 19:04:59 | Badalgama (Maha Oya) | 3.08 | 🟢 Normal | 0.000 |  |
| 2026-10-16 19:04:39 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-16 19:04:26 | Peradeniya (Mahaweli Ganga) | 3.29 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-10-16 19:03:58 | Nawalapitiya (Mahaweli Ganga) | 1.87 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-16 19:03:41 | Moragaswewa (Deduru Oya) | 2.20 | 🟢 Normal | -0.040 |  |
| 2026-10-16 19:03:36 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-10-16 19:03:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.93 | 🟡 Alert | 0.000 |  |
| 2026-10-16 19:03:31 | Dunamale (Aththanagalu Oya) | 3.28 | 🟢 Normal | 0.000 |  |
| 2026-10-16 19:03:20 | Giriulla (Maha Oya) | 1.84 | 🟢 Normal | -0.010 |  |
| 2026-10-16 19:03:18 | Thawalama (Gin Ganga) | 3.50 | 🟢 Normal | 0.139 | 🔺 Rising |
| 2026-10-16 19:03:12 | Holombuwa (Kelani Ganga) | 1.55 | 🟢 Normal | 0.567 | 🔺 Rising |
| 2026-10-16 19:03:03 | Hanwella (Kelani Ganga) | 3.24 | 🟢 Normal | -0.052 |  |
| 2026-10-16 19:02:58 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-10-16 19:02:57 | Deraniyagala (Kelani Ganga) | 1.13 | 🟢 Normal | 0.220 | 🔺 Rising |
| 2026-10-16 19:02:51 | Siyambalanduwa (Heda Oya) | 1.34 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-10-16 19:02:44 | Norwood (Kelani Ganga) | 1.37 | 🟢 Normal | -0.020 |  |
| 2026-10-16 19:02:27 | Moraketiya (Walawe Ganga) | 1.38 | 🟢 Normal | -0.021 |  |
| 2026-10-16 19:02:10 | Thanamalwila (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-10-16 19:01:20 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.092 |  |
| 2026-10-16 19:01:05 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-16 19:00:19 | Wellawaya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.170 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-16 18:08:47 | Thalgahagoda (Nilwala Ganga) | 1.98 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-16 18:05:04 | Panadugama (Nilwala Ganga) | 6.44 | 🟠 Minor Flood | -0.020 |  |
| 2026-10-16 19:03:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.93 | 🟡 Alert | 0.000 |  |
| 2026-10-16 19:05:09 | Padiyathalawa (Maduru Oya) | 0.70 | 🟢 Normal | 0.641 | 🔺 Rising |
| 2026-10-16 19:03:12 | Holombuwa (Kelani Ganga) | 1.55 | 🟢 Normal | 0.567 | 🔺 Rising |
| 2026-10-16 19:05:23 | Kithulgala (Kelani Ganga) | 2.45 | 🟢 Normal | 0.469 | 🔺 Rising |
| 2026-10-16 19:02:57 | Deraniyagala (Kelani Ganga) | 1.13 | 🟢 Normal | 0.220 | 🔺 Rising |
| 2026-10-16 19:07:08 | Rathnapura (Kalu Ganga) | 3.40 | 🟢 Normal | 0.201 | 🔺 Rising |
| 2026-10-16 19:00:19 | Wellawaya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.170 | 🔺 Rising |
| 2026-10-16 19:03:18 | Thawalama (Gin Ganga) | 3.50 | 🟢 Normal | 0.139 | 🔺 Rising |
| 2026-10-16 19:05:47 | Magura (Kalu Ganga) | 3.49 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-10-16 18:19:25 | Urawa (Nilwala Ganga) | 1.56 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-10-16 19:05:52 | Glencourse (Kelani Ganga) | 10.85 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-10-16 19:04:26 | Peradeniya (Mahaweli Ganga) | 3.29 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-10-16 19:03:36 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-10-16 18:07:55 | Pitabeddara (Nilwala Ganga) | 2.55 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-10-16 18:00:14 | Weraganthota (Mahaweli Ganga) | -3.21 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-10-16 19:02:51 | Siyambalanduwa (Heda Oya) | 1.34 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-10-16 19:03:58 | Nawalapitiya (Mahaweli Ganga) | 1.87 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-16 18:07:03 | Manampitiya (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-10-16 19:07:18 | Baddegama (Gin Ganga) | 3.32 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-10-16 18:00:08 | Horowpothana (Yan Oya) | 2.42 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-10-16 19:01:05 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-16 18:01:05 | Thanthirimale (Malwathu Oya) | 1.98 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-16 19:02:58 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-10-16 18:02:58 | Ellagawa (Kalu Ganga) | 7.34 | 🟢 Normal | 0.000 |  |
| 2026-10-16 19:03:31 | Dunamale (Aththanagalu Oya) | 3.28 | 🟢 Normal | 0.000 |  |
| 2026-10-16 19:04:39 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-16 18:01:14 | Putupaula (Kalu Ganga) | 2.29 | 🟢 Normal | 0.000 |  |
| 2026-10-16 19:04:59 | Badalgama (Maha Oya) | 3.08 | 🟢 Normal | 0.000 |  |
| 2026-10-16 19:02:10 | Thanamalwila (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-10-16 19:06:51 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | -0.009 |  |
| 2026-10-16 19:03:20 | Giriulla (Maha Oya) | 1.84 | 🟢 Normal | -0.010 |  |
| 2026-10-16 19:02:44 | Norwood (Kelani Ganga) | 1.37 | 🟢 Normal | -0.020 |  |
| 2026-10-16 19:02:27 | Moraketiya (Walawe Ganga) | 1.38 | 🟢 Normal | -0.021 |  |
| 2026-10-16 18:02:38 | Galgamuwa (Mee Oya) | 2.02 | 🟢 Normal | -0.023 |  |
| 2026-10-16 19:03:41 | Moragaswewa (Deduru Oya) | 2.20 | 🟢 Normal | -0.040 |  |
| 2026-10-16 19:03:03 | Hanwella (Kelani Ganga) | 3.24 | 🟢 Normal | -0.052 |  |
| 2026-10-16 19:01:20 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.092 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)