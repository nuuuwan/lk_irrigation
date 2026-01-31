# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--31_12:37:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **60,610 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-31 12:37:10 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-31 12:07:42 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-01-31 12:06:48 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-01-31 12:05:53 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-01-31 12:04:52 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-31 12:04:51 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-01-31 12:04:50 | Manampitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-01-31 12:04:38 | Thawalama (Gin Ganga) | 0.90 | 🟢 Normal | -0.049 |  |
| 2026-01-31 12:04:33 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | -0.010 |  |
| 2026-01-31 12:04:18 | Thaldena (Mahaweli Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-01-31 12:04:00 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-31 12:03:52 | Putupaula (Kalu Ganga) | 0.48 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-01-31 12:03:51 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-01-31 12:03:46 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-01-31 12:03:35 | Magura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-31 12:03:21 | Katharagama (Menik Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-01-31 12:03:09 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | -0.020 |  |
| 2026-01-31 12:03:01 | Rathnapura (Kalu Ganga) | 0.54 | 🟢 Normal | -2.250 |  |
| 2026-01-31 12:02:52 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-01-31 12:02:43 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-01-31 12:02:35 | Padiyathalawa (Maduru Oya) | 0.94 | 🟢 Normal | -0.063 |  |
| 2026-01-31 12:02:32 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-31 12:02:29 | Rathnapura (Kalu Ganga) | 0.56 | 🟢 Normal | -2.250 |  |
| 2026-01-31 12:02:28 | Horowpothana (Yan Oya) | 1.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-31 12:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-01-31 12:02:16 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-01-31 12:02:15 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-31 12:02:15 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-31 12:02:14 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-31 12:02:11 | Peradeniya (Mahaweli Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-01-31 12:02:11 | Ellagawa (Kalu Ganga) | 3.77 | 🟢 Normal | 0.000 |  |
| 2026-01-31 12:02:04 | Thanamalwila (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-31 12:02:03 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | -0.050 |  |
| 2026-01-31 12:01:53 | Thanthirimale (Malwathu Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-01-31 12:01:22 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-01-31 12:01:14 | Moragaswewa (Deduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-01-31 12:01:12 | Thanthirimale (Malwathu Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-01-31 12:01:10 | Nakkala (Kumbukkan Oya) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-01-31 12:00:40 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-31 12:00:20 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-01-31 12:00:12 | Weraganthota (Mahaweli Ganga) | -1.57 | 🟢 Normal | -0.021 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-31 12:04:50 | Manampitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-01-31 12:03:52 | Putupaula (Kalu Ganga) | 0.48 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-01-31 12:03:51 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-01-31 12:03:46 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-01-31 12:07:42 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-01-31 12:00:40 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-31 12:02:28 | Horowpothana (Yan Oya) | 1.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-31 12:02:32 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-31 12:01:14 | Moragaswewa (Deduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-01-31 12:04:00 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-31 12:37:10 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-31 12:04:52 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-31 12:03:35 | Magura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-31 12:01:22 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-01-31 12:02:15 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-31 12:02:11 | Ellagawa (Kalu Ganga) | 3.77 | 🟢 Normal | 0.000 |  |
| 2026-01-31 12:02:14 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-31 12:05:53 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-01-31 12:00:20 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-01-31 12:02:15 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-31 12:03:21 | Katharagama (Menik Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-01-31 12:06:48 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-01-31 12:01:53 | Thanthirimale (Malwathu Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-01-31 12:02:11 | Peradeniya (Mahaweli Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-01-31 12:04:51 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-01-31 12:02:52 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-01-31 12:02:43 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-01-31 12:02:04 | Thanamalwila (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-31 12:02:16 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-01-31 12:04:18 | Thaldena (Mahaweli Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-01-31 12:04:33 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | -0.010 |  |
| 2026-01-31 12:01:10 | Nakkala (Kumbukkan Oya) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-01-31 12:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-01-31 12:03:09 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | -0.020 |  |
| 2026-01-31 12:00:12 | Weraganthota (Mahaweli Ganga) | -1.57 | 🟢 Normal | -0.021 |  |
| 2026-01-31 12:04:38 | Thawalama (Gin Ganga) | 0.90 | 🟢 Normal | -0.049 |  |
| 2026-01-31 12:02:03 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | -0.050 |  |
| 2026-01-31 12:02:35 | Padiyathalawa (Maduru Oya) | 0.94 | 🟢 Normal | -0.063 |  |
| 2026-01-31 12:03:01 | Rathnapura (Kalu Ganga) | 0.54 | 🟢 Normal | -2.250 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)