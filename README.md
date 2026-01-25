# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--25_11:30:56-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **55,199 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-25 11:30:56 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-01-25 11:22:03 | Pitabeddara (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-25 11:21:29 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-25 11:14:31 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-25 11:09:41 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-25 11:08:23 | Magura (Kalu Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-25 11:08:17 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 10.800 | 🔺 Rising |
| 2026-01-25 11:07:57 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 10.800 | 🔺 Rising |
| 2026-01-25 11:07:37 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-01-25 11:07:15 | Deraniyagala (Kelani Ganga) | 0.26 | 🟢 Normal | -0.009 |  |
| 2026-01-25 11:06:36 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-01-25 11:06:34 | Peradeniya (Mahaweli Ganga) | 1.55 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-01-25 11:05:11 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-01-25 11:05:10 | Padiyathalawa (Maduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-25 11:04:27 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.058 |  |
| 2026-01-25 11:04:27 | Thawalama (Gin Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-25 11:04:12 | Putupaula (Kalu Ganga) | 0.29 | 🟢 Normal | -0.114 |  |
| 2026-01-25 11:03:49 | Horowpothana (Yan Oya) | 1.41 | 🟢 Normal | -0.011 |  |
| 2026-01-25 11:03:47 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-25 11:03:44 | Glencourse (Kelani Ganga) | 8.47 | 🟢 Normal | -0.010 |  |
| 2026-01-25 11:03:42 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-01-25 11:03:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.30 | 🟢 Normal | -0.050 |  |
| 2026-01-25 11:03:35 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-25 11:03:30 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.295 | 🔺 Rising |
| 2026-01-25 11:03:08 | Hanwella (Kelani Ganga) | 0.26 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-25 11:02:44 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-01-25 11:02:28 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-25 11:02:24 | Rathnapura (Kalu Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-01-25 11:02:21 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-01-25 11:02:17 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.074 |  |
| 2026-01-25 11:02:11 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-25 11:02:00 | Ellagawa (Kalu Ganga) | 3.79 | 🟢 Normal | -0.010 |  |
| 2026-01-25 11:01:51 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-25 11:01:29 | Thanthirimale (Malwathu Oya) | 1.57 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-01-25 11:01:23 | Yaka Wewa (Ma Oya) | 1.24 | 🟢 Normal | -0.020 |  |
| 2026-01-25 11:01:21 | Manampitiya (Mahaweli Ganga) | 1.07 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-01-25 11:01:06 | Moragaswewa (Deduru Oya) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-01-25 11:00:35 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-01-25 11:00:35 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-25 11:00:14 | Weraganthota (Mahaweli Ganga) | -1.95 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-25 11:08:17 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 10.800 | 🔺 Rising |
| 2026-01-25 11:03:30 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.295 | 🔺 Rising |
| 2026-01-25 11:06:34 | Peradeniya (Mahaweli Ganga) | 1.55 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-01-25 11:01:29 | Thanthirimale (Malwathu Oya) | 1.57 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-01-25 11:01:21 | Manampitiya (Mahaweli Ganga) | 1.07 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-01-25 11:03:08 | Hanwella (Kelani Ganga) | 0.26 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-25 11:00:35 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-25 11:01:51 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-25 11:21:29 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-25 11:03:35 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-25 11:05:11 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-01-25 11:08:23 | Magura (Kalu Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-25 11:22:03 | Pitabeddara (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-25 11:03:42 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-01-25 11:30:56 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-01-25 11:05:10 | Padiyathalawa (Maduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-25 11:02:28 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-25 11:03:47 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-25 11:14:31 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-25 11:00:35 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-01-25 11:02:11 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-25 11:02:21 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-01-25 11:04:27 | Thawalama (Gin Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-25 11:06:36 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-01-25 11:02:44 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-01-25 11:09:41 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-25 11:07:15 | Deraniyagala (Kelani Ganga) | 0.26 | 🟢 Normal | -0.009 |  |
| 2026-01-25 11:01:06 | Moragaswewa (Deduru Oya) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-01-25 11:07:37 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-01-25 11:02:00 | Ellagawa (Kalu Ganga) | 3.79 | 🟢 Normal | -0.010 |  |
| 2026-01-25 11:03:44 | Glencourse (Kelani Ganga) | 8.47 | 🟢 Normal | -0.010 |  |
| 2026-01-25 11:02:24 | Rathnapura (Kalu Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-01-25 11:03:49 | Horowpothana (Yan Oya) | 1.41 | 🟢 Normal | -0.011 |  |
| 2026-01-25 11:00:14 | Weraganthota (Mahaweli Ganga) | -1.95 | 🟢 Normal | -0.020 |  |
| 2026-01-25 11:01:23 | Yaka Wewa (Ma Oya) | 1.24 | 🟢 Normal | -0.020 |  |
| 2026-01-25 11:03:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.30 | 🟢 Normal | -0.050 |  |
| 2026-01-25 11:04:27 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.058 |  |
| 2026-01-25 11:02:17 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.074 |  |
| 2026-01-25 11:04:12 | Putupaula (Kalu Ganga) | 0.29 | 🟢 Normal | -0.114 |  |

## River Water Level Charts by Station

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)