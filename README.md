# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--04_03:26:59-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **306,247 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-04 03:26:59 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | -0.008 |  |
| 2026-11-04 03:20:00 | Nawalapitiya (Mahaweli Ganga) | 1.43 | 🟢 Normal | -0.031 |  |
| 2026-11-04 03:18:39 | Rathnapura (Kalu Ganga) | 3.69 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2026-11-04 03:13:19 | Deraniyagala (Kelani Ganga) | 0.97 | 🟢 Normal | -0.050 |  |
| 2026-11-04 03:12:09 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.056 |  |
| 2026-11-04 03:08:32 | Ellagawa (Kalu Ganga) | 6.55 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-11-04 03:08:17 | Thalgahagoda (Nilwala Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-11-04 03:07:32 | Hanwella (Kelani Ganga) | 3.07 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-11-04 03:06:42 | Thaldena (Mahaweli Ganga) | 0.62 | 🟢 Normal | -0.028 |  |
| 2026-11-04 03:06:19 | Moraketiya (Walawe Ganga) | 2.63 | 🟢 Normal | -0.020 |  |
| 2026-11-04 03:06:06 | Dunamale (Aththanagalu Oya) | 2.65 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-04 03:05:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.03 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-04 03:05:20 | Badalgama (Maha Oya) | 3.97 | 🟢 Normal | 0.361 | 🔺 Rising |
| 2026-11-04 03:05:14 | Giriulla (Maha Oya) | 3.72 | 🟢 Normal | 0.000 |  |
| 2026-11-04 03:04:50 | Baddegama (Gin Ganga) | 2.05 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-11-04 03:04:48 | Thawalama (Gin Ganga) | 3.50 | 🟢 Normal | -0.078 |  |
| 2026-11-04 03:04:38 | Norwood (Kelani Ganga) | 1.36 | 🟢 Normal | -0.019 |  |
| 2026-11-04 03:04:18 | Pitabeddara (Nilwala Ganga) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-11-04 03:04:16 | Pitabeddara (Nilwala Ganga) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-11-04 03:04:15 | Pitabeddara (Nilwala Ganga) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-11-04 03:04:12 | Holombuwa (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-11-04 03:04:09 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-11-04 03:04:05 | Glencourse (Kelani Ganga) | 11.38 | 🟢 Normal | -0.307 |  |
| 2026-11-04 03:03:14 | Horowpothana (Yan Oya) | 3.13 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-11-04 03:03:04 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-11-04 03:02:55 | Urawa (Nilwala Ganga) | 1.90 | 🟢 Normal | -0.692 |  |
| 2026-11-04 03:02:46 | Panadugama (Nilwala Ganga) | 4.40 | 🟢 Normal | 0.347 | 🔺 Rising |
| 2026-11-04 03:02:45 | Manampitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.041 |  |
| 2026-11-04 03:02:29 | Nakkala (Kumbukkan Oya) | 0.99 | 🟢 Normal | -0.039 |  |
| 2026-11-04 03:02:08 | Moragaswewa (Deduru Oya) | 4.15 | 🟢 Normal | -0.020 |  |
| 2026-11-04 03:01:53 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-04 03:01:28 | Peradeniya (Mahaweli Ganga) | 3.35 | 🟢 Normal | -0.128 |  |
| 2026-11-04 03:01:14 | Padiyathalawa (Maduru Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-11-04 02:51:39 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-04 03:05:20 | Badalgama (Maha Oya) | 3.97 | 🟢 Normal | 0.361 | 🔺 Rising |
| 2026-11-04 03:02:46 | Panadugama (Nilwala Ganga) | 4.40 | 🟢 Normal | 0.347 | 🔺 Rising |
| 2026-11-03 18:06:38 | Galgamuwa (Mee Oya) | 1.16 | 🟢 Normal | 0.248 | 🔺 Rising |
| 2026-11-04 01:06:59 | Magura (Kalu Ganga) | 3.45 | 🟢 Normal | 0.166 | 🔺 Rising |
| 2026-11-04 03:18:39 | Rathnapura (Kalu Ganga) | 3.69 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2026-11-04 03:03:14 | Horowpothana (Yan Oya) | 3.13 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-11-03 18:04:27 | Weraganthota (Mahaweli Ganga) | -2.51 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-11-04 03:07:32 | Hanwella (Kelani Ganga) | 3.07 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-11-04 03:08:32 | Ellagawa (Kalu Ganga) | 6.55 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-11-04 03:04:50 | Baddegama (Gin Ganga) | 2.05 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-11-04 03:06:06 | Dunamale (Aththanagalu Oya) | 2.65 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-04 03:05:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.03 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-04 03:04:09 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-11-04 03:01:53 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-04 03:05:14 | Giriulla (Maha Oya) | 3.72 | 🟢 Normal | 0.000 |  |
| 2026-11-04 03:04:18 | Pitabeddara (Nilwala Ganga) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-11-04 03:01:14 | Padiyathalawa (Maduru Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-11-04 03:03:04 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-11-04 02:51:39 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-11-04 03:04:12 | Holombuwa (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-11-03 18:50:18 | Thanthirimale (Malwathu Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-11-04 03:08:17 | Thalgahagoda (Nilwala Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-11-04 03:26:59 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | -0.008 |  |
| 2026-11-04 02:01:09 | Wellawaya (Kirindi Oya) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-11-04 03:04:38 | Norwood (Kelani Ganga) | 1.36 | 🟢 Normal | -0.019 |  |
| 2026-11-04 03:02:08 | Moragaswewa (Deduru Oya) | 4.15 | 🟢 Normal | -0.020 |  |
| 2026-11-04 03:06:19 | Moraketiya (Walawe Ganga) | 2.63 | 🟢 Normal | -0.020 |  |
| 2026-11-04 03:06:42 | Thaldena (Mahaweli Ganga) | 0.62 | 🟢 Normal | -0.028 |  |
| 2026-11-04 03:20:00 | Nawalapitiya (Mahaweli Ganga) | 1.43 | 🟢 Normal | -0.031 |  |
| 2026-11-04 03:02:29 | Nakkala (Kumbukkan Oya) | 0.99 | 🟢 Normal | -0.039 |  |
| 2026-11-04 03:02:45 | Manampitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.041 |  |
| 2026-11-04 03:13:19 | Deraniyagala (Kelani Ganga) | 0.97 | 🟢 Normal | -0.050 |  |
| 2026-11-04 03:12:09 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.056 |  |
| 2026-11-04 02:02:21 | Thanamalwila (Kirindi Oya) | 1.85 | 🟢 Normal | -0.066 |  |
| 2026-11-04 03:04:48 | Thawalama (Gin Ganga) | 3.50 | 🟢 Normal | -0.078 |  |
| 2026-11-04 03:01:28 | Peradeniya (Mahaweli Ganga) | 3.35 | 🟢 Normal | -0.128 |  |
| 2026-11-04 02:04:18 | Kuda Oya (Kirindi Oya) | 2.15 | 🟢 Normal | -0.162 |  |
| 2026-11-04 03:04:05 | Glencourse (Kelani Ganga) | 11.38 | 🟢 Normal | -0.307 |  |
| 2026-11-04 03:02:55 | Urawa (Nilwala Ganga) | 1.90 | 🟢 Normal | -0.692 |  |

## River Water Level Charts by Station

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)