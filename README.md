# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--04_15:15:45-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **89,046 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-04 15:15:45 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-04 15:12:25 | Magura (Kalu Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-04 15:08:39 | Peradeniya (Mahaweli Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-03-04 15:08:09 | Rathnapura (Kalu Ganga) | 0.40 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-04 15:06:17 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | -0.010 |  |
| 2026-03-04 15:06:14 | Badalgama (Maha Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-03-04 15:06:12 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.168 | 🔺 Rising |
| 2026-03-04 15:05:25 | Horowpothana (Yan Oya) | 1.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-04 15:05:23 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-04 15:05:21 | Panadugama (Nilwala Ganga) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-03-04 15:05:09 | Padiyathalawa (Maduru Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-04 15:05:08 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-04 15:04:59 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-03-04 15:04:56 | Manampitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-03-04 15:04:51 | Glencourse (Kelani Ganga) | 8.15 | 🟢 Normal | -0.049 |  |
| 2026-03-04 15:04:41 | Ellagawa (Kalu Ganga) | 3.83 | 🟢 Normal | -0.010 |  |
| 2026-03-04 15:04:09 | Giriulla (Maha Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-04 15:03:12 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-04 15:02:53 | Putupaula (Kalu Ganga) | 0.92 | 🟢 Normal | 0.158 | 🔺 Rising |
| 2026-03-04 15:02:51 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-04 15:02:50 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-03-04 15:02:45 | Hanwella (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-03-04 15:02:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.38 | 🟢 Normal | -0.021 |  |
| 2026-03-04 15:02:31 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-04 15:02:25 | Dunamale (Aththanagalu Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-04 15:02:20 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | -0.020 |  |
| 2026-03-04 15:02:18 | Moraketiya (Walawe Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-03-04 15:02:15 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-03-04 15:02:11 | Pitabeddara (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-03-04 15:02:11 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-03-04 15:02:07 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-04 15:01:50 | Thanthirimale (Malwathu Oya) | 0.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-04 15:01:44 | Norwood (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-04 15:01:32 | Weraganthota (Mahaweli Ganga) | -1.74 | 🟢 Normal | -0.020 |  |
| 2026-03-04 15:01:32 | Wellawaya (Kirindi Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-03-04 15:01:17 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-04 15:01:15 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-04 15:00:55 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-04 15:06:12 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.168 | 🔺 Rising |
| 2026-03-04 15:02:53 | Putupaula (Kalu Ganga) | 0.92 | 🟢 Normal | 0.158 | 🔺 Rising |
| 2026-03-04 15:02:50 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-03-04 14:07:43 | Thawalama (Gin Ganga) | 0.88 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-03-04 15:08:09 | Rathnapura (Kalu Ganga) | 0.40 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-04 15:05:25 | Horowpothana (Yan Oya) | 1.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-04 15:01:50 | Thanthirimale (Malwathu Oya) | 0.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-04 15:01:32 | Wellawaya (Kirindi Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-03-04 15:04:59 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-03-04 15:05:08 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-04 15:02:07 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-04 15:01:17 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-04 15:04:09 | Giriulla (Maha Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-04 15:05:23 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-04 15:12:25 | Magura (Kalu Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-04 15:02:11 | Pitabeddara (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-03-04 15:01:44 | Norwood (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-04 15:02:45 | Hanwella (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-03-04 15:02:11 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-03-04 15:05:21 | Panadugama (Nilwala Ganga) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-03-04 15:05:09 | Padiyathalawa (Maduru Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-04 15:00:55 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-04 15:02:25 | Dunamale (Aththanagalu Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-04 15:03:12 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-04 15:02:51 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-04 15:06:14 | Badalgama (Maha Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-03-04 15:04:56 | Manampitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-03-04 15:08:39 | Peradeniya (Mahaweli Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-03-04 15:15:45 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-04 15:02:31 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-04 15:01:15 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-04 15:04:41 | Ellagawa (Kalu Ganga) | 3.83 | 🟢 Normal | -0.010 |  |
| 2026-03-04 15:06:17 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | -0.010 |  |
| 2026-03-04 15:02:18 | Moraketiya (Walawe Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-03-04 15:02:15 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-03-04 15:01:32 | Weraganthota (Mahaweli Ganga) | -1.74 | 🟢 Normal | -0.020 |  |
| 2026-03-04 15:02:20 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | -0.020 |  |
| 2026-03-04 15:02:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.38 | 🟢 Normal | -0.021 |  |
| 2026-03-04 15:04:51 | Glencourse (Kelani Ganga) | 8.15 | 🟢 Normal | -0.049 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)