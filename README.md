# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--25_14:12:58-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **134,712 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-25 14:12:58 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-04-25 14:11:44 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | -0.018 |  |
| 2026-04-25 14:11:11 | Dunamale (Aththanagalu Oya) | 0.90 | 🟢 Normal | -0.030 |  |
| 2026-04-25 14:08:44 | Ellagawa (Kalu Ganga) | 4.55 | 🟢 Normal | 0.000 |  |
| 2026-04-25 14:08:05 | Thawalama (Gin Ganga) | 1.39 | 🟢 Normal | -0.009 |  |
| 2026-04-25 14:07:21 | Katharagama (Menik Ganga) | 1.58 | 🟢 Normal | -0.117 |  |
| 2026-04-25 14:07:02 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | -0.009 |  |
| 2026-04-25 14:06:20 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-04-25 14:06:08 | Panadugama (Nilwala Ganga) | 2.65 | 🟢 Normal | -0.039 |  |
| 2026-04-25 14:05:56 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-25 14:05:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.95 | 🟢 Normal | -0.020 |  |
| 2026-04-25 14:05:20 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-25 14:05:10 | Giriulla (Maha Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-04-25 14:05:05 | Peradeniya (Mahaweli Ganga) | 1.31 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-04-25 14:04:35 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | -0.010 |  |
| 2026-04-25 14:04:29 | Glencourse (Kelani Ganga) | 8.92 | 🟢 Normal | -0.020 |  |
| 2026-04-25 14:04:21 | Magura (Kalu Ganga) | 1.34 | 🟢 Normal | -0.020 |  |
| 2026-04-25 14:04:19 | Rathnapura (Kalu Ganga) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-04-25 14:04:05 | Badalgama (Maha Oya) | 2.23 | 🟢 Normal | -0.010 |  |
| 2026-04-25 14:03:37 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-25 14:03:10 | Thanamalwila (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-04-25 14:03:10 | Hanwella (Kelani Ganga) | 0.87 | 🟢 Normal | -0.030 |  |
| 2026-04-25 14:02:59 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-04-25 14:02:52 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | -0.020 |  |
| 2026-04-25 14:02:48 | Deraniyagala (Kelani Ganga) | 0.26 | 🟢 Normal | -0.084 |  |
| 2026-04-25 14:02:23 | Moragaswewa (Deduru Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-04-25 14:02:18 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-04-25 14:02:16 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-25 14:01:57 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-25 14:01:56 | Manampitiya (Mahaweli Ganga) | 0.04 | 🟢 Normal | -0.010 |  |
| 2026-04-25 14:01:42 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-25 14:01:21 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-04-25 14:01:18 | Thanthirimale (Malwathu Oya) | 1.78 | 🟢 Normal | -0.020 |  |
| 2026-04-25 14:00:47 | Weraganthota (Mahaweli Ganga) | -3.18 | 🟢 Normal | -0.050 |  |
| 2026-04-25 14:00:43 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.021 |  |
| 2026-04-25 14:00:40 | Kuda Oya (Kirindi Oya) | 1.57 | 🟢 Normal | -0.020 |  |
| 2026-04-25 14:00:40 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-25 13:43:44 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.033 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-25 14:05:05 | Peradeniya (Mahaweli Ganga) | 1.31 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-04-25 13:43:44 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-04-25 14:01:57 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-25 14:01:21 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-04-25 14:05:20 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-25 14:02:23 | Moragaswewa (Deduru Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-04-25 14:01:42 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-25 14:05:56 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-25 14:02:16 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-25 14:08:44 | Ellagawa (Kalu Ganga) | 4.55 | 🟢 Normal | 0.000 |  |
| 2026-04-25 14:02:59 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-04-25 14:03:37 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-25 14:12:58 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-04-25 14:02:18 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-04-25 14:00:40 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-25 14:03:10 | Thanamalwila (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-04-25 14:08:05 | Thawalama (Gin Ganga) | 1.39 | 🟢 Normal | -0.009 |  |
| 2026-04-25 14:07:02 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | -0.009 |  |
| 2026-04-25 14:04:05 | Badalgama (Maha Oya) | 2.23 | 🟢 Normal | -0.010 |  |
| 2026-04-25 14:01:56 | Manampitiya (Mahaweli Ganga) | 0.04 | 🟢 Normal | -0.010 |  |
| 2026-04-25 14:05:10 | Giriulla (Maha Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-04-25 14:06:20 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-04-25 14:04:19 | Rathnapura (Kalu Ganga) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-04-25 14:04:35 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | -0.010 |  |
| 2026-04-25 13:14:43 | Galgamuwa (Mee Oya) | 0.46 | 🟢 Normal | -0.017 |  |
| 2026-04-25 14:11:44 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | -0.018 |  |
| 2026-04-25 14:05:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.95 | 🟢 Normal | -0.020 |  |
| 2026-04-25 14:02:52 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | -0.020 |  |
| 2026-04-25 14:01:18 | Thanthirimale (Malwathu Oya) | 1.78 | 🟢 Normal | -0.020 |  |
| 2026-04-25 14:04:21 | Magura (Kalu Ganga) | 1.34 | 🟢 Normal | -0.020 |  |
| 2026-04-25 14:04:29 | Glencourse (Kelani Ganga) | 8.92 | 🟢 Normal | -0.020 |  |
| 2026-04-25 14:00:40 | Kuda Oya (Kirindi Oya) | 1.57 | 🟢 Normal | -0.020 |  |
| 2026-04-25 14:00:43 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.021 |  |
| 2026-04-25 14:11:11 | Dunamale (Aththanagalu Oya) | 0.90 | 🟢 Normal | -0.030 |  |
| 2026-04-25 14:03:10 | Hanwella (Kelani Ganga) | 0.87 | 🟢 Normal | -0.030 |  |
| 2026-04-25 14:06:08 | Panadugama (Nilwala Ganga) | 2.65 | 🟢 Normal | -0.039 |  |
| 2026-04-25 14:00:47 | Weraganthota (Mahaweli Ganga) | -3.18 | 🟢 Normal | -0.050 |  |
| 2026-04-25 14:02:48 | Deraniyagala (Kelani Ganga) | 0.26 | 🟢 Normal | -0.084 |  |
| 2026-04-25 14:07:21 | Katharagama (Menik Ganga) | 1.58 | 🟢 Normal | -0.117 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)