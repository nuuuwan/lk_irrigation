# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--20_05:28:59-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **22,777 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-20 05:28:59 | Glencourse (Kelani Ganga) | 9.05 | 🟢 Normal | 0.000 |  |
| 2025-12-20 05:28:58 | Glencourse (Kelani Ganga) | 9.05 | 🟢 Normal | 0.000 |  |
| 2025-12-20 05:21:45 | Thawalama (Gin Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2025-12-20 05:16:48 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | -0.036 |  |
| 2025-12-20 05:13:35 | Deraniyagala (Kelani Ganga) | 0.44 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2025-12-20 05:13:20 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-20 05:13:11 | Nawalapitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-20 05:12:16 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.080 |  |
| 2025-12-20 05:08:24 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-20 05:08:17 | Hanwella (Kelani Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2025-12-20 05:08:09 | Panadugama (Nilwala Ganga) | 2.62 | 🟢 Normal | -0.010 |  |
| 2025-12-20 05:07:11 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2025-12-20 05:05:57 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-20 05:05:32 | Rathnapura (Kalu Ganga) | 1.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-20 05:05:22 | Peradeniya (Mahaweli Ganga) | 2.62 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2025-12-20 05:04:51 | Kuda Oya (Kirindi Oya) | 1.43 | 🟢 Normal | -0.019 |  |
| 2025-12-20 05:03:34 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-20 05:03:26 | Badalgama (Maha Oya) | 2.58 | 🟢 Normal | -0.010 |  |
| 2025-12-20 05:03:22 | Nakkala (Kumbukkan Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2025-12-20 05:03:14 | Dunamale (Aththanagalu Oya) | 1.26 | 🟢 Normal | -0.010 |  |
| 2025-12-20 05:03:08 | Horowpothana (Yan Oya) | 6.36 | 🟡 Alert | 0.000 |  |
| 2025-12-20 05:03:07 | Horowpothana (Yan Oya) | 6.36 | 🟡 Alert | 0.000 |  |
| 2025-12-20 05:03:06 | Horowpothana (Yan Oya) | 6.36 | 🟡 Alert | 0.000 |  |
| 2025-12-20 05:02:45 | Ellagawa (Kalu Ganga) | 4.61 | 🟢 Normal | -0.019 |  |
| 2025-12-20 05:02:42 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | -0.010 |  |
| 2025-12-20 05:02:35 | Giriulla (Maha Oya) | 1.29 | 🟢 Normal | -0.030 |  |
| 2025-12-20 05:02:35 | Thanamalwila (Kirindi Oya) | 1.09 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2025-12-20 05:02:31 | Thalgahagoda (Nilwala Ganga) | 0.67 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2025-12-20 05:02:13 | Urawa (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2025-12-20 05:01:36 | Manampitiya (Mahaweli Ganga) | 4.20 | 🟡 Alert | -0.021 |  |
| 2025-12-20 05:01:35 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-20 05:01:27 | Thaldena (Mahaweli Ganga) | 0.91 | 🟢 Normal | -0.010 |  |
| 2025-12-20 05:01:14 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-20 05:00:45 | Moragaswewa (Deduru Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2025-12-20 05:00:33 | Siyambalanduwa (Heda Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-20 05:00:17 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | -0.051 |  |
| 2025-12-20 04:54:24 | Moragaswewa (Deduru Oya) | 1.79 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-19 18:02:45 | Thanthirimale (Malwathu Oya) | 5.54 | 🟡 Alert | 0.064 | 🔺 Rising |
| 2025-12-20 05:03:08 | Horowpothana (Yan Oya) | 6.36 | 🟡 Alert | 0.000 |  |
| 2025-12-20 05:01:36 | Manampitiya (Mahaweli Ganga) | 4.20 | 🟡 Alert | -0.021 |  |
| 2025-12-19 18:08:20 | Weraganthota (Mahaweli Ganga) | 1.38 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2025-12-20 05:02:31 | Thalgahagoda (Nilwala Ganga) | 0.67 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2025-12-20 05:07:11 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2025-12-20 05:05:22 | Peradeniya (Mahaweli Ganga) | 2.62 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2025-12-20 05:05:32 | Rathnapura (Kalu Ganga) | 1.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-20 05:13:35 | Deraniyagala (Kelani Ganga) | 0.44 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2025-12-20 05:02:35 | Thanamalwila (Kirindi Oya) | 1.09 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2025-12-20 05:03:34 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-20 05:03:22 | Nakkala (Kumbukkan Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2025-12-20 05:00:45 | Moragaswewa (Deduru Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2025-12-20 05:13:11 | Nawalapitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-20 05:01:35 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-19 18:03:13 | Galgamuwa (Mee Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2025-12-20 05:13:20 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-20 05:05:57 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-20 05:28:59 | Glencourse (Kelani Ganga) | 9.05 | 🟢 Normal | 0.000 |  |
| 2025-12-20 05:01:14 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-20 05:00:33 | Siyambalanduwa (Heda Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-20 05:08:24 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-20 05:21:45 | Thawalama (Gin Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2025-12-20 05:02:13 | Urawa (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2025-12-20 05:08:17 | Hanwella (Kelani Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2025-12-20 05:03:14 | Dunamale (Aththanagalu Oya) | 1.26 | 🟢 Normal | -0.010 |  |
| 2025-12-20 05:02:42 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | -0.010 |  |
| 2025-12-20 05:08:09 | Panadugama (Nilwala Ganga) | 2.62 | 🟢 Normal | -0.010 |  |
| 2025-12-20 05:01:27 | Thaldena (Mahaweli Ganga) | 0.91 | 🟢 Normal | -0.010 |  |
| 2025-12-20 05:03:26 | Badalgama (Maha Oya) | 2.58 | 🟢 Normal | -0.010 |  |
| 2025-12-20 04:00:49 | Magura (Kalu Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2025-12-20 05:04:51 | Kuda Oya (Kirindi Oya) | 1.43 | 🟢 Normal | -0.019 |  |
| 2025-12-20 05:02:45 | Ellagawa (Kalu Ganga) | 4.61 | 🟢 Normal | -0.019 |  |
| 2025-12-20 05:02:35 | Giriulla (Maha Oya) | 1.29 | 🟢 Normal | -0.030 |  |
| 2025-12-20 05:16:48 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | -0.036 |  |
| 2025-12-20 03:07:24 | Padiyathalawa (Maduru Oya) | 1.52 | 🟢 Normal | -0.049 |  |
| 2025-12-20 05:00:17 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | -0.051 |  |
| 2025-12-20 05:12:16 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.080 |  |
| 2025-12-20 04:06:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.30 | 🟢 Normal | -0.112 |  |

## River Water Level Charts by Station

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)