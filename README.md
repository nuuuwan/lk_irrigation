# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--26_16:26:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **108,003 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-26 16:26:10 | Rathnapura (Kalu Ganga) | 0.40 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-03-26 16:14:31 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-03-26 16:14:17 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-26 16:14:05 | Pitabeddara (Nilwala Ganga) | 0.04 | 🟢 Normal | -0.018 |  |
| 2026-03-26 16:09:31 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-26 16:08:36 | Padiyathalawa (Maduru Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-26 16:06:42 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-03-26 16:06:40 | Thawalama (Gin Ganga) | 1.13 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-03-26 16:06:38 | Baddegama (Gin Ganga) | 0.88 | 🟢 Normal | -0.019 |  |
| 2026-03-26 16:06:27 | Magura (Kalu Ganga) | 0.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-26 16:06:14 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | -0.009 |  |
| 2026-03-26 16:05:55 | Nawalapitiya (Mahaweli Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-03-26 16:05:49 | Glencourse (Kelani Ganga) | 8.53 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-03-26 16:05:29 | Dunamale (Aththanagalu Oya) | 0.41 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-03-26 16:05:27 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | -0.009 |  |
| 2026-03-26 16:04:49 | Giriulla (Maha Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-26 16:04:29 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-03-26 16:04:17 | Badalgama (Maha Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-03-26 16:04:11 | Putupaula (Kalu Ganga) | 0.63 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-03-26 16:03:57 | Ellagawa (Kalu Ganga) | 3.76 | 🟢 Normal | -0.010 |  |
| 2026-03-26 16:03:36 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-03-26 16:03:34 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | -0.011 |  |
| 2026-03-26 16:03:25 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-03-26 16:03:15 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | -0.020 |  |
| 2026-03-26 16:03:11 | Panadugama (Nilwala Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-03-26 16:03:05 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-26 16:03:02 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-26 16:02:31 | Deraniyagala (Kelani Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-26 16:02:26 | Thanamalwila (Kirindi Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-03-26 16:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-03-26 16:02:04 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.049 |  |
| 2026-03-26 16:02:00 | Wellawaya (Kirindi Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-03-26 16:01:43 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-26 16:01:28 | Horowpothana (Yan Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-03-26 16:01:20 | Manampitiya (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-03-26 16:01:15 | Moragaswewa (Deduru Oya) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-26 16:00:58 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-03-26 16:00:31 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-26 16:00:17 | Weraganthota (Mahaweli Ganga) | -3.01 | 🟢 Normal | -0.152 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-26 16:05:49 | Glencourse (Kelani Ganga) | 8.53 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-03-26 16:04:11 | Putupaula (Kalu Ganga) | 0.63 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-03-26 16:06:40 | Thawalama (Gin Ganga) | 1.13 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-03-26 16:09:31 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-26 16:03:25 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-03-26 16:05:29 | Dunamale (Aththanagalu Oya) | 0.41 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-03-26 16:06:27 | Magura (Kalu Ganga) | 0.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-26 16:26:10 | Rathnapura (Kalu Ganga) | 0.40 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-03-26 16:06:42 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-03-26 16:02:00 | Wellawaya (Kirindi Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-03-26 16:00:31 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-26 16:01:15 | Moragaswewa (Deduru Oya) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-26 16:05:55 | Nawalapitiya (Mahaweli Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-03-26 16:01:43 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-26 16:04:49 | Giriulla (Maha Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-26 16:01:28 | Horowpothana (Yan Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-03-26 16:14:17 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-26 16:03:02 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-26 16:02:31 | Deraniyagala (Kelani Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-26 16:03:11 | Panadugama (Nilwala Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-03-26 16:08:36 | Padiyathalawa (Maduru Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-26 16:03:05 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-26 16:04:17 | Badalgama (Maha Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-03-26 16:01:20 | Manampitiya (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-03-26 16:00:58 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-03-26 16:14:31 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-03-26 16:03:36 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-03-26 16:02:26 | Thanamalwila (Kirindi Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-03-26 16:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-03-26 16:06:14 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | -0.009 |  |
| 2026-03-26 16:05:27 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | -0.009 |  |
| 2026-03-26 16:03:57 | Ellagawa (Kalu Ganga) | 3.76 | 🟢 Normal | -0.010 |  |
| 2026-03-26 16:04:29 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-03-26 16:03:34 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | -0.011 |  |
| 2026-03-26 16:14:05 | Pitabeddara (Nilwala Ganga) | 0.04 | 🟢 Normal | -0.018 |  |
| 2026-03-26 16:06:38 | Baddegama (Gin Ganga) | 0.88 | 🟢 Normal | -0.019 |  |
| 2026-03-26 16:03:15 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | -0.020 |  |
| 2026-03-26 16:02:04 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.049 |  |
| 2026-03-26 16:00:17 | Weraganthota (Mahaweli Ganga) | -3.01 | 🟢 Normal | -0.152 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)