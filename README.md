# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--22_03:14:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **103,924 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-22 03:14:12 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-22 03:13:17 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-03-22 03:11:54 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-03-22 03:11:11 | Wellawaya (Kirindi Oya) | 0.71 | 🟢 Normal | -0.009 |  |
| 2026-03-22 03:10:57 | Nawalapitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-22 03:10:32 | Nawalapitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-22 03:10:18 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-22 03:09:21 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-03-22 03:08:29 | Rathnapura (Kalu Ganga) | 0.65 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-22 03:07:40 | Manampitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-03-22 03:06:09 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | -0.030 |  |
| 2026-03-22 03:05:51 | Peradeniya (Mahaweli Ganga) | 1.46 | 🟢 Normal | -0.203 |  |
| 2026-03-22 03:05:44 | Glencourse (Kelani Ganga) | 8.43 | 🟢 Normal | -0.028 |  |
| 2026-03-22 03:05:42 | Thanamalwila (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-03-22 03:05:36 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-03-22 03:05:28 | Panadugama (Nilwala Ganga) | 2.07 | 🟢 Normal | -0.011 |  |
| 2026-03-22 03:04:24 | Hanwella (Kelani Ganga) | 0.30 | 🟢 Normal | -0.020 |  |
| 2026-03-22 03:04:23 | Giriulla (Maha Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-03-22 03:04:17 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-03-22 03:04:10 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-03-22 03:03:52 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-22 03:03:23 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-03-22 03:03:10 | Magura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-03-22 03:02:59 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-03-22 03:02:50 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | -0.040 |  |
| 2026-03-22 03:02:29 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-03-22 03:02:22 | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-03-22 03:02:10 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-22 03:02:09 | Thawalama (Gin Ganga) | 2.40 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-03-22 03:01:53 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-22 03:01:52 | Ellagawa (Kalu Ganga) | 3.93 | 🟢 Normal | -0.010 |  |
| 2026-03-22 03:01:09 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-22 03:00:54 | Nakkala (Kumbukkan Oya) | 0.72 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-22 02:04:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.54 | 🟢 Normal | 5.000 | 🔺 Rising |
| 2026-03-22 03:09:21 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-03-22 03:03:10 | Magura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-03-22 02:04:20 | Dunamale (Aththanagalu Oya) | 0.50 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-03-22 03:02:09 | Thawalama (Gin Ganga) | 2.40 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-03-22 03:07:40 | Manampitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-03-22 02:34:27 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-03-22 03:08:29 | Rathnapura (Kalu Ganga) | 0.65 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-22 03:03:52 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-22 03:03:23 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-03-22 03:00:54 | Nakkala (Kumbukkan Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-03-22 03:02:10 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-22 03:10:57 | Nawalapitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-22 03:01:53 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-22 03:04:23 | Giriulla (Maha Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-03-22 02:22:50 | Horowpothana (Yan Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-03-21 18:01:02 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-22 03:02:59 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-03-22 03:04:10 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-03-22 03:13:17 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-03-22 03:02:29 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-03-22 03:10:18 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-22 03:01:09 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-22 03:14:12 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-22 03:05:36 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-03-22 03:05:42 | Thanamalwila (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-03-22 01:10:15 | Pitabeddara (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.009 |  |
| 2026-03-22 03:11:11 | Wellawaya (Kirindi Oya) | 0.71 | 🟢 Normal | -0.009 |  |
| 2026-03-22 03:01:52 | Ellagawa (Kalu Ganga) | 3.93 | 🟢 Normal | -0.010 |  |
| 2026-03-22 03:04:17 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-03-22 03:02:22 | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-03-21 18:01:35 | Thanthirimale (Malwathu Oya) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-03-22 03:05:28 | Panadugama (Nilwala Ganga) | 2.07 | 🟢 Normal | -0.011 |  |
| 2026-03-22 03:04:24 | Hanwella (Kelani Ganga) | 0.30 | 🟢 Normal | -0.020 |  |
| 2026-03-22 03:05:44 | Glencourse (Kelani Ganga) | 8.43 | 🟢 Normal | -0.028 |  |
| 2026-03-22 03:06:09 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | -0.030 |  |
| 2026-03-22 03:02:50 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | -0.040 |  |
| 2026-03-21 18:00:19 | Weraganthota (Mahaweli Ganga) | -2.90 | 🟢 Normal | -0.082 |  |
| 2026-03-22 03:05:51 | Peradeniya (Mahaweli Ganga) | 1.46 | 🟢 Normal | -0.203 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)