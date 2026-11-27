# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--28_04:03:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **327,627 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Panadugama — Alert; 🟡 Dunamale — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Moraketiya — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **21** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-28 04:03:15 | Katharagama (Menik Ganga) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-11-28 04:03:06 | Horowpothana (Yan Oya) | 2.38 | 🟢 Normal | 0.000 |  |
| 2026-11-28 04:02:57 | Kuda Oya (Kirindi Oya) | 3.18 | 🟢 Normal | -0.270 |  |
| 2026-11-28 04:02:47 | Moraketiya (Walawe Ganga) | 3.75 | 🟡 Alert | -0.050 |  |
| 2026-11-28 04:02:46 | Nakkala (Kumbukkan Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-11-28 04:02:46 | Deraniyagala (Kelani Ganga) | 1.04 | 🟢 Normal | -0.081 |  |
| 2026-11-28 04:02:38 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-11-28 04:02:35 | Badalgama (Maha Oya) | 4.55 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-11-28 04:02:28 | Dunamale (Aththanagalu Oya) | 3.88 | 🟡 Alert | 0.080 | 🔺 Rising |
| 2026-11-28 04:02:20 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.243 |  |
| 2026-11-28 04:02:02 | Glencourse (Kelani Ganga) | 12.27 | 🟢 Normal | -0.080 |  |
| 2026-11-28 04:01:39 | Peradeniya (Mahaweli Ganga) | 2.12 | 🟢 Normal | -1.159 |  |
| 2026-11-28 04:01:33 | Thaldena (Mahaweli Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-11-28 04:01:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.10 | 🟡 Alert | -0.020 |  |
| 2026-11-28 04:01:15 | Ellagawa (Kalu Ganga) | 7.41 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-28 04:01:09 | Manampitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.102 |  |
| 2026-11-28 04:01:02 | Magura (Kalu Ganga) | 3.98 | 🟢 Normal | 0.000 |  |
| 2026-11-28 04:01:00 | Wellawaya (Kirindi Oya) | 1.64 | 🟢 Normal | 1.455 | 🔺 Rising |
| 2026-11-28 04:00:33 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.011 |  |
| 2026-11-28 03:41:16 | Thalgahagoda (Nilwala Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-11-28 03:36:58 | Putupaula (Kalu Ganga) | 1.43 | 🟢 Normal | 0.012 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-28 03:08:07 | Panadugama (Nilwala Ganga) | 5.46 | 🟡 Alert | 4.696 | 🔺 Rising |
| 2026-11-28 04:02:28 | Dunamale (Aththanagalu Oya) | 3.88 | 🟡 Alert | 0.080 | 🔺 Rising |
| 2026-11-28 04:01:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.10 | 🟡 Alert | -0.020 |  |
| 2026-11-28 04:02:47 | Moraketiya (Walawe Ganga) | 3.75 | 🟡 Alert | -0.050 |  |
| 2026-11-28 04:01:00 | Wellawaya (Kirindi Oya) | 1.64 | 🟢 Normal | 1.455 | 🔺 Rising |
| 2026-11-28 03:12:05 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-11-28 04:02:35 | Badalgama (Maha Oya) | 4.55 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-11-28 04:01:15 | Ellagawa (Kalu Ganga) | 7.41 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-28 03:04:34 | Hanwella (Kelani Ganga) | 4.24 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-28 03:36:58 | Putupaula (Kalu Ganga) | 1.43 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-11-28 03:02:25 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-28 04:03:06 | Horowpothana (Yan Oya) | 2.38 | 🟢 Normal | 0.000 |  |
| 2026-11-27 18:04:37 | Galgamuwa (Mee Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-11-28 04:01:02 | Magura (Kalu Ganga) | 3.98 | 🟢 Normal | 0.000 |  |
| 2026-11-28 04:02:38 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-11-28 03:11:26 | Baddegama (Gin Ganga) | 2.11 | 🟢 Normal | 0.000 |  |
| 2026-11-28 04:01:33 | Thaldena (Mahaweli Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-11-28 03:41:16 | Thalgahagoda (Nilwala Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-11-28 03:03:54 | Thanamalwila (Kirindi Oya) | 3.12 | 🟢 Normal | 0.000 |  |
| 2026-11-28 04:02:46 | Nakkala (Kumbukkan Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-11-28 04:03:15 | Katharagama (Menik Ganga) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-11-28 04:00:33 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.011 |  |
| 2026-11-28 03:05:28 | Padiyathalawa (Maduru Oya) | 0.72 | 🟢 Normal | -0.011 |  |
| 2026-11-27 18:01:42 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | -0.031 |  |
| 2026-11-28 03:03:39 | Rathnapura (Kalu Ganga) | 3.13 | 🟢 Normal | -0.035 |  |
| 2026-11-28 03:03:31 | Thawalama (Gin Ganga) | 2.21 | 🟢 Normal | -0.041 |  |
| 2026-11-27 18:00:16 | Weraganthota (Mahaweli Ganga) | -1.98 | 🟢 Normal | -0.041 |  |
| 2026-11-28 03:04:01 | Siyambalanduwa (Heda Oya) | 1.15 | 🟢 Normal | -0.042 |  |
| 2026-11-28 03:02:32 | Moragaswewa (Deduru Oya) | 2.71 | 🟢 Normal | -0.059 |  |
| 2026-11-28 04:02:02 | Glencourse (Kelani Ganga) | 12.27 | 🟢 Normal | -0.080 |  |
| 2026-11-28 04:02:46 | Deraniyagala (Kelani Ganga) | 1.04 | 🟢 Normal | -0.081 |  |
| 2026-11-28 04:01:09 | Manampitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.102 |  |
| 2026-11-28 03:02:41 | Giriulla (Maha Oya) | 3.45 | 🟢 Normal | -0.112 |  |
| 2026-11-28 03:14:26 | Holombuwa (Kelani Ganga) | 1.87 | 🟢 Normal | -0.171 |  |
| 2026-11-28 04:02:20 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.243 |  |
| 2026-11-28 04:02:57 | Kuda Oya (Kirindi Oya) | 3.18 | 🟢 Normal | -0.270 |  |
| 2026-11-28 03:08:43 | Urawa (Nilwala Ganga) | 1.72 | 🟢 Normal | -0.335 |  |
| 2026-11-28 03:12:56 | Pitabeddara (Nilwala Ganga) | 1.77 | 🟢 Normal | -0.961 |  |
| 2026-11-28 04:01:39 | Peradeniya (Mahaweli Ganga) | 2.12 | 🟢 Normal | -1.159 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)