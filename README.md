# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--13_03:10:36-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **95,864 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-13 03:10:36 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-03-13 03:09:19 | Kithulgala (Kelani Ganga) | 1.09 | 🟢 Normal | -0.029 |  |
| 2026-03-13 03:09:15 | Rathnapura (Kalu Ganga) | 1.06 | 🟢 Normal | 0.257 | 🔺 Rising |
| 2026-03-13 03:07:26 | Thalgahagoda (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.020 |  |
| 2026-03-13 03:06:38 | Nawalapitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.143 | 🔺 Rising |
| 2026-03-13 03:06:07 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-13 03:06:00 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-03-13 03:05:58 | Wellawaya (Kirindi Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-13 03:05:36 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-13 03:05:30 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-03-13 03:05:27 | Thaldena (Mahaweli Ganga) | 0.54 | 🟢 Normal | -108.000 |  |
| 2026-03-13 03:05:26 | Thaldena (Mahaweli Ganga) | 0.57 | 🟢 Normal | -108.000 |  |
| 2026-03-13 03:05:18 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-13 03:05:12 | Deraniyagala (Kelani Ganga) | 0.30 | 🟢 Normal | -0.056 |  |
| 2026-03-13 03:05:00 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.234 |  |
| 2026-03-13 03:04:43 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-13 03:04:25 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-03-13 03:04:20 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | 1.500 | 🔺 Rising |
| 2026-03-13 03:03:56 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | 1.500 | 🔺 Rising |
| 2026-03-13 03:03:31 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-13 03:03:18 | Dunamale (Aththanagalu Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-13 03:03:10 | Ellagawa (Kalu Ganga) | 3.79 | 🟢 Normal | 0.000 |  |
| 2026-03-13 03:02:58 | Padiyathalawa (Maduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-13 03:02:47 | Badalgama (Maha Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-03-13 03:02:46 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-13 03:02:41 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.039 |  |
| 2026-03-13 03:02:21 | Giriulla (Maha Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-03-13 03:02:20 | Manampitiya (Mahaweli Ganga) | 0.43 | 🟢 Normal | -0.046 |  |
| 2026-03-13 03:02:17 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-13 03:02:17 | Thanamalwila (Kirindi Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-03-13 03:02:06 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-03-13 03:01:50 | Glencourse (Kelani Ganga) | 9.41 | 🟢 Normal | 0.376 | 🔺 Rising |
| 2026-03-13 03:00:46 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-13 02:28:56 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.143 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-13 03:04:20 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | 1.500 | 🔺 Rising |
| 2026-03-13 03:01:50 | Glencourse (Kelani Ganga) | 9.41 | 🟢 Normal | 0.376 | 🔺 Rising |
| 2026-03-13 03:09:15 | Rathnapura (Kalu Ganga) | 1.06 | 🟢 Normal | 0.257 | 🔺 Rising |
| 2026-03-13 03:06:38 | Nawalapitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.143 | 🔺 Rising |
| 2026-03-13 03:10:36 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-03-13 03:04:25 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-03-12 22:16:26 | Magura (Kalu Ganga) | 0.92 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-03-13 02:09:28 | Putupaula (Kalu Ganga) | 0.38 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-03-12 22:02:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.14 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-13 03:05:18 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-13 03:03:31 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-13 03:05:58 | Wellawaya (Kirindi Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-13 01:03:40 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-03-13 03:02:17 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-13 03:02:21 | Giriulla (Maha Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-03-13 03:02:06 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-03-12 18:05:52 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-13 03:03:10 | Ellagawa (Kalu Ganga) | 3.79 | 🟢 Normal | 0.000 |  |
| 2026-03-13 03:05:30 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-03-13 03:02:58 | Padiyathalawa (Maduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-13 03:04:43 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-13 03:00:46 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-13 03:02:46 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-13 03:03:18 | Dunamale (Aththanagalu Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-13 03:06:07 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-13 03:02:47 | Badalgama (Maha Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-03-12 18:03:01 | Thanthirimale (Malwathu Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-03-13 03:06:00 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-03-13 03:02:17 | Thanamalwila (Kirindi Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-03-13 02:09:25 | Panadugama (Nilwala Ganga) | 2.09 | 🟢 Normal | -0.009 |  |
| 2026-03-13 01:02:36 | Pitabeddara (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-03-13 03:07:26 | Thalgahagoda (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.020 |  |
| 2026-03-13 03:09:19 | Kithulgala (Kelani Ganga) | 1.09 | 🟢 Normal | -0.029 |  |
| 2026-03-13 03:02:41 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.039 |  |
| 2026-03-13 03:02:20 | Manampitiya (Mahaweli Ganga) | 0.43 | 🟢 Normal | -0.046 |  |
| 2026-03-13 03:05:12 | Deraniyagala (Kelani Ganga) | 0.30 | 🟢 Normal | -0.056 |  |
| 2026-03-12 18:02:28 | Weraganthota (Mahaweli Ganga) | -2.90 | 🟢 Normal | -0.083 |  |
| 2026-03-13 03:05:00 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.234 |  |
| 2026-03-13 03:05:27 | Thaldena (Mahaweli Ganga) | 0.54 | 🟢 Normal | -108.000 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)