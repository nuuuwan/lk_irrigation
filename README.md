# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--16_14:17:55-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **98,976 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-16 14:17:55 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-16 14:17:29 | Horowpothana (Yan Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-03-16 14:12:11 | Magura (Kalu Ganga) | 0.60 | 🟢 Normal | -0.012 |  |
| 2026-03-16 14:11:28 | Baddegama (Gin Ganga) | 0.78 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-03-16 14:10:25 | Weraganthota (Mahaweli Ganga) | -2.42 | 🟢 Normal | -0.043 |  |
| 2026-03-16 14:08:33 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-16 14:08:31 | Rathnapura (Kalu Ganga) | 0.44 | 🟢 Normal | -0.026 |  |
| 2026-03-16 14:07:46 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.037 |  |
| 2026-03-16 14:07:27 | Glencourse (Kelani Ganga) | 8.61 | 🟢 Normal | -0.065 |  |
| 2026-03-16 14:06:14 | Panadugama (Nilwala Ganga) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-03-16 14:06:13 | Thawalama (Gin Ganga) | 1.17 | 🟢 Normal | -0.050 |  |
| 2026-03-16 14:05:55 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-16 14:05:04 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-16 14:04:57 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-16 14:04:51 | Moragaswewa (Deduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-03-16 14:04:27 | Deraniyagala (Kelani Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-03-16 14:04:10 | Galgamuwa (Mee Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-16 14:04:06 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-16 14:04:01 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | -0.011 |  |
| 2026-03-16 14:03:56 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-16 14:03:42 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-16 14:03:32 | Padiyathalawa (Maduru Oya) | 0.44 | 🟢 Normal | -0.018 |  |
| 2026-03-16 14:03:04 | Dunamale (Aththanagalu Oya) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-03-16 14:02:59 | Giriulla (Maha Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-03-16 14:02:45 | Peradeniya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.022 |  |
| 2026-03-16 14:02:39 | Thanamalwila (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-03-16 14:02:32 | Moraketiya (Walawe Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-03-16 14:02:20 | Nawalapitiya (Mahaweli Ganga) | 0.67 | 🟢 Normal | -0.020 |  |
| 2026-03-16 14:02:19 | Manampitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-03-16 14:02:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-16 14:02:08 | Badalgama (Maha Oya) | 1.94 | 🟢 Normal | -0.010 |  |
| 2026-03-16 14:01:38 | Nakkala (Kumbukkan Oya) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-03-16 14:01:29 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | -0.011 |  |
| 2026-03-16 14:01:26 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-03-16 14:01:12 | Ellagawa (Kalu Ganga) | 3.90 | 🟢 Normal | 0.000 |  |
| 2026-03-16 14:01:11 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-03-16 14:01:09 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | -0.020 |  |
| 2026-03-16 14:00:46 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-16 14:00:20 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | 0.020 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-16 14:11:28 | Baddegama (Gin Ganga) | 0.78 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-03-16 14:02:19 | Manampitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-03-16 14:01:26 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-03-16 14:00:20 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-16 14:02:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-16 14:01:11 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-03-16 14:00:46 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-16 14:04:57 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-16 14:04:06 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-16 14:04:51 | Moragaswewa (Deduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-03-16 14:17:55 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-16 14:02:59 | Giriulla (Maha Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-03-16 14:17:29 | Horowpothana (Yan Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-03-16 14:04:10 | Galgamuwa (Mee Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-16 14:08:33 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-16 14:03:42 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-16 14:04:27 | Deraniyagala (Kelani Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-03-16 14:01:12 | Ellagawa (Kalu Ganga) | 3.90 | 🟢 Normal | 0.000 |  |
| 2026-03-16 14:06:14 | Panadugama (Nilwala Ganga) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-03-16 14:05:04 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-16 14:03:56 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-16 14:05:55 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-16 14:02:39 | Thanamalwila (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-03-16 14:03:04 | Dunamale (Aththanagalu Oya) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-03-16 14:02:32 | Moraketiya (Walawe Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-03-16 14:01:38 | Nakkala (Kumbukkan Oya) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-03-16 14:02:08 | Badalgama (Maha Oya) | 1.94 | 🟢 Normal | -0.010 |  |
| 2026-03-16 14:04:01 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | -0.011 |  |
| 2026-03-16 14:01:29 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | -0.011 |  |
| 2026-03-16 14:12:11 | Magura (Kalu Ganga) | 0.60 | 🟢 Normal | -0.012 |  |
| 2026-03-16 14:03:32 | Padiyathalawa (Maduru Oya) | 0.44 | 🟢 Normal | -0.018 |  |
| 2026-03-16 14:02:20 | Nawalapitiya (Mahaweli Ganga) | 0.67 | 🟢 Normal | -0.020 |  |
| 2026-03-16 14:01:09 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | -0.020 |  |
| 2026-03-16 14:02:45 | Peradeniya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.022 |  |
| 2026-03-16 14:08:31 | Rathnapura (Kalu Ganga) | 0.44 | 🟢 Normal | -0.026 |  |
| 2026-03-16 14:07:46 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.037 |  |
| 2026-03-16 14:10:25 | Weraganthota (Mahaweli Ganga) | -2.42 | 🟢 Normal | -0.043 |  |
| 2026-03-16 14:06:13 | Thawalama (Gin Ganga) | 1.17 | 🟢 Normal | -0.050 |  |
| 2026-03-16 14:07:27 | Glencourse (Kelani Ganga) | 8.61 | 🟢 Normal | -0.065 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)