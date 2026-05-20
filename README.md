# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--20_14:22:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **157,030 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-20 14:22:13 | Urawa (Nilwala Ganga) | 0.11 | 🟢 Normal | -0.008 |  |
| 2026-05-20 14:20:56 | Panadugama (Nilwala Ganga) | 2.45 | 🟢 Normal | 0.000 |  |
| 2026-05-20 14:16:50 | Dunamale (Aththanagalu Oya) | 2.38 | 🟢 Normal | -0.016 |  |
| 2026-05-20 14:08:29 | Baddegama (Gin Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-05-20 14:07:35 | Rathnapura (Kalu Ganga) | 1.42 | 🟢 Normal | -0.012 |  |
| 2026-05-20 14:07:29 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-20 14:06:18 | Holombuwa (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-20 14:05:50 | Ellagawa (Kalu Ganga) | 5.23 | 🟢 Normal | 0.000 |  |
| 2026-05-20 14:05:45 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-05-20 14:05:17 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | -0.005 |  |
| 2026-05-20 14:04:52 | Glencourse (Kelani Ganga) | 9.70 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-20 14:04:50 | Peradeniya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-05-20 14:04:42 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-05-20 14:04:28 | Badalgama (Maha Oya) | 2.69 | 🟢 Normal | 0.000 |  |
| 2026-05-20 14:04:09 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-05-20 14:04:06 | Nawalapitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-20 14:03:46 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-05-20 14:03:37 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-05-20 14:03:18 | Hanwella (Kelani Ganga) | 1.72 | 🟢 Normal | -0.040 |  |
| 2026-05-20 14:03:12 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-05-20 14:03:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.21 | 🟢 Normal | 0.000 |  |
| 2026-05-20 14:03:06 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | -0.009 |  |
| 2026-05-20 14:02:56 | Giriulla (Maha Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-05-20 14:02:51 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-05-20 14:02:51 | Moragaswewa (Deduru Oya) | 1.26 | 🟢 Normal | -0.045 |  |
| 2026-05-20 14:02:48 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-05-20 14:02:26 | Deraniyagala (Kelani Ganga) | 0.66 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-20 14:02:12 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-20 14:02:08 | Thanamalwila (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-05-20 14:01:53 | Thawalama (Gin Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-05-20 14:01:45 | Putupaula (Kalu Ganga) | 0.74 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-05-20 14:01:23 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-05-20 14:01:21 | Manampitiya (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-20 14:01:16 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-05-20 14:01:13 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | 0.000 |  |
| 2026-05-20 14:01:12 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | -0.012 |  |
| 2026-05-20 14:00:56 | Thanthirimale (Malwathu Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-05-20 14:00:47 | Galgamuwa (Mee Oya) | 0.78 | 🟢 Normal | 0.012 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-20 14:01:45 | Putupaula (Kalu Ganga) | 0.74 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-05-20 14:04:09 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-05-20 14:03:46 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-05-20 14:02:26 | Deraniyagala (Kelani Ganga) | 0.66 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-20 14:04:52 | Glencourse (Kelani Ganga) | 9.70 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-20 14:04:06 | Nawalapitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-20 14:00:47 | Galgamuwa (Mee Oya) | 0.78 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-05-20 14:03:12 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-05-20 14:01:13 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | 0.000 |  |
| 2026-05-20 14:02:51 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-05-20 14:01:16 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-05-20 14:05:45 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-05-20 14:02:56 | Giriulla (Maha Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-05-20 13:02:21 | Magura (Kalu Ganga) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-05-20 14:05:50 | Ellagawa (Kalu Ganga) | 5.23 | 🟢 Normal | 0.000 |  |
| 2026-05-20 14:08:29 | Baddegama (Gin Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-05-20 14:20:56 | Panadugama (Nilwala Ganga) | 2.45 | 🟢 Normal | 0.000 |  |
| 2026-05-20 14:02:12 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-20 14:07:29 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-20 14:04:42 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-05-20 14:04:28 | Badalgama (Maha Oya) | 2.69 | 🟢 Normal | 0.000 |  |
| 2026-05-20 14:06:18 | Holombuwa (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-20 14:01:21 | Manampitiya (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-20 14:00:56 | Thanthirimale (Malwathu Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-05-20 14:01:53 | Thawalama (Gin Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-05-20 14:04:50 | Peradeniya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-05-20 14:02:08 | Thanamalwila (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-05-20 14:03:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.21 | 🟢 Normal | 0.000 |  |
| 2026-05-20 14:05:17 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | -0.005 |  |
| 2026-05-20 14:22:13 | Urawa (Nilwala Ganga) | 0.11 | 🟢 Normal | -0.008 |  |
| 2026-05-20 14:03:06 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | -0.009 |  |
| 2026-05-20 14:02:48 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-05-20 14:03:37 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-05-20 14:01:23 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-05-20 14:07:35 | Rathnapura (Kalu Ganga) | 1.42 | 🟢 Normal | -0.012 |  |
| 2026-05-20 14:01:12 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | -0.012 |  |
| 2026-05-20 14:16:50 | Dunamale (Aththanagalu Oya) | 2.38 | 🟢 Normal | -0.016 |  |
| 2026-05-20 14:03:18 | Hanwella (Kelani Ganga) | 1.72 | 🟢 Normal | -0.040 |  |
| 2026-05-20 14:02:51 | Moragaswewa (Deduru Oya) | 1.26 | 🟢 Normal | -0.045 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

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

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)