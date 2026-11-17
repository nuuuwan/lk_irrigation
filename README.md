# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--17_22:15:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **318,644 measurements** from **39** stations.
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
| 2026-11-17 22:15:29 | Putupaula (Kalu Ganga) | 0.64 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-11-17 22:12:58 | Pitabeddara (Nilwala Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-11-17 22:11:13 | Rathnapura (Kalu Ganga) | 1.53 | 🟢 Normal | -0.038 |  |
| 2026-11-17 22:09:28 | Baddegama (Gin Ganga) | 1.57 | 🟢 Normal | -0.010 |  |
| 2026-11-17 22:07:29 | Giriulla (Maha Oya) | 1.33 | 🟢 Normal | -0.019 |  |
| 2026-11-17 22:07:21 | Holombuwa (Kelani Ganga) | 0.69 | 🟢 Normal | -0.009 |  |
| 2026-11-17 22:07:14 | Urawa (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.021 |  |
| 2026-11-17 22:06:52 | Magura (Kalu Ganga) | 1.59 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-11-17 22:05:56 | Badalgama (Maha Oya) | 2.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-17 22:05:23 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-17 22:05:20 | Glencourse (Kelani Ganga) | 10.20 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-11-17 22:05:15 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-11-17 22:04:30 | Deraniyagala (Kelani Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-11-17 22:04:06 | Kuda Oya (Kirindi Oya) | 1.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-17 22:04:05 | Thanamalwila (Kirindi Oya) | 1.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-17 22:03:31 | Moraketiya (Walawe Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-11-17 22:03:06 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-11-17 22:03:05 | Moragaswewa (Deduru Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-11-17 22:03:03 | Hanwella (Kelani Ganga) | 1.90 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-17 22:02:56 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.020 |  |
| 2026-11-17 22:02:52 | Ellagawa (Kalu Ganga) | 5.03 | 🟢 Normal | 0.000 |  |
| 2026-11-17 22:02:51 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-11-17 22:02:33 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-11-17 22:02:32 | Dunamale (Aththanagalu Oya) | 1.62 | 🟢 Normal | -0.020 |  |
| 2026-11-17 22:02:03 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-17 22:01:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.49 | 🟢 Normal | 0.000 |  |
| 2026-11-17 22:01:24 | Peradeniya (Mahaweli Ganga) | 2.78 | 🟢 Normal | 0.000 |  |
| 2026-11-17 22:00:58 | Horowpothana (Yan Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-11-17 22:00:50 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-11-17 22:00:43 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-11-17 22:00:39 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-17 22:00:23 | Manampitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-11-17 22:00:17 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-11-17 22:00:08 | Wellawaya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.020 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-17 22:06:52 | Magura (Kalu Ganga) | 1.59 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-11-17 22:05:20 | Glencourse (Kelani Ganga) | 10.20 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-11-17 22:15:29 | Putupaula (Kalu Ganga) | 0.64 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-11-17 22:00:08 | Wellawaya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-17 22:05:56 | Badalgama (Maha Oya) | 2.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-17 21:01:36 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-17 22:03:03 | Hanwella (Kelani Ganga) | 1.90 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-17 22:04:05 | Thanamalwila (Kirindi Oya) | 1.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-17 22:04:06 | Kuda Oya (Kirindi Oya) | 1.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-17 22:05:23 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-17 18:03:49 | Weraganthota (Mahaweli Ganga) | -2.19 | 🟢 Normal | 0.000 |  |
| 2026-11-17 22:00:43 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-11-17 22:03:05 | Moragaswewa (Deduru Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-11-17 22:02:33 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-11-17 22:02:03 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-17 22:00:58 | Horowpothana (Yan Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-11-17 18:03:41 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-11-17 22:12:58 | Pitabeddara (Nilwala Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-11-17 22:02:52 | Ellagawa (Kalu Ganga) | 5.03 | 🟢 Normal | 0.000 |  |
| 2026-11-17 21:07:28 | Panadugama (Nilwala Ganga) | 3.71 | 🟢 Normal | 0.000 |  |
| 2026-11-17 21:11:42 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-11-17 22:03:06 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-11-17 22:03:31 | Moraketiya (Walawe Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-11-17 22:00:39 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-17 22:05:15 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-11-17 18:01:44 | Thanthirimale (Malwathu Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-11-17 22:01:24 | Peradeniya (Mahaweli Ganga) | 2.78 | 🟢 Normal | 0.000 |  |
| 2026-11-17 22:00:17 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-11-17 22:01:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.49 | 🟢 Normal | 0.000 |  |
| 2026-11-17 22:07:21 | Holombuwa (Kelani Ganga) | 0.69 | 🟢 Normal | -0.009 |  |
| 2026-11-17 22:09:28 | Baddegama (Gin Ganga) | 1.57 | 🟢 Normal | -0.010 |  |
| 2026-11-17 22:04:30 | Deraniyagala (Kelani Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-11-17 22:00:23 | Manampitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-11-17 22:02:51 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-11-17 22:07:29 | Giriulla (Maha Oya) | 1.33 | 🟢 Normal | -0.019 |  |
| 2026-11-17 22:02:32 | Dunamale (Aththanagalu Oya) | 1.62 | 🟢 Normal | -0.020 |  |
| 2026-11-17 22:02:56 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.020 |  |
| 2026-11-17 22:07:14 | Urawa (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.021 |  |
| 2026-11-17 22:11:13 | Rathnapura (Kalu Ganga) | 1.53 | 🟢 Normal | -0.038 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)