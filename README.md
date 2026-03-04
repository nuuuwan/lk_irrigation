# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--05_00:42:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **89,382 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-05 00:42:37 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-05 00:41:07 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-05 00:40:35 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-05 00:32:49 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-03-05 00:15:55 | Panadugama (Nilwala Ganga) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-03-05 00:10:44 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-05 00:07:48 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-05 00:07:47 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-05 00:07:45 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-05 00:07:25 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | -0.009 |  |
| 2026-03-05 00:06:19 | Thawalama (Gin Ganga) | 0.96 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-05 00:06:12 | Magura (Kalu Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-05 00:06:01 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-03-05 00:06:00 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-05 00:05:58 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-03-05 00:05:09 | Hanwella (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-03-05 00:05:04 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | -0.029 |  |
| 2026-03-05 00:04:11 | Rathnapura (Kalu Ganga) | 0.40 | 🟢 Normal | -0.020 |  |
| 2026-03-05 00:03:50 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | -0.098 |  |
| 2026-03-05 00:03:44 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-05 00:03:30 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-05 00:03:23 | Glencourse (Kelani Ganga) | 8.21 | 🟢 Normal | -0.010 |  |
| 2026-03-05 00:03:22 | Padiyathalawa (Maduru Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-05 00:03:18 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | -0.038 |  |
| 2026-03-05 00:03:09 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-05 00:02:29 | Manampitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | -0.011 |  |
| 2026-03-05 00:01:57 | Nakkala (Kumbukkan Oya) | 0.89 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-05 00:01:50 | Badalgama (Maha Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-03-05 00:01:40 | Peradeniya (Mahaweli Ganga) | 2.04 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-03-05 00:01:39 | Giriulla (Maha Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-05 00:01:38 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-05 00:01:10 | Ellagawa (Kalu Ganga) | 3.84 | 🟢 Normal | 0.000 |  |
| 2026-03-05 00:00:45 | Wellawaya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-05 00:00:20 | Nawalapitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-05 00:00:18 | Moraketiya (Walawe Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-05 00:00:12 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-04 23:52:00 | Putupaula (Kalu Ganga) | 0.30 | 🟢 Normal | 0.058 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-05 00:01:40 | Peradeniya (Mahaweli Ganga) | 2.04 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-03-05 00:06:01 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-03-04 18:01:40 | Weraganthota (Mahaweli Ganga) | -1.87 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-03-04 23:52:00 | Putupaula (Kalu Ganga) | 0.30 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-03-05 00:06:19 | Thawalama (Gin Ganga) | 0.96 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-05 00:01:57 | Nakkala (Kumbukkan Oya) | 0.89 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-05 00:05:58 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-03-05 00:00:45 | Wellawaya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-04 18:01:42 | Thanthirimale (Malwathu Oya) | 0.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-05 00:03:44 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-05 00:03:09 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-05 00:00:20 | Nawalapitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-05 00:01:38 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-05 00:01:39 | Giriulla (Maha Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-05 00:41:07 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-04 18:02:59 | Galgamuwa (Mee Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-05 00:06:12 | Magura (Kalu Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-04 22:06:31 | Pitabeddara (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-03-05 00:07:48 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-05 00:05:09 | Hanwella (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-03-05 00:01:10 | Ellagawa (Kalu Ganga) | 3.84 | 🟢 Normal | 0.000 |  |
| 2026-03-05 00:15:55 | Panadugama (Nilwala Ganga) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-03-05 00:03:22 | Padiyathalawa (Maduru Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-05 00:00:18 | Moraketiya (Walawe Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-05 00:00:12 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-05 00:42:37 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-05 00:03:30 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-05 00:01:50 | Badalgama (Maha Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-03-05 00:06:00 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-05 00:40:35 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-05 00:32:49 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-03-04 21:03:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-03-05 00:07:25 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | -0.009 |  |
| 2026-03-05 00:03:23 | Glencourse (Kelani Ganga) | 8.21 | 🟢 Normal | -0.010 |  |
| 2026-03-05 00:02:29 | Manampitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | -0.011 |  |
| 2026-03-05 00:04:11 | Rathnapura (Kalu Ganga) | 0.40 | 🟢 Normal | -0.020 |  |
| 2026-03-05 00:05:04 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | -0.029 |  |
| 2026-03-05 00:03:18 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | -0.038 |  |
| 2026-03-05 00:03:50 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | -0.098 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)