# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--26_21:14:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **162,457 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-26 21:14:46 | Panadugama (Nilwala Ganga) | 2.89 | 🟢 Normal | -0.010 |  |
| 2026-05-26 21:12:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.24 | 🟡 Alert | 0.000 |  |
| 2026-05-26 21:08:41 | Magura (Kalu Ganga) | 2.86 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-05-26 21:08:23 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-05-26 21:08:21 | Holombuwa (Kelani Ganga) | 0.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-26 21:06:27 | Badalgama (Maha Oya) | 2.51 | 🟢 Normal | -0.010 |  |
| 2026-05-26 21:06:17 | Deraniyagala (Kelani Ganga) | 1.53 | 🟢 Normal | -0.039 |  |
| 2026-05-26 21:06:06 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-26 21:05:18 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-26 21:05:12 | Hanwella (Kelani Ganga) | 4.60 | 🟢 Normal | -0.038 |  |
| 2026-05-26 21:04:36 | Rathnapura (Kalu Ganga) | 4.08 | 🟢 Normal | -0.077 |  |
| 2026-05-26 21:04:22 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-26 21:03:58 | Nawalapitiya (Mahaweli Ganga) | 1.51 | 🟢 Normal | -0.010 |  |
| 2026-05-26 21:03:50 | Ellagawa (Kalu Ganga) | 8.68 | 🟢 Normal | -0.010 |  |
| 2026-05-26 21:03:38 | Kithulgala (Kelani Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-05-26 21:03:35 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-26 21:03:32 | Baddegama (Gin Ganga) | 2.06 | 🟢 Normal | -0.021 |  |
| 2026-05-26 21:03:23 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-26 21:03:14 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-26 21:03:08 | Giriulla (Maha Oya) | 1.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-26 21:02:53 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-26 21:02:48 | Dunamale (Aththanagalu Oya) | 2.57 | 🟢 Normal | -0.030 |  |
| 2026-05-26 21:02:33 | Thawalama (Gin Ganga) | 2.07 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-26 21:02:32 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-26 21:02:32 | Glencourse (Kelani Ganga) | 12.02 | 🟢 Normal | -0.040 |  |
| 2026-05-26 21:02:22 | Peradeniya (Mahaweli Ganga) | 1.76 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-05-26 21:02:13 | Thanamalwila (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-26 21:02:12 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-26 21:01:26 | Moragaswewa (Deduru Oya) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-05-26 21:01:23 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-26 21:01:10 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.021 |  |
| 2026-05-26 21:01:07 | Putupaula (Kalu Ganga) | 2.45 | 🟢 Normal | -0.025 |  |
| 2026-05-26 21:01:04 | Pitabeddara (Nilwala Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-26 21:00:54 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-26 21:00:45 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-26 21:12:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.24 | 🟡 Alert | 0.000 |  |
| 2026-05-26 21:02:22 | Peradeniya (Mahaweli Ganga) | 1.76 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-05-26 21:08:41 | Magura (Kalu Ganga) | 2.86 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-05-26 21:06:06 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-26 21:02:33 | Thawalama (Gin Ganga) | 2.07 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-26 20:35:43 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-05-26 18:04:02 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-26 21:03:08 | Giriulla (Maha Oya) | 1.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-26 21:08:21 | Holombuwa (Kelani Ganga) | 0.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-26 21:03:38 | Kithulgala (Kelani Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-05-26 21:00:45 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-26 21:00:54 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-26 21:01:23 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-26 21:05:18 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-26 21:01:04 | Pitabeddara (Nilwala Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-26 21:03:23 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-26 21:03:35 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-26 21:04:22 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-26 21:02:32 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-26 21:02:53 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-26 21:02:12 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-26 21:08:23 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-05-26 18:00:51 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-26 21:03:14 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-26 21:02:13 | Thanamalwila (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-26 21:14:46 | Panadugama (Nilwala Ganga) | 2.89 | 🟢 Normal | -0.010 |  |
| 2026-05-26 21:03:58 | Nawalapitiya (Mahaweli Ganga) | 1.51 | 🟢 Normal | -0.010 |  |
| 2026-05-26 21:03:50 | Ellagawa (Kalu Ganga) | 8.68 | 🟢 Normal | -0.010 |  |
| 2026-05-26 21:06:27 | Badalgama (Maha Oya) | 2.51 | 🟢 Normal | -0.010 |  |
| 2026-05-26 21:01:26 | Moragaswewa (Deduru Oya) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-05-26 18:04:06 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | -0.020 |  |
| 2026-05-26 21:01:10 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.021 |  |
| 2026-05-26 21:03:32 | Baddegama (Gin Ganga) | 2.06 | 🟢 Normal | -0.021 |  |
| 2026-05-26 21:01:07 | Putupaula (Kalu Ganga) | 2.45 | 🟢 Normal | -0.025 |  |
| 2026-05-26 21:02:48 | Dunamale (Aththanagalu Oya) | 2.57 | 🟢 Normal | -0.030 |  |
| 2026-05-26 21:05:12 | Hanwella (Kelani Ganga) | 4.60 | 🟢 Normal | -0.038 |  |
| 2026-05-26 21:06:17 | Deraniyagala (Kelani Ganga) | 1.53 | 🟢 Normal | -0.039 |  |
| 2026-05-26 21:02:32 | Glencourse (Kelani Ganga) | 12.02 | 🟢 Normal | -0.040 |  |
| 2026-05-26 21:04:36 | Rathnapura (Kalu Ganga) | 4.08 | 🟢 Normal | -0.077 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)