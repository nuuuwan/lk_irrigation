# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--12_14:19:11-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **313,864 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Moraketiya — Alert; 🟡 Dunamale — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-12 14:19:11 | Horowpothana (Yan Oya) | 2.49 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-11-12 14:16:58 | Thalgahagoda (Nilwala Ganga) | 1.80 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-12 14:16:54 | Dunamale (Aththanagalu Oya) | 4.18 | 🟡 Alert | -0.032 |  |
| 2026-11-12 14:12:57 | Baddegama (Gin Ganga) | 4.10 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-11-12 14:11:25 | Thaldena (Mahaweli Ganga) | 1.36 | 🟢 Normal | 0.242 | 🔺 Rising |
| 2026-11-12 14:10:23 | Ellagawa (Kalu Ganga) | 8.32 | 🟢 Normal | -0.009 |  |
| 2026-11-12 14:08:33 | Magura (Kalu Ganga) | 5.16 | 🟡 Alert | -0.054 |  |
| 2026-11-12 14:07:56 | Badalgama (Maha Oya) | 4.18 | 🟢 Normal | -0.059 |  |
| 2026-11-12 14:07:35 | Glencourse (Kelani Ganga) | 12.58 | 🟢 Normal | -0.162 |  |
| 2026-11-12 14:07:33 | Urawa (Nilwala Ganga) | 1.58 | 🟢 Normal | -0.046 |  |
| 2026-11-12 14:07:33 | Galgamuwa (Mee Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-11-12 14:06:59 | Rathnapura (Kalu Ganga) | 4.97 | 🟢 Normal | -0.081 |  |
| 2026-11-12 14:06:58 | Pitabeddara (Nilwala Ganga) | 2.37 | 🟢 Normal | -0.028 |  |
| 2026-11-12 14:06:36 | Giriulla (Maha Oya) | 2.69 | 🟢 Normal | -0.083 |  |
| 2026-11-12 14:06:35 | Katharagama (Menik Ganga) | 0.54 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-12 14:06:21 | Kuda Oya (Kirindi Oya) | 2.59 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-11-12 14:05:39 | Holombuwa (Kelani Ganga) | 1.63 | 🟢 Normal | -0.010 |  |
| 2026-11-12 14:05:38 | Manampitiya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.179 | 🔺 Rising |
| 2026-11-12 14:05:12 | Peradeniya (Mahaweli Ganga) | 4.65 | 🟢 Normal | -0.079 |  |
| 2026-11-12 14:04:46 | Padiyathalawa (Maduru Oya) | 0.84 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-12 14:04:37 | Thawalama (Gin Ganga) | 2.96 | 🟢 Normal | -0.035 |  |
| 2026-11-12 14:04:01 | Thanamalwila (Kirindi Oya) | 2.32 | 🟢 Normal | -0.042 |  |
| 2026-11-12 14:03:37 | Nagalagam Street (Kelani Ganga) | 0.94 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-11-12 14:03:27 | Putupaula (Kalu Ganga) | 2.53 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-11-12 14:03:22 | Norwood (Kelani Ganga) | 1.30 | 🟢 Normal | -0.020 |  |
| 2026-11-12 14:02:52 | Hanwella (Kelani Ganga) | 5.26 | 🟢 Normal | -0.110 |  |
| 2026-11-12 14:02:51 | Siyambalanduwa (Heda Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-11-12 14:02:46 | Panadugama (Nilwala Ganga) | 5.87 | 🟡 Alert | -0.034 |  |
| 2026-11-12 14:02:42 | Nawalapitiya (Mahaweli Ganga) | 1.58 | 🟢 Normal | -0.010 |  |
| 2026-11-12 14:02:39 | Moraketiya (Walawe Ganga) | 3.81 | 🟡 Alert | -0.030 |  |
| 2026-11-12 14:02:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.33 | 🟡 Alert | 0.000 |  |
| 2026-11-12 14:02:33 | Yaka Wewa (Ma Oya) | 0.77 | 🟢 Normal | -0.011 |  |
| 2026-11-12 14:02:16 | Kithulgala (Kelani Ganga) | 2.18 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-12 14:02:11 | Deraniyagala (Kelani Ganga) | 1.26 | 🟢 Normal | -0.020 |  |
| 2026-11-12 14:01:47 | Moragaswewa (Deduru Oya) | 3.09 | 🟢 Normal | -0.069 |  |
| 2026-11-12 14:01:46 | Wellawaya (Kirindi Oya) | 1.78 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-12 14:00:45 | Thanthirimale (Malwathu Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-11-12 14:00:38 | Weraganthota (Mahaweli Ganga) | -2.12 | 🟢 Normal | -0.109 |  |
| 2026-11-12 14:00:07 | Nakkala (Kumbukkan Oya) | 1.49 | 🟢 Normal | -0.041 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-12 14:12:57 | Baddegama (Gin Ganga) | 4.10 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-11-12 14:16:58 | Thalgahagoda (Nilwala Ganga) | 1.80 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-12 14:02:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.33 | 🟡 Alert | 0.000 |  |
| 2026-11-12 14:02:39 | Moraketiya (Walawe Ganga) | 3.81 | 🟡 Alert | -0.030 |  |
| 2026-11-12 14:16:54 | Dunamale (Aththanagalu Oya) | 4.18 | 🟡 Alert | -0.032 |  |
| 2026-11-12 14:02:46 | Panadugama (Nilwala Ganga) | 5.87 | 🟡 Alert | -0.034 |  |
| 2026-11-12 14:08:33 | Magura (Kalu Ganga) | 5.16 | 🟡 Alert | -0.054 |  |
| 2026-11-12 14:11:25 | Thaldena (Mahaweli Ganga) | 1.36 | 🟢 Normal | 0.242 | 🔺 Rising |
| 2026-11-12 14:05:38 | Manampitiya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.179 | 🔺 Rising |
| 2026-11-12 14:06:21 | Kuda Oya (Kirindi Oya) | 2.59 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-11-12 14:03:37 | Nagalagam Street (Kelani Ganga) | 0.94 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-11-12 14:01:46 | Wellawaya (Kirindi Oya) | 1.78 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-12 14:02:16 | Kithulgala (Kelani Ganga) | 2.18 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-12 14:06:35 | Katharagama (Menik Ganga) | 0.54 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-12 14:03:27 | Putupaula (Kalu Ganga) | 2.53 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-11-12 14:04:46 | Padiyathalawa (Maduru Oya) | 0.84 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-12 14:19:11 | Horowpothana (Yan Oya) | 2.49 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-11-12 14:07:33 | Galgamuwa (Mee Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-11-12 14:00:45 | Thanthirimale (Malwathu Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-11-12 14:10:23 | Ellagawa (Kalu Ganga) | 8.32 | 🟢 Normal | -0.009 |  |
| 2026-11-12 14:05:39 | Holombuwa (Kelani Ganga) | 1.63 | 🟢 Normal | -0.010 |  |
| 2026-11-12 14:02:42 | Nawalapitiya (Mahaweli Ganga) | 1.58 | 🟢 Normal | -0.010 |  |
| 2026-11-12 14:02:51 | Siyambalanduwa (Heda Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-11-12 14:02:33 | Yaka Wewa (Ma Oya) | 0.77 | 🟢 Normal | -0.011 |  |
| 2026-11-12 14:03:22 | Norwood (Kelani Ganga) | 1.30 | 🟢 Normal | -0.020 |  |
| 2026-11-12 14:02:11 | Deraniyagala (Kelani Ganga) | 1.26 | 🟢 Normal | -0.020 |  |
| 2026-11-12 14:06:58 | Pitabeddara (Nilwala Ganga) | 2.37 | 🟢 Normal | -0.028 |  |
| 2026-11-12 14:04:37 | Thawalama (Gin Ganga) | 2.96 | 🟢 Normal | -0.035 |  |
| 2026-11-12 14:00:07 | Nakkala (Kumbukkan Oya) | 1.49 | 🟢 Normal | -0.041 |  |
| 2026-11-12 14:04:01 | Thanamalwila (Kirindi Oya) | 2.32 | 🟢 Normal | -0.042 |  |
| 2026-11-12 14:07:33 | Urawa (Nilwala Ganga) | 1.58 | 🟢 Normal | -0.046 |  |
| 2026-11-12 14:07:56 | Badalgama (Maha Oya) | 4.18 | 🟢 Normal | -0.059 |  |
| 2026-11-12 14:01:47 | Moragaswewa (Deduru Oya) | 3.09 | 🟢 Normal | -0.069 |  |
| 2026-11-12 14:05:12 | Peradeniya (Mahaweli Ganga) | 4.65 | 🟢 Normal | -0.079 |  |
| 2026-11-12 14:06:59 | Rathnapura (Kalu Ganga) | 4.97 | 🟢 Normal | -0.081 |  |
| 2026-11-12 14:06:36 | Giriulla (Maha Oya) | 2.69 | 🟢 Normal | -0.083 |  |
| 2026-11-12 14:00:38 | Weraganthota (Mahaweli Ganga) | -2.12 | 🟢 Normal | -0.109 |  |
| 2026-11-12 14:02:52 | Hanwella (Kelani Ganga) | 5.26 | 🟢 Normal | -0.110 |  |
| 2026-11-12 14:07:35 | Glencourse (Kelani Ganga) | 12.58 | 🟢 Normal | -0.162 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)