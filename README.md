# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--25_09:39:39-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **27,364 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-25 09:39:39 | Panadugama (Nilwala Ganga) | 2.97 | 🟢 Normal | -0.007 |  |
| 2025-12-25 09:19:01 | Padiyathalawa (Maduru Oya) | 0.95 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2025-12-25 09:17:31 | Horowpothana (Yan Oya) | 2.22 | 🟢 Normal | -0.008 |  |
| 2025-12-25 09:16:46 | Urawa (Nilwala Ganga) | 0.95 | 🟢 Normal | -0.066 |  |
| 2025-12-25 09:14:04 | Galgamuwa (Mee Oya) | 0.42 | 🟢 Normal | -0.009 |  |
| 2025-12-25 09:09:24 | Magura (Kalu Ganga) | 1.90 | 🟢 Normal | -0.086 |  |
| 2025-12-25 09:08:54 | Yaka Wewa (Ma Oya) | 0.88 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2025-12-25 09:07:23 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.089 |  |
| 2025-12-25 09:06:25 | Thalgahagoda (Nilwala Ganga) | 0.66 | 🟢 Normal | -0.023 |  |
| 2025-12-25 09:06:20 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | -0.010 |  |
| 2025-12-25 09:05:40 | Glencourse (Kelani Ganga) | 9.04 | 🟢 Normal | 0.000 |  |
| 2025-12-25 09:05:39 | Badalgama (Maha Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2025-12-25 09:05:28 | Thanamalwila (Kirindi Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-25 09:05:26 | Weraganthota (Mahaweli Ganga) | -1.23 | 🟢 Normal | -0.201 |  |
| 2025-12-25 09:05:14 | Manampitiya (Mahaweli Ganga) | 1.72 | 🟢 Normal | -0.009 |  |
| 2025-12-25 09:04:54 | Rathnapura (Kalu Ganga) | 1.84 | 🟢 Normal | -0.040 |  |
| 2025-12-25 09:04:40 | Pitabeddara (Nilwala Ganga) | 1.13 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2025-12-25 09:03:52 | Hanwella (Kelani Ganga) | 0.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-25 09:03:52 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-25 09:03:40 | Giriulla (Maha Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-25 09:03:35 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2025-12-25 09:03:29 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-25 09:02:59 | Putupaula (Kalu Ganga) | 0.76 | 🟢 Normal | -0.074 |  |
| 2025-12-25 09:02:42 | Thanthirimale (Malwathu Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2025-12-25 09:02:32 | Moraketiya (Walawe Ganga) | 1.20 | 🟢 Normal | 0.194 | 🔺 Rising |
| 2025-12-25 09:02:28 | Dunamale (Aththanagalu Oya) | 0.78 | 🟢 Normal | -0.010 |  |
| 2025-12-25 09:02:23 | Nawalapitiya (Mahaweli Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-25 09:02:17 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.010 |  |
| 2025-12-25 09:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.71 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2025-12-25 09:02:07 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2025-12-25 09:02:05 | Ellagawa (Kalu Ganga) | 5.02 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2025-12-25 09:02:00 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2025-12-25 09:01:33 | Moragaswewa (Deduru Oya) | 0.63 | 🟢 Normal | -0.010 |  |
| 2025-12-25 09:01:27 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2025-12-25 09:01:08 | Baddegama (Gin Ganga) | 1.74 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2025-12-25 09:00:27 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-25 09:00:06 | Nakkala (Kumbukkan Oya) | 1.15 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-25 09:02:32 | Moraketiya (Walawe Ganga) | 1.20 | 🟢 Normal | 0.194 | 🔺 Rising |
| 2025-12-25 09:04:40 | Pitabeddara (Nilwala Ganga) | 1.13 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2025-12-25 09:08:54 | Yaka Wewa (Ma Oya) | 0.88 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2025-12-25 09:02:05 | Ellagawa (Kalu Ganga) | 5.02 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2025-12-25 09:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.71 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2025-12-25 09:03:29 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-25 09:01:08 | Baddegama (Gin Ganga) | 1.74 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2025-12-25 09:19:01 | Padiyathalawa (Maduru Oya) | 0.95 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2025-12-25 09:02:00 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2025-12-25 09:03:52 | Hanwella (Kelani Ganga) | 0.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-25 09:02:07 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2025-12-25 09:00:06 | Nakkala (Kumbukkan Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-25 09:02:23 | Nawalapitiya (Mahaweli Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-25 09:03:40 | Giriulla (Maha Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-25 09:03:52 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-25 09:05:40 | Glencourse (Kelani Ganga) | 9.04 | 🟢 Normal | 0.000 |  |
| 2025-12-25 09:00:27 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-25 09:03:35 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2025-12-25 09:05:39 | Badalgama (Maha Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2025-12-25 09:02:42 | Thanthirimale (Malwathu Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2025-12-25 08:11:49 | Thawalama (Gin Ganga) | 2.64 | 🟢 Normal | 0.000 |  |
| 2025-12-25 08:05:31 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2025-12-25 09:01:27 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2025-12-25 09:05:28 | Thanamalwila (Kirindi Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-25 09:39:39 | Panadugama (Nilwala Ganga) | 2.97 | 🟢 Normal | -0.007 |  |
| 2025-12-25 09:17:31 | Horowpothana (Yan Oya) | 2.22 | 🟢 Normal | -0.008 |  |
| 2025-12-25 09:05:14 | Manampitiya (Mahaweli Ganga) | 1.72 | 🟢 Normal | -0.009 |  |
| 2025-12-25 09:14:04 | Galgamuwa (Mee Oya) | 0.42 | 🟢 Normal | -0.009 |  |
| 2025-12-25 09:02:28 | Dunamale (Aththanagalu Oya) | 0.78 | 🟢 Normal | -0.010 |  |
| 2025-12-25 09:01:33 | Moragaswewa (Deduru Oya) | 0.63 | 🟢 Normal | -0.010 |  |
| 2025-12-25 09:02:17 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.010 |  |
| 2025-12-25 09:06:20 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | -0.010 |  |
| 2025-12-25 09:06:25 | Thalgahagoda (Nilwala Ganga) | 0.66 | 🟢 Normal | -0.023 |  |
| 2025-12-25 09:04:54 | Rathnapura (Kalu Ganga) | 1.84 | 🟢 Normal | -0.040 |  |
| 2025-12-25 09:16:46 | Urawa (Nilwala Ganga) | 0.95 | 🟢 Normal | -0.066 |  |
| 2025-12-25 09:02:59 | Putupaula (Kalu Ganga) | 0.76 | 🟢 Normal | -0.074 |  |
| 2025-12-25 09:09:24 | Magura (Kalu Ganga) | 1.90 | 🟢 Normal | -0.086 |  |
| 2025-12-25 09:07:23 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.089 |  |
| 2025-12-25 09:05:26 | Weraganthota (Mahaweli Ganga) | -1.23 | 🟢 Normal | -0.201 |  |

## River Water Level Charts by Station

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)