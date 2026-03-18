# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--19_00:28:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **101,131 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-19 00:28:49 | Magura (Kalu Ganga) | 0.65 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-03-19 00:23:46 | Putupaula (Kalu Ganga) | 0.20 | 🟢 Normal | -0.044 |  |
| 2026-03-19 00:17:33 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-03-19 00:07:20 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.043 |  |
| 2026-03-19 00:07:02 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-19 00:07:01 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-19 00:06:13 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-19 00:05:33 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-03-19 00:05:09 | Ellagawa (Kalu Ganga) | 3.94 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-03-19 00:05:06 | Rathnapura (Kalu Ganga) | 1.19 | 🟢 Normal | 0.211 | 🔺 Rising |
| 2026-03-19 00:04:54 | Baddegama (Gin Ganga) | 1.05 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-19 00:04:38 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-19 00:04:35 | Manampitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-03-19 00:03:50 | Moraketiya (Walawe Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-03-19 00:03:45 | Thanamalwila (Kirindi Oya) | 0.49 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-03-19 00:03:37 | Pitabeddara (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-19 00:03:32 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.590 | 🔺 Rising |
| 2026-03-19 00:03:28 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-19 00:03:02 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-19 00:03:01 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-03-19 00:02:47 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-19 00:02:46 | Holombuwa (Kelani Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-19 00:02:31 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.590 | 🔺 Rising |
| 2026-03-19 00:01:58 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-19 00:01:58 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-03-19 00:01:57 | Glencourse (Kelani Ganga) | 8.40 | 🟢 Normal | -0.039 |  |
| 2026-03-19 00:01:49 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-19 00:01:46 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-03-19 00:01:38 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-19 00:01:33 | Peradeniya (Mahaweli Ganga) | 2.20 | 🟢 Normal | -0.168 |  |
| 2026-03-19 00:01:32 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-19 00:01:30 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-19 00:01:15 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-03-19 00:00:59 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-19 00:03:32 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.590 | 🔺 Rising |
| 2026-03-19 00:05:06 | Rathnapura (Kalu Ganga) | 1.19 | 🟢 Normal | 0.211 | 🔺 Rising |
| 2026-03-19 00:01:58 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-03-18 23:04:23 | Thawalama (Gin Ganga) | 1.41 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-03-18 23:08:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.51 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-03-19 00:05:09 | Ellagawa (Kalu Ganga) | 3.94 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-03-19 00:03:45 | Thanamalwila (Kirindi Oya) | 0.49 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-03-19 00:04:54 | Baddegama (Gin Ganga) | 1.05 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-19 00:01:49 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-19 00:01:30 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-19 00:28:49 | Magura (Kalu Ganga) | 0.65 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-03-19 00:03:01 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-03-19 00:01:46 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-03-19 00:01:32 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-19 00:00:59 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-03-19 00:01:58 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-19 00:01:38 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-19 00:17:33 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-03-18 18:02:16 | Galgamuwa (Mee Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-19 00:03:37 | Pitabeddara (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-19 00:07:02 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-19 00:04:38 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-19 00:05:33 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-03-18 22:03:30 | Panadugama (Nilwala Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-03-19 00:02:47 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-19 00:03:50 | Moraketiya (Walawe Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-03-19 00:03:02 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-19 00:06:13 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-19 00:03:28 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-19 00:01:15 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-03-19 00:02:46 | Holombuwa (Kelani Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-19 00:04:35 | Manampitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-03-18 18:02:03 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-03-18 23:15:14 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.019 |  |
| 2026-03-19 00:01:57 | Glencourse (Kelani Ganga) | 8.40 | 🟢 Normal | -0.039 |  |
| 2026-03-19 00:07:20 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.043 |  |
| 2026-03-19 00:23:46 | Putupaula (Kalu Ganga) | 0.20 | 🟢 Normal | -0.044 |  |
| 2026-03-18 18:02:41 | Weraganthota (Mahaweli Ganga) | -2.92 | 🟢 Normal | -0.088 |  |
| 2026-03-19 00:01:33 | Peradeniya (Mahaweli Ganga) | 2.20 | 🟢 Normal | -0.168 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)