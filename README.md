# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--29_10:29:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **246,152 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-29 10:29:53 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-29 10:22:48 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-29 10:20:05 | Thalgahagoda (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-08-29 10:14:29 | Rathnapura (Kalu Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-08-29 10:10:32 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-29 10:10:24 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-08-29 10:08:12 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-08-29 10:08:05 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-29 10:07:53 | Glencourse (Kelani Ganga) | 10.18 | 🟢 Normal | 0.000 |  |
| 2026-08-29 10:07:14 | Thawalama (Gin Ganga) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-08-29 10:06:48 | Thanthirimale (Malwathu Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-29 10:06:27 | Urawa (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-08-29 10:06:24 | Badalgama (Maha Oya) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-08-29 10:05:32 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-08-29 10:05:12 | Pitabeddara (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-29 10:05:06 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | -0.010 |  |
| 2026-08-29 10:05:05 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-29 10:05:04 | Panadugama (Nilwala Ganga) | 3.36 | 🟢 Normal | 0.136 | 🔺 Rising |
| 2026-08-29 10:04:57 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-29 10:04:30 | Baddegama (Gin Ganga) | 1.70 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-29 10:04:26 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-29 10:04:19 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | -0.076 |  |
| 2026-08-29 10:04:15 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-29 10:04:12 | Nagalagam Street (Kelani Ganga) | 0.20 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-08-29 10:04:06 | Hanwella (Kelani Ganga) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-08-29 10:03:46 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | -0.019 |  |
| 2026-08-29 10:03:43 | Moraketiya (Walawe Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-08-29 10:03:14 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-29 10:02:56 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-08-29 10:02:55 | Dunamale (Aththanagalu Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-08-29 10:02:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.49 | 🟢 Normal | -0.010 |  |
| 2026-08-29 10:02:41 | Galgamuwa (Mee Oya) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-29 10:02:37 | Magura (Kalu Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-08-29 10:02:30 | Deraniyagala (Kelani Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-08-29 10:02:15 | Ellagawa (Kalu Ganga) | 5.26 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-29 10:02:00 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | -0.030 |  |
| 2026-08-29 10:01:47 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | -0.079 |  |
| 2026-08-29 10:01:06 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-29 10:00:51 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-08-29 10:00:47 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-29 10:05:04 | Panadugama (Nilwala Ganga) | 3.36 | 🟢 Normal | 0.136 | 🔺 Rising |
| 2026-08-29 10:05:12 | Pitabeddara (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-29 10:02:15 | Ellagawa (Kalu Ganga) | 5.26 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-29 10:04:30 | Baddegama (Gin Ganga) | 1.70 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-29 10:04:12 | Nagalagam Street (Kelani Ganga) | 0.20 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-08-29 10:04:57 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-29 10:08:12 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-08-29 10:03:14 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-29 10:10:24 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-08-29 10:29:53 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-29 10:02:41 | Galgamuwa (Mee Oya) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-29 10:02:37 | Magura (Kalu Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-08-29 10:04:15 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-29 10:04:06 | Hanwella (Kelani Ganga) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-08-29 10:05:05 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-29 10:07:53 | Glencourse (Kelani Ganga) | 10.18 | 🟢 Normal | 0.000 |  |
| 2026-08-29 10:03:43 | Moraketiya (Walawe Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-08-29 10:10:32 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-29 10:02:55 | Dunamale (Aththanagalu Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-08-29 10:01:06 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-29 10:04:26 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-29 10:06:24 | Badalgama (Maha Oya) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-08-29 10:14:29 | Rathnapura (Kalu Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-08-29 10:06:48 | Thanthirimale (Malwathu Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-29 10:07:14 | Thawalama (Gin Ganga) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-08-29 10:20:05 | Thalgahagoda (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-08-29 10:22:48 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-29 09:07:46 | Thanamalwila (Kirindi Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-29 10:06:27 | Urawa (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-08-29 10:02:56 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-08-29 10:05:32 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-08-29 10:02:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.49 | 🟢 Normal | -0.010 |  |
| 2026-08-29 10:05:06 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | -0.010 |  |
| 2026-08-29 10:02:30 | Deraniyagala (Kelani Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-08-29 10:00:51 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-08-29 10:03:46 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | -0.019 |  |
| 2026-08-29 10:02:00 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | -0.030 |  |
| 2026-08-29 10:04:19 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | -0.076 |  |
| 2026-08-29 10:01:47 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | -0.079 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)