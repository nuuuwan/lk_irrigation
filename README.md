# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--28_13:16:43-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **163,947 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-28 13:16:43 | Urawa (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.227 | 🔺 Rising |
| 2026-05-28 13:12:22 | Thawalama (Gin Ganga) | 1.53 | 🟢 Normal | -0.933 |  |
| 2026-05-28 13:11:22 | Panadugama (Nilwala Ganga) | 3.06 | 🟢 Normal | 0.000 |  |
| 2026-05-28 13:07:34 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-28 13:07:20 | Magura (Kalu Ganga) | 4.71 | 🟡 Alert | 0.048 | 🔺 Rising |
| 2026-05-28 13:07:09 | Dunamale (Aththanagalu Oya) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-05-28 13:07:08 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-05-28 13:06:54 | Peradeniya (Mahaweli Ganga) | 1.66 | 🟢 Normal | -0.021 |  |
| 2026-05-28 13:06:49 | Rathnapura (Kalu Ganga) | 3.85 | 🟢 Normal | -0.051 |  |
| 2026-05-28 13:06:17 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-28 13:05:46 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-05-28 13:05:40 | Baddegama (Gin Ganga) | 2.75 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-05-28 13:05:14 | Hanwella (Kelani Ganga) | 4.07 | 🟢 Normal | -0.078 |  |
| 2026-05-28 13:04:14 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-28 13:03:42 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-05-28 13:03:35 | Badalgama (Maha Oya) | 2.39 | 🟢 Normal | 0.000 |  |
| 2026-05-28 13:03:26 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-28 13:03:10 | Giriulla (Maha Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-05-28 13:03:00 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-28 13:02:56 | Nawalapitiya (Mahaweli Ganga) | 1.51 | 🟢 Normal | -0.010 |  |
| 2026-05-28 13:02:52 | Thalgahagoda (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-28 13:02:38 | Putupaula (Kalu Ganga) | 2.50 | 🟢 Normal | 0.000 |  |
| 2026-05-28 13:02:30 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-05-28 13:02:27 | Moragaswewa (Deduru Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-28 13:02:20 | Glencourse (Kelani Ganga) | 11.51 | 🟢 Normal | -0.050 |  |
| 2026-05-28 13:02:19 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-28 13:02:19 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-05-28 13:02:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.19 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-05-28 13:02:15 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-28 13:01:40 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-05-28 13:01:40 | Ellagawa (Kalu Ganga) | 8.58 | 🟢 Normal | -0.010 |  |
| 2026-05-28 13:01:36 | Deraniyagala (Kelani Ganga) | 1.58 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-28 13:01:35 | Thanthirimale (Malwathu Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-05-28 13:01:35 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-05-28 13:01:22 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-28 13:01:19 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-28 13:01:07 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-28 13:00:40 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-05-28 12:53:21 | Pitabeddara (Nilwala Ganga) | 1.13 | 🟢 Normal | 0.316 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-28 13:07:20 | Magura (Kalu Ganga) | 4.71 | 🟡 Alert | 0.048 | 🔺 Rising |
| 2026-05-28 13:02:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.19 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-05-28 12:53:21 | Pitabeddara (Nilwala Ganga) | 1.13 | 🟢 Normal | 0.316 | 🔺 Rising |
| 2026-05-28 13:16:43 | Urawa (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.227 | 🔺 Rising |
| 2026-05-28 13:05:46 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-05-28 13:07:08 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-05-28 13:05:40 | Baddegama (Gin Ganga) | 2.75 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-05-28 13:01:36 | Deraniyagala (Kelani Ganga) | 1.58 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-28 13:02:52 | Thalgahagoda (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-28 13:01:19 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-28 13:02:19 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-28 13:03:00 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-28 13:04:14 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-28 13:02:19 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-05-28 13:01:07 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-28 13:02:27 | Moragaswewa (Deduru Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-28 13:01:22 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-28 13:06:17 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-28 13:03:26 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-28 13:11:22 | Panadugama (Nilwala Ganga) | 3.06 | 🟢 Normal | 0.000 |  |
| 2026-05-28 13:01:35 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-05-28 13:07:09 | Dunamale (Aththanagalu Oya) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-05-28 13:01:40 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-05-28 13:07:34 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-28 13:02:38 | Putupaula (Kalu Ganga) | 2.50 | 🟢 Normal | 0.000 |  |
| 2026-05-28 13:03:35 | Badalgama (Maha Oya) | 2.39 | 🟢 Normal | 0.000 |  |
| 2026-05-28 13:02:30 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-05-28 13:01:35 | Thanthirimale (Malwathu Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-05-28 13:02:15 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-28 13:03:42 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-05-28 13:01:40 | Ellagawa (Kalu Ganga) | 8.58 | 🟢 Normal | -0.010 |  |
| 2026-05-28 13:00:40 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-05-28 13:02:56 | Nawalapitiya (Mahaweli Ganga) | 1.51 | 🟢 Normal | -0.010 |  |
| 2026-05-28 13:03:10 | Giriulla (Maha Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-05-28 13:06:54 | Peradeniya (Mahaweli Ganga) | 1.66 | 🟢 Normal | -0.021 |  |
| 2026-05-28 13:02:20 | Glencourse (Kelani Ganga) | 11.51 | 🟢 Normal | -0.050 |  |
| 2026-05-28 13:06:49 | Rathnapura (Kalu Ganga) | 3.85 | 🟢 Normal | -0.051 |  |
| 2026-05-28 13:05:14 | Hanwella (Kelani Ganga) | 4.07 | 🟢 Normal | -0.078 |  |
| 2026-05-28 13:12:22 | Thawalama (Gin Ganga) | 1.53 | 🟢 Normal | -0.933 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)