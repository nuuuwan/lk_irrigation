# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--01_16:11:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **86,398 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-01 16:11:20 | Horowpothana (Yan Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-03-01 16:10:26 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-03-01 16:10:04 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-01 16:09:47 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-01 16:09:37 | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-03-01 16:09:18 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-01 16:08:38 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-01 16:07:29 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-03-01 16:07:23 | Putupaula (Kalu Ganga) | 0.72 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-03-01 16:06:46 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.018 |  |
| 2026-03-01 16:06:15 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.057 |  |
| 2026-03-01 16:05:57 | Padiyathalawa (Maduru Oya) | 0.72 | 🟢 Normal | -0.020 |  |
| 2026-03-01 16:05:35 | Panadugama (Nilwala Ganga) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-03-01 16:04:37 | Glencourse (Kelani Ganga) | 8.32 | 🟢 Normal | -0.038 |  |
| 2026-03-01 16:04:36 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | -0.010 |  |
| 2026-03-01 16:04:35 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-01 16:04:22 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-01 16:04:21 | Manampitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-03-01 16:04:13 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.011 |  |
| 2026-03-01 16:03:58 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-01 16:03:55 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-03-01 16:03:23 | Thanthirimale (Malwathu Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-03-01 16:03:23 | Thanamalwila (Kirindi Oya) | 0.57 | 🟢 Normal | -0.011 |  |
| 2026-03-01 16:03:14 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-03-01 16:03:14 | Thawalama (Gin Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-03-01 16:02:59 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.010 |  |
| 2026-03-01 16:02:31 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-03-01 16:02:21 | Dunamale (Aththanagalu Oya) | 0.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-01 16:02:17 | Pitabeddara (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.010 |  |
| 2026-03-01 16:02:15 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-01 16:02:03 | Ellagawa (Kalu Ganga) | 4.08 | 🟢 Normal | -0.020 |  |
| 2026-03-01 16:02:00 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-01 16:01:55 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-03-01 16:01:25 | Weraganthota (Mahaweli Ganga) | -2.47 | 🟢 Normal | -0.092 |  |
| 2026-03-01 16:01:19 | Rathnapura (Kalu Ganga) | 0.46 | 🟢 Normal | -0.057 |  |
| 2026-03-01 16:00:38 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-03-01 16:00:37 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-01 16:07:23 | Putupaula (Kalu Ganga) | 0.72 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-03-01 15:06:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.60 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-03-01 15:13:55 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-01 16:02:21 | Dunamale (Aththanagalu Oya) | 0.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-01 16:01:55 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-03-01 16:00:38 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-03-01 16:09:18 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-01 16:02:15 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-01 16:03:58 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-01 16:07:29 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-03-01 16:11:20 | Horowpothana (Yan Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-03-01 16:09:47 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-01 16:09:37 | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-03-01 16:10:04 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-01 16:10:26 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-03-01 16:05:35 | Panadugama (Nilwala Ganga) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-03-01 16:04:35 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-01 16:02:00 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-01 16:08:38 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-01 16:04:21 | Manampitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-03-01 16:03:14 | Thawalama (Gin Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-03-01 16:04:22 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-01 15:06:08 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | -0.010 |  |
| 2026-03-01 16:04:36 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | -0.010 |  |
| 2026-03-01 16:03:14 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-03-01 16:03:55 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-03-01 16:03:23 | Thanthirimale (Malwathu Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-03-01 16:02:59 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.010 |  |
| 2026-03-01 16:02:31 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-03-01 16:02:17 | Pitabeddara (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.010 |  |
| 2026-03-01 16:03:23 | Thanamalwila (Kirindi Oya) | 0.57 | 🟢 Normal | -0.011 |  |
| 2026-03-01 16:04:13 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.011 |  |
| 2026-03-01 16:06:46 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.018 |  |
| 2026-03-01 16:02:03 | Ellagawa (Kalu Ganga) | 4.08 | 🟢 Normal | -0.020 |  |
| 2026-03-01 16:05:57 | Padiyathalawa (Maduru Oya) | 0.72 | 🟢 Normal | -0.020 |  |
| 2026-03-01 16:04:37 | Glencourse (Kelani Ganga) | 8.32 | 🟢 Normal | -0.038 |  |
| 2026-03-01 16:01:19 | Rathnapura (Kalu Ganga) | 0.46 | 🟢 Normal | -0.057 |  |
| 2026-03-01 16:06:15 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.057 |  |
| 2026-03-01 16:01:25 | Weraganthota (Mahaweli Ganga) | -2.47 | 🟢 Normal | -0.092 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)