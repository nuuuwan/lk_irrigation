# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--26_09:14:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **56,005 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-26 09:14:53 | Dunamale (Aththanagalu Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-26 09:10:57 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.023 |  |
| 2026-01-26 09:08:59 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | -0.010 |  |
| 2026-01-26 09:08:43 | Ellagawa (Kalu Ganga) | 3.92 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-26 09:07:41 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-01-26 09:07:19 | Magura (Kalu Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-26 09:06:58 | Panadugama (Nilwala Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-01-26 09:06:53 | Padiyathalawa (Maduru Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-26 09:05:35 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-26 09:05:32 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-26 09:05:21 | Thanamalwila (Kirindi Oya) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-01-26 09:04:29 | Padiyathalawa (Maduru Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-26 09:04:25 | Glencourse (Kelani Ganga) | 8.35 | 🟢 Normal | -0.050 |  |
| 2026-01-26 09:04:18 | Horowpothana (Yan Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-01-26 09:04:09 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-26 09:04:00 | Manampitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | -0.049 |  |
| 2026-01-26 09:03:53 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-01-26 09:03:39 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-26 09:03:35 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.089 |  |
| 2026-01-26 09:03:27 | Rathnapura (Kalu Ganga) | 0.72 | 🟢 Normal | -0.021 |  |
| 2026-01-26 09:03:22 | Thawalama (Gin Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-01-26 09:03:17 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-26 09:03:14 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-26 09:03:07 | Putupaula (Kalu Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-26 09:02:50 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-26 09:02:39 | Hanwella (Kelani Ganga) | 0.30 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-26 09:02:38 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-01-26 09:02:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.74 | 🟢 Normal | -0.035 |  |
| 2026-01-26 09:02:22 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-01-26 09:02:21 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-01-26 09:01:59 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-26 09:01:58 | Pitabeddara (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-01-26 09:01:54 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-01-26 09:01:40 | Thanthirimale (Malwathu Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-01-26 09:01:28 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-01-26 09:01:25 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-01-26 09:01:20 | Yaka Wewa (Ma Oya) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-01-26 09:01:15 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-26 09:01:12 | Weraganthota (Mahaweli Ganga) | -1.85 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-01-26 09:00:42 | Moragaswewa (Deduru Oya) | 0.31 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-26 09:02:22 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-01-26 09:01:25 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-01-26 09:01:12 | Weraganthota (Mahaweli Ganga) | -1.85 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-01-26 09:02:39 | Hanwella (Kelani Ganga) | 0.30 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-26 09:01:15 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-26 09:03:17 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-26 09:08:43 | Ellagawa (Kalu Ganga) | 3.92 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-26 09:05:35 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-26 09:03:14 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-26 09:00:42 | Moragaswewa (Deduru Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-26 09:02:50 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-26 09:03:39 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-26 09:04:18 | Horowpothana (Yan Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-01-26 09:07:41 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-01-26 09:07:19 | Magura (Kalu Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-26 09:01:58 | Pitabeddara (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-01-26 09:04:09 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-26 09:03:53 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-01-26 09:06:58 | Panadugama (Nilwala Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-01-26 09:06:53 | Padiyathalawa (Maduru Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-26 09:01:59 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-26 09:14:53 | Dunamale (Aththanagalu Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-26 09:02:38 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-01-26 09:03:07 | Putupaula (Kalu Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-26 09:01:54 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-01-26 09:05:32 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-26 09:01:40 | Thanthirimale (Malwathu Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-01-26 09:03:22 | Thawalama (Gin Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-01-26 09:05:21 | Thanamalwila (Kirindi Oya) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-01-26 09:02:21 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-01-26 09:01:28 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-01-26 09:08:59 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | -0.010 |  |
| 2026-01-26 09:01:20 | Yaka Wewa (Ma Oya) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-01-26 09:03:27 | Rathnapura (Kalu Ganga) | 0.72 | 🟢 Normal | -0.021 |  |
| 2026-01-26 09:10:57 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.023 |  |
| 2026-01-26 09:02:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.74 | 🟢 Normal | -0.035 |  |
| 2026-01-26 09:04:00 | Manampitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | -0.049 |  |
| 2026-01-26 09:04:25 | Glencourse (Kelani Ganga) | 8.35 | 🟢 Normal | -0.050 |  |
| 2026-01-26 09:03:35 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.089 |  |

## River Water Level Charts by Station

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)