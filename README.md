# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--24_10:29:40-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **133,666 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-24 10:29:40 | Badalgama (Maha Oya) | 2.53 | 🟢 Normal | 0.000 |  |
| 2026-04-24 10:19:03 | Thalgahagoda (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-04-24 10:18:21 | Dunamale (Aththanagalu Oya) | 1.70 | 🟢 Normal | -0.032 |  |
| 2026-04-24 10:12:53 | Baddegama (Gin Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-04-24 10:12:24 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | -0.025 |  |
| 2026-04-24 10:11:19 | Rathnapura (Kalu Ganga) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-04-24 10:11:17 | Galgamuwa (Mee Oya) | 0.92 | 🟢 Normal | -0.009 |  |
| 2026-04-24 10:10:18 | Glencourse (Kelani Ganga) | 9.57 | 🟢 Normal | -0.037 |  |
| 2026-04-24 10:08:56 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-04-24 10:07:40 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.029 |  |
| 2026-04-24 10:07:11 | Kithulgala (Kelani Ganga) | 1.23 | 🟢 Normal | -0.069 |  |
| 2026-04-24 10:07:06 | Magura (Kalu Ganga) | 1.70 | 🟢 Normal | -0.029 |  |
| 2026-04-24 10:06:25 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | -0.101 |  |
| 2026-04-24 10:06:18 | Pitabeddara (Nilwala Ganga) | 0.59 | 🟢 Normal | -0.039 |  |
| 2026-04-24 10:06:05 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | -0.010 |  |
| 2026-04-24 10:06:00 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | -0.048 |  |
| 2026-04-24 10:05:39 | Katharagama (Menik Ganga) | 2.08 | 🟢 Normal | -0.086 |  |
| 2026-04-24 10:05:37 | Ellagawa (Kalu Ganga) | 5.31 | 🟢 Normal | -0.019 |  |
| 2026-04-24 10:05:19 | Panadugama (Nilwala Ganga) | 2.99 | 🟢 Normal | 0.000 |  |
| 2026-04-24 10:05:12 | Putupaula (Kalu Ganga) | 0.83 | 🟢 Normal | 0.126 | 🔺 Rising |
| 2026-04-24 10:04:24 | Moraketiya (Walawe Ganga) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-04-24 10:03:44 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-24 10:03:40 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-04-24 10:03:16 | Nawalapitiya (Mahaweli Ganga) | 0.87 | 🟢 Normal | -0.019 |  |
| 2026-04-24 10:03:12 | Hanwella (Kelani Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-04-24 10:02:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.56 | 🟢 Normal | -0.040 |  |
| 2026-04-24 10:02:54 | Thawalama (Gin Ganga) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-04-24 10:02:42 | Norwood (Kelani Ganga) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-04-24 10:02:32 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-24 10:02:30 | Badalgama (Maha Oya) | 2.53 | 🟢 Normal | 0.000 |  |
| 2026-04-24 10:02:14 | Nakkala (Kumbukkan Oya) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-04-24 10:02:13 | Giriulla (Maha Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-04-24 10:02:13 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-24 10:01:56 | Thanamalwila (Kirindi Oya) | 1.68 | 🟢 Normal | -0.052 |  |
| 2026-04-24 10:01:52 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | -0.020 |  |
| 2026-04-24 10:01:20 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-04-24 10:00:59 | Thanthirimale (Malwathu Oya) | 1.82 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-24 10:00:50 | Manampitiya (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-24 10:00:34 | Kuda Oya (Kirindi Oya) | 1.85 | 🟢 Normal | -0.020 |  |
| 2026-04-24 10:00:27 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-24 10:05:12 | Putupaula (Kalu Ganga) | 0.83 | 🟢 Normal | 0.126 | 🔺 Rising |
| 2026-04-24 10:08:56 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-04-24 10:00:59 | Thanthirimale (Malwathu Oya) | 1.82 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-24 10:19:03 | Thalgahagoda (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-04-24 10:03:40 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-04-24 10:02:13 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-24 10:02:13 | Giriulla (Maha Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-04-24 10:03:12 | Hanwella (Kelani Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-04-24 10:02:32 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-24 10:12:53 | Baddegama (Gin Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-04-24 10:05:19 | Panadugama (Nilwala Ganga) | 2.99 | 🟢 Normal | 0.000 |  |
| 2026-04-24 10:03:44 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-24 10:01:20 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-04-24 10:29:40 | Badalgama (Maha Oya) | 2.53 | 🟢 Normal | 0.000 |  |
| 2026-04-24 10:00:50 | Manampitiya (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-24 10:02:54 | Thawalama (Gin Ganga) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-04-24 10:11:17 | Galgamuwa (Mee Oya) | 0.92 | 🟢 Normal | -0.009 |  |
| 2026-04-24 10:02:14 | Nakkala (Kumbukkan Oya) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-04-24 10:04:24 | Moraketiya (Walawe Ganga) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-04-24 10:11:19 | Rathnapura (Kalu Ganga) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-04-24 10:06:05 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | -0.010 |  |
| 2026-04-24 10:02:42 | Norwood (Kelani Ganga) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-04-24 10:03:16 | Nawalapitiya (Mahaweli Ganga) | 0.87 | 🟢 Normal | -0.019 |  |
| 2026-04-24 10:05:37 | Ellagawa (Kalu Ganga) | 5.31 | 🟢 Normal | -0.019 |  |
| 2026-04-24 10:01:52 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | -0.020 |  |
| 2026-04-24 10:00:34 | Kuda Oya (Kirindi Oya) | 1.85 | 🟢 Normal | -0.020 |  |
| 2026-04-24 10:00:27 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.020 |  |
| 2026-04-24 10:12:24 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | -0.025 |  |
| 2026-04-24 10:07:06 | Magura (Kalu Ganga) | 1.70 | 🟢 Normal | -0.029 |  |
| 2026-04-24 10:07:40 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.029 |  |
| 2026-04-24 10:18:21 | Dunamale (Aththanagalu Oya) | 1.70 | 🟢 Normal | -0.032 |  |
| 2026-04-24 10:10:18 | Glencourse (Kelani Ganga) | 9.57 | 🟢 Normal | -0.037 |  |
| 2026-04-24 10:06:18 | Pitabeddara (Nilwala Ganga) | 0.59 | 🟢 Normal | -0.039 |  |
| 2026-04-24 10:02:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.56 | 🟢 Normal | -0.040 |  |
| 2026-04-24 10:06:00 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | -0.048 |  |
| 2026-04-24 10:01:56 | Thanamalwila (Kirindi Oya) | 1.68 | 🟢 Normal | -0.052 |  |
| 2026-04-24 10:07:11 | Kithulgala (Kelani Ganga) | 1.23 | 🟢 Normal | -0.069 |  |
| 2026-04-24 10:05:39 | Katharagama (Menik Ganga) | 2.08 | 🟢 Normal | -0.086 |  |
| 2026-04-24 10:06:25 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | -0.101 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)