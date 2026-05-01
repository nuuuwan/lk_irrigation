# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--01_23:04:36-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **140,377 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-01 23:04:36 | Panadugama (Nilwala Ganga) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-05-01 23:04:36 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-05-01 23:04:24 | Thalgahagoda (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.065 |  |
| 2026-05-01 23:04:12 | Ellagawa (Kalu Ganga) | 4.60 | 🟢 Normal | -90.000 |  |
| 2026-05-01 23:04:10 | Ellagawa (Kalu Ganga) | 4.65 | 🟢 Normal | -90.000 |  |
| 2026-05-01 23:04:09 | Deraniyagala (Kelani Ganga) | 0.59 | 🟢 Normal | -0.020 |  |
| 2026-05-01 23:04:02 | Thawalama (Gin Ganga) | 1.71 | 🟢 Normal | -0.010 |  |
| 2026-05-01 23:03:27 | Glencourse (Kelani Ganga) | 8.57 | 🟢 Normal | -0.010 |  |
| 2026-05-01 23:03:05 | Badalgama (Maha Oya) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-05-01 23:02:51 | Dunamale (Aththanagalu Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-01 23:02:32 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-01 23:02:28 | Moragaswewa (Deduru Oya) | 0.89 | 🟢 Normal | -0.020 |  |
| 2026-05-01 23:02:27 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | -0.010 |  |
| 2026-05-01 23:02:14 | Manampitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-05-01 23:02:08 | Thanamalwila (Kirindi Oya) | 0.77 | 🟢 Normal | -0.024 |  |
| 2026-05-01 23:02:02 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-05-01 23:02:01 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-05-01 23:01:40 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-01 23:01:34 | Siyambalanduwa (Heda Oya) | 0.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-01 23:01:33 | Peradeniya (Mahaweli Ganga) | 1.36 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-05-01 23:01:31 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-05-01 23:00:54 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-05-01 23:00:34 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | -0.012 |  |
| 2026-05-01 22:36:37 | Thanamalwila (Kirindi Oya) | 0.78 | 🟢 Normal | -0.024 |  |
| 2026-05-01 22:34:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.67 | 🟢 Normal | -0.007 |  |
| 2026-05-01 22:18:18 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.065 |  |
| 2026-05-01 22:15:18 | Putupaula (Kalu Ganga) | 0.83 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-05-01 22:14:02 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-01 22:10:56 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | -0.012 |  |
| 2026-05-01 22:10:50 | Panadugama (Nilwala Ganga) | 1.97 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-01 23:01:33 | Peradeniya (Mahaweli Ganga) | 1.36 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-05-01 23:02:02 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-05-01 22:15:18 | Putupaula (Kalu Ganga) | 0.83 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-05-01 23:01:34 | Siyambalanduwa (Heda Oya) | 0.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-01 23:02:32 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-01 21:00:15 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-01 23:01:40 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-01 23:04:36 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-05-01 18:05:08 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-05-01 22:04:17 | Magura (Kalu Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-01 21:10:47 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-01 22:02:50 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-05-01 23:04:36 | Panadugama (Nilwala Ganga) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-05-01 23:00:54 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-05-01 22:00:49 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-01 23:02:51 | Dunamale (Aththanagalu Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-01 22:14:02 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-01 23:03:05 | Badalgama (Maha Oya) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-05-01 22:06:57 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-01 23:02:14 | Manampitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-05-01 22:05:00 | Rathnapura (Kalu Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-05-01 21:57:42 | Urawa (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-05-01 22:34:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.67 | 🟢 Normal | -0.007 |  |
| 2026-05-01 22:09:06 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | -0.009 |  |
| 2026-05-01 23:02:01 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-05-01 23:04:02 | Thawalama (Gin Ganga) | 1.71 | 🟢 Normal | -0.010 |  |
| 2026-05-01 23:01:31 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-05-01 23:02:27 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | -0.010 |  |
| 2026-05-01 23:03:27 | Glencourse (Kelani Ganga) | 8.57 | 🟢 Normal | -0.010 |  |
| 2026-05-01 18:00:31 | Weraganthota (Mahaweli Ganga) | -3.18 | 🟢 Normal | -0.010 |  |
| 2026-05-01 22:05:14 | Baddegama (Gin Ganga) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-05-01 23:00:34 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | -0.012 |  |
| 2026-05-01 23:04:09 | Deraniyagala (Kelani Ganga) | 0.59 | 🟢 Normal | -0.020 |  |
| 2026-05-01 23:02:28 | Moragaswewa (Deduru Oya) | 0.89 | 🟢 Normal | -0.020 |  |
| 2026-05-01 23:02:08 | Thanamalwila (Kirindi Oya) | 0.77 | 🟢 Normal | -0.024 |  |
| 2026-05-01 18:00:26 | Thanthirimale (Malwathu Oya) | 2.59 | 🟢 Normal | -0.031 |  |
| 2026-05-01 22:03:05 | Norwood (Kelani Ganga) | 0.95 | 🟢 Normal | -0.031 |  |
| 2026-05-01 23:04:24 | Thalgahagoda (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.065 |  |
| 2026-05-01 23:04:12 | Ellagawa (Kalu Ganga) | 4.60 | 🟢 Normal | -90.000 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)