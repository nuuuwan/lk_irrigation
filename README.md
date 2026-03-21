# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--22_01:06:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **103,847 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **28** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-22 01:06:03 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-03-22 01:05:28 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.144 | 🔺 Rising |
| 2026-03-22 01:05:08 | Padiyathalawa (Maduru Oya) | 0.38 | 🟢 Normal | -0.020 |  |
| 2026-03-22 01:04:19 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-22 01:04:04 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-03-22 01:03:28 | Panadugama (Nilwala Ganga) | 2.08 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-03-22 01:03:24 | Wellawaya (Kirindi Oya) | 0.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-22 01:03:23 | Glencourse (Kelani Ganga) | 8.40 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-03-22 01:03:06 | Deraniyagala (Kelani Ganga) | 0.25 | 🟢 Normal | -0.080 |  |
| 2026-03-22 01:02:45 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-03-22 01:02:38 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-03-22 01:02:12 | Thanamalwila (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-03-22 01:02:08 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-03-22 01:01:55 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-22 01:01:54 | Thawalama (Gin Ganga) | 2.15 | 🟢 Normal | 0.162 | 🔺 Rising |
| 2026-03-22 01:01:29 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-03-22 01:01:27 | Peradeniya (Mahaweli Ganga) | 1.73 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-03-22 01:01:26 | Nawalapitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-22 01:01:23 | Ellagawa (Kalu Ganga) | 3.93 | 🟢 Normal | 0.000 |  |
| 2026-03-22 01:00:58 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-22 01:00:53 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-22 01:00:31 | Manampitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | -0.021 |  |
| 2026-03-22 00:29:23 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-03-22 00:23:22 | Panadugama (Nilwala Ganga) | 2.07 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-03-22 00:23:08 | Panadugama (Nilwala Ganga) | 2.06 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-03-22 00:14:45 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-22 00:12:48 | Glencourse (Kelani Ganga) | 8.37 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-03-22 00:12:46 | Glencourse (Kelani Ganga) | 8.37 | 🟢 Normal | 0.036 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-22 01:01:54 | Thawalama (Gin Ganga) | 2.15 | 🟢 Normal | 0.162 | 🔺 Rising |
| 2026-03-22 01:05:28 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.144 | 🔺 Rising |
| 2026-03-22 01:01:27 | Peradeniya (Mahaweli Ganga) | 1.73 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-03-22 01:03:23 | Glencourse (Kelani Ganga) | 8.40 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-03-22 00:06:50 | Rathnapura (Kalu Ganga) | 0.56 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-22 01:03:28 | Panadugama (Nilwala Ganga) | 2.08 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-03-21 22:37:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.44 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-03-22 01:03:24 | Wellawaya (Kirindi Oya) | 0.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-22 01:02:45 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-03-22 00:01:01 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-03-22 01:01:55 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-22 01:01:26 | Nawalapitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-22 00:08:49 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-22 00:02:22 | Giriulla (Maha Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-03-21 18:01:02 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-21 23:19:06 | Magura (Kalu Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-22 00:01:25 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-03-22 01:04:04 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-03-22 01:01:23 | Ellagawa (Kalu Ganga) | 3.93 | 🟢 Normal | 0.000 |  |
| 2026-03-22 00:06:37 | Baddegama (Gin Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-03-22 00:00:59 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-03-22 01:00:58 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-22 01:00:53 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-22 01:02:38 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-03-22 01:01:29 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-03-22 01:04:19 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-22 00:00:48 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-22 01:06:03 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-03-22 01:02:12 | Thanamalwila (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-03-21 22:08:28 | Horowpothana (Yan Oya) | 1.23 | 🟢 Normal | -0.009 |  |
| 2026-03-22 00:03:59 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-03-22 01:02:08 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-03-21 18:01:35 | Thanthirimale (Malwathu Oya) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-03-22 01:05:08 | Padiyathalawa (Maduru Oya) | 0.38 | 🟢 Normal | -0.020 |  |
| 2026-03-22 01:00:31 | Manampitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | -0.021 |  |
| 2026-03-22 00:03:34 | Hanwella (Kelani Ganga) | 0.37 | 🟢 Normal | -0.031 |  |
| 2026-03-22 01:03:06 | Deraniyagala (Kelani Ganga) | 0.25 | 🟢 Normal | -0.080 |  |
| 2026-03-21 18:00:19 | Weraganthota (Mahaweli Ganga) | -2.90 | 🟢 Normal | -0.082 |  |
| 2026-03-21 22:04:33 | Putupaula (Kalu Ganga) | 0.30 | 🟢 Normal | -0.234 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)