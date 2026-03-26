# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--26_13:18:23-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **107,883 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-26 13:18:23 | Panadugama (Nilwala Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-03-26 13:15:32 | Magura (Kalu Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-26 13:14:53 | Nawalapitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-03-26 13:14:35 | Thanamalwila (Kirindi Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-03-26 13:13:55 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-26 13:07:13 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-03-26 13:06:30 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | -0.020 |  |
| 2026-03-26 13:06:13 | Baddegama (Gin Ganga) | 0.97 | 🟢 Normal | -0.049 |  |
| 2026-03-26 13:06:12 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-26 13:06:07 | Giriulla (Maha Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-26 13:05:51 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | -0.383 |  |
| 2026-03-26 13:05:49 | Ellagawa (Kalu Ganga) | 3.77 | 🟢 Normal | 0.000 |  |
| 2026-03-26 13:05:47 | Badalgama (Maha Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-03-26 13:05:39 | Glencourse (Kelani Ganga) | 8.32 | 🟢 Normal | -0.047 |  |
| 2026-03-26 13:05:07 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-03-26 13:04:17 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | -0.383 |  |
| 2026-03-26 13:04:12 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2026-03-26 13:04:06 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-26 13:03:54 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-03-26 13:03:54 | Moragaswewa (Deduru Oya) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-26 13:03:43 | Padiyathalawa (Maduru Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-26 13:03:17 | Deraniyagala (Kelani Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-26 13:03:08 | Hanwella (Kelani Ganga) | 0.37 | 🟢 Normal | -0.020 |  |
| 2026-03-26 13:02:58 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-26 13:02:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.38 | 🟢 Normal | -0.011 |  |
| 2026-03-26 13:02:12 | Holombuwa (Kelani Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-26 13:01:55 | Wellawaya (Kirindi Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-03-26 13:01:45 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-03-26 13:01:40 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-26 13:01:40 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-26 13:01:31 | Pitabeddara (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-03-26 13:01:28 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-03-26 13:01:27 | Horowpothana (Yan Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-03-26 13:01:26 | Horowpothana (Yan Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-03-26 13:01:13 | Peradeniya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.122 |  |
| 2026-03-26 13:01:12 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-03-26 13:00:50 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.152 |  |
| 2026-03-26 13:00:16 | Weraganthota (Mahaweli Ganga) | -2.41 | 🟢 Normal | -0.238 |  |
| 2026-03-26 13:00:10 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-26 12:28:57 | Panadugama (Nilwala Ganga) | 1.94 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-26 13:04:12 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2026-03-26 13:01:45 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-03-26 13:07:13 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-03-26 13:14:53 | Nawalapitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-03-26 13:01:55 | Wellawaya (Kirindi Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-03-26 13:00:10 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-26 13:03:54 | Moragaswewa (Deduru Oya) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-26 13:01:40 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-26 13:06:07 | Giriulla (Maha Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-26 13:01:27 | Horowpothana (Yan Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-03-26 13:06:12 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-26 13:15:32 | Magura (Kalu Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-26 13:01:31 | Pitabeddara (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-03-26 13:02:58 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-26 13:03:17 | Deraniyagala (Kelani Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-26 13:05:49 | Ellagawa (Kalu Ganga) | 3.77 | 🟢 Normal | 0.000 |  |
| 2026-03-26 13:18:23 | Panadugama (Nilwala Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-03-26 13:03:43 | Padiyathalawa (Maduru Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-26 13:01:12 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-03-26 13:01:40 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-26 13:13:55 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-26 13:05:07 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-03-26 13:05:47 | Badalgama (Maha Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-03-26 13:02:12 | Holombuwa (Kelani Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-26 13:01:28 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-03-26 13:04:06 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-26 13:03:54 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-03-26 12:08:17 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-03-26 13:14:35 | Thanamalwila (Kirindi Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-03-26 13:02:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.38 | 🟢 Normal | -0.011 |  |
| 2026-03-26 12:02:46 | Rathnapura (Kalu Ganga) | 0.37 | 🟢 Normal | -0.012 |  |
| 2026-03-26 13:03:08 | Hanwella (Kelani Ganga) | 0.37 | 🟢 Normal | -0.020 |  |
| 2026-03-26 13:06:30 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | -0.020 |  |
| 2026-03-26 13:05:39 | Glencourse (Kelani Ganga) | 8.32 | 🟢 Normal | -0.047 |  |
| 2026-03-26 13:06:13 | Baddegama (Gin Ganga) | 0.97 | 🟢 Normal | -0.049 |  |
| 2026-03-26 13:01:13 | Peradeniya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.122 |  |
| 2026-03-26 13:00:50 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.152 |  |
| 2026-03-26 13:00:16 | Weraganthota (Mahaweli Ganga) | -2.41 | 🟢 Normal | -0.238 |  |
| 2026-03-26 13:05:51 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | -0.383 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)