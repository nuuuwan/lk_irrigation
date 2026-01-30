# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--30_07:01:14-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **59,477 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **21** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-30 07:01:14 | Manampitiya (Mahaweli Ganga) | 1.02 | 🟢 Normal | -0.052 |  |
| 2026-01-30 07:00:56 | Thanthirimale (Malwathu Oya) | 1.43 | 🟢 Normal | 0.002 |  |
| 2026-01-30 07:00:53 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-30 07:00:40 | Weraganthota (Mahaweli Ganga) | -1.91 | 🟢 Normal | -0.041 |  |
| 2026-01-30 06:32:25 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-01-30 06:13:48 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-30 06:12:55 | Panadugama (Nilwala Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-01-30 06:12:15 | Horowpothana (Yan Oya) | 1.35 | 🟢 Normal | 0.005 |  |
| 2026-01-30 06:10:51 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-01-30 06:10:08 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-30 06:09:36 | Thanamalwila (Kirindi Oya) | 0.49 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-01-30 06:06:46 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-30 06:06:32 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-01-30 06:06:07 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-30 06:05:30 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | -0.010 |  |
| 2026-01-30 06:05:30 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-30 06:05:09 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.141 |  |
| 2026-01-30 06:05:08 | Baddegama (Gin Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-01-30 06:04:30 | Nakkala (Kumbukkan Oya) | 0.82 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-30 06:04:29 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-30 06:04:28 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-30 06:02:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.56 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-01-30 06:05:30 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-30 06:09:36 | Thanamalwila (Kirindi Oya) | 0.49 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-01-30 06:01:28 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-30 06:04:30 | Nakkala (Kumbukkan Oya) | 0.82 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-30 06:12:15 | Horowpothana (Yan Oya) | 1.35 | 🟢 Normal | 0.005 |  |
| 2026-01-30 07:00:56 | Thanthirimale (Malwathu Oya) | 1.43 | 🟢 Normal | 0.002 |  |
| 2026-01-30 06:10:08 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-30 06:00:14 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-30 07:00:53 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-30 06:06:07 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-30 06:04:29 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-30 06:32:25 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-01-30 06:02:32 | Magura (Kalu Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-30 06:10:51 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-01-30 06:03:28 | Ellagawa (Kalu Ganga) | 3.79 | 🟢 Normal | 0.000 |  |
| 2026-01-30 06:05:08 | Baddegama (Gin Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-01-30 06:12:55 | Panadugama (Nilwala Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-01-30 06:02:29 | Padiyathalawa (Maduru Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-30 06:06:46 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-30 06:01:12 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-30 06:02:19 | Dunamale (Aththanagalu Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-30 06:04:03 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-30 06:06:32 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-01-30 06:04:08 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-01-30 06:13:48 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-30 06:03:31 | Rathnapura (Kalu Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-30 06:04:28 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-01-30 06:01:41 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-01-30 06:03:08 | Putupaula (Kalu Ganga) | 0.42 | 🟢 Normal | -0.006 |  |
| 2026-01-30 06:04:14 | Moragaswewa (Deduru Oya) | 0.15 | 🟢 Normal | -0.009 |  |
| 2026-01-30 06:05:30 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | -0.010 |  |
| 2026-01-30 06:01:10 | Thawalama (Gin Ganga) | 0.94 | 🟢 Normal | -0.011 |  |
| 2026-01-30 06:01:14 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.020 |  |
| 2026-01-30 06:02:10 | Hanwella (Kelani Ganga) | 0.25 | 🟢 Normal | -0.021 |  |
| 2026-01-30 07:00:40 | Weraganthota (Mahaweli Ganga) | -1.91 | 🟢 Normal | -0.041 |  |
| 2026-01-30 07:01:14 | Manampitiya (Mahaweli Ganga) | 1.02 | 🟢 Normal | -0.052 |  |
| 2026-01-30 06:05:09 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.141 |  |
| 2026-01-30 06:01:24 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | -0.202 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)