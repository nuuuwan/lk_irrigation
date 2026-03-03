# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--03_11:22:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **88,003 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-03 11:22:37 | Panadugama (Nilwala Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-03-03 11:14:58 | Weraganthota (Mahaweli Ganga) | -1.72 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-03-03 11:14:23 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | -0.005 |  |
| 2026-03-03 11:12:24 | Panadugama (Nilwala Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-03-03 11:09:34 | Putupaula (Kalu Ganga) | 0.25 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-03-03 11:09:19 | Magura (Kalu Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-03-03 11:09:17 | Dunamale (Aththanagalu Oya) | 0.77 | 🟢 Normal | -0.027 |  |
| 2026-03-03 11:08:35 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-03 11:07:34 | Badalgama (Maha Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-03-03 11:06:53 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | -0.009 |  |
| 2026-03-03 11:06:25 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-03 11:06:03 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-03-03 11:05:52 | Thalgahagoda (Nilwala Ganga) | 0.15 | 🟢 Normal | -0.010 |  |
| 2026-03-03 11:05:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-03-03 11:05:11 | Moraketiya (Walawe Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-03 11:05:08 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-03 11:05:01 | Wellawaya (Kirindi Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-03-03 11:04:46 | Rathnapura (Kalu Ganga) | 0.48 | 🟢 Normal | -0.012 |  |
| 2026-03-03 11:04:38 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-03 11:04:27 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.149 | 🔺 Rising |
| 2026-03-03 11:04:22 | Pitabeddara (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-03 11:04:19 | Padiyathalawa (Maduru Oya) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-03-03 11:03:31 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.299 | 🔺 Rising |
| 2026-03-03 11:03:30 | Hanwella (Kelani Ganga) | 0.31 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-03 11:03:20 | Glencourse (Kelani Ganga) | 8.36 | 🟢 Normal | -0.050 |  |
| 2026-03-03 11:03:16 | Norwood (Kelani Ganga) | 0.32 | 🟢 Normal | -0.040 |  |
| 2026-03-03 11:03:06 | Thawalama (Gin Ganga) | 0.90 | 🟢 Normal | -0.059 |  |
| 2026-03-03 11:03:02 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-03-03 11:02:53 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-03 11:02:37 | Peradeniya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-03 11:02:33 | Giriulla (Maha Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-03-03 11:02:27 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-03 11:02:25 | Ellagawa (Kalu Ganga) | 3.87 | 🟢 Normal | -0.010 |  |
| 2026-03-03 11:01:49 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-03 11:01:48 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-03 11:01:45 | Manampitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-03-03 11:01:19 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-03-03 11:00:08 | Thanthirimale (Malwathu Oya) | 0.88 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-03 11:00:06 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-03 11:03:31 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.299 | 🔺 Rising |
| 2026-03-03 11:04:27 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.149 | 🔺 Rising |
| 2026-03-03 11:09:34 | Putupaula (Kalu Ganga) | 0.25 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-03-03 11:01:45 | Manampitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-03-03 11:03:30 | Hanwella (Kelani Ganga) | 0.31 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-03 11:02:37 | Peradeniya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-03 11:00:08 | Thanthirimale (Malwathu Oya) | 0.88 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-03 11:14:58 | Weraganthota (Mahaweli Ganga) | -1.72 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-03-03 11:05:01 | Wellawaya (Kirindi Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-03-03 11:00:06 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-03-03 11:01:48 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-03 11:02:27 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-03 11:01:49 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-03 11:02:33 | Giriulla (Maha Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-03-03 11:04:38 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-03 11:05:08 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-03 11:04:22 | Pitabeddara (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-03 11:03:02 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-03-03 11:22:37 | Panadugama (Nilwala Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-03-03 11:05:11 | Moraketiya (Walawe Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-03 11:07:34 | Badalgama (Maha Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-03-03 11:06:03 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-03-03 11:08:35 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-03 11:06:25 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-03 11:02:53 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-03 11:05:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-03-03 11:14:23 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | -0.005 |  |
| 2026-03-03 10:05:23 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | -0.009 |  |
| 2026-03-03 11:06:53 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | -0.009 |  |
| 2026-03-03 11:09:19 | Magura (Kalu Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-03-03 11:01:19 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-03-03 11:04:19 | Padiyathalawa (Maduru Oya) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-03-03 11:02:25 | Ellagawa (Kalu Ganga) | 3.87 | 🟢 Normal | -0.010 |  |
| 2026-03-03 11:05:52 | Thalgahagoda (Nilwala Ganga) | 0.15 | 🟢 Normal | -0.010 |  |
| 2026-03-03 11:04:46 | Rathnapura (Kalu Ganga) | 0.48 | 🟢 Normal | -0.012 |  |
| 2026-03-03 11:09:17 | Dunamale (Aththanagalu Oya) | 0.77 | 🟢 Normal | -0.027 |  |
| 2026-03-03 11:03:16 | Norwood (Kelani Ganga) | 0.32 | 🟢 Normal | -0.040 |  |
| 2026-03-03 11:03:20 | Glencourse (Kelani Ganga) | 8.36 | 🟢 Normal | -0.050 |  |
| 2026-03-03 11:03:06 | Thawalama (Gin Ganga) | 0.90 | 🟢 Normal | -0.059 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

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

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)