# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--10_18:03:56-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **202,627 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **25** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-10 18:03:56 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-10 18:03:49 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-10 18:03:47 | Yaka Wewa (Ma Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-10 18:03:42 | Magura (Kalu Ganga) | 1.19 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-07-10 18:03:17 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-10 18:03:16 | Thawalama (Gin Ganga) | 1.28 | 🟢 Normal | -0.011 |  |
| 2026-07-10 18:02:59 | Rathnapura (Kalu Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-07-10 18:02:58 | Ellagawa (Kalu Ganga) | 4.49 | 🟢 Normal | 0.000 |  |
| 2026-07-10 18:02:55 | Thalgahagoda (Nilwala Ganga) | 0.16 | 🟢 Normal | -0.010 |  |
| 2026-07-10 18:02:41 | Yaka Wewa (Ma Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-10 18:02:39 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-07-10 18:02:29 | Ellagawa (Kalu Ganga) | 4.49 | 🟢 Normal | 0.000 |  |
| 2026-07-10 18:02:27 | Glencourse (Kelani Ganga) | 9.72 | 🟢 Normal | 0.000 |  |
| 2026-07-10 18:02:24 | Deraniyagala (Kelani Ganga) | 1.13 | 🟢 Normal | 0.162 | 🔺 Rising |
| 2026-07-10 18:02:15 | Putupaula (Kalu Ganga) | 0.30 | 🟢 Normal | -0.020 |  |
| 2026-07-10 18:01:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.94 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-07-10 18:01:50 | Wellawaya (Kirindi Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-07-10 18:01:40 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-07-10 18:01:03 | Thanamalwila (Kirindi Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-07-10 18:01:02 | Nawalapitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.040 |  |
| 2026-07-10 18:00:52 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-10 18:00:32 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-07-10 18:00:14 | Weraganthota (Mahaweli Ganga) | -3.43 | 🟢 Normal | -0.010 |  |
| 2026-07-10 17:22:32 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-10 17:16:24 | Panadugama (Nilwala Ganga) | 2.29 | 🟢 Normal | 0.018 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-10 18:02:24 | Deraniyagala (Kelani Ganga) | 1.13 | 🟢 Normal | 0.162 | 🔺 Rising |
| 2026-07-10 18:03:42 | Magura (Kalu Ganga) | 1.19 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-07-10 18:01:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.94 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-07-10 17:00:19 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-07-10 17:03:29 | Hanwella (Kelani Ganga) | 1.27 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-07-10 17:08:46 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-07-10 17:01:39 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-07-10 17:03:57 | Baddegama (Gin Ganga) | 1.40 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-07-10 17:16:24 | Panadugama (Nilwala Ganga) | 2.29 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-07-10 18:03:17 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-10 18:02:39 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-07-10 18:01:50 | Wellawaya (Kirindi Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-07-10 18:00:52 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-10 18:03:49 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-10 18:03:47 | Yaka Wewa (Ma Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-10 17:05:00 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-07-10 17:22:32 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-10 17:06:34 | Pitabeddara (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-10 17:02:51 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-10 18:02:58 | Ellagawa (Kalu Ganga) | 4.49 | 🟢 Normal | 0.000 |  |
| 2026-07-10 18:03:56 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-10 18:02:27 | Glencourse (Kelani Ganga) | 9.72 | 🟢 Normal | 0.000 |  |
| 2026-07-10 17:11:21 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-10 18:00:32 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-07-10 17:07:50 | Dunamale (Aththanagalu Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-07-10 17:02:30 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-10 17:06:18 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-07-10 17:03:35 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-10 18:02:59 | Rathnapura (Kalu Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-07-10 18:01:40 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-07-10 17:05:52 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-10 17:07:13 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-07-10 18:01:03 | Thanamalwila (Kirindi Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-07-10 18:02:55 | Thalgahagoda (Nilwala Ganga) | 0.16 | 🟢 Normal | -0.010 |  |
| 2026-07-10 18:00:14 | Weraganthota (Mahaweli Ganga) | -3.43 | 🟢 Normal | -0.010 |  |
| 2026-07-10 18:03:16 | Thawalama (Gin Ganga) | 1.28 | 🟢 Normal | -0.011 |  |
| 2026-07-10 17:03:34 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | -0.011 |  |
| 2026-07-10 18:02:15 | Putupaula (Kalu Ganga) | 0.30 | 🟢 Normal | -0.020 |  |
| 2026-07-10 18:01:02 | Nawalapitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.040 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)