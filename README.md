# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--19_17:12:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **101,784 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-19 17:12:16 | Magura (Kalu Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-03-19 17:11:16 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-19 17:10:12 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-19 17:09:35 | Urawa (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-03-19 17:08:21 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-19 17:07:34 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-03-19 17:07:03 | Rathnapura (Kalu Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-19 17:07:02 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-19 17:06:54 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.095 |  |
| 2026-03-19 17:06:36 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-03-19 17:06:34 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-19 17:06:31 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-03-19 17:06:20 | Baddegama (Gin Ganga) | 1.48 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-19 17:05:10 | Glencourse (Kelani Ganga) | 8.64 | 🟢 Normal | -0.030 |  |
| 2026-03-19 17:05:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.51 | 🟢 Normal | -0.009 |  |
| 2026-03-19 17:04:53 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-19 17:04:38 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-03-19 17:04:34 | Thawalama (Gin Ganga) | 1.56 | 🟢 Normal | -0.022 |  |
| 2026-03-19 17:04:09 | Ellagawa (Kalu Ganga) | 4.18 | 🟢 Normal | -0.019 |  |
| 2026-03-19 17:03:57 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | -0.039 |  |
| 2026-03-19 17:03:54 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | -0.020 |  |
| 2026-03-19 17:03:46 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-19 17:03:28 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-19 17:03:24 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | -0.011 |  |
| 2026-03-19 17:03:22 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | -0.060 |  |
| 2026-03-19 17:03:13 | Hanwella (Kelani Ganga) | 0.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-19 17:03:11 | Putupaula (Kalu Ganga) | 0.84 | 🟢 Normal | -0.087 |  |
| 2026-03-19 17:03:07 | Giriulla (Maha Oya) | 1.10 | 🟢 Normal | -0.030 |  |
| 2026-03-19 17:02:48 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | -0.111 |  |
| 2026-03-19 17:02:35 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-19 17:02:30 | Thanamalwila (Kirindi Oya) | 0.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-19 17:02:06 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-19 17:01:52 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-19 17:01:48 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-19 17:01:22 | Weraganthota (Mahaweli Ganga) | -2.85 | 🟢 Normal | -0.143 |  |
| 2026-03-19 17:01:21 | Manampitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-03-19 17:00:50 | Thanthirimale (Malwathu Oya) | 1.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-19 17:00:29 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.045 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-19 17:09:35 | Urawa (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-03-19 17:00:29 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-03-19 17:04:38 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-03-19 17:02:06 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-19 17:03:13 | Hanwella (Kelani Ganga) | 0.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-19 17:06:20 | Baddegama (Gin Ganga) | 1.48 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-19 17:03:28 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-19 17:00:50 | Thanthirimale (Malwathu Oya) | 1.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-19 17:02:30 | Thanamalwila (Kirindi Oya) | 0.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-19 17:08:21 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-19 17:11:16 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-19 17:02:35 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-19 17:01:48 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-19 16:01:29 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-03-19 17:03:46 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-19 17:12:16 | Magura (Kalu Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-03-19 17:10:12 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-19 17:04:53 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-19 17:06:34 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-19 17:07:34 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-03-19 17:01:21 | Manampitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-03-19 17:07:03 | Rathnapura (Kalu Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-19 17:07:02 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-19 17:01:52 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-19 17:05:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.51 | 🟢 Normal | -0.009 |  |
| 2026-03-19 17:06:36 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-03-19 17:06:31 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-03-19 17:03:24 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | -0.011 |  |
| 2026-03-19 17:04:09 | Ellagawa (Kalu Ganga) | 4.18 | 🟢 Normal | -0.019 |  |
| 2026-03-19 17:03:54 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | -0.020 |  |
| 2026-03-19 17:04:34 | Thawalama (Gin Ganga) | 1.56 | 🟢 Normal | -0.022 |  |
| 2026-03-19 17:05:10 | Glencourse (Kelani Ganga) | 8.64 | 🟢 Normal | -0.030 |  |
| 2026-03-19 17:03:07 | Giriulla (Maha Oya) | 1.10 | 🟢 Normal | -0.030 |  |
| 2026-03-19 17:03:57 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | -0.039 |  |
| 2026-03-19 17:03:22 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | -0.060 |  |
| 2026-03-19 17:03:11 | Putupaula (Kalu Ganga) | 0.84 | 🟢 Normal | -0.087 |  |
| 2026-03-19 17:06:54 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.095 |  |
| 2026-03-19 17:02:48 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | -0.111 |  |
| 2026-03-19 17:01:22 | Weraganthota (Mahaweli Ganga) | -2.85 | 🟢 Normal | -0.143 |  |

## River Water Level Charts by Station

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)