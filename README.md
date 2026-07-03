# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--03_08:07:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **195,955 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-03 08:07:26 | Thanamalwila (Kirindi Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-07-03 08:07:06 | Panadugama (Nilwala Ganga) | 2.46 | 🟢 Normal | 0.000 |  |
| 2026-07-03 08:06:53 | Hanwella (Kelani Ganga) | 1.43 | 🟢 Normal | -0.010 |  |
| 2026-07-03 08:06:49 | Thawalama (Gin Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-07-03 08:06:32 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-07-03 08:06:00 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | -0.009 |  |
| 2026-07-03 08:05:01 | Badalgama (Maha Oya) | 2.10 | 🟢 Normal | -0.010 |  |
| 2026-07-03 08:04:10 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2026-07-03 08:04:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.32 | 🟢 Normal | -0.116 |  |
| 2026-07-03 08:03:57 | Dunamale (Aththanagalu Oya) | 1.05 | 🟢 Normal | -0.011 |  |
| 2026-07-03 08:03:33 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-07-03 08:03:27 | Magura (Kalu Ganga) | 1.33 | 🟢 Normal | -0.012 |  |
| 2026-07-03 08:03:23 | Glencourse (Kelani Ganga) | 9.57 | 🟢 Normal | -0.030 |  |
| 2026-07-03 08:02:54 | Putupaula (Kalu Ganga) | 0.48 | 🟢 Normal | -0.103 |  |
| 2026-07-03 08:02:47 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-07-03 08:02:39 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-07-03 08:02:33 | Baddegama (Gin Ganga) | 1.09 | 🟢 Normal | -0.020 |  |
| 2026-07-03 08:02:28 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-03 08:02:28 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-07-03 08:02:24 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-03 08:02:23 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.061 |  |
| 2026-07-03 08:02:18 | Deraniyagala (Kelani Ganga) | 0.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-03 08:02:12 | Ellagawa (Kalu Ganga) | 4.94 | 🟢 Normal | -0.010 |  |
| 2026-07-03 08:02:01 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | -0.109 |  |
| 2026-07-03 08:01:25 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-03 08:01:25 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-03 08:01:20 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-07-03 08:01:19 | Thanthirimale (Malwathu Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-07-03 08:01:11 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-07-03 08:01:06 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-03 08:00:30 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-03 08:00:19 | Weraganthota (Mahaweli Ganga) | -3.29 | 🟢 Normal | -0.061 |  |
| 2026-07-03 08:00:09 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-07-03 07:32:11 | Panadugama (Nilwala Ganga) | 2.46 | 🟢 Normal | 0.000 |  |
| 2026-07-03 07:25:05 | Rathnapura (Kalu Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-07-03 07:23:16 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | -0.001 |  |
| 2026-07-03 07:19:22 | Pitabeddara (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-03 08:04:10 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2026-07-03 08:02:47 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-07-03 08:00:30 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-03 07:06:38 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-03 08:02:28 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-03 08:02:18 | Deraniyagala (Kelani Ganga) | 0.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-03 08:02:28 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-07-03 08:00:09 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-07-03 08:02:24 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-03 08:01:20 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-07-03 08:01:25 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-03 08:01:11 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-07-03 08:01:06 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-03 07:19:22 | Pitabeddara (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-03 08:07:06 | Panadugama (Nilwala Ganga) | 2.46 | 🟢 Normal | 0.000 |  |
| 2026-07-03 08:03:33 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-07-03 08:01:25 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-03 07:25:05 | Rathnapura (Kalu Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-07-03 08:01:19 | Thanthirimale (Malwathu Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-07-03 08:06:49 | Thawalama (Gin Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-07-03 07:07:00 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-03 08:02:39 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-07-03 08:07:26 | Thanamalwila (Kirindi Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-07-03 07:23:16 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | -0.001 |  |
| 2026-07-03 08:06:00 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | -0.009 |  |
| 2026-07-03 08:06:53 | Hanwella (Kelani Ganga) | 1.43 | 🟢 Normal | -0.010 |  |
| 2026-07-03 08:02:12 | Ellagawa (Kalu Ganga) | 4.94 | 🟢 Normal | -0.010 |  |
| 2026-07-03 08:06:32 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-07-03 08:05:01 | Badalgama (Maha Oya) | 2.10 | 🟢 Normal | -0.010 |  |
| 2026-07-03 08:03:57 | Dunamale (Aththanagalu Oya) | 1.05 | 🟢 Normal | -0.011 |  |
| 2026-07-03 08:03:27 | Magura (Kalu Ganga) | 1.33 | 🟢 Normal | -0.012 |  |
| 2026-07-03 08:02:33 | Baddegama (Gin Ganga) | 1.09 | 🟢 Normal | -0.020 |  |
| 2026-07-03 07:00:18 | Thalgahagoda (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.024 |  |
| 2026-07-03 08:03:23 | Glencourse (Kelani Ganga) | 9.57 | 🟢 Normal | -0.030 |  |
| 2026-07-03 08:02:23 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.061 |  |
| 2026-07-03 08:00:19 | Weraganthota (Mahaweli Ganga) | -3.29 | 🟢 Normal | -0.061 |  |
| 2026-07-03 08:02:54 | Putupaula (Kalu Ganga) | 0.48 | 🟢 Normal | -0.103 |  |
| 2026-07-03 08:02:01 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | -0.109 |  |
| 2026-07-03 08:04:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.32 | 🟢 Normal | -0.116 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)