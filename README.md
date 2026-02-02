# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--02_17:12:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **62,630 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-02 17:12:26 | Magura (Kalu Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-02 17:10:19 | Peradeniya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.038 |  |
| 2026-02-02 17:09:52 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-02-02 17:09:33 | Urawa (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-02-02 17:09:05 | Baddegama (Gin Ganga) | 0.97 | 🟢 Normal | -0.022 |  |
| 2026-02-02 17:08:24 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-02-02 17:07:18 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | -0.010 |  |
| 2026-02-02 17:07:17 | Thanamalwila (Kirindi Oya) | 0.48 | 🟢 Normal | -0.012 |  |
| 2026-02-02 17:06:57 | Dunamale (Aththanagalu Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-02-02 17:05:54 | Panadugama (Nilwala Ganga) | 2.21 | 🟢 Normal | 0.000 |  |
| 2026-02-02 17:05:45 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-02-02 17:05:42 | Thanthirimale (Malwathu Oya) | 2.39 | 🟢 Normal | -0.019 |  |
| 2026-02-02 17:05:16 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-02 17:05:04 | Glencourse (Kelani Ganga) | 8.47 | 🟢 Normal | -0.010 |  |
| 2026-02-02 17:04:34 | Thawalama (Gin Ganga) | 1.15 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-02-02 17:04:22 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-02-02 17:04:11 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-02-02 17:03:50 | Deraniyagala (Kelani Ganga) | 0.14 | 🟢 Normal | -0.029 |  |
| 2026-02-02 17:03:33 | Rathnapura (Kalu Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-02-02 17:03:27 | Horowpothana (Yan Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-02 17:03:16 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-02-02 17:02:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.65 | 🟢 Normal | -0.030 |  |
| 2026-02-02 17:02:50 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-02-02 17:02:28 | Pitabeddara (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-02-02 17:02:20 | Weraganthota (Mahaweli Ganga) | -2.46 | 🟢 Normal | -0.079 |  |
| 2026-02-02 17:02:15 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-02 17:02:13 | Yaka Wewa (Ma Oya) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-02-02 17:02:12 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-02-02 17:01:48 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-02-02 17:01:46 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.092 |  |
| 2026-02-02 17:01:42 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-02 17:01:30 | Ellagawa (Kalu Ganga) | 4.31 | 🟢 Normal | -0.021 |  |
| 2026-02-02 17:01:25 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-02 17:01:15 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | -0.074 |  |
| 2026-02-02 17:00:47 | Manampitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.020 |  |
| 2026-02-02 17:00:45 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | -0.020 |  |
| 2026-02-02 17:00:06 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-02 17:09:33 | Urawa (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-02-02 17:04:34 | Thawalama (Gin Ganga) | 1.15 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-02-02 17:03:16 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-02-02 17:09:52 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-02-02 17:08:24 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-02-02 16:16:29 | Galgamuwa (Mee Oya) | 0.40 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-02-02 17:01:25 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-02 17:01:42 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-02 17:00:06 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-02 16:03:24 | Moragaswewa (Deduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-02-02 17:02:15 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-02 17:02:50 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-02-02 17:03:27 | Horowpothana (Yan Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-02 17:12:26 | Magura (Kalu Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-02 17:02:28 | Pitabeddara (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-02-02 17:04:11 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-02-02 17:05:54 | Panadugama (Nilwala Ganga) | 2.21 | 🟢 Normal | 0.000 |  |
| 2026-02-02 17:05:16 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-02 17:04:22 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-02-02 17:05:45 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-02-02 17:01:48 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-02-02 17:07:18 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | -0.010 |  |
| 2026-02-02 17:05:04 | Glencourse (Kelani Ganga) | 8.47 | 🟢 Normal | -0.010 |  |
| 2026-02-02 17:02:13 | Yaka Wewa (Ma Oya) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-02-02 17:02:12 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-02-02 17:06:57 | Dunamale (Aththanagalu Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-02-02 17:03:33 | Rathnapura (Kalu Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-02-02 17:07:17 | Thanamalwila (Kirindi Oya) | 0.48 | 🟢 Normal | -0.012 |  |
| 2026-02-02 17:05:42 | Thanthirimale (Malwathu Oya) | 2.39 | 🟢 Normal | -0.019 |  |
| 2026-02-02 17:00:47 | Manampitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.020 |  |
| 2026-02-02 17:00:45 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | -0.020 |  |
| 2026-02-02 17:01:30 | Ellagawa (Kalu Ganga) | 4.31 | 🟢 Normal | -0.021 |  |
| 2026-02-02 17:09:05 | Baddegama (Gin Ganga) | 0.97 | 🟢 Normal | -0.022 |  |
| 2026-02-02 17:03:50 | Deraniyagala (Kelani Ganga) | 0.14 | 🟢 Normal | -0.029 |  |
| 2026-02-02 17:02:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.65 | 🟢 Normal | -0.030 |  |
| 2026-02-02 17:10:19 | Peradeniya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.038 |  |
| 2026-02-02 17:01:15 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | -0.074 |  |
| 2026-02-02 17:02:20 | Weraganthota (Mahaweli Ganga) | -2.46 | 🟢 Normal | -0.079 |  |
| 2026-02-02 17:01:46 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.092 |  |

## River Water Level Charts by Station

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)