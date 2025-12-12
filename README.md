# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--12_22:18:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **16,224 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-12 22:18:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.07 | 🟢 Normal | -0.022 |  |
| 2025-12-12 22:17:21 | Magura (Kalu Ganga) | 2.40 | 🟢 Normal | 0.000 |  |
| 2025-12-12 22:13:58 | Dunamale (Aththanagalu Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-12 22:11:40 | Rathnapura (Kalu Ganga) | 2.53 | 🟢 Normal | -0.018 |  |
| 2025-12-12 22:09:09 | Thaldena (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-12 22:08:15 | Baddegama (Gin Ganga) | 1.89 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-12 22:07:21 | Putupaula (Kalu Ganga) | 1.09 | 🟢 Normal | -0.019 |  |
| 2025-12-12 22:06:50 | Urawa (Nilwala Ganga) | 0.68 | 🟢 Normal | -0.009 |  |
| 2025-12-12 22:06:19 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-12 22:05:50 | Panadugama (Nilwala Ganga) | 3.63 | 🟢 Normal | -0.040 |  |
| 2025-12-12 22:05:14 | Badalgama (Maha Oya) | 2.52 | 🟢 Normal | -0.010 |  |
| 2025-12-12 22:05:03 | Thalgahagoda (Nilwala Ganga) | 0.88 | 🟢 Normal | -0.039 |  |
| 2025-12-12 22:04:43 | Hanwella (Kelani Ganga) | 1.84 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-12 22:04:38 | Manampitiya (Mahaweli Ganga) | 2.65 | 🟢 Normal | -0.110 |  |
| 2025-12-12 22:04:00 | Wellawaya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-12 22:03:52 | Nakkala (Kumbukkan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2025-12-12 22:03:31 | Thanamalwila (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2025-12-12 22:03:28 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | -0.066 |  |
| 2025-12-12 22:03:05 | Norwood (Kelani Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2025-12-12 22:03:04 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.021 |  |
| 2025-12-12 22:03:00 | Moragaswewa (Deduru Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2025-12-12 22:02:38 | Katharagama (Menik Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2025-12-12 22:02:36 | Moragaswewa (Deduru Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2025-12-12 22:02:13 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-12 22:02:12 | Yaka Wewa (Ma Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-12 22:02:08 | Siyambalanduwa (Heda Oya) | 0.95 | 🟢 Normal | -0.020 |  |
| 2025-12-12 22:01:30 | Ellagawa (Kalu Ganga) | 6.02 | 🟢 Normal | -0.020 |  |
| 2025-12-12 22:01:27 | Kuda Oya (Kirindi Oya) | 1.69 | 🟢 Normal | -0.020 |  |
| 2025-12-12 22:01:22 | Nawalapitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-12 22:01:18 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.070 |  |
| 2025-12-12 22:01:17 | Giriulla (Maha Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2025-12-12 22:01:13 | Pitabeddara (Nilwala Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-12 22:00:52 | Moraketiya (Walawe Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-12 22:00:51 | Horowpothana (Yan Oya) | 6.36 | 🟡 Alert | -0.021 |  |
| 2025-12-12 22:00:46 | Peradeniya (Mahaweli Ganga) | 2.59 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-12 22:00:38 | Padiyathalawa (Maduru Oya) | 1.40 | 🟢 Normal | -0.021 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-12 22:00:51 | Horowpothana (Yan Oya) | 6.36 | 🟡 Alert | -0.021 |  |
| 2025-12-12 22:00:46 | Peradeniya (Mahaweli Ganga) | 2.59 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-12 22:04:43 | Hanwella (Kelani Ganga) | 1.84 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-12 22:06:19 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-12 22:08:15 | Baddegama (Gin Ganga) | 1.89 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-12 22:04:00 | Wellawaya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-12 22:03:52 | Nakkala (Kumbukkan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2025-12-12 22:03:00 | Moragaswewa (Deduru Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2025-12-12 22:01:22 | Nawalapitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-12 22:02:12 | Yaka Wewa (Ma Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-12 22:01:17 | Giriulla (Maha Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2025-12-12 18:09:46 | Galgamuwa (Mee Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-12 22:17:21 | Magura (Kalu Ganga) | 2.40 | 🟢 Normal | 0.000 |  |
| 2025-12-12 22:01:13 | Pitabeddara (Nilwala Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-12 22:02:13 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-12 21:12:58 | Glencourse (Kelani Ganga) | 9.85 | 🟢 Normal | 0.000 |  |
| 2025-12-12 22:00:52 | Moraketiya (Walawe Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-12 22:13:58 | Dunamale (Aththanagalu Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-12 22:09:09 | Thaldena (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-12 22:02:38 | Katharagama (Menik Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2025-12-12 18:03:10 | Thanthirimale (Malwathu Oya) | 4.35 | 🟢 Normal | 0.000 |  |
| 2025-12-12 22:03:31 | Thanamalwila (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2025-12-12 22:06:50 | Urawa (Nilwala Ganga) | 0.68 | 🟢 Normal | -0.009 |  |
| 2025-12-12 22:05:14 | Badalgama (Maha Oya) | 2.52 | 🟢 Normal | -0.010 |  |
| 2025-12-12 22:03:05 | Norwood (Kelani Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2025-12-12 22:11:40 | Rathnapura (Kalu Ganga) | 2.53 | 🟢 Normal | -0.018 |  |
| 2025-12-12 22:07:21 | Putupaula (Kalu Ganga) | 1.09 | 🟢 Normal | -0.019 |  |
| 2025-12-12 22:01:27 | Kuda Oya (Kirindi Oya) | 1.69 | 🟢 Normal | -0.020 |  |
| 2025-12-12 22:01:30 | Ellagawa (Kalu Ganga) | 6.02 | 🟢 Normal | -0.020 |  |
| 2025-12-12 22:02:08 | Siyambalanduwa (Heda Oya) | 0.95 | 🟢 Normal | -0.020 |  |
| 2025-12-12 22:03:04 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.021 |  |
| 2025-12-12 22:00:38 | Padiyathalawa (Maduru Oya) | 1.40 | 🟢 Normal | -0.021 |  |
| 2025-12-12 22:18:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.07 | 🟢 Normal | -0.022 |  |
| 2025-12-12 22:05:03 | Thalgahagoda (Nilwala Ganga) | 0.88 | 🟢 Normal | -0.039 |  |
| 2025-12-12 22:05:50 | Panadugama (Nilwala Ganga) | 3.63 | 🟢 Normal | -0.040 |  |
| 2025-12-12 22:03:28 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | -0.066 |  |
| 2025-12-12 22:01:18 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.070 |  |
| 2025-12-12 18:01:38 | Weraganthota (Mahaweli Ganga) | -1.25 | 🟢 Normal | -0.106 |  |
| 2025-12-12 22:04:38 | Manampitiya (Mahaweli Ganga) | 2.65 | 🟢 Normal | -0.110 |  |

## River Water Level Charts by Station

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)