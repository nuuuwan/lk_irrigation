# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--15_20:11:23-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **98,306 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-15 20:11:23 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.026 |  |
| 2026-03-15 20:10:58 | Putupaula (Kalu Ganga) | 0.44 | 🟢 Normal | -0.028 |  |
| 2026-03-15 20:09:49 | Thawalama (Gin Ganga) | 1.43 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-03-15 20:08:09 | Moragaswewa (Deduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-03-15 20:07:44 | Thaldena (Mahaweli Ganga) | 0.85 | 🟢 Normal | 0.532 | 🔺 Rising |
| 2026-03-15 20:07:31 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | -0.009 |  |
| 2026-03-15 20:06:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.68 | 🟢 Normal | -0.034 |  |
| 2026-03-15 20:06:38 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-03-15 20:05:46 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-15 20:05:32 | Badalgama (Maha Oya) | 2.16 | 🟢 Normal | -0.021 |  |
| 2026-03-15 20:04:30 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-15 20:04:21 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-03-15 20:03:58 | Kithulgala (Kelani Ganga) | 1.62 | 🟢 Normal | 0.363 | 🔺 Rising |
| 2026-03-15 20:03:57 | Nakkala (Kumbukkan Oya) | 0.82 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-15 20:03:35 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | -0.040 |  |
| 2026-03-15 20:03:27 | Padiyathalawa (Maduru Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-15 20:03:08 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-03-15 20:02:59 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-03-15 20:02:53 | Dunamale (Aththanagalu Oya) | 0.64 | 🟢 Normal | -0.020 |  |
| 2026-03-15 20:02:49 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-03-15 20:02:31 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-15 20:02:29 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-15 20:02:21 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | -0.021 |  |
| 2026-03-15 20:02:18 | Thanamalwila (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-03-15 20:01:57 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-03-15 20:01:57 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.012 |  |
| 2026-03-15 20:01:53 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-15 20:01:51 | Glencourse (Kelani Ganga) | 8.70 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-03-15 20:01:46 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-15 20:01:33 | Magura (Kalu Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-15 20:01:24 | Ellagawa (Kalu Ganga) | 3.94 | 🟢 Normal | -0.011 |  |
| 2026-03-15 20:01:06 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-03-15 20:00:41 | Manampitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | -0.050 |  |
| 2026-03-15 19:17:57 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-15 20:07:44 | Thaldena (Mahaweli Ganga) | 0.85 | 🟢 Normal | 0.532 | 🔺 Rising |
| 2026-03-15 20:03:58 | Kithulgala (Kelani Ganga) | 1.62 | 🟢 Normal | 0.363 | 🔺 Rising |
| 2026-03-15 20:03:08 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-03-15 20:09:49 | Thawalama (Gin Ganga) | 1.43 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-03-15 20:01:51 | Glencourse (Kelani Ganga) | 8.70 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-03-15 19:12:24 | Rathnapura (Kalu Ganga) | 0.43 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-03-15 20:03:57 | Nakkala (Kumbukkan Oya) | 0.82 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-15 20:01:06 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-03-15 20:08:09 | Moragaswewa (Deduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-03-15 20:01:46 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-15 20:01:57 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-03-15 18:05:04 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-03-15 20:01:33 | Magura (Kalu Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-15 20:01:53 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-15 20:04:21 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-03-15 20:03:27 | Padiyathalawa (Maduru Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-15 20:02:29 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-15 20:05:46 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-15 18:02:20 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-15 19:17:57 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-15 20:04:30 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-15 20:02:31 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-15 20:02:18 | Thanamalwila (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-03-15 20:07:31 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | -0.009 |  |
| 2026-03-15 20:02:49 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-03-15 20:02:59 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-03-15 20:06:38 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-03-15 20:01:24 | Ellagawa (Kalu Ganga) | 3.94 | 🟢 Normal | -0.011 |  |
| 2026-03-15 20:01:57 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.012 |  |
| 2026-03-15 20:02:53 | Dunamale (Aththanagalu Oya) | 0.64 | 🟢 Normal | -0.020 |  |
| 2026-03-15 20:05:32 | Badalgama (Maha Oya) | 2.16 | 🟢 Normal | -0.021 |  |
| 2026-03-15 20:02:21 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | -0.021 |  |
| 2026-03-15 20:11:23 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.026 |  |
| 2026-03-15 20:10:58 | Putupaula (Kalu Ganga) | 0.44 | 🟢 Normal | -0.028 |  |
| 2026-03-15 20:06:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.68 | 🟢 Normal | -0.034 |  |
| 2026-03-15 18:02:59 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | -0.040 |  |
| 2026-03-15 20:03:35 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | -0.040 |  |
| 2026-03-15 20:00:41 | Manampitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | -0.050 |  |
| 2026-03-15 19:11:17 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | -0.085 |  |

## River Water Level Charts by Station

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)