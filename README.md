# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--12_10:05:41-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **43,470 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-12 10:05:41 | Katharagama (Menik Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-01-12 10:05:35 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | -0.021 |  |
| 2026-01-12 10:05:13 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | -0.009 |  |
| 2026-01-12 10:05:13 | Siyambalanduwa (Heda Oya) | 1.07 | 🟢 Normal | -0.009 |  |
| 2026-01-12 10:04:41 | Magura (Kalu Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-12 10:04:37 | Hanwella (Kelani Ganga) | 1.55 | 🟢 Normal | -0.061 |  |
| 2026-01-12 10:04:10 | Holombuwa (Kelani Ganga) | 0.65 | 🟢 Normal | -0.074 |  |
| 2026-01-12 10:04:06 | Nakkala (Kumbukkan Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-01-12 10:03:19 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | -0.011 |  |
| 2026-01-12 10:03:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.75 | 🟢 Normal | -0.039 |  |
| 2026-01-12 10:03:14 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-01-12 10:02:50 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | -0.089 |  |
| 2026-01-12 10:02:46 | Dunamale (Aththanagalu Oya) | 0.98 | 🟢 Normal | -0.057 |  |
| 2026-01-12 10:02:37 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-12 10:02:34 | Moragaswewa (Deduru Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-01-12 10:01:55 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-01-12 10:01:41 | Putupaula (Kalu Ganga) | 0.58 | 🟢 Normal | -0.041 |  |
| 2026-01-12 10:01:39 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-01-12 10:01:09 | Ellagawa (Kalu Ganga) | 4.15 | 🟢 Normal | -0.010 |  |
| 2026-01-12 10:01:07 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-12 10:00:57 | Weraganthota (Mahaweli Ganga) | -1.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-12 10:00:57 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-12 10:00:34 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-12 10:00:31 | Horowpothana (Yan Oya) | 2.26 | 🟢 Normal | 0.000 |  |
| 2026-01-12 10:00:24 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-12 09:59:56 | Padiyathalawa (Maduru Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-12 09:12:01 | Panadugama (Nilwala Ganga) | 2.26 | 🟢 Normal | -0.009 |  |
| 2026-01-12 09:11:03 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-01-12 09:09:52 | Dunamale (Aththanagalu Oya) | 1.03 | 🟢 Normal | -0.057 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-12 09:07:46 | Glencourse (Kelani Ganga) | 9.70 | 🟢 Normal | 1.366 | 🔺 Rising |
| 2026-01-12 09:00:33 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | 0.217 | 🔺 Rising |
| 2026-01-12 10:01:55 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-01-12 09:03:15 | Deraniyagala (Kelani Ganga) | 0.44 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-01-12 09:02:27 | Badalgama (Maha Oya) | 2.29 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-12 09:00:51 | Thanamalwila (Kirindi Oya) | 1.09 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-12 10:00:34 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-12 10:00:57 | Weraganthota (Mahaweli Ganga) | -1.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-12 10:02:34 | Moragaswewa (Deduru Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-01-12 10:00:24 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-12 09:01:31 | Yaka Wewa (Ma Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-12 10:00:31 | Horowpothana (Yan Oya) | 2.26 | 🟢 Normal | 0.000 |  |
| 2026-01-12 09:07:35 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-12 10:04:41 | Magura (Kalu Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-12 09:02:26 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-12 10:02:37 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-12 09:59:56 | Padiyathalawa (Maduru Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-12 10:01:07 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-12 10:00:57 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-12 10:05:41 | Katharagama (Menik Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-01-12 09:01:38 | Thanthirimale (Malwathu Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-12 10:03:14 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-01-12 10:01:39 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-01-12 09:12:01 | Panadugama (Nilwala Ganga) | 2.26 | 🟢 Normal | -0.009 |  |
| 2026-01-12 10:05:13 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | -0.009 |  |
| 2026-01-12 10:05:13 | Siyambalanduwa (Heda Oya) | 1.07 | 🟢 Normal | -0.009 |  |
| 2026-01-12 10:04:06 | Nakkala (Kumbukkan Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-01-12 10:01:09 | Ellagawa (Kalu Ganga) | 4.15 | 🟢 Normal | -0.010 |  |
| 2026-01-12 09:08:24 | Rathnapura (Kalu Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-01-12 10:03:19 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | -0.011 |  |
| 2026-01-12 10:05:35 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | -0.021 |  |
| 2026-01-12 09:06:34 | Giriulla (Maha Oya) | 1.32 | 🟢 Normal | -0.024 |  |
| 2026-01-12 09:00:55 | Manampitiya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.032 |  |
| 2026-01-12 10:03:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.75 | 🟢 Normal | -0.039 |  |
| 2026-01-12 10:01:41 | Putupaula (Kalu Ganga) | 0.58 | 🟢 Normal | -0.041 |  |
| 2026-01-12 10:02:46 | Dunamale (Aththanagalu Oya) | 0.98 | 🟢 Normal | -0.057 |  |
| 2026-01-12 10:04:37 | Hanwella (Kelani Ganga) | 1.55 | 🟢 Normal | -0.061 |  |
| 2026-01-12 10:04:10 | Holombuwa (Kelani Ganga) | 0.65 | 🟢 Normal | -0.074 |  |
| 2026-01-12 10:02:50 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | -0.089 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)