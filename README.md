# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--17_04:45:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **99,470 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-17 04:45:12 | Kuda Oya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-03-17 04:39:23 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-17 04:26:02 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-17 04:09:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.90 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-03-17 04:05:54 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-17 04:05:25 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-03-17 04:04:20 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.093 |  |
| 2026-03-17 04:04:19 | Thawalama (Gin Ganga) | 1.31 | 🟢 Normal | -0.040 |  |
| 2026-03-17 04:03:40 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-03-17 04:03:40 | Glencourse (Kelani Ganga) | 8.56 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-17 04:03:25 | Norwood (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-17 04:03:23 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-17 04:03:22 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-03-17 04:03:05 | Manampitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-17 04:03:01 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-17 04:02:59 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | -0.030 |  |
| 2026-03-17 04:02:53 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | -0.010 |  |
| 2026-03-17 04:02:22 | Magura (Kalu Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-17 04:02:17 | Thanamalwila (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-03-17 04:02:17 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-03-17 04:02:14 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-17 04:01:56 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-17 04:01:46 | Horowpothana (Yan Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-03-17 04:01:30 | Deraniyagala (Kelani Ganga) | 0.30 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-03-17 04:01:26 | Moraketiya (Walawe Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-17 04:01:25 | Ellagawa (Kalu Ganga) | 3.83 | 🟢 Normal | -0.011 |  |
| 2026-03-17 04:00:55 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-03-17 04:00:53 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-03-17 04:00:37 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-17 04:00:33 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.020 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-17 04:09:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.90 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-03-17 04:00:55 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-03-17 04:01:30 | Deraniyagala (Kelani Ganga) | 0.30 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-03-17 00:08:55 | Putupaula (Kalu Ganga) | 0.28 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-03-17 04:03:40 | Glencourse (Kelani Ganga) | 8.56 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-17 03:05:00 | Rathnapura (Kalu Ganga) | 0.45 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-17 03:05:59 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-17 04:00:33 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-17 04:02:17 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-03-17 04:00:53 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-03-17 04:01:56 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-17 04:00:37 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-17 03:12:33 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-17 04:01:46 | Horowpothana (Yan Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-03-16 18:04:59 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-17 04:02:22 | Magura (Kalu Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-17 04:26:02 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-17 04:03:25 | Norwood (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-17 03:19:29 | Padiyathalawa (Maduru Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-17 04:01:26 | Moraketiya (Walawe Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-17 04:03:23 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-17 04:39:23 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-17 04:03:01 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-17 04:05:25 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-03-17 04:03:05 | Manampitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-16 18:01:58 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-17 04:02:14 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-17 04:45:12 | Kuda Oya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-03-17 04:02:17 | Thanamalwila (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-03-17 04:03:40 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-03-17 04:02:53 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | -0.010 |  |
| 2026-03-17 04:03:22 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-03-17 04:01:25 | Ellagawa (Kalu Ganga) | 3.83 | 🟢 Normal | -0.011 |  |
| 2026-03-17 00:07:39 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | -0.016 |  |
| 2026-03-17 04:02:59 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | -0.030 |  |
| 2026-03-17 04:04:19 | Thawalama (Gin Ganga) | 1.31 | 🟢 Normal | -0.040 |  |
| 2026-03-17 04:04:20 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.093 |  |
| 2026-03-16 18:00:13 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | -0.210 |  |
| 2026-03-17 03:02:43 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.256 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)