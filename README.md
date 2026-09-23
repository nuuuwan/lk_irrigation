# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--23_19:06:34-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **269,007 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Baddegama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **25** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-23 19:06:34 | Kithulgala (Kelani Ganga) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-09-23 19:06:22 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-23 19:06:07 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.028 |  |
| 2026-09-23 19:05:47 | Deraniyagala (Kelani Ganga) | 1.90 | 🟢 Normal | -0.050 |  |
| 2026-09-23 19:05:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.87 | 🟠 Minor Flood | -0.019 |  |
| 2026-09-23 19:05:21 | Urawa (Nilwala Ganga) | 1.09 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-09-23 19:04:50 | Hanwella (Kelani Ganga) | 4.66 | 🟢 Normal | -0.030 |  |
| 2026-09-23 19:04:41 | Nawalapitiya (Mahaweli Ganga) | 2.70 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-09-23 19:03:40 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-23 19:03:40 | Glencourse (Kelani Ganga) | 12.49 | 🟢 Normal | -0.010 |  |
| 2026-09-23 19:03:39 | Ellagawa (Kalu Ganga) | 7.87 | 🟢 Normal | -0.010 |  |
| 2026-09-23 19:03:02 | Norwood (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-09-23 19:02:59 | Pitabeddara (Nilwala Ganga) | 1.50 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-09-23 19:02:57 | Magura (Kalu Ganga) | 3.86 | 🟢 Normal | -0.049 |  |
| 2026-09-23 19:02:49 | Manampitiya (Mahaweli Ganga) | -0.25 | 🟢 Normal | -0.010 |  |
| 2026-09-23 19:02:38 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | -0.019 |  |
| 2026-09-23 19:02:16 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-23 19:02:14 | Thanamalwila (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-09-23 19:02:03 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-23 19:01:33 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-09-23 19:01:30 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-23 19:01:19 | Kuda Oya (Kirindi Oya) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-09-23 19:01:03 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-09-23 19:01:03 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-23 18:31:10 | Panadugama (Nilwala Ganga) | 4.31 | 🟢 Normal | 0.027 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-23 19:05:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.87 | 🟠 Minor Flood | -0.019 |  |
| 2026-09-23 18:01:53 | Baddegama (Gin Ganga) | 3.67 | 🟡 Alert | -0.011 |  |
| 2026-09-23 18:03:48 | Rathnapura (Kalu Ganga) | 3.93 | 🟢 Normal | 0.142 | 🔺 Rising |
| 2026-09-23 19:04:41 | Nawalapitiya (Mahaweli Ganga) | 2.70 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-09-23 18:01:14 | Peradeniya (Mahaweli Ganga) | 3.10 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-09-23 19:05:21 | Urawa (Nilwala Ganga) | 1.09 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-09-23 18:07:06 | Holombuwa (Kelani Ganga) | 1.18 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-09-23 19:02:59 | Pitabeddara (Nilwala Ganga) | 1.50 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-09-23 18:02:41 | Thawalama (Gin Ganga) | 2.77 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-09-23 18:31:10 | Panadugama (Nilwala Ganga) | 4.31 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-09-23 19:02:16 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-23 19:06:34 | Kithulgala (Kelani Ganga) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-09-23 19:03:40 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-23 19:06:22 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-23 19:02:03 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-23 19:01:30 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-23 19:01:03 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-09-23 19:03:02 | Norwood (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-09-23 18:02:17 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-23 19:01:33 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-09-23 19:01:03 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-23 18:03:31 | Thanthirimale (Malwathu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-23 18:09:35 | Thalgahagoda (Nilwala Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-09-23 19:02:14 | Thanamalwila (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-09-23 18:10:48 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | -0.009 |  |
| 2026-09-23 18:06:29 | Giriulla (Maha Oya) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-09-23 19:03:39 | Ellagawa (Kalu Ganga) | 7.87 | 🟢 Normal | -0.010 |  |
| 2026-09-23 19:02:49 | Manampitiya (Mahaweli Ganga) | -0.25 | 🟢 Normal | -0.010 |  |
| 2026-09-23 19:01:19 | Kuda Oya (Kirindi Oya) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-09-23 18:03:57 | Badalgama (Maha Oya) | 2.66 | 🟢 Normal | -0.010 |  |
| 2026-09-23 19:03:40 | Glencourse (Kelani Ganga) | 12.49 | 🟢 Normal | -0.010 |  |
| 2026-09-23 19:02:38 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | -0.019 |  |
| 2026-09-23 18:01:34 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | -0.020 |  |
| 2026-09-23 18:02:06 | Putupaula (Kalu Ganga) | 2.81 | 🟢 Normal | -0.020 |  |
| 2026-09-23 19:06:07 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.028 |  |
| 2026-09-23 19:04:50 | Hanwella (Kelani Ganga) | 4.66 | 🟢 Normal | -0.030 |  |
| 2026-09-23 18:08:23 | Dunamale (Aththanagalu Oya) | 2.46 | 🟢 Normal | -0.036 |  |
| 2026-09-23 19:02:57 | Magura (Kalu Ganga) | 3.86 | 🟢 Normal | -0.049 |  |
| 2026-09-23 19:05:47 | Deraniyagala (Kelani Ganga) | 1.90 | 🟢 Normal | -0.050 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)