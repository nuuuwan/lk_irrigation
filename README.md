# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--12_16:06:01-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **149,925 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-12 16:06:01 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-12 16:05:58 | Urawa (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.021 |  |
| 2026-05-12 16:05:50 | Baddegama (Gin Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-05-12 16:05:41 | Magura (Kalu Ganga) | 2.27 | 🟢 Normal | -0.021 |  |
| 2026-05-12 16:05:36 | Badalgama (Maha Oya) | 2.73 | 🟢 Normal | -0.010 |  |
| 2026-05-12 16:05:36 | Siyambalanduwa (Heda Oya) | 0.66 | 🟢 Normal | -0.019 |  |
| 2026-05-12 16:05:01 | Galgamuwa (Mee Oya) | 1.64 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-12 16:04:40 | Katharagama (Menik Ganga) | 1.99 | 🟢 Normal | -0.020 |  |
| 2026-05-12 16:04:20 | Rathnapura (Kalu Ganga) | 1.93 | 🟢 Normal | 0.262 | 🔺 Rising |
| 2026-05-12 16:04:08 | Panadugama (Nilwala Ganga) | 3.52 | 🟢 Normal | 0.238 | 🔺 Rising |
| 2026-05-12 16:03:58 | Hanwella (Kelani Ganga) | 1.76 | 🟢 Normal | -0.020 |  |
| 2026-05-12 16:03:50 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | -0.048 |  |
| 2026-05-12 16:03:43 | Thanthirimale (Malwathu Oya) | 3.40 | 🟢 Normal | 0.000 |  |
| 2026-05-12 16:03:35 | Weraganthota (Mahaweli Ganga) | -2.87 | 🟢 Normal | -0.039 |  |
| 2026-05-12 16:03:27 | Deraniyagala (Kelani Ganga) | 0.96 | 🟢 Normal | 0.263 | 🔺 Rising |
| 2026-05-12 16:03:07 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.019 |  |
| 2026-05-12 16:02:49 | Dunamale (Aththanagalu Oya) | 1.50 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-05-12 16:02:28 | Kuda Oya (Kirindi Oya) | 1.94 | 🟢 Normal | -0.010 |  |
| 2026-05-12 16:02:27 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-05-12 16:02:23 | Thalgahagoda (Nilwala Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-12 16:02:07 | Moragaswewa (Deduru Oya) | 2.08 | 🟢 Normal | -0.129 |  |
| 2026-05-12 16:02:00 | Nawalapitiya (Mahaweli Ganga) | 0.95 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-12 16:01:55 | Horowpothana (Yan Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-05-12 16:01:52 | Pitabeddara (Nilwala Ganga) | 1.85 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-05-12 16:01:51 | Giriulla (Maha Oya) | 1.53 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-12 16:01:28 | Ellagawa (Kalu Ganga) | 5.59 | 🟢 Normal | -0.030 |  |
| 2026-05-12 16:00:49 | Manampitiya (Mahaweli Ganga) | 0.92 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-05-12 16:00:47 | Padiyathalawa (Maduru Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-12 16:00:21 | Wellawaya (Kirindi Oya) | 1.60 | 🟢 Normal | -0.010 |  |
| 2026-05-12 16:00:09 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-12 15:10:27 | Thawalama (Gin Ganga) | 3.12 | 🟢 Normal | 0.994 | 🔺 Rising |
| 2026-05-12 16:03:27 | Deraniyagala (Kelani Ganga) | 0.96 | 🟢 Normal | 0.263 | 🔺 Rising |
| 2026-05-12 16:04:20 | Rathnapura (Kalu Ganga) | 1.93 | 🟢 Normal | 0.262 | 🔺 Rising |
| 2026-05-12 16:04:08 | Panadugama (Nilwala Ganga) | 3.52 | 🟢 Normal | 0.238 | 🔺 Rising |
| 2026-05-12 16:01:52 | Pitabeddara (Nilwala Ganga) | 1.85 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-05-12 16:02:49 | Dunamale (Aththanagalu Oya) | 1.50 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-05-12 16:05:01 | Galgamuwa (Mee Oya) | 1.64 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-12 15:09:48 | Glencourse (Kelani Ganga) | 9.87 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-12 16:01:51 | Giriulla (Maha Oya) | 1.53 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-12 16:00:49 | Manampitiya (Mahaweli Ganga) | 0.92 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-05-12 16:02:00 | Nawalapitiya (Mahaweli Ganga) | 0.95 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-12 16:06:01 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-12 16:01:55 | Horowpothana (Yan Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-05-12 16:05:50 | Baddegama (Gin Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-05-12 16:00:47 | Padiyathalawa (Maduru Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-12 16:03:43 | Thanthirimale (Malwathu Oya) | 3.40 | 🟢 Normal | 0.000 |  |
| 2026-05-12 16:02:23 | Thalgahagoda (Nilwala Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-12 15:07:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.88 | 🟢 Normal | 0.000 |  |
| 2026-05-12 16:02:28 | Kuda Oya (Kirindi Oya) | 1.94 | 🟢 Normal | -0.010 |  |
| 2026-05-12 15:09:52 | Holombuwa (Kelani Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-05-12 16:05:36 | Badalgama (Maha Oya) | 2.73 | 🟢 Normal | -0.010 |  |
| 2026-05-12 16:02:27 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-05-12 16:00:21 | Wellawaya (Kirindi Oya) | 1.60 | 🟢 Normal | -0.010 |  |
| 2026-05-12 16:00:09 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | -0.011 |  |
| 2026-05-12 16:05:36 | Siyambalanduwa (Heda Oya) | 0.66 | 🟢 Normal | -0.019 |  |
| 2026-05-12 16:03:07 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.019 |  |
| 2026-05-12 15:06:02 | Thanamalwila (Kirindi Oya) | 1.95 | 🟢 Normal | -0.020 |  |
| 2026-05-12 16:03:58 | Hanwella (Kelani Ganga) | 1.76 | 🟢 Normal | -0.020 |  |
| 2026-05-12 16:04:40 | Katharagama (Menik Ganga) | 1.99 | 🟢 Normal | -0.020 |  |
| 2026-05-12 15:01:11 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | -0.020 |  |
| 2026-05-12 16:05:58 | Urawa (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.021 |  |
| 2026-05-12 16:05:41 | Magura (Kalu Ganga) | 2.27 | 🟢 Normal | -0.021 |  |
| 2026-05-12 15:03:52 | Moraketiya (Walawe Ganga) | 1.07 | 🟢 Normal | -0.029 |  |
| 2026-05-12 16:01:28 | Ellagawa (Kalu Ganga) | 5.59 | 🟢 Normal | -0.030 |  |
| 2026-05-12 15:02:03 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.030 |  |
| 2026-05-12 16:03:35 | Weraganthota (Mahaweli Ganga) | -2.87 | 🟢 Normal | -0.039 |  |
| 2026-05-12 16:03:50 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | -0.048 |  |
| 2026-05-12 15:08:50 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | -0.051 |  |
| 2026-05-12 16:02:07 | Moragaswewa (Deduru Oya) | 2.08 | 🟢 Normal | -0.129 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)