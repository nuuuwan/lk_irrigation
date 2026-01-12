# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--12_23:10:35-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **43,979 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-12 23:10:35 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | -0.017 |  |
| 2026-01-12 23:10:14 | Nakkala (Kumbukkan Oya) | 1.42 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-12 23:10:06 | Putupaula (Kalu Ganga) | 0.41 | 🟢 Normal | -0.094 |  |
| 2026-01-12 23:09:55 | Horowpothana (Yan Oya) | 3.32 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-01-12 23:07:43 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-12 23:07:22 | Glencourse (Kelani Ganga) | 9.31 | 🟢 Normal | -0.010 |  |
| 2026-01-12 23:07:18 | Giriulla (Maha Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-01-12 23:07:05 | Hanwella (Kelani Ganga) | 0.96 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-01-12 23:06:01 | Giriulla (Maha Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-01-12 23:05:35 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | -0.009 |  |
| 2026-01-12 23:04:57 | Badalgama (Maha Oya) | 2.36 | 🟢 Normal | -0.010 |  |
| 2026-01-12 23:04:41 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-01-12 23:04:18 | Dunamale (Aththanagalu Oya) | 1.52 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-01-12 23:04:14 | Padiyathalawa (Maduru Oya) | 1.36 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-01-12 23:04:13 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-01-12 23:04:12 | Rathnapura (Kalu Ganga) | 0.62 | 🟢 Normal | -0.021 |  |
| 2026-01-12 23:04:05 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-12 23:03:34 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-12 23:03:31 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-01-12 23:03:17 | Panadugama (Nilwala Ganga) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-01-12 23:03:06 | Deraniyagala (Kelani Ganga) | 0.36 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-12 23:02:50 | Peradeniya (Mahaweli Ganga) | 2.65 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-01-12 23:02:37 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-01-12 23:02:16 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-12 23:02:01 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-12 23:01:53 | Baddegama (Gin Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-12 23:01:47 | Moragaswewa (Deduru Oya) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-01-12 23:01:42 | Yaka Wewa (Ma Oya) | 1.22 | 🟢 Normal | -0.202 |  |
| 2026-01-12 23:01:15 | Ellagawa (Kalu Ganga) | 4.11 | 🟢 Normal | 0.000 |  |
| 2026-01-12 23:01:11 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-01-12 23:01:11 | Holombuwa (Kelani Ganga) | 0.76 | 🟢 Normal | -0.046 |  |
| 2026-01-12 23:01:07 | Manampitiya (Mahaweli Ganga) | 2.04 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-01-12 23:00:33 | Siyambalanduwa (Heda Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-01-12 23:00:10 | Magura (Kalu Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-01-12 22:21:51 | Giriulla (Maha Oya) | 1.17 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-12 23:02:50 | Peradeniya (Mahaweli Ganga) | 2.65 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-01-12 23:04:18 | Dunamale (Aththanagalu Oya) | 1.52 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-01-12 23:04:14 | Padiyathalawa (Maduru Oya) | 1.36 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-01-12 23:09:55 | Horowpothana (Yan Oya) | 3.32 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-01-12 23:01:07 | Manampitiya (Mahaweli Ganga) | 2.04 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-01-12 23:07:05 | Hanwella (Kelani Ganga) | 0.96 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-01-12 23:03:06 | Deraniyagala (Kelani Ganga) | 0.36 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-12 23:10:14 | Nakkala (Kumbukkan Oya) | 1.42 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-12 18:00:10 | Weraganthota (Mahaweli Ganga) | -1.45 | 🟢 Normal | 0.000 |  |
| 2026-01-12 23:04:41 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-01-12 23:02:01 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-12 23:07:18 | Giriulla (Maha Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-01-12 18:04:27 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-12 23:03:34 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-12 23:02:16 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-12 23:01:15 | Ellagawa (Kalu Ganga) | 4.11 | 🟢 Normal | 0.000 |  |
| 2026-01-12 23:01:53 | Baddegama (Gin Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-12 23:03:17 | Panadugama (Nilwala Ganga) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-01-12 23:04:05 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-12 22:00:12 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-12 23:00:33 | Siyambalanduwa (Heda Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-01-12 23:07:43 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-12 18:02:58 | Thanthirimale (Malwathu Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-12 23:03:31 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-01-12 23:02:37 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-01-12 23:01:11 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-01-12 23:05:35 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | -0.009 |  |
| 2026-01-12 23:04:13 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-01-12 23:07:22 | Glencourse (Kelani Ganga) | 9.31 | 🟢 Normal | -0.010 |  |
| 2026-01-12 23:01:47 | Moragaswewa (Deduru Oya) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-01-12 23:00:10 | Magura (Kalu Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-01-12 22:07:04 | Thanamalwila (Kirindi Oya) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-01-12 23:04:57 | Badalgama (Maha Oya) | 2.36 | 🟢 Normal | -0.010 |  |
| 2026-01-12 23:10:35 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | -0.017 |  |
| 2026-01-12 23:04:12 | Rathnapura (Kalu Ganga) | 0.62 | 🟢 Normal | -0.021 |  |
| 2026-01-12 22:01:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.56 | 🟢 Normal | -0.021 |  |
| 2026-01-12 23:01:11 | Holombuwa (Kelani Ganga) | 0.76 | 🟢 Normal | -0.046 |  |
| 2026-01-12 23:10:06 | Putupaula (Kalu Ganga) | 0.41 | 🟢 Normal | -0.094 |  |
| 2026-01-12 23:01:42 | Yaka Wewa (Ma Oya) | 1.22 | 🟢 Normal | -0.202 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)