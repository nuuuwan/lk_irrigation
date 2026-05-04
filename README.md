# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--04_23:22:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **143,042 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-04 23:22:26 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.015 |  |
| 2026-05-04 23:13:04 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | -0.027 |  |
| 2026-05-04 23:10:32 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-05-04 23:09:26 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-05-04 23:07:46 | Rathnapura (Kalu Ganga) | 2.39 | 🟢 Normal | -0.019 |  |
| 2026-05-04 23:07:36 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-04 23:07:25 | Putupaula (Kalu Ganga) | 0.30 | 🟢 Normal | -0.050 |  |
| 2026-05-04 23:07:19 | Magura (Kalu Ganga) | 0.86 | 🟢 Normal | -0.009 |  |
| 2026-05-04 23:06:45 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | -0.020 |  |
| 2026-05-04 23:06:27 | Panadugama (Nilwala Ganga) | 2.06 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-05-04 23:06:27 | Thanamalwila (Kirindi Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-04 23:05:41 | Holombuwa (Kelani Ganga) | 1.34 | 🟢 Normal | 0.860 | 🔺 Rising |
| 2026-05-04 23:04:50 | Thawalama (Gin Ganga) | 1.33 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-04 23:04:39 | Norwood (Kelani Ganga) | 1.11 | 🟢 Normal | -0.039 |  |
| 2026-05-04 23:04:12 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-05-04 23:03:45 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-05-04 23:03:20 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-05-04 23:02:52 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-04 23:02:44 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | 0.274 | 🔺 Rising |
| 2026-05-04 23:02:42 | Giriulla (Maha Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-05-04 23:02:34 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-05-04 23:02:32 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | -0.011 |  |
| 2026-05-04 23:02:29 | Deraniyagala (Kelani Ganga) | 0.93 | 🟢 Normal | 0.185 | 🔺 Rising |
| 2026-05-04 23:02:24 | Dunamale (Aththanagalu Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-05-04 23:02:14 | Moragaswewa (Deduru Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-05-04 23:02:05 | Ellagawa (Kalu Ganga) | 4.29 | 🟢 Normal | 0.000 |  |
| 2026-05-04 23:01:59 | Manampitiya (Mahaweli Ganga) | 0.31 | 🟢 Normal | -0.011 |  |
| 2026-05-04 23:01:51 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.030 |  |
| 2026-05-04 23:01:40 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | 0.205 | 🔺 Rising |
| 2026-05-04 23:01:34 | Yaka Wewa (Ma Oya) | 1.25 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-05-04 23:01:00 | Glencourse (Kelani Ganga) | 8.40 | 🟢 Normal | 0.000 |  |
| 2026-05-04 23:00:46 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-05-04 23:00:27 | Nawalapitiya (Mahaweli Ganga) | 0.83 | 🟢 Normal | 0.021 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-04 23:05:41 | Holombuwa (Kelani Ganga) | 1.34 | 🟢 Normal | 0.860 | 🔺 Rising |
| 2026-05-04 23:02:44 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | 0.274 | 🔺 Rising |
| 2026-05-04 23:01:40 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | 0.205 | 🔺 Rising |
| 2026-05-04 23:02:29 | Deraniyagala (Kelani Ganga) | 0.93 | 🟢 Normal | 0.185 | 🔺 Rising |
| 2026-05-04 23:01:34 | Yaka Wewa (Ma Oya) | 1.25 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-05-04 23:06:27 | Panadugama (Nilwala Ganga) | 2.06 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-05-04 23:00:27 | Nawalapitiya (Mahaweli Ganga) | 0.83 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-04 23:04:50 | Thawalama (Gin Ganga) | 1.33 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-04 21:03:58 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-04 18:02:41 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | 0.000 |  |
| 2026-05-04 23:02:34 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-05-04 23:03:20 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-05-04 23:02:14 | Moragaswewa (Deduru Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-05-04 23:02:42 | Giriulla (Maha Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-05-04 22:00:55 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-05-04 18:01:37 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-04 23:07:36 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-04 23:02:05 | Ellagawa (Kalu Ganga) | 4.29 | 🟢 Normal | 0.000 |  |
| 2026-05-04 23:02:52 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-04 23:01:00 | Glencourse (Kelani Ganga) | 8.40 | 🟢 Normal | 0.000 |  |
| 2026-05-04 23:00:46 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-05-04 23:02:24 | Dunamale (Aththanagalu Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-05-04 23:09:26 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-05-04 18:03:48 | Thanthirimale (Malwathu Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-05-04 23:04:12 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-05-04 23:10:32 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-05-04 23:06:27 | Thanamalwila (Kirindi Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-04 23:07:19 | Magura (Kalu Ganga) | 0.86 | 🟢 Normal | -0.009 |  |
| 2026-05-04 23:01:59 | Manampitiya (Mahaweli Ganga) | 0.31 | 🟢 Normal | -0.011 |  |
| 2026-05-04 23:02:32 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | -0.011 |  |
| 2026-05-04 22:39:19 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | -0.012 |  |
| 2026-05-04 23:22:26 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.015 |  |
| 2026-05-04 23:07:46 | Rathnapura (Kalu Ganga) | 2.39 | 🟢 Normal | -0.019 |  |
| 2026-05-04 23:06:45 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | -0.020 |  |
| 2026-05-04 20:09:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.56 | 🟢 Normal | -0.024 |  |
| 2026-05-04 23:13:04 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | -0.027 |  |
| 2026-05-04 23:01:51 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.030 |  |
| 2026-05-04 23:04:39 | Norwood (Kelani Ganga) | 1.11 | 🟢 Normal | -0.039 |  |
| 2026-05-04 23:07:25 | Putupaula (Kalu Ganga) | 0.30 | 🟢 Normal | -0.050 |  |

## River Water Level Charts by Station

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)