# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--05_23:34:45-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **37,696 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-05 23:34:45 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-05 23:11:37 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-01-05 23:10:52 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | -0.054 |  |
| 2026-01-05 23:10:27 | Panadugama (Nilwala Ganga) | 2.41 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-01-05 23:10:12 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-01-05 23:08:33 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-01-05 23:07:44 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-01-05 23:06:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.70 | 🟢 Normal | 0.154 | 🔺 Rising |
| 2026-01-05 23:06:51 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-05 23:06:06 | Magura (Kalu Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-05 23:04:45 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-05 23:04:27 | Dunamale (Aththanagalu Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-05 23:04:16 | Baddegama (Gin Ganga) | 1.02 | 🟢 Normal | -0.020 |  |
| 2026-01-05 23:03:52 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | -0.019 |  |
| 2026-01-05 23:03:48 | Padiyathalawa (Maduru Oya) | 2.00 | 🟢 Normal | -0.518 |  |
| 2026-01-05 23:03:33 | Thawalama (Gin Ganga) | 1.46 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-01-05 23:03:17 | Horowpothana (Yan Oya) | 1.49 | 🟢 Normal | 0.005 |  |
| 2026-01-05 23:03:12 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-05 23:03:01 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-05 23:02:37 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-05 23:02:37 | Thanamalwila (Kirindi Oya) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-01-05 23:02:06 | Wellawaya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.263 | 🔺 Rising |
| 2026-01-05 23:01:56 | Glencourse (Kelani Ganga) | 8.56 | 🟢 Normal | -0.020 |  |
| 2026-01-05 23:01:51 | Yaka Wewa (Ma Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-05 23:01:27 | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | -0.010 |  |
| 2026-01-05 23:01:21 | Peradeniya (Mahaweli Ganga) | 2.75 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-01-05 23:01:14 | Thaldena (Mahaweli Ganga) | 0.82 | 🟢 Normal | -0.031 |  |
| 2026-01-05 23:00:55 | Manampitiya (Mahaweli Ganga) | 1.98 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-01-05 23:00:45 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-05 23:00:11 | Kithulgala (Kelani Ganga) | 1.64 | 🟢 Normal | -0.021 |  |
| 2026-01-05 23:00:10 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-05 23:02:06 | Wellawaya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.263 | 🔺 Rising |
| 2026-01-05 23:06:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.70 | 🟢 Normal | 0.154 | 🔺 Rising |
| 2026-01-05 18:04:03 | Weraganthota (Mahaweli Ganga) | -1.35 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-01-05 23:01:21 | Peradeniya (Mahaweli Ganga) | 2.75 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-01-05 23:00:55 | Manampitiya (Mahaweli Ganga) | 1.98 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-01-05 22:11:05 | Urawa (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-01-05 23:03:33 | Thawalama (Gin Ganga) | 1.46 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-01-05 22:28:34 | Pitabeddara (Nilwala Ganga) | 0.71 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-01-05 23:03:01 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-05 22:04:59 | Rathnapura (Kalu Ganga) | 0.82 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-05 23:08:33 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-01-05 23:10:27 | Panadugama (Nilwala Ganga) | 2.41 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-01-05 23:11:37 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-01-05 23:06:51 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-05 23:02:37 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-05 23:03:17 | Horowpothana (Yan Oya) | 1.49 | 🟢 Normal | 0.005 |  |
| 2026-01-05 22:12:48 | Moragaswewa (Deduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-01-05 23:00:45 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-05 23:01:51 | Yaka Wewa (Ma Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-05 23:04:45 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-05 18:12:56 | Galgamuwa (Mee Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-01-05 23:06:06 | Magura (Kalu Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-05 23:07:44 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-01-05 23:00:10 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-05 23:04:27 | Dunamale (Aththanagalu Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-05 23:34:45 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-05 23:03:12 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-05 23:02:37 | Thanamalwila (Kirindi Oya) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-01-05 23:10:12 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-01-05 23:01:27 | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | -0.010 |  |
| 2026-01-05 18:04:30 | Thanthirimale (Malwathu Oya) | 1.43 | 🟢 Normal | -0.011 |  |
| 2026-01-05 23:03:52 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | -0.019 |  |
| 2026-01-05 23:04:16 | Baddegama (Gin Ganga) | 1.02 | 🟢 Normal | -0.020 |  |
| 2026-01-05 23:01:56 | Glencourse (Kelani Ganga) | 8.56 | 🟢 Normal | -0.020 |  |
| 2026-01-05 23:00:11 | Kithulgala (Kelani Ganga) | 1.64 | 🟢 Normal | -0.021 |  |
| 2026-01-05 23:01:14 | Thaldena (Mahaweli Ganga) | 0.82 | 🟢 Normal | -0.031 |  |
| 2026-01-05 22:29:04 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.034 |  |
| 2026-01-05 23:10:52 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | -0.054 |  |
| 2026-01-05 23:03:48 | Padiyathalawa (Maduru Oya) | 2.00 | 🟢 Normal | -0.518 |  |

## River Water Level Charts by Station

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)