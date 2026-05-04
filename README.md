# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--04_05:13:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **142,358 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-04 05:13:05 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-05-04 05:11:54 | Holombuwa (Kelani Ganga) | 0.21 | 🟢 Normal | -0.009 |  |
| 2026-05-04 05:11:07 | Rathnapura (Kalu Ganga) | 1.31 | 🟢 Normal | -0.088 |  |
| 2026-05-04 05:10:58 | Peradeniya (Mahaweli Ganga) | 1.39 | 🟢 Normal | -0.043 |  |
| 2026-05-04 05:09:23 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 1.038 | 🔺 Rising |
| 2026-05-04 05:07:29 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.094 |  |
| 2026-05-04 05:07:17 | Putupaula (Kalu Ganga) | 0.69 | 🟢 Normal | -0.133 |  |
| 2026-05-04 05:07:10 | Baddegama (Gin Ganga) | 1.48 | 🟢 Normal | -0.022 |  |
| 2026-05-04 05:06:55 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-04 05:05:42 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-04 05:05:38 | Ellagawa (Kalu Ganga) | 4.40 | 🟢 Normal | -0.059 |  |
| 2026-05-04 05:05:15 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-05-04 05:04:52 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-04 05:04:42 | Deraniyagala (Kelani Ganga) | 0.28 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-05-04 05:04:37 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-04 05:04:19 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-04 05:04:13 | Moragaswewa (Deduru Oya) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-05-04 05:03:17 | Glencourse (Kelani Ganga) | 8.72 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-05-04 05:03:09 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-04 05:02:59 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-04 05:02:49 | Giriulla (Maha Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-05-04 05:02:38 | Panadugama (Nilwala Ganga) | 2.15 | 🟢 Normal | -0.020 |  |
| 2026-05-04 05:02:24 | Hanwella (Kelani Ganga) | 0.37 | 🟢 Normal | -0.020 |  |
| 2026-05-04 05:02:24 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-05-04 05:02:04 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-05-04 05:02:02 | Thanamalwila (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-04 05:01:47 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-04 05:01:35 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-04 05:01:21 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | -0.011 |  |
| 2026-05-04 05:01:02 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | -0.010 |  |
| 2026-05-04 05:00:43 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | 1.038 | 🔺 Rising |
| 2026-05-04 04:33:29 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-05-04 04:32:56 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-04 05:09:23 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 1.038 | 🔺 Rising |
| 2026-05-04 05:03:17 | Glencourse (Kelani Ganga) | 8.72 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-05-04 03:03:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.24 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-05-04 05:04:42 | Deraniyagala (Kelani Ganga) | 0.28 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-05-04 05:13:05 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-05-03 18:00:12 | Weraganthota (Mahaweli Ganga) | -3.18 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-04 05:04:52 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-04 05:05:42 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-04 05:06:55 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-04 05:01:47 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-04 05:02:49 | Giriulla (Maha Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-05-04 05:03:09 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-03 18:01:35 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-04 04:10:53 | Magura (Kalu Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-04 03:56:00 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-05-04 05:02:59 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-04 05:04:19 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-04 05:04:37 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-04 05:01:35 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-04 05:02:24 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-05-04 05:05:15 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-05-04 04:00:34 | Manampitiya (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-05-03 18:00:54 | Thanthirimale (Malwathu Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-05-04 05:02:04 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-05-04 05:02:02 | Thanamalwila (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-04 05:11:54 | Holombuwa (Kelani Ganga) | 0.21 | 🟢 Normal | -0.009 |  |
| 2026-05-04 05:04:13 | Moragaswewa (Deduru Oya) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-05-04 03:01:18 | Thawalama (Gin Ganga) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-05-04 05:01:02 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | -0.010 |  |
| 2026-05-04 05:01:21 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | -0.011 |  |
| 2026-05-04 05:02:38 | Panadugama (Nilwala Ganga) | 2.15 | 🟢 Normal | -0.020 |  |
| 2026-05-04 05:02:24 | Hanwella (Kelani Ganga) | 0.37 | 🟢 Normal | -0.020 |  |
| 2026-05-04 04:05:00 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | -0.020 |  |
| 2026-05-04 05:07:10 | Baddegama (Gin Ganga) | 1.48 | 🟢 Normal | -0.022 |  |
| 2026-05-04 05:10:58 | Peradeniya (Mahaweli Ganga) | 1.39 | 🟢 Normal | -0.043 |  |
| 2026-05-04 05:05:38 | Ellagawa (Kalu Ganga) | 4.40 | 🟢 Normal | -0.059 |  |
| 2026-05-04 05:11:07 | Rathnapura (Kalu Ganga) | 1.31 | 🟢 Normal | -0.088 |  |
| 2026-05-04 05:07:29 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.094 |  |
| 2026-05-04 05:07:17 | Putupaula (Kalu Ganga) | 0.69 | 🟢 Normal | -0.133 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)