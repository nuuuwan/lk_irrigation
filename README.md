# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--20_04:21:58-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **156,644 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-20 04:21:58 | Putupaula (Kalu Ganga) | 0.97 | 🟢 Normal | -0.015 |  |
| 2026-05-20 04:18:53 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.024 |  |
| 2026-05-20 04:17:35 | Pitabeddara (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-20 04:11:39 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-05-20 04:11:27 | Manampitiya (Mahaweli Ganga) | 0.38 | 🟢 Normal | -0.059 |  |
| 2026-05-20 04:11:26 | Thanamalwila (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-05-20 04:09:18 | Badalgama (Maha Oya) | 2.71 | 🟢 Normal | -0.009 |  |
| 2026-05-20 04:09:14 | Panadugama (Nilwala Ganga) | 2.49 | 🟢 Normal | -0.006 |  |
| 2026-05-20 04:06:15 | Baddegama (Gin Ganga) | 1.39 | 🟢 Normal | -0.009 |  |
| 2026-05-20 04:05:31 | Holombuwa (Kelani Ganga) | 0.76 | 🟢 Normal | -0.021 |  |
| 2026-05-20 04:05:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.30 | 🟢 Normal | 0.000 |  |
| 2026-05-20 04:04:45 | Giriulla (Maha Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-05-20 04:04:41 | Hanwella (Kelani Ganga) | 1.74 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-20 04:04:20 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-05-20 04:04:03 | Horowpothana (Yan Oya) | 1.34 | 🟢 Normal | -0.020 |  |
| 2026-05-20 04:03:58 | Nawalapitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-20 04:03:53 | Peradeniya (Mahaweli Ganga) | 1.52 | 🟢 Normal | -0.189 |  |
| 2026-05-20 04:03:49 | Thawalama (Gin Ganga) | 1.59 | 🟢 Normal | -0.005 |  |
| 2026-05-20 04:03:48 | Magura (Kalu Ganga) | 1.73 | 🟢 Normal | -0.010 |  |
| 2026-05-20 04:03:43 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-05-20 04:03:35 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-20 04:03:29 | Moragaswewa (Deduru Oya) | 1.62 | 🟢 Normal | -0.039 |  |
| 2026-05-20 04:03:06 | Giriulla (Maha Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-05-20 04:03:00 | Kithulgala (Kelani Ganga) | 1.35 | 🟢 Normal | -0.101 |  |
| 2026-05-20 04:02:54 | Ellagawa (Kalu Ganga) | 5.19 | 🟢 Normal | -0.020 |  |
| 2026-05-20 04:02:40 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-05-20 04:02:27 | Dunamale (Aththanagalu Oya) | 2.38 | 🟢 Normal | 0.000 |  |
| 2026-05-20 04:02:19 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-05-20 04:01:49 | Glencourse (Kelani Ganga) | 9.87 | 🟢 Normal | 0.179 | 🔺 Rising |
| 2026-05-20 04:01:19 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-05-20 04:01:18 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-20 04:01:17 | Manampitiya (Mahaweli Ganga) | 0.39 | 🟢 Normal | -0.059 |  |
| 2026-05-20 04:01:04 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-05-20 04:00:56 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-05-20 04:00:44 | Manampitiya (Mahaweli Ganga) | 0.40 | 🟢 Normal | -0.059 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-20 04:01:49 | Glencourse (Kelani Ganga) | 9.87 | 🟢 Normal | 0.179 | 🔺 Rising |
| 2026-05-20 04:11:39 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-05-20 04:01:04 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-05-20 04:03:58 | Nawalapitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-20 04:01:18 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-20 04:04:41 | Hanwella (Kelani Ganga) | 1.74 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-19 18:04:04 | Weraganthota (Mahaweli Ganga) | -3.29 | 🟢 Normal | 0.000 |  |
| 2026-05-20 03:03:20 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-05-20 04:03:43 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-05-20 03:02:00 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-05-20 04:04:45 | Giriulla (Maha Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-05-19 18:03:48 | Galgamuwa (Mee Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-05-20 04:17:35 | Pitabeddara (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-20 04:04:20 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-05-20 04:03:35 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-20 03:00:13 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-20 04:02:27 | Dunamale (Aththanagalu Oya) | 2.38 | 🟢 Normal | 0.000 |  |
| 2026-05-20 04:02:40 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-05-20 03:03:58 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-05-20 04:01:19 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-05-20 04:11:26 | Thanamalwila (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-05-20 04:05:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.30 | 🟢 Normal | 0.000 |  |
| 2026-05-20 04:03:49 | Thawalama (Gin Ganga) | 1.59 | 🟢 Normal | -0.005 |  |
| 2026-05-20 04:09:14 | Panadugama (Nilwala Ganga) | 2.49 | 🟢 Normal | -0.006 |  |
| 2026-05-20 04:09:18 | Badalgama (Maha Oya) | 2.71 | 🟢 Normal | -0.009 |  |
| 2026-05-20 03:04:46 | Rathnapura (Kalu Ganga) | 1.49 | 🟢 Normal | -0.009 |  |
| 2026-05-20 04:06:15 | Baddegama (Gin Ganga) | 1.39 | 🟢 Normal | -0.009 |  |
| 2026-05-20 04:03:48 | Magura (Kalu Ganga) | 1.73 | 🟢 Normal | -0.010 |  |
| 2026-05-20 04:02:19 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-05-20 04:21:58 | Putupaula (Kalu Ganga) | 0.97 | 🟢 Normal | -0.015 |  |
| 2026-05-20 04:02:54 | Ellagawa (Kalu Ganga) | 5.19 | 🟢 Normal | -0.020 |  |
| 2026-05-20 04:04:03 | Horowpothana (Yan Oya) | 1.34 | 🟢 Normal | -0.020 |  |
| 2026-05-19 18:02:04 | Thanthirimale (Malwathu Oya) | 2.22 | 🟢 Normal | -0.021 |  |
| 2026-05-20 04:05:31 | Holombuwa (Kelani Ganga) | 0.76 | 🟢 Normal | -0.021 |  |
| 2026-05-20 04:18:53 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.024 |  |
| 2026-05-20 04:03:29 | Moragaswewa (Deduru Oya) | 1.62 | 🟢 Normal | -0.039 |  |
| 2026-05-20 04:11:27 | Manampitiya (Mahaweli Ganga) | 0.38 | 🟢 Normal | -0.059 |  |
| 2026-05-20 04:03:00 | Kithulgala (Kelani Ganga) | 1.35 | 🟢 Normal | -0.101 |  |
| 2026-05-20 04:03:53 | Peradeniya (Mahaweli Ganga) | 1.52 | 🟢 Normal | -0.189 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)