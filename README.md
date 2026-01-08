# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--08_06:09:43-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **39,718 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **44** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-08 06:09:43 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | -0.009 |  |
| 2026-01-08 06:08:37 | Panadugama (Nilwala Ganga) | 3.94 | 🟢 Normal | -0.057 |  |
| 2026-01-08 06:07:15 | Dunamale (Aththanagalu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-01-08 06:06:37 | Padiyathalawa (Maduru Oya) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-01-08 06:06:03 | Manampitiya (Mahaweli Ganga) | 2.47 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-01-08 06:06:02 | Thanamalwila (Kirindi Oya) | 1.06 | 🟢 Normal | -0.019 |  |
| 2026-01-08 06:05:57 | Siyambalanduwa (Heda Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-01-08 06:05:43 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-08 06:05:28 | Ellagawa (Kalu Ganga) | 4.16 | 🟢 Normal | -0.010 |  |
| 2026-01-08 06:04:39 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -3.919 |  |
| 2026-01-08 06:04:38 | Urawa (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.337 |  |
| 2026-01-08 06:04:37 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | -0.013 |  |
| 2026-01-08 06:04:36 | Deraniyagala (Kelani Ganga) | 0.22 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-01-08 06:04:35 | Glencourse (Kelani Ganga) | 8.64 | 🟢 Normal | -0.053 |  |
| 2026-01-08 06:04:30 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-08 06:04:27 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-08 06:04:17 | Katharagama (Menik Ganga) | 0.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-08 06:04:11 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -3.919 |  |
| 2026-01-08 06:02:33 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-08 06:02:28 | Badalgama (Maha Oya) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-01-08 06:02:25 | Thaldena (Mahaweli Ganga) | 0.85 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-08 06:02:22 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-01-08 06:02:12 | Moragaswewa (Deduru Oya) | 0.52 | 🟢 Normal | -0.012 |  |
| 2026-01-08 06:02:10 | Nakkala (Kumbukkan Oya) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-01-08 06:02:07 | Magura (Kalu Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-08 06:01:52 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-08 06:01:49 | Weraganthota (Mahaweli Ganga) | -1.15 | 🟢 Normal | 0.000 |  |
| 2026-01-08 06:01:42 | Rathnapura (Kalu Ganga) | 0.74 | 🟢 Normal | -0.013 |  |
| 2026-01-08 06:01:32 | Horowpothana (Yan Oya) | 2.35 | 🟢 Normal | 0.000 |  |
| 2026-01-08 06:01:24 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-08 06:01:24 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-01-08 06:00:54 | Nawalapitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-08 06:00:31 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-01-08 06:00:14 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.167 |  |
| 2026-01-08 06:00:11 | Pitabeddara (Nilwala Ganga) | 1.35 | 🟢 Normal | -0.133 |  |
| 2026-01-08 05:41:30 | Urawa (Nilwala Ganga) | 0.71 | 🟢 Normal | -0.337 |  |
| 2026-01-08 05:35:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.84 | 🟢 Normal | 12.706 | 🔺 Rising |
| 2026-01-08 05:35:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.78 | 🟢 Normal | 12.706 | 🔺 Rising |
| 2026-01-08 05:35:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.72 | 🟢 Normal | 12.706 | 🔺 Rising |
| 2026-01-08 05:34:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.68 | 🟢 Normal | 12.706 | 🔺 Rising |
| 2026-01-08 05:20:34 | Magura (Kalu Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-08 05:16:40 | Yaka Wewa (Ma Oya) | 0.79 | 🟢 Normal | -0.013 |  |
| 2026-01-08 05:16:07 | Putupaula (Kalu Ganga) | 0.74 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-01-08 05:14:35 | Rathnapura (Kalu Ganga) | 0.75 | 🟢 Normal | -0.013 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-08 05:35:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.84 | 🟢 Normal | 12.706 | 🔺 Rising |
| 2026-01-08 06:06:03 | Manampitiya (Mahaweli Ganga) | 2.47 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-01-08 06:01:24 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-01-08 06:04:36 | Deraniyagala (Kelani Ganga) | 0.22 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-01-08 06:02:25 | Thaldena (Mahaweli Ganga) | 0.85 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-08 05:12:14 | Thalgahagoda (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-01-08 04:08:04 | Thawalama (Gin Ganga) | 1.31 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-08 06:01:52 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-08 06:02:33 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-08 06:04:17 | Katharagama (Menik Ganga) | 0.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-08 06:01:49 | Weraganthota (Mahaweli Ganga) | -1.15 | 🟢 Normal | 0.000 |  |
| 2026-01-08 06:00:54 | Nawalapitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-08 06:01:32 | Horowpothana (Yan Oya) | 2.35 | 🟢 Normal | 0.000 |  |
| 2026-01-07 18:01:21 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-01-08 06:02:07 | Magura (Kalu Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-08 06:04:30 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-08 06:02:22 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-01-08 06:05:43 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-08 06:01:24 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-08 06:05:57 | Siyambalanduwa (Heda Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-01-08 06:07:15 | Dunamale (Aththanagalu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-01-08 06:02:28 | Badalgama (Maha Oya) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-01-08 06:04:27 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-08 06:09:43 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | -0.009 |  |
| 2026-01-08 06:05:28 | Ellagawa (Kalu Ganga) | 4.16 | 🟢 Normal | -0.010 |  |
| 2026-01-08 06:02:10 | Nakkala (Kumbukkan Oya) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-01-08 06:06:37 | Padiyathalawa (Maduru Oya) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-01-08 06:00:31 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-01-08 06:02:12 | Moragaswewa (Deduru Oya) | 0.52 | 🟢 Normal | -0.012 |  |
| 2026-01-08 06:04:37 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | -0.013 |  |
| 2026-01-08 06:01:42 | Rathnapura (Kalu Ganga) | 0.74 | 🟢 Normal | -0.013 |  |
| 2026-01-08 06:06:02 | Thanamalwila (Kirindi Oya) | 1.06 | 🟢 Normal | -0.019 |  |
| 2026-01-07 18:03:25 | Thanthirimale (Malwathu Oya) | 1.77 | 🟢 Normal | -0.023 |  |
| 2026-01-08 06:04:35 | Glencourse (Kelani Ganga) | 8.64 | 🟢 Normal | -0.053 |  |
| 2026-01-08 06:08:37 | Panadugama (Nilwala Ganga) | 3.94 | 🟢 Normal | -0.057 |  |
| 2026-01-08 06:00:11 | Pitabeddara (Nilwala Ganga) | 1.35 | 🟢 Normal | -0.133 |  |
| 2026-01-08 06:00:14 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.167 |  |
| 2026-01-08 06:04:38 | Urawa (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.337 |  |
| 2026-01-08 06:04:39 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -3.919 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)