# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--21_16:34:39-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **103,532 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-21 16:34:39 | Panadugama (Nilwala Ganga) | 2.01 | 🟢 Normal | -0.007 |  |
| 2026-03-21 16:10:19 | Rathnapura (Kalu Ganga) | 0.54 | 🟢 Normal | -0.009 |  |
| 2026-03-21 16:09:11 | Glencourse (Kelani Ganga) | 8.48 | 🟢 Normal | 0.000 |  |
| 2026-03-21 16:09:10 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-03-21 16:07:25 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-03-21 16:07:13 | Thanamalwila (Kirindi Oya) | 0.58 | 🟢 Normal | -0.018 |  |
| 2026-03-21 16:07:04 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-21 16:06:54 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-03-21 16:06:23 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-21 16:06:11 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-03-21 16:05:57 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-21 16:05:52 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | -0.058 |  |
| 2026-03-21 16:05:44 | Thawalama (Gin Ganga) | 1.35 | 🟢 Normal | -0.028 |  |
| 2026-03-21 16:05:15 | Peradeniya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-03-21 16:04:47 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | -0.010 |  |
| 2026-03-21 16:04:05 | Padiyathalawa (Maduru Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-03-21 16:03:46 | Hanwella (Kelani Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-03-21 16:03:33 | Glencourse (Kelani Ganga) | 8.48 | 🟢 Normal | 0.000 |  |
| 2026-03-21 16:03:23 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-21 16:03:00 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-03-21 16:02:45 | Weraganthota (Mahaweli Ganga) | -2.74 | 🟢 Normal | -0.089 |  |
| 2026-03-21 16:02:45 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-03-21 16:02:34 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-03-21 16:02:34 | Kithulgala (Kelani Ganga) | 1.38 | 🟢 Normal | -0.010 |  |
| 2026-03-21 16:02:33 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-21 16:02:24 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2026-03-21 16:02:19 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-03-21 16:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.34 | 🟢 Normal | -0.020 |  |
| 2026-03-21 16:02:05 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-21 16:02:00 | Nawalapitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-03-21 16:01:52 | Magura (Kalu Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-21 16:01:50 | Manampitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-03-21 16:01:42 | Thanthirimale (Malwathu Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-03-21 16:01:30 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-03-21 16:01:13 | Wellawaya (Kirindi Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-03-21 16:01:10 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-21 16:01:08 | Ellagawa (Kalu Ganga) | 3.98 | 🟢 Normal | 0.000 |  |
| 2026-03-21 16:00:50 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-03-21 16:00:33 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-21 16:00:27 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-21 15:57:30 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-21 16:02:24 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2026-03-21 16:01:50 | Manampitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-03-21 16:09:10 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-03-21 16:00:33 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-21 16:03:23 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-21 16:00:27 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-21 16:01:10 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-21 16:02:05 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-21 16:07:25 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-03-21 16:00:50 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-03-21 16:02:33 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-21 16:01:52 | Magura (Kalu Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-21 16:06:54 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-03-21 16:01:08 | Ellagawa (Kalu Ganga) | 3.98 | 🟢 Normal | 0.000 |  |
| 2026-03-21 16:04:05 | Padiyathalawa (Maduru Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-03-21 16:06:11 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-03-21 16:09:11 | Glencourse (Kelani Ganga) | 8.48 | 🟢 Normal | 0.000 |  |
| 2026-03-21 16:05:57 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-21 16:02:19 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-03-21 16:06:23 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-21 16:01:42 | Thanthirimale (Malwathu Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-03-21 16:05:15 | Peradeniya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-03-21 16:07:04 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-21 16:01:30 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-03-21 16:34:39 | Panadugama (Nilwala Ganga) | 2.01 | 🟢 Normal | -0.007 |  |
| 2026-03-21 16:10:19 | Rathnapura (Kalu Ganga) | 0.54 | 🟢 Normal | -0.009 |  |
| 2026-03-21 16:04:47 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | -0.010 |  |
| 2026-03-21 16:03:00 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-03-21 16:03:46 | Hanwella (Kelani Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-03-21 16:02:34 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-03-21 16:02:34 | Kithulgala (Kelani Ganga) | 1.38 | 🟢 Normal | -0.010 |  |
| 2026-03-21 16:02:00 | Nawalapitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-03-21 16:02:45 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-03-21 16:01:13 | Wellawaya (Kirindi Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-03-21 16:07:13 | Thanamalwila (Kirindi Oya) | 0.58 | 🟢 Normal | -0.018 |  |
| 2026-03-21 16:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.34 | 🟢 Normal | -0.020 |  |
| 2026-03-21 16:05:44 | Thawalama (Gin Ganga) | 1.35 | 🟢 Normal | -0.028 |  |
| 2026-03-21 16:05:52 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | -0.058 |  |
| 2026-03-21 16:02:45 | Weraganthota (Mahaweli Ganga) | -2.74 | 🟢 Normal | -0.089 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)