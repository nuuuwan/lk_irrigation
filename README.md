# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--15_14:28:38-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **98,078 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-15 14:28:38 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-03-15 14:27:06 | Baddegama (Gin Ganga) | 1.60 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-15 14:12:13 | Peradeniya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-03-15 14:10:28 | Padiyathalawa (Maduru Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-15 14:10:10 | Badalgama (Maha Oya) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-03-15 14:09:18 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | -0.009 |  |
| 2026-03-15 14:09:01 | Moragaswewa (Deduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-03-15 14:08:49 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-03-15 14:08:45 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | -0.009 |  |
| 2026-03-15 14:07:09 | Moraketiya (Walawe Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-15 14:06:47 | Moragaswewa (Deduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-03-15 14:06:11 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-03-15 14:05:34 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-15 14:05:10 | Padiyathalawa (Maduru Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-15 14:05:05 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-03-15 14:04:38 | Dunamale (Aththanagalu Oya) | 0.76 | 🟢 Normal | -0.027 |  |
| 2026-03-15 14:04:29 | Nagalagam Street (Kelani Ganga) | 0.50 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-03-15 14:03:57 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-15 14:03:49 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-03-15 14:03:45 | Glencourse (Kelani Ganga) | 8.68 | 🟢 Normal | -0.020 |  |
| 2026-03-15 14:03:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.91 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-03-15 14:03:16 | Giriulla (Maha Oya) | 1.10 | 🟢 Normal | -0.020 |  |
| 2026-03-15 14:03:11 | Thanamalwila (Kirindi Oya) | 0.93 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-15 14:03:06 | Hanwella (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-15 14:03:06 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-15 14:02:54 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.011 |  |
| 2026-03-15 14:02:44 | Magura (Kalu Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-15 14:02:16 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | -0.010 |  |
| 2026-03-15 14:02:15 | Thawalama (Gin Ganga) | 1.47 | 🟢 Normal | -0.052 |  |
| 2026-03-15 14:02:11 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | -0.020 |  |
| 2026-03-15 14:02:00 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-03-15 14:01:53 | Rathnapura (Kalu Ganga) | 0.46 | 🟢 Normal | -0.030 |  |
| 2026-03-15 14:01:17 | Nawalapitiya (Mahaweli Ganga) | 0.67 | 🟢 Normal | -0.024 |  |
| 2026-03-15 14:01:15 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-15 14:01:14 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-15 14:01:08 | Ellagawa (Kalu Ganga) | 4.00 | 🟢 Normal | 0.000 |  |
| 2026-03-15 14:01:07 | Thanthirimale (Malwathu Oya) | 1.17 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-15 14:00:48 | Manampitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-03-15 14:00:30 | Weraganthota (Mahaweli Ganga) | -2.64 | 🟢 Normal | -0.129 |  |
| 2026-03-15 14:00:14 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-15 14:28:38 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-03-15 14:03:49 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-03-15 14:04:29 | Nagalagam Street (Kelani Ganga) | 0.50 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-03-15 14:00:48 | Manampitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-03-15 14:03:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.91 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-03-15 14:03:11 | Thanamalwila (Kirindi Oya) | 0.93 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-15 14:02:00 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-03-15 14:27:06 | Baddegama (Gin Ganga) | 1.60 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-15 14:12:13 | Peradeniya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-03-15 14:01:07 | Thanthirimale (Malwathu Oya) | 1.17 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-15 14:09:01 | Moragaswewa (Deduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-03-15 12:01:43 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-15 14:02:44 | Magura (Kalu Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-15 14:05:34 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-15 14:03:06 | Hanwella (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-15 14:01:08 | Ellagawa (Kalu Ganga) | 4.00 | 🟢 Normal | 0.000 |  |
| 2026-03-15 14:08:49 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-03-15 14:10:28 | Padiyathalawa (Maduru Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-15 14:07:09 | Moraketiya (Walawe Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-15 14:03:06 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-15 14:01:15 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-15 14:10:10 | Badalgama (Maha Oya) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-03-15 14:03:57 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-15 14:01:14 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-15 14:09:18 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | -0.009 |  |
| 2026-03-15 14:08:45 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | -0.009 |  |
| 2026-03-15 14:05:05 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-03-15 14:06:11 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-03-15 14:00:14 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-03-15 14:02:16 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | -0.010 |  |
| 2026-03-15 14:02:54 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.011 |  |
| 2026-03-15 14:03:16 | Giriulla (Maha Oya) | 1.10 | 🟢 Normal | -0.020 |  |
| 2026-03-15 14:02:11 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | -0.020 |  |
| 2026-03-15 14:03:45 | Glencourse (Kelani Ganga) | 8.68 | 🟢 Normal | -0.020 |  |
| 2026-03-15 14:01:17 | Nawalapitiya (Mahaweli Ganga) | 0.67 | 🟢 Normal | -0.024 |  |
| 2026-03-15 14:04:38 | Dunamale (Aththanagalu Oya) | 0.76 | 🟢 Normal | -0.027 |  |
| 2026-03-15 14:01:53 | Rathnapura (Kalu Ganga) | 0.46 | 🟢 Normal | -0.030 |  |
| 2026-03-15 14:02:15 | Thawalama (Gin Ganga) | 1.47 | 🟢 Normal | -0.052 |  |
| 2026-03-15 14:00:30 | Weraganthota (Mahaweli Ganga) | -2.64 | 🟢 Normal | -0.129 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

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

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)