# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--12_22:13:24-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **204,585 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-12 22:13:24 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-12 22:09:30 | Panadugama (Nilwala Ganga) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-07-12 22:09:22 | Putupaula (Kalu Ganga) | 0.15 | 🟢 Normal | -0.018 |  |
| 2026-07-12 22:07:05 | Baddegama (Gin Ganga) | 0.98 | 🟢 Normal | -0.031 |  |
| 2026-07-12 22:06:35 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-07-12 22:06:28 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-07-12 22:05:51 | Glencourse (Kelani Ganga) | 9.15 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-07-12 22:05:22 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-12 22:05:06 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-07-12 22:04:42 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-07-12 22:04:14 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-07-12 22:03:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.62 | 🟢 Normal | -0.020 |  |
| 2026-07-12 22:03:37 | Rathnapura (Kalu Ganga) | 0.92 | 🟢 Normal | -0.020 |  |
| 2026-07-12 22:03:32 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-07-12 22:03:28 | Magura (Kalu Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-07-12 22:03:27 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-12 22:03:15 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-12 22:03:14 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-07-12 22:02:41 | Thanamalwila (Kirindi Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-07-12 22:02:39 | Badalgama (Maha Oya) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-07-12 22:02:26 | Hanwella (Kelani Ganga) | 0.96 | 🟢 Normal | -0.020 |  |
| 2026-07-12 22:02:14 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-07-12 22:02:10 | Thalgahagoda (Nilwala Ganga) | 0.04 | 🟢 Normal | -0.054 |  |
| 2026-07-12 22:02:08 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-12 22:01:58 | Nawalapitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-07-12 22:01:56 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-12 22:01:54 | Peradeniya (Mahaweli Ganga) | 2.23 | 🟢 Normal | 0.245 | 🔺 Rising |
| 2026-07-12 22:01:39 | Pitabeddara (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-07-12 22:01:31 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-12 22:01:05 | Ellagawa (Kalu Ganga) | 4.38 | 🟢 Normal | -0.010 |  |
| 2026-07-12 22:01:03 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-07-12 22:01:01 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | -0.010 |  |
| 2026-07-12 22:00:41 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-12 22:01:54 | Peradeniya (Mahaweli Ganga) | 2.23 | 🟢 Normal | 0.245 | 🔺 Rising |
| 2026-07-12 22:05:51 | Glencourse (Kelani Ganga) | 9.15 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-07-12 22:04:42 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-07-12 22:01:56 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-12 22:02:14 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-07-12 18:00:50 | Weraganthota (Mahaweli Ganga) | -3.39 | 🟢 Normal | 0.000 |  |
| 2026-07-12 22:02:08 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-12 22:01:31 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-12 22:01:03 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-07-12 22:01:58 | Nawalapitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-07-12 21:05:40 | Yaka Wewa (Ma Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-12 22:06:35 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-07-12 22:00:41 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-12 18:02:26 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-12 22:03:28 | Magura (Kalu Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-07-12 22:01:39 | Pitabeddara (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-07-12 22:03:14 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-07-12 22:04:14 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-07-12 22:09:30 | Panadugama (Nilwala Ganga) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-07-12 22:03:15 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-12 22:03:32 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-07-12 22:03:27 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-12 21:04:17 | Dunamale (Aththanagalu Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-07-12 22:13:24 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-12 22:02:39 | Badalgama (Maha Oya) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-07-12 21:05:04 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-07-12 18:01:22 | Thanthirimale (Malwathu Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-07-12 22:05:22 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-12 22:05:06 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-07-12 22:02:41 | Thanamalwila (Kirindi Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-07-12 22:06:28 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-07-12 22:01:05 | Ellagawa (Kalu Ganga) | 4.38 | 🟢 Normal | -0.010 |  |
| 2026-07-12 22:01:01 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | -0.010 |  |
| 2026-07-12 22:09:22 | Putupaula (Kalu Ganga) | 0.15 | 🟢 Normal | -0.018 |  |
| 2026-07-12 22:02:26 | Hanwella (Kelani Ganga) | 0.96 | 🟢 Normal | -0.020 |  |
| 2026-07-12 22:03:37 | Rathnapura (Kalu Ganga) | 0.92 | 🟢 Normal | -0.020 |  |
| 2026-07-12 22:03:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.62 | 🟢 Normal | -0.020 |  |
| 2026-07-12 22:07:05 | Baddegama (Gin Ganga) | 0.98 | 🟢 Normal | -0.031 |  |
| 2026-07-12 22:02:10 | Thalgahagoda (Nilwala Ganga) | 0.04 | 🟢 Normal | -0.054 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)