# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--30_18:05:33-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **111,657 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-30 18:05:33 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-30 18:05:32 | Baddegama (Gin Ganga) | 1.09 | 🟢 Normal | -0.032 |  |
| 2026-03-30 18:04:56 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.123 |  |
| 2026-03-30 18:04:45 | Dunamale (Aththanagalu Oya) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-03-30 18:04:30 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-03-30 18:04:17 | Hanwella (Kelani Ganga) | 0.27 | 🟢 Normal | -0.031 |  |
| 2026-03-30 18:04:12 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-30 18:03:53 | Giriulla (Maha Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-30 18:03:46 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-03-30 18:03:45 | Thawalama (Gin Ganga) | 0.89 | 🟢 Normal | -72.000 |  |
| 2026-03-30 18:03:44 | Glencourse (Kelani Ganga) | 8.33 | 🟢 Normal | -0.021 |  |
| 2026-03-30 18:03:44 | Thawalama (Gin Ganga) | 0.91 | 🟢 Normal | -72.000 |  |
| 2026-03-30 18:03:43 | Thawalama (Gin Ganga) | 0.93 | 🟢 Normal | -72.000 |  |
| 2026-03-30 18:03:41 | Ellagawa (Kalu Ganga) | 3.68 | 🟢 Normal | 0.000 |  |
| 2026-03-30 18:03:22 | Padiyathalawa (Maduru Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-03-30 18:03:14 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-30 18:03:12 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | -0.049 |  |
| 2026-03-30 18:02:58 | Deraniyagala (Kelani Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-30 18:02:54 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | -0.101 |  |
| 2026-03-30 18:02:21 | Thanamalwila (Kirindi Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-30 18:02:19 | Manampitiya (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-03-30 18:02:12 | Badalgama (Maha Oya) | 1.66 | 🟢 Normal | -0.010 |  |
| 2026-03-30 18:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-03-30 18:01:53 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-30 18:01:43 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | -0.100 |  |
| 2026-03-30 18:01:18 | Peradeniya (Mahaweli Ganga) | 1.02 | 🟢 Normal | -0.047 |  |
| 2026-03-30 18:00:48 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-30 18:00:31 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-03-30 18:00:26 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-03-30 18:00:11 | Nawalapitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-30 18:02:19 | Manampitiya (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-03-30 17:04:59 | Rathnapura (Kalu Ganga) | 0.45 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-30 17:08:39 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-03-30 18:00:48 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-30 18:01:53 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-30 18:00:11 | Nawalapitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-03-30 17:08:22 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-30 18:03:53 | Giriulla (Maha Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-30 18:05:33 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-30 17:02:15 | Galgamuwa (Mee Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-03-30 17:05:29 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-30 18:02:58 | Deraniyagala (Kelani Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-30 18:03:41 | Ellagawa (Kalu Ganga) | 3.68 | 🟢 Normal | 0.000 |  |
| 2026-03-30 18:03:22 | Padiyathalawa (Maduru Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-03-30 18:04:12 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-30 18:04:30 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-03-30 18:03:46 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-03-30 18:00:31 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-03-30 18:03:14 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-30 18:00:26 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-03-30 18:02:21 | Thanamalwila (Kirindi Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-30 18:04:45 | Dunamale (Aththanagalu Oya) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-03-30 17:04:02 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-03-30 18:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-03-30 18:02:12 | Badalgama (Maha Oya) | 1.66 | 🟢 Normal | -0.010 |  |
| 2026-03-30 17:00:35 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-03-30 17:01:17 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.011 |  |
| 2026-03-30 17:03:27 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | -0.011 |  |
| 2026-03-30 17:06:44 | Magura (Kalu Ganga) | 0.59 | 🟢 Normal | -0.020 |  |
| 2026-03-30 18:03:44 | Glencourse (Kelani Ganga) | 8.33 | 🟢 Normal | -0.021 |  |
| 2026-03-30 18:04:17 | Hanwella (Kelani Ganga) | 0.27 | 🟢 Normal | -0.031 |  |
| 2026-03-30 18:05:32 | Baddegama (Gin Ganga) | 1.09 | 🟢 Normal | -0.032 |  |
| 2026-03-30 17:02:41 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | -0.035 |  |
| 2026-03-30 18:01:18 | Peradeniya (Mahaweli Ganga) | 1.02 | 🟢 Normal | -0.047 |  |
| 2026-03-30 18:03:12 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | -0.049 |  |
| 2026-03-30 18:01:43 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | -0.100 |  |
| 2026-03-30 18:02:54 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | -0.101 |  |
| 2026-03-30 18:04:56 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.123 |  |
| 2026-03-30 18:03:45 | Thawalama (Gin Ganga) | 0.89 | 🟢 Normal | -72.000 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)