# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--26_08:06:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **135,368 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-26 08:06:26 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-04-26 08:06:05 | Pitabeddara (Nilwala Ganga) | 4.00 | 🟡 Alert | 4.457 | 🔺 Rising |
| 2026-04-26 08:06:02 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-26 08:05:56 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | -0.011 |  |
| 2026-04-26 08:05:46 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-26 08:05:24 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-04-26 08:05:19 | Putupaula (Kalu Ganga) | 0.47 | 🟢 Normal | -0.041 |  |
| 2026-04-26 08:04:49 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-04-26 08:04:39 | Thawalama (Gin Ganga) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-04-26 08:04:30 | Deraniyagala (Kelani Ganga) | 0.36 | 🟢 Normal | -0.020 |  |
| 2026-04-26 08:04:18 | Panadugama (Nilwala Ganga) | 2.24 | 🟢 Normal | -0.054 |  |
| 2026-04-26 08:03:56 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-04-26 08:03:49 | Katharagama (Menik Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-04-26 08:03:42 | Ellagawa (Kalu Ganga) | 4.34 | 🟢 Normal | 0.000 |  |
| 2026-04-26 08:03:26 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | -0.040 |  |
| 2026-04-26 08:03:08 | Hanwella (Kelani Ganga) | 0.74 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-26 08:03:04 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | -0.011 |  |
| 2026-04-26 08:02:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.20 | 🟢 Normal | -0.089 |  |
| 2026-04-26 08:02:26 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-26 08:01:54 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | -0.020 |  |
| 2026-04-26 08:01:40 | Glencourse (Kelani Ganga) | 8.97 | 🟢 Normal | -0.031 |  |
| 2026-04-26 08:01:27 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-04-26 08:01:16 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-26 08:01:13 | Peradeniya (Mahaweli Ganga) | 1.22 | 🟢 Normal | -0.064 |  |
| 2026-04-26 08:00:54 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-26 08:00:53 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | -0.065 |  |
| 2026-04-26 08:00:50 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-04-26 08:00:37 | Manampitiya (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.020 |  |
| 2026-04-26 07:30:16 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-26 07:23:13 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.030 |  |
| 2026-04-26 07:17:37 | Pitabeddara (Nilwala Ganga) | 0.40 | 🟢 Normal | 4.457 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-26 08:06:05 | Pitabeddara (Nilwala Ganga) | 4.00 | 🟡 Alert | 4.457 | 🔺 Rising |
| 2026-04-26 07:11:36 | Kithulgala (Kelani Ganga) | 1.64 | 🟢 Normal | 0.508 | 🔺 Rising |
| 2026-04-26 08:05:46 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-26 07:01:46 | Weraganthota (Mahaweli Ganga) | -2.97 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-26 08:03:08 | Hanwella (Kelani Ganga) | 0.74 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-26 08:01:27 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-04-26 08:01:16 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-26 07:03:18 | Nawalapitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-26 08:02:26 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-26 08:04:49 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-04-26 08:00:54 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-26 07:01:28 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-26 08:03:42 | Ellagawa (Kalu Ganga) | 4.34 | 🟢 Normal | 0.000 |  |
| 2026-04-26 07:30:16 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-26 08:05:24 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-04-26 08:06:02 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-26 08:03:49 | Katharagama (Menik Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-04-26 08:06:26 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-04-26 07:04:05 | Rathnapura (Kalu Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-04-26 08:00:50 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-04-26 07:03:33 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-04-26 08:03:56 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-04-26 07:07:13 | Magura (Kalu Ganga) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-04-26 08:04:39 | Thawalama (Gin Ganga) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-04-26 08:03:04 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | -0.011 |  |
| 2026-04-26 08:05:56 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | -0.011 |  |
| 2026-04-26 07:02:22 | Baddegama (Gin Ganga) | 1.02 | 🟢 Normal | -0.012 |  |
| 2026-04-26 08:04:30 | Deraniyagala (Kelani Ganga) | 0.36 | 🟢 Normal | -0.020 |  |
| 2026-04-26 08:00:37 | Manampitiya (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.020 |  |
| 2026-04-26 08:01:54 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | -0.020 |  |
| 2026-04-26 07:05:17 | Moragaswewa (Deduru Oya) | 0.83 | 🟢 Normal | -0.028 |  |
| 2026-04-26 07:23:13 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.030 |  |
| 2026-04-26 08:01:40 | Glencourse (Kelani Ganga) | 8.97 | 🟢 Normal | -0.031 |  |
| 2026-04-26 08:03:26 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | -0.040 |  |
| 2026-04-26 08:05:19 | Putupaula (Kalu Ganga) | 0.47 | 🟢 Normal | -0.041 |  |
| 2026-04-26 08:04:18 | Panadugama (Nilwala Ganga) | 2.24 | 🟢 Normal | -0.054 |  |
| 2026-04-26 08:01:13 | Peradeniya (Mahaweli Ganga) | 1.22 | 🟢 Normal | -0.064 |  |
| 2026-04-26 08:00:53 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | -0.065 |  |
| 2026-04-26 08:02:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.20 | 🟢 Normal | -0.089 |  |

## River Water Level Charts by Station

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)