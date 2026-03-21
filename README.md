# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--21_22:09:04-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **103,752 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-21 22:09:04 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-03-21 22:08:28 | Horowpothana (Yan Oya) | 1.23 | 🟢 Normal | -0.009 |  |
| 2026-03-21 22:06:59 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-21 22:06:48 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-21 22:06:20 | Thalgahagoda (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.019 |  |
| 2026-03-21 22:06:08 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.063 |  |
| 2026-03-21 22:05:18 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-03-21 22:04:52 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | -0.033 |  |
| 2026-03-21 22:04:33 | Putupaula (Kalu Ganga) | 0.30 | 🟢 Normal | -0.234 |  |
| 2026-03-21 22:04:06 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-21 22:03:51 | Glencourse (Kelani Ganga) | 8.37 | 🟢 Normal | -0.036 |  |
| 2026-03-21 22:03:50 | Padiyathalawa (Maduru Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-21 22:03:48 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | -0.039 |  |
| 2026-03-21 22:03:33 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-03-21 22:03:20 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | -0.030 |  |
| 2026-03-21 22:03:14 | Nawalapitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-21 22:03:14 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-03-21 22:02:54 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-03-21 22:02:52 | Manampitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | -0.049 |  |
| 2026-03-21 22:02:35 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | -0.021 |  |
| 2026-03-21 22:02:35 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-21 22:02:32 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-21 22:02:15 | Wellawaya (Kirindi Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-03-21 22:02:09 | Thanamalwila (Kirindi Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-03-21 22:02:02 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | -0.010 |  |
| 2026-03-21 22:01:58 | Magura (Kalu Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-21 22:01:58 | Ellagawa (Kalu Ganga) | 3.94 | 🟢 Normal | 0.000 |  |
| 2026-03-21 22:01:55 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-21 22:01:53 | Thawalama (Gin Ganga) | 1.42 | 🟢 Normal | 3.273 | 🔺 Rising |
| 2026-03-21 22:01:51 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-21 22:01:46 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-03-21 22:01:31 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | 3.273 | 🔺 Rising |
| 2026-03-21 22:01:16 | Panadugama (Nilwala Ganga) | 2.05 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-03-21 22:00:34 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.371 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-21 22:01:53 | Thawalama (Gin Ganga) | 1.42 | 🟢 Normal | 3.273 | 🔺 Rising |
| 2026-03-21 22:00:34 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.371 | 🔺 Rising |
| 2026-03-21 22:02:32 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-21 21:11:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.42 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-03-21 22:01:16 | Panadugama (Nilwala Ganga) | 2.05 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-03-21 21:03:12 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-21 22:02:15 | Wellawaya (Kirindi Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-03-21 22:01:46 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-03-21 22:01:55 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-21 22:03:14 | Nawalapitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-21 22:01:51 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-21 18:01:02 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-21 22:01:58 | Magura (Kalu Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-21 21:05:18 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-03-21 22:01:58 | Ellagawa (Kalu Ganga) | 3.94 | 🟢 Normal | 0.000 |  |
| 2026-03-21 22:03:50 | Padiyathalawa (Maduru Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-21 22:09:04 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-03-21 22:02:35 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-21 22:04:06 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-21 22:03:33 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-03-21 22:03:14 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-03-21 22:06:59 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-21 21:01:21 | Rathnapura (Kalu Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-03-21 21:11:02 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-21 22:02:54 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-03-21 22:08:28 | Horowpothana (Yan Oya) | 1.23 | 🟢 Normal | -0.009 |  |
| 2026-03-21 22:02:09 | Thanamalwila (Kirindi Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-03-21 22:02:02 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | -0.010 |  |
| 2026-03-21 18:01:35 | Thanthirimale (Malwathu Oya) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-03-21 22:06:20 | Thalgahagoda (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.019 |  |
| 2026-03-21 22:02:35 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | -0.021 |  |
| 2026-03-21 22:03:20 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | -0.030 |  |
| 2026-03-21 22:04:52 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | -0.033 |  |
| 2026-03-21 22:03:51 | Glencourse (Kelani Ganga) | 8.37 | 🟢 Normal | -0.036 |  |
| 2026-03-21 22:03:48 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | -0.039 |  |
| 2026-03-21 22:02:52 | Manampitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | -0.049 |  |
| 2026-03-21 22:06:08 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.063 |  |
| 2026-03-21 18:00:19 | Weraganthota (Mahaweli Ganga) | -2.90 | 🟢 Normal | -0.082 |  |
| 2026-03-21 22:04:33 | Putupaula (Kalu Ganga) | 0.30 | 🟢 Normal | -0.234 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)