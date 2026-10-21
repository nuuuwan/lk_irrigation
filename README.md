# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--22_01:04:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **294,443 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Rathnapura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **27** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-22 01:04:48 | Thawalama (Gin Ganga) | 1.75 | 🟢 Normal | -0.040 |  |
| 2026-10-22 01:04:18 | Giriulla (Maha Oya) | 1.53 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-10-22 01:04:07 | Wellawaya (Kirindi Oya) | 1.55 | 🟢 Normal | -0.056 |  |
| 2026-10-22 01:03:46 | Moragaswewa (Deduru Oya) | 1.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-22 01:03:19 | Holombuwa (Kelani Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-10-22 01:02:56 | Glencourse (Kelani Ganga) | 13.06 | 🟢 Normal | 1.144 | 🔺 Rising |
| 2026-10-22 01:02:56 | Baddegama (Gin Ganga) | 1.74 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-22 01:02:41 | Kithulgala (Kelani Ganga) | 2.27 | 🟢 Normal | -0.120 |  |
| 2026-10-22 01:02:15 | Badalgama (Maha Oya) | 2.70 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-10-22 01:02:07 | Kuda Oya (Kirindi Oya) | 1.98 | 🟢 Normal | -0.316 |  |
| 2026-10-22 01:01:42 | Panadugama (Nilwala Ganga) | 4.78 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-10-22 01:01:31 | Thanamalwila (Kirindi Oya) | 1.91 | 🟢 Normal | -0.061 |  |
| 2026-10-22 01:01:28 | Nawalapitiya (Mahaweli Ganga) | 2.25 | 🟢 Normal | -0.161 |  |
| 2026-10-22 01:01:26 | Yaka Wewa (Ma Oya) | 1.58 | 🟢 Normal | -0.021 |  |
| 2026-10-22 01:01:22 | Peradeniya (Mahaweli Ganga) | 3.82 | 🟢 Normal | -0.086 |  |
| 2026-10-22 01:01:07 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | -0.021 |  |
| 2026-10-22 01:01:06 | Horowpothana (Yan Oya) | 2.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-22 01:01:03 | Nakkala (Kumbukkan Oya) | 1.15 | 🟢 Normal | -0.134 |  |
| 2026-10-22 01:00:13 | Thalgahagoda (Nilwala Ganga) | 1.25 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-10-22 00:29:37 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-22 00:23:21 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-10-22 00:20:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.56 | 🟢 Normal | 2.535 | 🔺 Rising |
| 2026-10-22 00:19:36 | Pitabeddara (Nilwala Ganga) | 2.30 | 🟢 Normal | -0.017 |  |
| 2026-10-22 00:18:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.51 | 🟢 Normal | 2.535 | 🔺 Rising |
| 2026-10-22 00:18:22 | Glencourse (Kelani Ganga) | 12.21 | 🟢 Normal | 1.144 | 🔺 Rising |
| 2026-10-22 00:17:20 | Thalgahagoda (Nilwala Ganga) | 1.24 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-10-22 00:16:55 | Holombuwa (Kelani Ganga) | 2.00 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-22 00:05:39 | Rathnapura (Kalu Ganga) | 5.30 | 🟡 Alert | 0.401 | 🔺 Rising |
| 2026-10-22 00:20:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.56 | 🟢 Normal | 2.535 | 🔺 Rising |
| 2026-10-22 01:02:56 | Glencourse (Kelani Ganga) | 13.06 | 🟢 Normal | 1.144 | 🔺 Rising |
| 2026-10-21 18:01:26 | Galgamuwa (Mee Oya) | 1.81 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-10-22 01:01:42 | Panadugama (Nilwala Ganga) | 4.78 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-10-22 00:05:00 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-10-22 01:04:18 | Giriulla (Maha Oya) | 1.53 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-10-21 23:05:37 | Ellagawa (Kalu Ganga) | 5.60 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-10-22 00:05:52 | Hanwella (Kelani Ganga) | 2.39 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-10-21 23:04:34 | Urawa (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-10-22 01:02:15 | Badalgama (Maha Oya) | 2.70 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-10-21 18:01:56 | Thanthirimale (Malwathu Oya) | 1.92 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-10-22 01:02:56 | Baddegama (Gin Ganga) | 1.74 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-22 00:04:14 | Dunamale (Aththanagalu Oya) | 1.88 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-22 01:00:13 | Thalgahagoda (Nilwala Ganga) | 1.25 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-10-22 00:08:58 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-10-22 01:01:06 | Horowpothana (Yan Oya) | 2.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-22 01:03:46 | Moragaswewa (Deduru Oya) | 1.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-21 20:04:28 | Norwood (Kelani Ganga) | 1.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-22 00:02:48 | Magura (Kalu Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-10-22 00:23:21 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-10-22 00:02:58 | Moraketiya (Walawe Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-10-22 00:29:37 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-22 01:03:19 | Holombuwa (Kelani Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-10-22 00:02:58 | Manampitiya (Mahaweli Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-10-22 00:19:36 | Pitabeddara (Nilwala Ganga) | 2.30 | 🟢 Normal | -0.017 |  |
| 2026-10-22 01:01:07 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | -0.021 |  |
| 2026-10-22 01:01:26 | Yaka Wewa (Ma Oya) | 1.58 | 🟢 Normal | -0.021 |  |
| 2026-10-22 01:04:48 | Thawalama (Gin Ganga) | 1.75 | 🟢 Normal | -0.040 |  |
| 2026-10-22 01:04:07 | Wellawaya (Kirindi Oya) | 1.55 | 🟢 Normal | -0.056 |  |
| 2026-10-22 01:01:31 | Thanamalwila (Kirindi Oya) | 1.91 | 🟢 Normal | -0.061 |  |
| 2026-10-21 18:00:26 | Weraganthota (Mahaweli Ganga) | -3.12 | 🟢 Normal | -0.070 |  |
| 2026-10-22 01:01:22 | Peradeniya (Mahaweli Ganga) | 3.82 | 🟢 Normal | -0.086 |  |
| 2026-10-22 01:02:41 | Kithulgala (Kelani Ganga) | 2.27 | 🟢 Normal | -0.120 |  |
| 2026-10-22 01:01:03 | Nakkala (Kumbukkan Oya) | 1.15 | 🟢 Normal | -0.134 |  |
| 2026-10-22 01:01:28 | Nawalapitiya (Mahaweli Ganga) | 2.25 | 🟢 Normal | -0.161 |  |
| 2026-10-22 01:02:07 | Kuda Oya (Kirindi Oya) | 1.98 | 🟢 Normal | -0.316 |  |
| 2026-10-22 00:03:17 | Deraniyagala (Kelani Ganga) | 2.68 | 🟢 Normal | -0.495 |  |
| 2026-10-22 00:06:15 | Siyambalanduwa (Heda Oya) | 2.47 | 🟢 Normal | -0.543 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)