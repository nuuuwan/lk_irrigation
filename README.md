# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--14_19:23:23-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **287,909 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Holombuwa — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Panadugama — Alert; 🟡 Magura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-14 19:23:23 | Panadugama (Nilwala Ganga) | 5.53 | 🟡 Alert | -0.041 |  |
| 2026-10-14 19:17:38 | Urawa (Nilwala Ganga) | 1.07 | 🟢 Normal | -0.008 |  |
| 2026-10-14 19:14:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.04 | 🟡 Alert | 0.016 | 🔺 Rising |
| 2026-10-14 19:14:43 | Baddegama (Gin Ganga) | 2.63 | 🟢 Normal | -0.026 |  |
| 2026-10-14 19:11:26 | Thanamalwila (Kirindi Oya) | 0.80 | 🟢 Normal | -0.017 |  |
| 2026-10-14 19:09:24 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | -0.009 |  |
| 2026-10-14 19:08:39 | Magura (Kalu Ganga) | 4.60 | 🟡 Alert | -0.084 |  |
| 2026-10-14 19:08:36 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-10-14 19:08:36 | Putupaula (Kalu Ganga) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-10-14 19:08:20 | Rathnapura (Kalu Ganga) | 4.00 | 🟢 Normal | 0.528 | 🔺 Rising |
| 2026-10-14 19:07:54 | Holombuwa (Kelani Ganga) | 4.75 | 🟠 Minor Flood | 0.831 | 🔺 Rising |
| 2026-10-14 19:07:49 | Badalgama (Maha Oya) | 2.80 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-10-14 19:07:01 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-14 19:06:54 | Giriulla (Maha Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-10-14 19:06:48 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.144 |  |
| 2026-10-14 19:06:40 | Kithulgala (Kelani Ganga) | 1.95 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-10-14 19:06:36 | Thalgahagoda (Nilwala Ganga) | 1.74 | 🟠 Minor Flood | 0.028 | 🔺 Rising |
| 2026-10-14 19:06:23 | Hanwella (Kelani Ganga) | 3.16 | 🟢 Normal | 0.222 | 🔺 Rising |
| 2026-10-14 19:05:37 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-10-14 19:05:32 | Deraniyagala (Kelani Ganga) | 1.39 | 🟢 Normal | 0.532 | 🔺 Rising |
| 2026-10-14 19:05:32 | Glencourse (Kelani Ganga) | 12.00 | 🟢 Normal | 0.282 | 🔺 Rising |
| 2026-10-14 19:05:25 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.419 | 🔺 Rising |
| 2026-10-14 19:04:38 | Pitabeddara (Nilwala Ganga) | 1.67 | 🟢 Normal | -0.020 |  |
| 2026-10-14 19:04:37 | Nawalapitiya (Mahaweli Ganga) | 1.67 | 🟢 Normal | 0.163 | 🔺 Rising |
| 2026-10-14 19:03:57 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-14 19:03:29 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-14 19:03:08 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | -0.010 |  |
| 2026-10-14 19:02:59 | Norwood (Kelani Ganga) | 1.05 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-14 19:02:26 | Peradeniya (Mahaweli Ganga) | 3.88 | 🟢 Normal | 0.428 | 🔺 Rising |
| 2026-10-14 19:02:10 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | -0.020 |  |
| 2026-10-14 19:02:06 | Ellagawa (Kalu Ganga) | 7.77 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-14 19:02:05 | Moragaswewa (Deduru Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-10-14 19:02:05 | Dunamale (Aththanagalu Oya) | 2.50 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-10-14 19:01:48 | Thawalama (Gin Ganga) | 3.21 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-10-14 19:01:03 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-14 19:00:52 | Moraketiya (Walawe Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-10-14 19:00:28 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-14 19:07:54 | Holombuwa (Kelani Ganga) | 4.75 | 🟠 Minor Flood | 0.831 | 🔺 Rising |
| 2026-10-14 19:06:36 | Thalgahagoda (Nilwala Ganga) | 1.74 | 🟠 Minor Flood | 0.028 | 🔺 Rising |
| 2026-10-14 19:14:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.04 | 🟡 Alert | 0.016 | 🔺 Rising |
| 2026-10-14 19:23:23 | Panadugama (Nilwala Ganga) | 5.53 | 🟡 Alert | -0.041 |  |
| 2026-10-14 19:08:39 | Magura (Kalu Ganga) | 4.60 | 🟡 Alert | -0.084 |  |
| 2026-10-14 19:05:32 | Deraniyagala (Kelani Ganga) | 1.39 | 🟢 Normal | 0.532 | 🔺 Rising |
| 2026-10-14 19:08:20 | Rathnapura (Kalu Ganga) | 4.00 | 🟢 Normal | 0.528 | 🔺 Rising |
| 2026-10-14 19:02:26 | Peradeniya (Mahaweli Ganga) | 3.88 | 🟢 Normal | 0.428 | 🔺 Rising |
| 2026-10-14 19:05:25 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.419 | 🔺 Rising |
| 2026-10-14 19:05:32 | Glencourse (Kelani Ganga) | 12.00 | 🟢 Normal | 0.282 | 🔺 Rising |
| 2026-10-14 19:06:23 | Hanwella (Kelani Ganga) | 3.16 | 🟢 Normal | 0.222 | 🔺 Rising |
| 2026-10-14 19:04:37 | Nawalapitiya (Mahaweli Ganga) | 1.67 | 🟢 Normal | 0.163 | 🔺 Rising |
| 2026-10-14 19:02:05 | Dunamale (Aththanagalu Oya) | 2.50 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-10-14 19:01:48 | Thawalama (Gin Ganga) | 3.21 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-10-14 19:06:40 | Kithulgala (Kelani Ganga) | 1.95 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-10-14 19:07:49 | Badalgama (Maha Oya) | 2.80 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-10-14 19:02:59 | Norwood (Kelani Ganga) | 1.05 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-14 19:01:03 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-14 19:02:06 | Ellagawa (Kalu Ganga) | 7.77 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-14 19:07:01 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-14 18:02:30 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | 0.000 |  |
| 2026-10-14 19:00:28 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-10-14 19:02:05 | Moragaswewa (Deduru Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-10-14 19:06:54 | Giriulla (Maha Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-10-14 18:02:58 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-10-14 19:00:52 | Moraketiya (Walawe Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-10-14 19:03:57 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-14 19:08:36 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-10-14 19:08:36 | Putupaula (Kalu Ganga) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-10-14 18:02:47 | Thanthirimale (Malwathu Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-10-14 19:05:37 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-10-14 19:17:38 | Urawa (Nilwala Ganga) | 1.07 | 🟢 Normal | -0.008 |  |
| 2026-10-14 19:09:24 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | -0.009 |  |
| 2026-10-14 19:03:08 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | -0.010 |  |
| 2026-10-14 19:11:26 | Thanamalwila (Kirindi Oya) | 0.80 | 🟢 Normal | -0.017 |  |
| 2026-10-14 19:02:10 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | -0.020 |  |
| 2026-10-14 19:04:38 | Pitabeddara (Nilwala Ganga) | 1.67 | 🟢 Normal | -0.020 |  |
| 2026-10-14 19:14:43 | Baddegama (Gin Ganga) | 2.63 | 🟢 Normal | -0.026 |  |
| 2026-10-14 19:06:48 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.144 |  |

## River Water Level Charts by Station

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)