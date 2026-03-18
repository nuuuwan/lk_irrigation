# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--18_21:21:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **101,029 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-18 21:21:03 | Panadugama (Nilwala Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-03-18 21:15:34 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.043 |  |
| 2026-03-18 21:13:20 | Pitabeddara (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-18 21:13:02 | Ellagawa (Kalu Ganga) | 3.88 | 🟢 Normal | 0.000 |  |
| 2026-03-18 21:08:42 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | 25.714 | 🔺 Rising |
| 2026-03-18 21:08:35 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | 25.714 | 🔺 Rising |
| 2026-03-18 21:08:34 | Holombuwa (Kelani Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-18 21:06:23 | Thanamalwila (Kirindi Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-18 21:05:35 | Panadugama (Nilwala Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-03-18 21:05:17 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-03-18 21:05:16 | Peradeniya (Mahaweli Ganga) | 1.78 | 🟢 Normal | 0.457 | 🔺 Rising |
| 2026-03-18 21:05:03 | Rathnapura (Kalu Ganga) | 0.76 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-03-18 21:04:17 | Moraketiya (Walawe Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-18 21:04:14 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-18 21:03:56 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-18 21:03:34 | Glencourse (Kelani Ganga) | 8.47 | 🟢 Normal | 0.000 |  |
| 2026-03-18 21:03:12 | Putupaula (Kalu Ganga) | 0.42 | 🟢 Normal | -0.102 |  |
| 2026-03-18 21:03:08 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | -0.174 |  |
| 2026-03-18 21:03:06 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.270 | 🔺 Rising |
| 2026-03-18 21:02:49 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-18 21:02:47 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | -0.020 |  |
| 2026-03-18 21:02:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.44 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-18 21:02:37 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-03-18 21:02:36 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | -0.020 |  |
| 2026-03-18 21:02:35 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-03-18 21:02:30 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-18 21:02:28 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-18 21:02:25 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-03-18 21:02:21 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-18 21:02:20 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-18 21:02:13 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-03-18 21:02:11 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-18 21:02:00 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-18 21:01:54 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.061 |  |
| 2026-03-18 21:01:35 | Baddegama (Gin Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-03-18 21:01:32 | Manampitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-03-18 21:01:25 | Magura (Kalu Ganga) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-18 21:01:18 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-03-18 21:01:06 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-18 21:08:42 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | 25.714 | 🔺 Rising |
| 2026-03-18 21:05:16 | Peradeniya (Mahaweli Ganga) | 1.78 | 🟢 Normal | 0.457 | 🔺 Rising |
| 2026-03-18 21:03:06 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.270 | 🔺 Rising |
| 2026-03-18 21:05:03 | Rathnapura (Kalu Ganga) | 0.76 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-03-18 21:02:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.44 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-18 21:02:30 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-18 21:01:06 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-18 21:01:25 | Magura (Kalu Ganga) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-18 21:02:49 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-18 21:02:21 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-18 21:02:00 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-18 21:05:17 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-03-18 21:01:18 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-03-18 18:02:16 | Galgamuwa (Mee Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-18 21:13:20 | Pitabeddara (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-18 21:02:28 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-18 21:02:25 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-03-18 21:13:02 | Ellagawa (Kalu Ganga) | 3.88 | 🟢 Normal | 0.000 |  |
| 2026-03-18 21:01:35 | Baddegama (Gin Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-03-18 21:21:03 | Panadugama (Nilwala Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-03-18 21:02:11 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-18 21:03:34 | Glencourse (Kelani Ganga) | 8.47 | 🟢 Normal | 0.000 |  |
| 2026-03-18 21:04:17 | Moraketiya (Walawe Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-18 21:02:37 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-03-18 21:02:20 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-18 21:03:56 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-18 21:02:35 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-03-18 21:08:34 | Holombuwa (Kelani Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-18 21:01:32 | Manampitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-03-18 18:02:03 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-03-18 21:04:14 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-18 21:06:23 | Thanamalwila (Kirindi Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-18 21:02:47 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | -0.020 |  |
| 2026-03-18 21:02:36 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | -0.020 |  |
| 2026-03-18 21:15:34 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.043 |  |
| 2026-03-18 21:01:54 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.061 |  |
| 2026-03-18 18:02:41 | Weraganthota (Mahaweli Ganga) | -2.92 | 🟢 Normal | -0.088 |  |
| 2026-03-18 21:03:12 | Putupaula (Kalu Ganga) | 0.42 | 🟢 Normal | -0.102 |  |
| 2026-03-18 21:03:08 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | -0.174 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)