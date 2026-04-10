# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--10_17:17:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **121,457 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-10 17:17:02 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | -0.008 |  |
| 2026-04-10 17:14:57 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-10 17:12:44 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-04-10 17:09:41 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-10 17:08:57 | Deraniyagala (Kelani Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-04-10 17:08:54 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-04-10 17:08:13 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-04-10 17:06:34 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-04-10 17:06:21 | Panadugama (Nilwala Ganga) | 1.85 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-10 17:06:20 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | -0.010 |  |
| 2026-04-10 17:04:55 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-04-10 17:04:14 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-04-10 17:03:53 | Hanwella (Kelani Ganga) | 0.27 | 🟢 Normal | -0.010 |  |
| 2026-04-10 17:03:47 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-10 17:03:45 | Magura (Kalu Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-10 17:03:42 | Rathnapura (Kalu Ganga) | 0.45 | 🟢 Normal | -0.020 |  |
| 2026-04-10 17:03:34 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-04-10 17:03:33 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-10 17:03:20 | Ellagawa (Kalu Ganga) | 3.93 | 🟢 Normal | -0.021 |  |
| 2026-04-10 17:03:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-04-10 17:03:10 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-04-10 17:03:10 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-10 17:03:07 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-10 17:03:04 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-10 17:02:44 | Putupaula (Kalu Ganga) | 0.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-10 17:02:35 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 2.118 | 🔺 Rising |
| 2026-04-10 17:02:28 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-10 17:02:20 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-10 17:02:20 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-04-10 17:02:18 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | 2.118 | 🔺 Rising |
| 2026-04-10 17:02:15 | Glencourse (Kelani Ganga) | 8.40 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-10 17:01:50 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-10 17:01:48 | Peradeniya (Mahaweli Ganga) | 1.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-10 17:01:41 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | -0.049 |  |
| 2026-04-10 17:01:32 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-10 17:01:13 | Manampitiya (Mahaweli Ganga) | 0.01 | 🟢 Normal | -0.030 |  |
| 2026-04-10 17:01:13 | Thanamalwila (Kirindi Oya) | 0.28 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-10 17:01:10 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-04-10 17:01:05 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-04-10 17:00:53 | Thanthirimale (Malwathu Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-04-10 17:00:45 | Horowpothana (Yan Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-04-10 17:00:13 | Nawalapitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-10 17:02:35 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 2.118 | 🔺 Rising |
| 2026-04-10 17:06:34 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-04-10 17:08:54 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-04-10 17:04:55 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-04-10 17:03:34 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-04-10 17:12:44 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-04-10 17:01:10 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-04-10 17:06:21 | Panadugama (Nilwala Ganga) | 1.85 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-10 17:01:13 | Thanamalwila (Kirindi Oya) | 0.28 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-10 17:01:48 | Peradeniya (Mahaweli Ganga) | 1.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-10 17:02:15 | Glencourse (Kelani Ganga) | 8.40 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-10 17:08:13 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-04-10 17:03:10 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-10 17:02:44 | Putupaula (Kalu Ganga) | 0.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-10 17:00:13 | Nawalapitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-10 17:09:41 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-10 17:03:07 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-10 17:01:50 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-10 17:01:32 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-10 17:02:20 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-04-10 17:00:45 | Horowpothana (Yan Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-04-10 17:03:45 | Magura (Kalu Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-10 17:08:57 | Deraniyagala (Kelani Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-04-10 17:01:05 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-04-10 17:03:04 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-10 17:14:57 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-10 17:03:33 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-10 17:03:47 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-10 17:00:53 | Thanthirimale (Malwathu Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-04-10 17:17:02 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | -0.008 |  |
| 2026-04-10 17:06:20 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | -0.010 |  |
| 2026-04-10 17:04:14 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-04-10 17:03:10 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-04-10 17:03:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-04-10 17:03:53 | Hanwella (Kelani Ganga) | 0.27 | 🟢 Normal | -0.010 |  |
| 2026-04-10 17:03:42 | Rathnapura (Kalu Ganga) | 0.45 | 🟢 Normal | -0.020 |  |
| 2026-04-10 17:03:20 | Ellagawa (Kalu Ganga) | 3.93 | 🟢 Normal | -0.021 |  |
| 2026-04-10 17:01:13 | Manampitiya (Mahaweli Ganga) | 0.01 | 🟢 Normal | -0.030 |  |
| 2026-04-10 17:01:41 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | -0.049 |  |

## River Water Level Charts by Station

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)