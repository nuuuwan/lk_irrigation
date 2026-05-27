# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--27_07:28:04-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **162,812 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-27 07:28:04 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-27 07:26:04 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-27 07:17:34 | Thawalama (Gin Ganga) | 1.94 | 🟢 Normal | -0.016 |  |
| 2026-05-27 07:17:26 | Rathnapura (Kalu Ganga) | 3.53 | 🟢 Normal | -0.033 |  |
| 2026-05-27 07:14:30 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | -0.008 |  |
| 2026-05-27 07:13:29 | Glencourse (Kelani Ganga) | 11.48 | 🟢 Normal | -0.061 |  |
| 2026-05-27 07:12:10 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-27 07:10:34 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-27 07:10:02 | Magura (Kalu Ganga) | 3.11 | 🟢 Normal | 0.000 |  |
| 2026-05-27 07:07:59 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-05-27 07:07:55 | Kithulgala (Kelani Ganga) | 1.89 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-05-27 07:07:03 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-05-27 07:06:33 | Badalgama (Maha Oya) | 2.51 | 🟢 Normal | 0.000 |  |
| 2026-05-27 07:06:16 | Panadugama (Nilwala Ganga) | 2.74 | 🟢 Normal | -0.033 |  |
| 2026-05-27 07:04:58 | Dunamale (Aththanagalu Oya) | 2.17 | 🟢 Normal | -0.019 |  |
| 2026-05-27 07:04:54 | Hanwella (Kelani Ganga) | 4.08 | 🟢 Normal | -0.058 |  |
| 2026-05-27 07:04:42 | Pitabeddara (Nilwala Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-05-27 07:04:15 | Ellagawa (Kalu Ganga) | 8.56 | 🟢 Normal | -0.019 |  |
| 2026-05-27 07:04:04 | Manampitiya (Mahaweli Ganga) | 0.09 | 🟢 Normal | -0.010 |  |
| 2026-05-27 07:03:53 | Baddegama (Gin Ganga) | 1.96 | 🟢 Normal | -0.010 |  |
| 2026-05-27 07:03:47 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | -0.009 |  |
| 2026-05-27 07:03:43 | Nawalapitiya (Mahaweli Ganga) | 1.43 | 🟢 Normal | -0.049 |  |
| 2026-05-27 07:03:37 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-27 07:03:20 | Putupaula (Kalu Ganga) | 2.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-27 07:03:17 | Weraganthota (Mahaweli Ganga) | -3.19 | 🟢 Normal | -0.067 |  |
| 2026-05-27 07:03:08 | Thanthirimale (Malwathu Oya) | 1.21 | 🟢 Normal | -0.007 |  |
| 2026-05-27 07:03:00 | Giriulla (Maha Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-05-27 07:02:59 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-27 07:02:45 | Deraniyagala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-27 07:02:44 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-27 07:02:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.24 | 🟡 Alert | 0.000 |  |
| 2026-05-27 07:02:11 | Thanamalwila (Kirindi Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-27 07:02:10 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-27 07:01:54 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-27 07:01:36 | Moragaswewa (Deduru Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-27 07:01:04 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-27 07:00:59 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-27 07:00:54 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-05-27 07:00:11 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-27 07:02:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.24 | 🟡 Alert | 0.000 |  |
| 2026-05-27 07:07:03 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-05-27 07:07:59 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-05-27 07:07:55 | Kithulgala (Kelani Ganga) | 1.89 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-05-27 07:02:10 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-27 07:02:45 | Deraniyagala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-27 07:03:20 | Putupaula (Kalu Ganga) | 2.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-27 07:10:34 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-27 07:01:04 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-27 07:00:11 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-27 07:01:36 | Moragaswewa (Deduru Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-27 07:01:54 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-27 07:03:00 | Giriulla (Maha Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-05-27 07:28:04 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-27 07:00:54 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-05-27 07:10:02 | Magura (Kalu Ganga) | 3.11 | 🟢 Normal | 0.000 |  |
| 2026-05-27 07:02:44 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-27 07:12:10 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-27 07:03:37 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-27 07:06:33 | Badalgama (Maha Oya) | 2.51 | 🟢 Normal | 0.000 |  |
| 2026-05-27 07:26:04 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-27 07:00:59 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-27 07:02:59 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-27 07:02:11 | Thanamalwila (Kirindi Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-27 07:03:08 | Thanthirimale (Malwathu Oya) | 1.21 | 🟢 Normal | -0.007 |  |
| 2026-05-27 07:14:30 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | -0.008 |  |
| 2026-05-27 07:03:47 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | -0.009 |  |
| 2026-05-27 07:04:42 | Pitabeddara (Nilwala Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-05-27 07:04:04 | Manampitiya (Mahaweli Ganga) | 0.09 | 🟢 Normal | -0.010 |  |
| 2026-05-27 07:03:53 | Baddegama (Gin Ganga) | 1.96 | 🟢 Normal | -0.010 |  |
| 2026-05-27 07:17:34 | Thawalama (Gin Ganga) | 1.94 | 🟢 Normal | -0.016 |  |
| 2026-05-27 07:04:58 | Dunamale (Aththanagalu Oya) | 2.17 | 🟢 Normal | -0.019 |  |
| 2026-05-27 07:04:15 | Ellagawa (Kalu Ganga) | 8.56 | 🟢 Normal | -0.019 |  |
| 2026-05-27 07:06:16 | Panadugama (Nilwala Ganga) | 2.74 | 🟢 Normal | -0.033 |  |
| 2026-05-27 07:17:26 | Rathnapura (Kalu Ganga) | 3.53 | 🟢 Normal | -0.033 |  |
| 2026-05-27 07:03:43 | Nawalapitiya (Mahaweli Ganga) | 1.43 | 🟢 Normal | -0.049 |  |
| 2026-05-27 07:04:54 | Hanwella (Kelani Ganga) | 4.08 | 🟢 Normal | -0.058 |  |
| 2026-05-27 07:13:29 | Glencourse (Kelani Ganga) | 11.48 | 🟢 Normal | -0.061 |  |
| 2026-05-27 07:03:17 | Weraganthota (Mahaweli Ganga) | -3.19 | 🟢 Normal | -0.067 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)