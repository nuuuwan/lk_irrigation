# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--17_17:11:58-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **263,531 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Magura — Alert; 🟡 Baddegama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-17 17:11:58 | Weraganthota (Mahaweli Ganga) | -2.84 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-09-17 17:09:19 | Glencourse (Kelani Ganga) | 9.53 | 🟢 Normal | -0.009 |  |
| 2026-09-17 17:07:48 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-09-17 17:07:01 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | -0.010 |  |
| 2026-09-17 17:06:52 | Urawa (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-09-17 17:06:50 | Holombuwa (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-17 17:06:32 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-17 17:06:28 | Thawalama (Gin Ganga) | 2.28 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-09-17 17:06:19 | Rathnapura (Kalu Ganga) | 1.34 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-17 17:06:17 | Putupaula (Kalu Ganga) | 0.91 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-17 17:05:32 | Dunamale (Aththanagalu Oya) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-09-17 17:04:53 | Thalgahagoda (Nilwala Ganga) | 0.76 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-17 17:04:34 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-17 17:03:46 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-09-17 17:03:36 | Kithulgala (Kelani Ganga) | 1.77 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-09-17 17:03:30 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | -0.011 |  |
| 2026-09-17 17:03:30 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-09-17 17:03:18 | Baddegama (Gin Ganga) | 3.59 | 🟡 Alert | -0.011 |  |
| 2026-09-17 17:03:17 | Magura (Kalu Ganga) | 4.78 | 🟡 Alert | 0.121 | 🔺 Rising |
| 2026-09-17 17:03:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.89 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-09-17 17:03:11 | Panadugama (Nilwala Ganga) | 4.69 | 🟢 Normal | -0.026 |  |
| 2026-09-17 17:02:30 | Nawalapitiya (Mahaweli Ganga) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-09-17 17:02:30 | Hanwella (Kelani Ganga) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-09-17 17:02:30 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-09-17 17:02:23 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-09-17 17:02:18 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-17 17:02:17 | Wellawaya (Kirindi Oya) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-09-17 17:02:08 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | -0.030 |  |
| 2026-09-17 17:02:07 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-17 17:01:55 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-17 17:01:49 | Thanthirimale (Malwathu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-17 17:01:43 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | -0.020 |  |
| 2026-09-17 17:01:32 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | -0.011 |  |
| 2026-09-17 17:01:26 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-09-17 17:01:16 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-09-17 17:01:01 | Horowpothana (Yan Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-09-17 17:00:57 | Pitabeddara (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-09-17 17:00:36 | Manampitiya (Mahaweli Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-17 16:59:01 | Manampitiya (Mahaweli Ganga) | -0.04 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-17 17:03:17 | Magura (Kalu Ganga) | 4.78 | 🟡 Alert | 0.121 | 🔺 Rising |
| 2026-09-17 17:03:18 | Baddegama (Gin Ganga) | 3.59 | 🟡 Alert | -0.011 |  |
| 2026-09-17 17:03:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.89 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-09-17 17:06:28 | Thawalama (Gin Ganga) | 2.28 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-09-17 17:07:48 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-09-17 17:03:36 | Kithulgala (Kelani Ganga) | 1.77 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-09-17 17:06:17 | Putupaula (Kalu Ganga) | 0.91 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-17 17:04:53 | Thalgahagoda (Nilwala Ganga) | 0.76 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-17 17:06:19 | Rathnapura (Kalu Ganga) | 1.34 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-17 17:11:58 | Weraganthota (Mahaweli Ganga) | -2.84 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-09-17 17:06:32 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-17 17:01:55 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-17 17:02:23 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-09-17 17:01:01 | Horowpothana (Yan Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-09-17 17:02:18 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-17 17:00:57 | Pitabeddara (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-09-17 17:03:46 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-09-17 17:04:34 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-17 17:05:32 | Dunamale (Aththanagalu Oya) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-09-17 17:02:07 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-17 17:03:30 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-09-17 17:06:50 | Holombuwa (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-17 17:00:36 | Manampitiya (Mahaweli Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-17 17:01:49 | Thanthirimale (Malwathu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-17 17:01:16 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-09-17 17:01:26 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-09-17 16:09:43 | Ellagawa (Kalu Ganga) | 4.87 | 🟢 Normal | -0.009 |  |
| 2026-09-17 17:09:19 | Glencourse (Kelani Ganga) | 9.53 | 🟢 Normal | -0.009 |  |
| 2026-09-17 17:07:01 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | -0.010 |  |
| 2026-09-17 17:02:30 | Nawalapitiya (Mahaweli Ganga) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-09-17 17:02:30 | Hanwella (Kelani Ganga) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-09-17 17:02:30 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-09-17 17:02:17 | Wellawaya (Kirindi Oya) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-09-17 17:06:52 | Urawa (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-09-17 17:03:30 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | -0.011 |  |
| 2026-09-17 17:01:32 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | -0.011 |  |
| 2026-09-17 17:01:43 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | -0.020 |  |
| 2026-09-17 17:03:11 | Panadugama (Nilwala Ganga) | 4.69 | 🟢 Normal | -0.026 |  |
| 2026-09-17 17:02:08 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | -0.030 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)