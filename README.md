# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--18_06:21:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **100,438 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-18 06:21:30 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-18 06:14:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-03-18 06:13:56 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-18 06:13:30 | Panadugama (Nilwala Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-03-18 06:13:05 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.058 |  |
| 2026-03-18 06:13:00 | Rathnapura (Kalu Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-18 06:10:49 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-03-18 06:08:55 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-18 06:07:04 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-18 06:06:48 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.052 |  |
| 2026-03-18 06:06:27 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-18 06:06:12 | Ellagawa (Kalu Ganga) | 3.78 | 🟢 Normal | 0.000 |  |
| 2026-03-18 06:05:39 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-18 06:05:39 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-18 06:04:50 | Norwood (Kelani Ganga) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-03-18 06:04:39 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-18 06:04:13 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-03-18 06:04:10 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.020 |  |
| 2026-03-18 06:04:09 | Rathnapura (Kalu Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-18 06:04:03 | Magura (Kalu Ganga) | 0.76 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-18 06:03:56 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-03-18 06:03:48 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-18 06:03:32 | Peradeniya (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.126 |  |
| 2026-03-18 06:03:25 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | -0.010 |  |
| 2026-03-18 06:03:20 | Manampitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-18 06:03:11 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-03-18 06:03:01 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | -0.041 |  |
| 2026-03-18 06:02:59 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-18 06:02:53 | Thanamalwila (Kirindi Oya) | 0.52 | 🟢 Normal | -0.030 |  |
| 2026-03-18 06:02:37 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-18 06:01:48 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-03-18 06:01:34 | Moraketiya (Walawe Ganga) | 0.68 | 🟢 Normal | -0.020 |  |
| 2026-03-18 06:00:59 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-03-18 06:00:38 | Weraganthota (Mahaweli Ganga) | -2.18 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-03-18 06:00:17 | Wellawaya (Kirindi Oya) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-03-18 05:59:20 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-03-18 05:31:47 | Moraketiya (Walawe Ganga) | 0.69 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-18 05:04:25 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-03-18 06:00:38 | Weraganthota (Mahaweli Ganga) | -2.18 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-03-18 06:03:11 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-03-18 06:04:03 | Magura (Kalu Ganga) | 0.76 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-18 06:08:55 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-18 06:04:39 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-18 06:07:04 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-18 05:04:48 | Kithulgala (Kelani Ganga) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-03-18 06:04:13 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-03-18 06:21:30 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-18 06:13:56 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-18 06:03:48 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-18 06:10:49 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-03-17 18:04:05 | Galgamuwa (Mee Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-18 06:06:12 | Ellagawa (Kalu Ganga) | 3.78 | 🟢 Normal | 0.000 |  |
| 2026-03-18 06:13:30 | Panadugama (Nilwala Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-03-18 06:05:39 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-18 06:02:37 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-18 06:05:39 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-18 06:06:27 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-18 06:03:56 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-03-18 06:00:59 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-03-18 06:03:20 | Manampitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-18 06:13:00 | Rathnapura (Kalu Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-17 18:01:54 | Thanthirimale (Malwathu Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-03-18 06:01:48 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-03-18 06:04:50 | Norwood (Kelani Ganga) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-03-18 06:14:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-03-18 06:00:17 | Wellawaya (Kirindi Oya) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-03-18 06:03:25 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | -0.010 |  |
| 2026-03-18 05:59:20 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-03-18 06:04:10 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.020 |  |
| 2026-03-18 06:01:34 | Moraketiya (Walawe Ganga) | 0.68 | 🟢 Normal | -0.020 |  |
| 2026-03-18 06:02:53 | Thanamalwila (Kirindi Oya) | 0.52 | 🟢 Normal | -0.030 |  |
| 2026-03-18 06:03:01 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | -0.041 |  |
| 2026-03-18 06:06:48 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.052 |  |
| 2026-03-18 06:13:05 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.058 |  |
| 2026-03-18 05:05:25 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | -0.088 |  |
| 2026-03-18 06:03:32 | Peradeniya (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.126 |  |

## River Water Level Charts by Station

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)