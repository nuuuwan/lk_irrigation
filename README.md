# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--20_15:11:07-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **102,595 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-20 15:11:07 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-03-20 15:09:30 | Baddegama (Gin Ganga) | 0.96 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-03-20 15:07:43 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-03-20 15:05:54 | Rathnapura (Kalu Ganga) | 0.95 | 🟢 Normal | -0.020 |  |
| 2026-03-20 15:05:53 | Panadugama (Nilwala Ganga) | 2.27 | 🟢 Normal | -0.010 |  |
| 2026-03-20 15:05:10 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | -0.028 |  |
| 2026-03-20 15:04:49 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-03-20 15:04:45 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-20 15:04:24 | Badalgama (Maha Oya) | 1.98 | 🟢 Normal | -0.010 |  |
| 2026-03-20 15:04:13 | Thawalama (Gin Ganga) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-03-20 15:04:08 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-20 15:04:04 | Magura (Kalu Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-03-20 15:03:46 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-03-20 15:03:43 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-03-20 15:03:35 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | 0.146 | 🔺 Rising |
| 2026-03-20 15:03:24 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-03-20 15:03:15 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-20 15:03:13 | Thanamalwila (Kirindi Oya) | 0.68 | 🟢 Normal | -0.031 |  |
| 2026-03-20 15:03:10 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.022 |  |
| 2026-03-20 15:03:09 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-03-20 15:03:09 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-20 15:03:08 | Hanwella (Kelani Ganga) | 0.51 | 🟢 Normal | -0.030 |  |
| 2026-03-20 15:03:06 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-03-20 15:02:50 | Glencourse (Kelani Ganga) | 8.44 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-03-20 15:02:48 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | -0.050 |  |
| 2026-03-20 15:02:41 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-20 15:02:35 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.103 |  |
| 2026-03-20 15:02:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.95 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-20 15:01:54 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-20 15:01:35 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-03-20 15:01:34 | Weraganthota (Mahaweli Ganga) | -2.58 | 🟢 Normal | -0.070 |  |
| 2026-03-20 15:01:31 | Thanthirimale (Malwathu Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-03-20 15:01:24 | Kithulgala (Kelani Ganga) | 1.38 | 🟢 Normal | -0.020 |  |
| 2026-03-20 15:01:05 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-03-20 15:01:03 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-20 15:01:00 | Manampitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.093 |  |
| 2026-03-20 15:00:22 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-03-20 15:00:16 | Horowpothana (Yan Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-03-20 15:00:11 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-03-20 14:46:04 | Horowpothana (Yan Oya) | 1.22 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-20 15:03:35 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | 0.146 | 🔺 Rising |
| 2026-03-20 15:03:24 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-03-20 15:02:50 | Glencourse (Kelani Ganga) | 8.44 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-03-20 15:01:05 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-03-20 15:02:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.95 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-20 15:04:45 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-20 15:09:30 | Baddegama (Gin Ganga) | 0.96 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-03-20 15:00:22 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-03-20 15:03:09 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-20 15:01:03 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-20 15:01:54 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-20 15:00:16 | Horowpothana (Yan Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-03-20 15:03:15 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-20 15:04:04 | Magura (Kalu Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-03-20 15:04:08 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-20 15:07:43 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-03-20 15:00:11 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-03-20 15:03:43 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-03-20 15:02:41 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-20 15:01:31 | Thanthirimale (Malwathu Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-03-20 15:11:07 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-03-20 15:03:06 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-03-20 15:04:49 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-03-20 15:05:53 | Panadugama (Nilwala Ganga) | 2.27 | 🟢 Normal | -0.010 |  |
| 2026-03-20 15:03:09 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-03-20 15:04:24 | Badalgama (Maha Oya) | 1.98 | 🟢 Normal | -0.010 |  |
| 2026-03-20 15:01:35 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-03-20 15:04:13 | Thawalama (Gin Ganga) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-03-20 15:05:54 | Rathnapura (Kalu Ganga) | 0.95 | 🟢 Normal | -0.020 |  |
| 2026-03-20 15:01:24 | Kithulgala (Kelani Ganga) | 1.38 | 🟢 Normal | -0.020 |  |
| 2026-03-20 15:03:10 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.022 |  |
| 2026-03-20 15:05:10 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | -0.028 |  |
| 2026-03-20 15:03:08 | Hanwella (Kelani Ganga) | 0.51 | 🟢 Normal | -0.030 |  |
| 2026-03-20 14:01:53 | Ellagawa (Kalu Ganga) | 4.47 | 🟢 Normal | -0.030 |  |
| 2026-03-20 15:03:13 | Thanamalwila (Kirindi Oya) | 0.68 | 🟢 Normal | -0.031 |  |
| 2026-03-20 15:02:48 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | -0.050 |  |
| 2026-03-20 15:01:34 | Weraganthota (Mahaweli Ganga) | -2.58 | 🟢 Normal | -0.070 |  |
| 2026-03-20 15:01:00 | Manampitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.093 |  |
| 2026-03-20 15:02:35 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.103 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)