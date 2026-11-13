# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--14_00:03:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **315,115 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Baddegama — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Panadugama — Alert; 🟡 Moraketiya — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **16** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-14 00:03:15 | Kithulgala (Kelani Ganga) | 2.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-14 00:02:43 | Kuda Oya (Kirindi Oya) | 2.24 | 🟢 Normal | -0.011 |  |
| 2026-11-14 00:02:34 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | -0.021 |  |
| 2026-11-14 00:02:23 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-11-14 00:02:21 | Badalgama (Maha Oya) | 3.13 | 🟢 Normal | -0.020 |  |
| 2026-11-14 00:02:21 | Dunamale (Aththanagalu Oya) | 2.66 | 🟢 Normal | -0.033 |  |
| 2026-11-14 00:02:17 | Siyambalanduwa (Heda Oya) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-11-14 00:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.62 | 🟡 Alert | -0.039 |  |
| 2026-11-14 00:02:04 | Nawalapitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-11-14 00:01:56 | Pitabeddara (Nilwala Ganga) | 1.72 | 🟢 Normal | -0.030 |  |
| 2026-11-14 00:01:43 | Giriulla (Maha Oya) | 1.81 | 🟢 Normal | -0.010 |  |
| 2026-11-14 00:01:37 | Padiyathalawa (Maduru Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-11-14 00:01:10 | Nakkala (Kumbukkan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-11-14 00:00:39 | Thalgahagoda (Nilwala Ganga) | 1.94 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-13 23:36:55 | Katharagama (Menik Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-11-13 23:26:18 | Dunamale (Aththanagalu Oya) | 2.68 | 🟢 Normal | -0.033 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-14 00:00:39 | Thalgahagoda (Nilwala Ganga) | 1.94 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-13 23:03:53 | Baddegama (Gin Ganga) | 3.95 | 🟡 Alert | -0.021 |  |
| 2026-11-14 00:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.62 | 🟡 Alert | -0.039 |  |
| 2026-11-13 23:04:04 | Panadugama (Nilwala Ganga) | 5.90 | 🟡 Alert | -0.068 |  |
| 2026-11-13 23:04:27 | Moraketiya (Walawe Ganga) | 3.15 | 🟡 Alert | -0.145 |  |
| 2026-11-13 23:01:59 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-11-13 18:01:48 | Weraganthota (Mahaweli Ganga) | -2.33 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-13 23:03:25 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-14 00:03:15 | Kithulgala (Kelani Ganga) | 2.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-13 23:00:11 | Wellawaya (Kirindi Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-11-14 00:01:10 | Nakkala (Kumbukkan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-11-13 23:02:07 | Moragaswewa (Deduru Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-11-14 00:02:23 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-11-13 23:03:36 | Horowpothana (Yan Oya) | 2.57 | 🟢 Normal | 0.000 |  |
| 2026-11-13 18:04:50 | Galgamuwa (Mee Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-13 23:05:53 | Norwood (Kelani Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-11-14 00:01:37 | Padiyathalawa (Maduru Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-11-13 23:36:55 | Katharagama (Menik Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-11-13 23:05:23 | Glencourse (Kelani Ganga) | 10.98 | 🟢 Normal | -0.010 |  |
| 2026-11-13 22:05:41 | Urawa (Nilwala Ganga) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-11-14 00:02:04 | Nawalapitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-11-13 22:06:36 | Thanamalwila (Kirindi Oya) | 1.96 | 🟢 Normal | -0.010 |  |
| 2026-11-14 00:02:17 | Siyambalanduwa (Heda Oya) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-11-14 00:01:43 | Giriulla (Maha Oya) | 1.81 | 🟢 Normal | -0.010 |  |
| 2026-11-14 00:02:43 | Kuda Oya (Kirindi Oya) | 2.24 | 🟢 Normal | -0.011 |  |
| 2026-11-13 23:05:09 | Thaldena (Mahaweli Ganga) | 0.89 | 🟢 Normal | -0.016 |  |
| 2026-11-13 23:05:36 | Putupaula (Kalu Ganga) | 2.18 | 🟢 Normal | -0.019 |  |
| 2026-11-14 00:02:21 | Badalgama (Maha Oya) | 3.13 | 🟢 Normal | -0.020 |  |
| 2026-11-14 00:02:34 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | -0.021 |  |
| 2026-11-13 18:04:09 | Thanthirimale (Malwathu Oya) | 1.92 | 🟢 Normal | -0.029 |  |
| 2026-11-14 00:01:56 | Pitabeddara (Nilwala Ganga) | 1.72 | 🟢 Normal | -0.030 |  |
| 2026-11-14 00:02:21 | Dunamale (Aththanagalu Oya) | 2.66 | 🟢 Normal | -0.033 |  |
| 2026-11-13 23:03:10 | Hanwella (Kelani Ganga) | 3.17 | 🟢 Normal | -0.039 |  |
| 2026-11-13 23:02:37 | Thawalama (Gin Ganga) | 2.29 | 🟢 Normal | -0.042 |  |
| 2026-11-13 23:02:00 | Peradeniya (Mahaweli Ganga) | 3.46 | 🟢 Normal | -0.048 |  |
| 2026-11-13 23:02:40 | Manampitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.060 |  |
| 2026-11-13 23:01:13 | Rathnapura (Kalu Ganga) | 2.83 | 🟢 Normal | -0.070 |  |
| 2026-11-13 23:08:10 | Magura (Kalu Ganga) | 2.71 | 🟢 Normal | -0.102 |  |
| 2026-11-13 23:02:11 | Ellagawa (Kalu Ganga) | 7.17 | 🟢 Normal | -0.114 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)