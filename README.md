# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--13_21:14:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **17,092 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-13 21:14:26 | Moragaswewa (Deduru Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2025-12-13 21:09:28 | Glencourse (Kelani Ganga) | 9.21 | 🟢 Normal | -0.064 |  |
| 2025-12-13 21:08:40 | Baddegama (Gin Ganga) | 1.48 | 🟢 Normal | -0.010 |  |
| 2025-12-13 21:08:31 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-13 21:07:06 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-13 21:07:01 | Rathnapura (Kalu Ganga) | 1.75 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-13 21:06:27 | Thanamalwila (Kirindi Oya) | 1.16 | 🟢 Normal | -0.010 |  |
| 2025-12-13 21:06:09 | Panadugama (Nilwala Ganga) | 3.15 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2025-12-13 21:06:02 | Moragaswewa (Deduru Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2025-12-13 21:05:51 | Putupaula (Kalu Ganga) | 0.97 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-13 21:05:46 | Siyambalanduwa (Heda Oya) | 0.82 | 🟢 Normal | -0.010 |  |
| 2025-12-13 21:05:40 | Padiyathalawa (Maduru Oya) | 1.03 | 🟢 Normal | -0.020 |  |
| 2025-12-13 21:05:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.81 | 🟢 Normal | -0.029 |  |
| 2025-12-13 21:05:05 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-13 21:04:51 | Thawalama (Gin Ganga) | 1.99 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2025-12-13 21:04:21 | Hanwella (Kelani Ganga) | 1.44 | 🟢 Normal | -0.040 |  |
| 2025-12-13 21:04:07 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-13 21:03:57 | Katharagama (Menik Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2025-12-13 21:03:26 | Giriulla (Maha Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2025-12-13 21:03:19 | Norwood (Kelani Ganga) | 1.02 | 🟢 Normal | -0.024 |  |
| 2025-12-13 21:03:16 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-13 21:03:08 | Urawa (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-13 21:03:03 | Dunamale (Aththanagalu Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2025-12-13 21:03:01 | Moragaswewa (Deduru Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2025-12-13 21:03:00 | Horowpothana (Yan Oya) | 5.44 | 🟢 Normal | -0.049 |  |
| 2025-12-13 21:02:34 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | -0.021 |  |
| 2025-12-13 21:02:21 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | -0.201 |  |
| 2025-12-13 21:02:16 | Badalgama (Maha Oya) | 2.47 | 🟢 Normal | 0.000 |  |
| 2025-12-13 21:02:13 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-13 21:02:13 | Magura (Kalu Ganga) | 2.16 | 🟢 Normal | -0.010 |  |
| 2025-12-13 21:02:07 | Thalgahagoda (Nilwala Ganga) | 0.65 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-13 21:02:05 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-13 21:02:03 | Peradeniya (Mahaweli Ganga) | 2.71 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2025-12-13 21:01:58 | Kuda Oya (Kirindi Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-13 21:01:54 | Nawalapitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | -0.011 |  |
| 2025-12-13 21:01:19 | Ellagawa (Kalu Ganga) | 5.36 | 🟢 Normal | -0.011 |  |
| 2025-12-13 21:00:53 | Manampitiya (Mahaweli Ganga) | 2.27 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2025-12-13 21:00:43 | Yaka Wewa (Ma Oya) | 1.05 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-13 21:02:03 | Peradeniya (Mahaweli Ganga) | 2.71 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2025-12-13 21:04:51 | Thawalama (Gin Ganga) | 1.99 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2025-12-13 21:06:09 | Panadugama (Nilwala Ganga) | 3.15 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2025-12-13 21:00:53 | Manampitiya (Mahaweli Ganga) | 2.27 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2025-12-13 18:02:22 | Thanthirimale (Malwathu Oya) | 4.30 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-13 21:02:07 | Thalgahagoda (Nilwala Ganga) | 0.65 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-13 21:05:51 | Putupaula (Kalu Ganga) | 0.97 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-13 21:07:01 | Rathnapura (Kalu Ganga) | 1.75 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-13 21:02:13 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-13 21:04:07 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-13 21:14:26 | Moragaswewa (Deduru Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2025-12-13 21:00:43 | Yaka Wewa (Ma Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-13 21:03:26 | Giriulla (Maha Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2025-12-13 18:03:58 | Galgamuwa (Mee Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2025-12-13 21:03:16 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-13 21:08:31 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-13 21:05:05 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-13 21:03:57 | Katharagama (Menik Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2025-12-13 21:02:16 | Badalgama (Maha Oya) | 2.47 | 🟢 Normal | 0.000 |  |
| 2025-12-13 21:07:06 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-13 21:03:08 | Urawa (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-13 21:01:58 | Kuda Oya (Kirindi Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-13 21:08:40 | Baddegama (Gin Ganga) | 1.48 | 🟢 Normal | -0.010 |  |
| 2025-12-13 21:03:03 | Dunamale (Aththanagalu Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2025-12-13 21:05:46 | Siyambalanduwa (Heda Oya) | 0.82 | 🟢 Normal | -0.010 |  |
| 2025-12-13 21:06:27 | Thanamalwila (Kirindi Oya) | 1.16 | 🟢 Normal | -0.010 |  |
| 2025-12-13 21:02:13 | Magura (Kalu Ganga) | 2.16 | 🟢 Normal | -0.010 |  |
| 2025-12-13 21:01:54 | Nawalapitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | -0.011 |  |
| 2025-12-13 21:01:19 | Ellagawa (Kalu Ganga) | 5.36 | 🟢 Normal | -0.011 |  |
| 2025-12-13 21:05:40 | Padiyathalawa (Maduru Oya) | 1.03 | 🟢 Normal | -0.020 |  |
| 2025-12-13 21:02:34 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | -0.021 |  |
| 2025-12-13 21:03:19 | Norwood (Kelani Ganga) | 1.02 | 🟢 Normal | -0.024 |  |
| 2025-12-13 21:05:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.81 | 🟢 Normal | -0.029 |  |
| 2025-12-13 20:10:25 | Pitabeddara (Nilwala Ganga) | 0.81 | 🟢 Normal | -0.039 |  |
| 2025-12-13 21:04:21 | Hanwella (Kelani Ganga) | 1.44 | 🟢 Normal | -0.040 |  |
| 2025-12-13 18:05:54 | Weraganthota (Mahaweli Ganga) | -1.36 | 🟢 Normal | -0.048 |  |
| 2025-12-13 21:03:00 | Horowpothana (Yan Oya) | 5.44 | 🟢 Normal | -0.049 |  |
| 2025-12-13 21:09:28 | Glencourse (Kelani Ganga) | 9.21 | 🟢 Normal | -0.064 |  |
| 2025-12-13 21:02:21 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | -0.201 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)