# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--13_12:24:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **314,687 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Panadugama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟡 Moraketiya — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-13 12:24:10 | Urawa (Nilwala Ganga) | 1.48 | 🟢 Normal | -0.015 |  |
| 2026-11-13 12:11:17 | Magura (Kalu Ganga) | 3.59 | 🟢 Normal | -0.062 |  |
| 2026-11-13 12:10:35 | Panadugama (Nilwala Ganga) | 6.26 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-13 12:08:16 | Thalgahagoda (Nilwala Ganga) | 1.86 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-13 12:07:34 | Horowpothana (Yan Oya) | 2.73 | 🟢 Normal | -0.019 |  |
| 2026-11-13 12:07:13 | Dunamale (Aththanagalu Oya) | 3.18 | 🟢 Normal | -0.018 |  |
| 2026-11-13 12:07:06 | Deraniyagala (Kelani Ganga) | 0.94 | 🟢 Normal | -0.074 |  |
| 2026-11-13 12:06:34 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-11-13 12:06:05 | Glencourse (Kelani Ganga) | 11.34 | 🟢 Normal | -0.039 |  |
| 2026-11-13 12:05:53 | Holombuwa (Kelani Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-11-13 12:05:48 | Kuda Oya (Kirindi Oya) | 2.37 | 🟢 Normal | -0.010 |  |
| 2026-11-13 12:04:58 | Badalgama (Maha Oya) | 3.39 | 🟢 Normal | -0.032 |  |
| 2026-11-13 12:04:55 | Norwood (Kelani Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-11-13 12:04:22 | Manampitiya (Mahaweli Ganga) | 2.21 | 🟢 Normal | -0.020 |  |
| 2026-11-13 12:03:47 | Norwood (Kelani Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-11-13 12:03:45 | Wellawaya (Kirindi Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-11-13 12:03:21 | Siyambalanduwa (Heda Oya) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-11-13 12:03:19 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-11-13 12:03:18 | Panadugama (Nilwala Ganga) | 6.26 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-13 12:03:14 | Hanwella (Kelani Ganga) | 3.67 | 🟢 Normal | -0.071 |  |
| 2026-11-13 12:03:11 | Giriulla (Maha Oya) | 2.03 | 🟢 Normal | -0.051 |  |
| 2026-11-13 12:02:54 | Ellagawa (Kalu Ganga) | 7.92 | 🟢 Normal | -0.019 |  |
| 2026-11-13 12:02:51 | Pitabeddara (Nilwala Ganga) | 2.07 | 🟢 Normal | -0.021 |  |
| 2026-11-13 12:02:47 | Putupaula (Kalu Ganga) | 2.33 | 🟢 Normal | -0.032 |  |
| 2026-11-13 12:02:38 | Weraganthota (Mahaweli Ganga) | -1.87 | 🟢 Normal | -0.112 |  |
| 2026-11-13 12:02:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.03 | 🟡 Alert | -0.020 |  |
| 2026-11-13 12:02:27 | Moraketiya (Walawe Ganga) | 3.78 | 🟡 Alert | 0.000 |  |
| 2026-11-13 12:02:20 | Thanamalwila (Kirindi Oya) | 2.11 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-13 12:02:13 | Thaldena (Mahaweli Ganga) | 1.08 | 🟢 Normal | -0.033 |  |
| 2026-11-13 12:02:11 | Galgamuwa (Mee Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-13 12:02:10 | Galgamuwa (Mee Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-13 12:02:08 | Katharagama (Menik Ganga) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-11-13 12:02:01 | Kithulgala (Kelani Ganga) | 2.06 | 🟢 Normal | -0.020 |  |
| 2026-11-13 12:01:59 | Nakkala (Kumbukkan Oya) | 1.42 | 🟢 Normal | -0.020 |  |
| 2026-11-13 12:01:41 | Nawalapitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.020 |  |
| 2026-11-13 12:01:39 | Moragaswewa (Deduru Oya) | 1.25 | 🟢 Normal | -0.031 |  |
| 2026-11-13 12:01:26 | Thawalama (Gin Ganga) | 2.65 | 🟢 Normal | -0.036 |  |
| 2026-11-13 12:01:12 | Peradeniya (Mahaweli Ganga) | 3.95 | 🟢 Normal | -0.025 |  |
| 2026-11-13 12:01:07 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-11-13 12:00:36 | Rathnapura (Kalu Ganga) | 3.64 | 🟢 Normal | -0.083 |  |
| 2026-11-13 12:00:34 | Thanthirimale (Malwathu Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-11-13 12:00:15 | Baddegama (Gin Ganga) | 4.16 | 🟠 Minor Flood | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-13 12:00:15 | Baddegama (Gin Ganga) | 4.16 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-13 12:10:35 | Panadugama (Nilwala Ganga) | 6.26 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-13 12:08:16 | Thalgahagoda (Nilwala Ganga) | 1.86 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-13 12:02:27 | Moraketiya (Walawe Ganga) | 3.78 | 🟡 Alert | 0.000 |  |
| 2026-11-13 12:02:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.03 | 🟡 Alert | -0.020 |  |
| 2026-11-13 12:03:19 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-11-13 12:02:20 | Thanamalwila (Kirindi Oya) | 2.11 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-13 12:03:45 | Wellawaya (Kirindi Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-11-13 12:01:07 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-11-13 12:02:11 | Galgamuwa (Mee Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-13 12:04:55 | Norwood (Kelani Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-11-13 12:06:34 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-11-13 12:05:53 | Holombuwa (Kelani Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-11-13 12:00:34 | Thanthirimale (Malwathu Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-11-13 12:05:48 | Kuda Oya (Kirindi Oya) | 2.37 | 🟢 Normal | -0.010 |  |
| 2026-11-13 12:03:21 | Siyambalanduwa (Heda Oya) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-11-13 12:02:08 | Katharagama (Menik Ganga) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-11-13 12:24:10 | Urawa (Nilwala Ganga) | 1.48 | 🟢 Normal | -0.015 |  |
| 2026-11-13 12:07:13 | Dunamale (Aththanagalu Oya) | 3.18 | 🟢 Normal | -0.018 |  |
| 2026-11-13 12:07:34 | Horowpothana (Yan Oya) | 2.73 | 🟢 Normal | -0.019 |  |
| 2026-11-13 12:02:54 | Ellagawa (Kalu Ganga) | 7.92 | 🟢 Normal | -0.019 |  |
| 2026-11-13 12:04:22 | Manampitiya (Mahaweli Ganga) | 2.21 | 🟢 Normal | -0.020 |  |
| 2026-11-13 12:01:41 | Nawalapitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.020 |  |
| 2026-11-13 12:02:01 | Kithulgala (Kelani Ganga) | 2.06 | 🟢 Normal | -0.020 |  |
| 2026-11-13 12:01:59 | Nakkala (Kumbukkan Oya) | 1.42 | 🟢 Normal | -0.020 |  |
| 2026-11-13 12:02:51 | Pitabeddara (Nilwala Ganga) | 2.07 | 🟢 Normal | -0.021 |  |
| 2026-11-13 12:01:12 | Peradeniya (Mahaweli Ganga) | 3.95 | 🟢 Normal | -0.025 |  |
| 2026-11-13 12:01:39 | Moragaswewa (Deduru Oya) | 1.25 | 🟢 Normal | -0.031 |  |
| 2026-11-13 12:02:47 | Putupaula (Kalu Ganga) | 2.33 | 🟢 Normal | -0.032 |  |
| 2026-11-13 12:04:58 | Badalgama (Maha Oya) | 3.39 | 🟢 Normal | -0.032 |  |
| 2026-11-13 12:02:13 | Thaldena (Mahaweli Ganga) | 1.08 | 🟢 Normal | -0.033 |  |
| 2026-11-13 12:01:26 | Thawalama (Gin Ganga) | 2.65 | 🟢 Normal | -0.036 |  |
| 2026-11-13 12:06:05 | Glencourse (Kelani Ganga) | 11.34 | 🟢 Normal | -0.039 |  |
| 2026-11-13 12:03:11 | Giriulla (Maha Oya) | 2.03 | 🟢 Normal | -0.051 |  |
| 2026-11-13 12:11:17 | Magura (Kalu Ganga) | 3.59 | 🟢 Normal | -0.062 |  |
| 2026-11-13 12:03:14 | Hanwella (Kelani Ganga) | 3.67 | 🟢 Normal | -0.071 |  |
| 2026-11-13 12:07:06 | Deraniyagala (Kelani Ganga) | 0.94 | 🟢 Normal | -0.074 |  |
| 2026-11-13 12:00:36 | Rathnapura (Kalu Ganga) | 3.64 | 🟢 Normal | -0.083 |  |
| 2026-11-13 12:02:38 | Weraganthota (Mahaweli Ganga) | -1.87 | 🟢 Normal | -0.112 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)