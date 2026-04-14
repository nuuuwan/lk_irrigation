# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--14_17:19:59-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **125,021 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-14 17:19:59 | Baddegama (Gin Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-04-14 17:18:26 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-04-14 17:16:46 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-14 17:14:27 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-14 17:12:59 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-04-14 17:09:54 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-04-14 17:08:27 | Magura (Kalu Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-04-14 17:07:18 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.093 |  |
| 2026-04-14 17:06:37 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-14 17:06:15 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-14 17:06:08 | Rathnapura (Kalu Ganga) | 0.96 | 🟢 Normal | -0.025 |  |
| 2026-04-14 17:06:07 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-14 17:05:48 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-04-14 17:05:40 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | -0.011 |  |
| 2026-04-14 17:05:14 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-14 17:04:55 | Baddegama (Gin Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-04-14 17:04:45 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.236 | 🔺 Rising |
| 2026-04-14 17:04:28 | Peradeniya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-04-14 17:04:13 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | -0.020 |  |
| 2026-04-14 17:04:08 | Moragaswewa (Deduru Oya) | 0.94 | 🟢 Normal | -0.019 |  |
| 2026-04-14 17:04:02 | Badalgama (Maha Oya) | 2.03 | 🟢 Normal | -0.010 |  |
| 2026-04-14 17:03:57 | Dunamale (Aththanagalu Oya) | 0.47 | 🟢 Normal | -0.142 |  |
| 2026-04-14 17:03:34 | Ellagawa (Kalu Ganga) | 4.40 | 🟢 Normal | 0.000 |  |
| 2026-04-14 17:03:27 | Weraganthota (Mahaweli Ganga) | -2.94 | 🟢 Normal | -0.216 |  |
| 2026-04-14 17:03:23 | Glencourse (Kelani Ganga) | 8.49 | 🟢 Normal | 0.000 |  |
| 2026-04-14 17:02:56 | Putupaula (Kalu Ganga) | 0.81 | 🟢 Normal | -0.119 |  |
| 2026-04-14 17:02:55 | Manampitiya (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-14 17:02:31 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-04-14 17:02:14 | Katharagama (Menik Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-14 17:02:10 | Deraniyagala (Kelani Ganga) | 0.25 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-04-14 17:01:54 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.010 |  |
| 2026-04-14 17:01:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.14 | 🟢 Normal | -0.040 |  |
| 2026-04-14 17:01:26 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | -0.011 |  |
| 2026-04-14 17:01:24 | Kuda Oya (Kirindi Oya) | 1.46 | 🟢 Normal | -0.020 |  |
| 2026-04-14 17:01:12 | Thanamalwila (Kirindi Oya) | 1.30 | 🟢 Normal | -0.064 |  |
| 2026-04-14 17:00:58 | Horowpothana (Yan Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-04-14 17:00:56 | Thanthirimale (Malwathu Oya) | 3.85 | 🟢 Normal | -0.080 |  |
| 2026-04-14 17:00:31 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-04-14 17:00:28 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-04-14 17:00:12 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-04-14 16:59:44 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | -0.142 |  |
| 2026-04-14 16:52:28 | Horowpothana (Yan Oya) | 1.53 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-14 17:04:45 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.236 | 🔺 Rising |
| 2026-04-14 17:02:10 | Deraniyagala (Kelani Ganga) | 0.25 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-04-14 17:00:28 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-04-14 17:18:26 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-04-14 17:16:46 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-14 17:00:58 | Horowpothana (Yan Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-04-14 17:06:07 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-14 17:08:27 | Magura (Kalu Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-04-14 17:03:34 | Ellagawa (Kalu Ganga) | 4.40 | 🟢 Normal | 0.000 |  |
| 2026-04-14 17:19:59 | Baddegama (Gin Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-04-14 17:00:12 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-04-14 17:05:14 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-14 17:03:23 | Glencourse (Kelani Ganga) | 8.49 | 🟢 Normal | 0.000 |  |
| 2026-04-14 17:12:59 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-04-14 17:02:31 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-04-14 17:02:14 | Katharagama (Menik Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-14 17:14:27 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-14 17:02:55 | Manampitiya (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-14 17:06:37 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-14 17:04:28 | Peradeniya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-04-14 17:06:15 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-14 17:05:48 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-04-14 17:04:02 | Badalgama (Maha Oya) | 2.03 | 🟢 Normal | -0.010 |  |
| 2026-04-14 17:00:31 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-04-14 17:01:54 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.010 |  |
| 2026-04-14 17:05:40 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | -0.011 |  |
| 2026-04-14 17:01:26 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | -0.011 |  |
| 2026-04-14 17:04:08 | Moragaswewa (Deduru Oya) | 0.94 | 🟢 Normal | -0.019 |  |
| 2026-04-14 17:04:13 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | -0.020 |  |
| 2026-04-14 16:01:17 | Nawalapitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | -0.020 |  |
| 2026-04-14 17:01:24 | Kuda Oya (Kirindi Oya) | 1.46 | 🟢 Normal | -0.020 |  |
| 2026-04-14 17:06:08 | Rathnapura (Kalu Ganga) | 0.96 | 🟢 Normal | -0.025 |  |
| 2026-04-14 17:01:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.14 | 🟢 Normal | -0.040 |  |
| 2026-04-14 17:01:12 | Thanamalwila (Kirindi Oya) | 1.30 | 🟢 Normal | -0.064 |  |
| 2026-04-14 17:00:56 | Thanthirimale (Malwathu Oya) | 3.85 | 🟢 Normal | -0.080 |  |
| 2026-04-14 17:07:18 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.093 |  |
| 2026-04-14 17:02:56 | Putupaula (Kalu Ganga) | 0.81 | 🟢 Normal | -0.119 |  |
| 2026-04-14 17:03:57 | Dunamale (Aththanagalu Oya) | 0.47 | 🟢 Normal | -0.142 |  |
| 2026-04-14 17:03:27 | Weraganthota (Mahaweli Ganga) | -2.94 | 🟢 Normal | -0.216 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)