# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--21_21:22:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **79,398 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-21 21:22:49 | Padiyathalawa (Maduru Oya) | 1.35 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-02-21 21:20:14 | Urawa (Nilwala Ganga) | 1.58 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-02-21 21:19:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.06 | 🟢 Normal | -0.016 |  |
| 2026-02-21 21:19:00 | Panadugama (Nilwala Ganga) | 3.11 | 🟢 Normal | 0.219 | 🔺 Rising |
| 2026-02-21 21:15:58 | Ellagawa (Kalu Ganga) | 5.05 | 🟢 Normal | 0.627 | 🔺 Rising |
| 2026-02-21 21:10:46 | Thawalama (Gin Ganga) | 1.43 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-02-21 21:08:55 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-21 21:08:13 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | 0.154 | 🔺 Rising |
| 2026-02-21 21:07:34 | Thaldena (Mahaweli Ganga) | 1.67 | 🟢 Normal | 2.704 | 🔺 Rising |
| 2026-02-21 21:07:00 | Glencourse (Kelani Ganga) | 9.26 | 🟢 Normal | 0.414 | 🔺 Rising |
| 2026-02-21 21:06:59 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.152 |  |
| 2026-02-21 21:06:12 | Moraketiya (Walawe Ganga) | 1.78 | 🟢 Normal | -0.146 |  |
| 2026-02-21 21:06:01 | Holombuwa (Kelani Ganga) | 1.71 | 🟢 Normal | 1.447 | 🔺 Rising |
| 2026-02-21 21:05:28 | Thalgahagoda (Nilwala Ganga) | 0.76 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-21 21:05:21 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-21 21:05:16 | Manampitiya (Mahaweli Ganga) | 2.15 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-02-21 21:04:53 | Deraniyagala (Kelani Ganga) | 1.38 | 🟢 Normal | -0.300 |  |
| 2026-02-21 21:04:33 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.110 |  |
| 2026-02-21 21:04:22 | Pitabeddara (Nilwala Ganga) | 1.70 | 🟢 Normal | 0.146 | 🔺 Rising |
| 2026-02-21 21:04:20 | Wellawaya (Kirindi Oya) | 1.42 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-02-21 21:04:17 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-02-21 21:04:06 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-02-21 21:04:05 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-21 21:04:00 | Rathnapura (Kalu Ganga) | 4.56 | 🟢 Normal | 0.955 | 🔺 Rising |
| 2026-02-21 21:03:16 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-21 21:03:10 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-21 21:02:59 | Peradeniya (Mahaweli Ganga) | 4.20 | 🟢 Normal | 0.431 | 🔺 Rising |
| 2026-02-21 21:02:55 | Nakkala (Kumbukkan Oya) | 3.60 | 🟢 Normal | -0.765 |  |
| 2026-02-21 21:02:55 | Norwood (Kelani Ganga) | 1.36 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-02-21 21:02:52 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-21 21:02:45 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-21 21:02:43 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-02-21 21:02:21 | Magura (Kalu Ganga) | 1.20 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-02-21 21:02:01 | Nawalapitiya (Mahaweli Ganga) | 1.74 | 🟢 Normal | 0.286 | 🔺 Rising |
| 2026-02-21 21:01:40 | Horowpothana (Yan Oya) | 1.57 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-21 21:01:40 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-21 21:00:28 | Thaldena (Mahaweli Ganga) | 1.35 | 🟢 Normal | 2.704 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-21 21:07:34 | Thaldena (Mahaweli Ganga) | 1.67 | 🟢 Normal | 2.704 | 🔺 Rising |
| 2026-02-21 21:06:01 | Holombuwa (Kelani Ganga) | 1.71 | 🟢 Normal | 1.447 | 🔺 Rising |
| 2026-02-21 21:04:00 | Rathnapura (Kalu Ganga) | 4.56 | 🟢 Normal | 0.955 | 🔺 Rising |
| 2026-02-21 21:15:58 | Ellagawa (Kalu Ganga) | 5.05 | 🟢 Normal | 0.627 | 🔺 Rising |
| 2026-02-21 21:02:59 | Peradeniya (Mahaweli Ganga) | 4.20 | 🟢 Normal | 0.431 | 🔺 Rising |
| 2026-02-21 21:07:00 | Glencourse (Kelani Ganga) | 9.26 | 🟢 Normal | 0.414 | 🔺 Rising |
| 2026-02-21 21:02:01 | Nawalapitiya (Mahaweli Ganga) | 1.74 | 🟢 Normal | 0.286 | 🔺 Rising |
| 2026-02-21 21:19:00 | Panadugama (Nilwala Ganga) | 3.11 | 🟢 Normal | 0.219 | 🔺 Rising |
| 2026-02-21 21:08:13 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | 0.154 | 🔺 Rising |
| 2026-02-21 21:04:22 | Pitabeddara (Nilwala Ganga) | 1.70 | 🟢 Normal | 0.146 | 🔺 Rising |
| 2026-02-21 21:02:43 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-02-21 21:10:46 | Thawalama (Gin Ganga) | 1.43 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-02-21 21:20:14 | Urawa (Nilwala Ganga) | 1.58 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-02-21 21:04:20 | Wellawaya (Kirindi Oya) | 1.42 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-02-21 21:05:16 | Manampitiya (Mahaweli Ganga) | 2.15 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-02-21 21:02:55 | Norwood (Kelani Ganga) | 1.36 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-02-21 21:02:21 | Magura (Kalu Ganga) | 1.20 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-02-21 21:04:05 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-21 21:03:16 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-21 21:05:28 | Thalgahagoda (Nilwala Ganga) | 0.76 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-21 21:22:49 | Padiyathalawa (Maduru Oya) | 1.35 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-02-21 21:01:40 | Horowpothana (Yan Oya) | 1.57 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-21 21:03:10 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-21 18:05:22 | Thanthirimale (Malwathu Oya) | 1.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-21 21:04:17 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-02-21 21:08:55 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-21 21:01:40 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-21 21:02:52 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-21 18:03:47 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-21 21:05:21 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-21 21:02:45 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-21 21:04:06 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-02-21 21:19:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.06 | 🟢 Normal | -0.016 |  |
| 2026-02-21 18:03:01 | Weraganthota (Mahaweli Ganga) | -1.88 | 🟢 Normal | -0.020 |  |
| 2026-02-21 21:04:33 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.110 |  |
| 2026-02-21 21:06:12 | Moraketiya (Walawe Ganga) | 1.78 | 🟢 Normal | -0.146 |  |
| 2026-02-21 21:06:59 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.152 |  |
| 2026-02-21 21:04:53 | Deraniyagala (Kelani Ganga) | 1.38 | 🟢 Normal | -0.300 |  |
| 2026-02-21 21:02:55 | Nakkala (Kumbukkan Oya) | 3.60 | 🟢 Normal | -0.765 |  |

## River Water Level Charts by Station

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)