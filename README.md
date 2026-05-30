# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--30_18:25:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **165,927 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **43** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-30 18:25:20 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-05-30 18:16:53 | Panadugama (Nilwala Ganga) | 3.29 | 🟢 Normal | -0.018 |  |
| 2026-05-30 18:13:57 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-05-30 18:09:25 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-30 18:09:10 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-05-30 18:09:09 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-30 18:08:19 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-05-30 18:06:43 | Glencourse (Kelani Ganga) | 10.30 | 🟢 Normal | -0.049 |  |
| 2026-05-30 18:06:37 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-05-30 18:06:36 | Dunamale (Aththanagalu Oya) | 1.59 | 🟢 Normal | -0.009 |  |
| 2026-05-30 18:06:35 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.056 |  |
| 2026-05-30 18:06:14 | Rathnapura (Kalu Ganga) | 2.28 | 🟢 Normal | -0.040 |  |
| 2026-05-30 18:06:00 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-30 18:06:00 | Deraniyagala (Kelani Ganga) | 1.28 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-30 18:05:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.20 | 🟡 Alert | -0.041 |  |
| 2026-05-30 18:05:02 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-05-30 18:04:48 | Galgamuwa (Mee Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-05-30 18:04:36 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-30 18:04:16 | Baddegama (Gin Ganga) | 2.67 | 🟢 Normal | -0.041 |  |
| 2026-05-30 18:04:08 | Putupaula (Kalu Ganga) | 2.48 | 🟢 Normal | -0.020 |  |
| 2026-05-30 18:04:03 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-05-30 18:03:55 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-30 18:03:54 | Badalgama (Maha Oya) | 2.30 | 🟢 Normal | -0.010 |  |
| 2026-05-30 18:03:53 | Ellagawa (Kalu Ganga) | 7.24 | 🟢 Normal | -0.101 |  |
| 2026-05-30 18:03:47 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-30 18:03:46 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-30 18:03:33 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-30 18:03:31 | Thanthirimale (Malwathu Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-05-30 18:03:25 | Magura (Kalu Ganga) | 2.67 | 🟢 Normal | -0.038 |  |
| 2026-05-30 18:03:18 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-30 18:03:01 | Thalgahagoda (Nilwala Ganga) | 0.64 | 🟢 Normal | -0.041 |  |
| 2026-05-30 18:02:27 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-30 18:02:17 | Thanamalwila (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-30 18:02:15 | Hanwella (Kelani Ganga) | 2.68 | 🟢 Normal | -0.071 |  |
| 2026-05-30 18:02:05 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | -0.030 |  |
| 2026-05-30 18:02:04 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | -30.857 |  |
| 2026-05-30 18:01:57 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | -30.857 |  |
| 2026-05-30 18:01:55 | Giriulla (Maha Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-05-30 18:01:33 | Thawalama (Gin Ganga) | 1.89 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-05-30 18:01:05 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | -0.020 |  |
| 2026-05-30 18:00:56 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | 0.000 |  |
| 2026-05-30 18:00:35 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-05-30 18:00:19 | Nawalapitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.022 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-30 18:05:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.20 | 🟡 Alert | -0.041 |  |
| 2026-05-30 18:01:33 | Thawalama (Gin Ganga) | 1.89 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-05-30 18:06:37 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-05-30 18:06:00 | Deraniyagala (Kelani Ganga) | 1.28 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-30 18:00:56 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | 0.000 |  |
| 2026-05-30 18:03:47 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-30 18:25:20 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-05-30 18:09:25 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-30 18:04:03 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-05-30 18:04:48 | Galgamuwa (Mee Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-05-30 18:04:36 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-30 18:03:55 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-30 18:03:33 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-30 18:03:18 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-30 18:05:02 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-05-30 18:08:19 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-05-30 18:03:31 | Thanthirimale (Malwathu Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-05-30 18:13:57 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-05-30 18:06:00 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-30 18:02:17 | Thanamalwila (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-30 17:04:56 | Pitabeddara (Nilwala Ganga) | 0.82 | 🟢 Normal | -0.005 |  |
| 2026-05-30 18:06:36 | Dunamale (Aththanagalu Oya) | 1.59 | 🟢 Normal | -0.009 |  |
| 2026-05-30 18:01:55 | Giriulla (Maha Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-05-30 18:00:35 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-05-30 18:03:54 | Badalgama (Maha Oya) | 2.30 | 🟢 Normal | -0.010 |  |
| 2026-05-30 18:16:53 | Panadugama (Nilwala Ganga) | 3.29 | 🟢 Normal | -0.018 |  |
| 2026-05-30 18:01:05 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | -0.020 |  |
| 2026-05-30 18:04:08 | Putupaula (Kalu Ganga) | 2.48 | 🟢 Normal | -0.020 |  |
| 2026-05-30 18:00:19 | Nawalapitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.022 |  |
| 2026-05-30 18:02:05 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | -0.030 |  |
| 2026-05-30 18:03:25 | Magura (Kalu Ganga) | 2.67 | 🟢 Normal | -0.038 |  |
| 2026-05-30 18:06:14 | Rathnapura (Kalu Ganga) | 2.28 | 🟢 Normal | -0.040 |  |
| 2026-05-30 18:03:01 | Thalgahagoda (Nilwala Ganga) | 0.64 | 🟢 Normal | -0.041 |  |
| 2026-05-30 18:04:16 | Baddegama (Gin Ganga) | 2.67 | 🟢 Normal | -0.041 |  |
| 2026-05-30 18:06:43 | Glencourse (Kelani Ganga) | 10.30 | 🟢 Normal | -0.049 |  |
| 2026-05-30 18:06:35 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.056 |  |
| 2026-05-30 18:02:15 | Hanwella (Kelani Ganga) | 2.68 | 🟢 Normal | -0.071 |  |
| 2026-05-30 18:03:53 | Ellagawa (Kalu Ganga) | 7.24 | 🟢 Normal | -0.101 |  |
| 2026-05-30 18:02:04 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | -30.857 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)