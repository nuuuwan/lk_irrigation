# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--26_17:13:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **56,317 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-26 17:13:42 | Magura (Kalu Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-26 17:12:22 | Horowpothana (Yan Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-01-26 17:11:44 | Panadugama (Nilwala Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-01-26 17:10:48 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-26 17:08:11 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | -0.013 |  |
| 2026-01-26 17:07:58 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.064 |  |
| 2026-01-26 17:07:54 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | -0.010 |  |
| 2026-01-26 17:07:44 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-01-26 17:07:19 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-26 17:06:50 | Thawalama (Gin Ganga) | 1.03 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-01-26 17:06:37 | Glencourse (Kelani Ganga) | 8.46 | 🟢 Normal | 0.000 |  |
| 2026-01-26 17:06:21 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | -0.009 |  |
| 2026-01-26 17:06:18 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-26 17:06:11 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-26 17:05:59 | Glencourse (Kelani Ganga) | 8.46 | 🟢 Normal | 0.000 |  |
| 2026-01-26 17:05:51 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-01-26 17:05:37 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-01-26 17:05:00 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-26 17:04:50 | Thanamalwila (Kirindi Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-01-26 17:04:26 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-01-26 17:04:24 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-01-26 17:03:53 | Dunamale (Aththanagalu Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-26 17:03:33 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | -0.064 |  |
| 2026-01-26 17:03:33 | Baddegama (Gin Ganga) | 0.88 | 🟢 Normal | -0.021 |  |
| 2026-01-26 17:03:27 | Ellagawa (Kalu Ganga) | 4.10 | 🟢 Normal | 0.000 |  |
| 2026-01-26 17:03:12 | Hanwella (Kelani Ganga) | 0.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-26 17:03:10 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-26 17:03:06 | Padiyathalawa (Maduru Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-26 17:03:04 | Manampitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-01-26 17:02:59 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-26 17:02:44 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-01-26 17:02:39 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-01-26 17:02:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.89 | 🟢 Normal | -0.021 |  |
| 2026-01-26 17:02:07 | Thanthirimale (Malwathu Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-01-26 17:01:40 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-26 17:01:36 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-26 17:01:11 | Pitabeddara (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-01-26 17:01:00 | Moragaswewa (Deduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-26 17:00:21 | Weraganthota (Mahaweli Ganga) | -2.12 | 🟢 Normal | 0.061 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-26 17:06:50 | Thawalama (Gin Ganga) | 1.03 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-01-26 17:02:39 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-01-26 17:00:21 | Weraganthota (Mahaweli Ganga) | -2.12 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-01-26 17:02:44 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-01-26 17:06:18 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-26 17:04:24 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-01-26 17:03:12 | Hanwella (Kelani Ganga) | 0.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-26 17:01:36 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-26 17:03:10 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-26 17:01:00 | Moragaswewa (Deduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-26 17:10:48 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-26 17:01:40 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-26 17:06:11 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-26 17:12:22 | Horowpothana (Yan Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-01-26 17:07:44 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-01-26 17:13:42 | Magura (Kalu Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-26 17:01:11 | Pitabeddara (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-01-26 17:05:00 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-26 17:03:27 | Ellagawa (Kalu Ganga) | 4.10 | 🟢 Normal | 0.000 |  |
| 2026-01-26 17:11:44 | Panadugama (Nilwala Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-01-26 17:03:06 | Padiyathalawa (Maduru Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-26 17:06:37 | Glencourse (Kelani Ganga) | 8.46 | 🟢 Normal | 0.000 |  |
| 2026-01-26 17:07:19 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-26 17:03:53 | Dunamale (Aththanagalu Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-26 17:02:59 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-26 17:05:37 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-01-26 17:03:04 | Manampitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-01-26 17:02:07 | Thanthirimale (Malwathu Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-01-26 17:05:51 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-01-26 17:04:50 | Thanamalwila (Kirindi Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-01-26 17:06:21 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | -0.009 |  |
| 2026-01-26 17:04:26 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-01-26 17:07:54 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | -0.010 |  |
| 2026-01-26 16:03:15 | Rathnapura (Kalu Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-01-26 17:08:11 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | -0.013 |  |
| 2026-01-26 17:02:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.89 | 🟢 Normal | -0.021 |  |
| 2026-01-26 17:03:33 | Baddegama (Gin Ganga) | 0.88 | 🟢 Normal | -0.021 |  |
| 2026-01-26 17:03:33 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | -0.064 |  |
| 2026-01-26 17:07:58 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.064 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)