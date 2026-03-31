# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--31_16:18:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **112,474 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **43** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-31 16:18:27 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-31 16:13:08 | Ellagawa (Kalu Ganga) | 3.76 | 🟢 Normal | 0.000 |  |
| 2026-03-31 16:12:59 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-03-31 16:11:49 | Pitabeddara (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-03-31 16:11:12 | Urawa (Nilwala Ganga) | -0.09 | 🟢 Normal | -0.009 |  |
| 2026-03-31 16:11:04 | Baddegama (Gin Ganga) | 0.81 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-31 16:11:00 | Panadugama (Nilwala Ganga) | 1.84 | 🟢 Normal | -0.012 |  |
| 2026-03-31 16:10:55 | Glencourse (Kelani Ganga) | 8.22 | 🟢 Normal | -0.018 |  |
| 2026-03-31 16:09:43 | Peradeniya (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-03-31 16:07:57 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-03-31 16:07:34 | Magura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-31 16:04:54 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-31 16:04:46 | Weraganthota (Mahaweli Ganga) | -2.94 | 🟢 Normal | -0.056 |  |
| 2026-03-31 16:04:42 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | -0.005 |  |
| 2026-03-31 16:04:29 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-31 16:04:18 | Badalgama (Maha Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-03-31 16:04:09 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | -18.000 |  |
| 2026-03-31 16:04:09 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-31 16:04:07 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | -18.000 |  |
| 2026-03-31 16:04:07 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-31 16:03:33 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-03-31 16:03:32 | Hanwella (Kelani Ganga) | 0.36 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-31 16:03:13 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-03-31 16:02:47 | Deraniyagala (Kelani Ganga) | 0.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-31 16:02:37 | Rathnapura (Kalu Ganga) | 0.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-31 16:02:31 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.103 |  |
| 2026-03-31 16:02:29 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-31 16:02:26 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-31 16:02:26 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.060 |  |
| 2026-03-31 16:02:16 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-31 16:02:14 | Giriulla (Maha Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-31 16:02:12 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-03-31 16:02:11 | Nawalapitiya (Mahaweli Ganga) | 0.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-31 16:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-03-31 16:01:49 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-03-31 16:01:35 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-31 16:01:22 | Thanthirimale (Malwathu Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-03-31 16:01:20 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-31 16:01:19 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-31 16:00:10 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-03-31 16:00:05 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-31 15:51:23 | Thawalama (Gin Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-03-31 15:51:22 | Thawalama (Gin Ganga) | 1.09 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-31 16:12:59 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-03-31 16:07:57 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-03-31 16:03:32 | Hanwella (Kelani Ganga) | 0.36 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-31 16:02:37 | Rathnapura (Kalu Ganga) | 0.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-31 16:04:07 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-31 16:11:04 | Baddegama (Gin Ganga) | 0.81 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-31 16:02:47 | Deraniyagala (Kelani Ganga) | 0.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-31 16:02:11 | Nawalapitiya (Mahaweli Ganga) | 0.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-31 16:03:33 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-03-31 16:04:29 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-31 16:01:35 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-31 16:04:54 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-31 16:02:26 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-31 16:02:14 | Giriulla (Maha Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-31 16:01:20 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-31 16:07:34 | Magura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-31 16:11:49 | Pitabeddara (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-03-31 16:02:29 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-31 16:13:08 | Ellagawa (Kalu Ganga) | 3.76 | 🟢 Normal | 0.000 |  |
| 2026-03-31 16:01:49 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-03-31 16:00:05 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-31 16:18:27 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-31 16:03:13 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-03-31 16:02:12 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-03-31 16:04:18 | Badalgama (Maha Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-03-31 16:01:22 | Thanthirimale (Malwathu Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-03-31 15:51:23 | Thawalama (Gin Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-03-31 16:09:43 | Peradeniya (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-03-31 16:00:10 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-03-31 16:02:16 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-31 16:04:42 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | -0.005 |  |
| 2026-03-31 16:11:12 | Urawa (Nilwala Ganga) | -0.09 | 🟢 Normal | -0.009 |  |
| 2026-03-31 16:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-03-31 16:11:00 | Panadugama (Nilwala Ganga) | 1.84 | 🟢 Normal | -0.012 |  |
| 2026-03-31 16:10:55 | Glencourse (Kelani Ganga) | 8.22 | 🟢 Normal | -0.018 |  |
| 2026-03-31 16:04:46 | Weraganthota (Mahaweli Ganga) | -2.94 | 🟢 Normal | -0.056 |  |
| 2026-03-31 16:02:26 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.060 |  |
| 2026-03-31 16:02:31 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.103 |  |
| 2026-03-31 16:04:09 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | -18.000 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)