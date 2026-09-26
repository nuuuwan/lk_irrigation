# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--26_23:31:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **271,885 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Baddegama — Minor Flood; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-26 23:31:13 | Dunamale (Aththanagalu Oya) | 2.55 | 🟢 Normal | 0.000 |  |
| 2026-09-26 23:27:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.84 | 🟠 Minor Flood | -0.007 |  |
| 2026-09-26 23:17:03 | Giriulla (Maha Oya) | 1.59 | 🟢 Normal | -0.017 |  |
| 2026-09-26 23:11:01 | Baddegama (Gin Ganga) | 4.79 | 🟠 Minor Flood | -0.009 |  |
| 2026-09-26 23:08:41 | Rathnapura (Kalu Ganga) | 4.53 | 🟢 Normal | -0.087 |  |
| 2026-09-26 23:07:35 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-26 23:06:44 | Holombuwa (Kelani Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-09-26 23:06:33 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-26 23:06:02 | Thawalama (Gin Ganga) | 2.96 | 🟢 Normal | -0.090 |  |
| 2026-09-26 23:05:53 | Panadugama (Nilwala Ganga) | 5.77 | 🟡 Alert | -0.035 |  |
| 2026-09-26 23:05:45 | Dunamale (Aththanagalu Oya) | 2.55 | 🟢 Normal | 0.000 |  |
| 2026-09-26 23:05:38 | Badalgama (Maha Oya) | 2.87 | 🟢 Normal | -0.009 |  |
| 2026-09-26 23:04:47 | Magura (Kalu Ganga) | 3.43 | 🟢 Normal | -0.042 |  |
| 2026-09-26 23:04:46 | Thalgahagoda (Nilwala Ganga) | 1.96 | 🟠 Minor Flood | 0.014 | 🔺 Rising |
| 2026-09-26 23:04:46 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-26 23:04:34 | Putupaula (Kalu Ganga) | 2.89 | 🟢 Normal | -0.011 |  |
| 2026-09-26 23:04:28 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-26 23:04:21 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | -0.031 |  |
| 2026-09-26 23:04:17 | Kithulgala (Kelani Ganga) | 2.51 | 🟢 Normal | -0.117 |  |
| 2026-09-26 23:04:08 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-26 23:03:46 | Urawa (Nilwala Ganga) | 1.00 | 🟢 Normal | -0.020 |  |
| 2026-09-26 23:03:23 | Deraniyagala (Kelani Ganga) | 1.61 | 🟢 Normal | -0.010 |  |
| 2026-09-26 23:03:14 | Norwood (Kelani Ganga) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-09-26 23:03:02 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-26 23:02:59 | Manampitiya (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-26 23:02:32 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-09-26 23:02:15 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-26 23:02:14 | Peradeniya (Mahaweli Ganga) | 3.57 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-09-26 23:02:09 | Hanwella (Kelani Ganga) | 5.08 | 🟢 Normal | -0.052 |  |
| 2026-09-26 23:02:08 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-26 23:01:50 | Glencourse (Kelani Ganga) | 12.62 | 🟢 Normal | -0.097 |  |
| 2026-09-26 23:01:46 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-26 23:01:36 | Nawalapitiya (Mahaweli Ganga) | 2.09 | 🟢 Normal | -0.021 |  |
| 2026-09-26 23:01:25 | Ellagawa (Kalu Ganga) | 8.84 | 🟢 Normal | -0.010 |  |
| 2026-09-26 23:01:23 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-26 23:01:17 | Pitabeddara (Nilwala Ganga) | 1.63 | 🟢 Normal | -0.024 |  |
| 2026-09-26 23:01:12 | Kuda Oya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-26 23:00:39 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-26 23:04:46 | Thalgahagoda (Nilwala Ganga) | 1.96 | 🟠 Minor Flood | 0.014 | 🔺 Rising |
| 2026-09-26 23:27:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.84 | 🟠 Minor Flood | -0.007 |  |
| 2026-09-26 23:11:01 | Baddegama (Gin Ganga) | 4.79 | 🟠 Minor Flood | -0.009 |  |
| 2026-09-26 23:05:53 | Panadugama (Nilwala Ganga) | 5.77 | 🟡 Alert | -0.035 |  |
| 2026-09-26 23:02:14 | Peradeniya (Mahaweli Ganga) | 3.57 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-09-26 23:04:08 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-26 23:01:23 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-26 23:02:59 | Manampitiya (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-26 23:02:15 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-26 23:00:39 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-26 23:04:46 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-26 23:01:46 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-26 23:04:28 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-26 18:05:10 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-26 23:02:08 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-26 23:02:32 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-09-26 23:06:33 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-26 23:31:13 | Dunamale (Aththanagalu Oya) | 2.55 | 🟢 Normal | 0.000 |  |
| 2026-09-26 23:07:35 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-26 23:06:44 | Holombuwa (Kelani Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-09-26 23:01:12 | Kuda Oya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-26 23:05:38 | Badalgama (Maha Oya) | 2.87 | 🟢 Normal | -0.009 |  |
| 2026-09-26 23:03:23 | Deraniyagala (Kelani Ganga) | 1.61 | 🟢 Normal | -0.010 |  |
| 2026-09-26 23:03:14 | Norwood (Kelani Ganga) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-09-26 23:01:25 | Ellagawa (Kalu Ganga) | 8.84 | 🟢 Normal | -0.010 |  |
| 2026-09-26 18:02:21 | Thanthirimale (Malwathu Oya) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-09-26 23:04:34 | Putupaula (Kalu Ganga) | 2.89 | 🟢 Normal | -0.011 |  |
| 2026-09-26 23:17:03 | Giriulla (Maha Oya) | 1.59 | 🟢 Normal | -0.017 |  |
| 2026-09-26 23:03:46 | Urawa (Nilwala Ganga) | 1.00 | 🟢 Normal | -0.020 |  |
| 2026-09-26 23:01:36 | Nawalapitiya (Mahaweli Ganga) | 2.09 | 🟢 Normal | -0.021 |  |
| 2026-09-26 23:01:17 | Pitabeddara (Nilwala Ganga) | 1.63 | 🟢 Normal | -0.024 |  |
| 2026-09-26 23:04:21 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | -0.031 |  |
| 2026-09-26 23:04:47 | Magura (Kalu Ganga) | 3.43 | 🟢 Normal | -0.042 |  |
| 2026-09-26 23:02:09 | Hanwella (Kelani Ganga) | 5.08 | 🟢 Normal | -0.052 |  |
| 2026-09-26 23:08:41 | Rathnapura (Kalu Ganga) | 4.53 | 🟢 Normal | -0.087 |  |
| 2026-09-26 18:00:27 | Weraganthota (Mahaweli Ganga) | -3.23 | 🟢 Normal | -0.089 |  |
| 2026-09-26 23:06:02 | Thawalama (Gin Ganga) | 2.96 | 🟢 Normal | -0.090 |  |
| 2026-09-26 23:01:50 | Glencourse (Kelani Ganga) | 12.62 | 🟢 Normal | -0.097 |  |
| 2026-09-26 23:04:17 | Kithulgala (Kelani Ganga) | 2.51 | 🟢 Normal | -0.117 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)