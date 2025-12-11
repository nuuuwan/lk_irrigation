# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--11_18:26:44-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **15,200 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-11 18:26:44 | Thalgahagoda (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-11 18:10:07 | Magura (Kalu Ganga) | 1.67 | 🟢 Normal | 0.000 |  |
| 2025-12-11 18:08:24 | Dunamale (Aththanagalu Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2025-12-11 18:07:58 | Holombuwa (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-11 18:07:03 | Pitabeddara (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-11 18:06:32 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-11 18:06:04 | Nakkala (Kumbukkan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-11 18:05:57 | Padiyathalawa (Maduru Oya) | 2.73 | 🟢 Normal | 1.399 | 🔺 Rising |
| 2025-12-11 18:05:50 | Katharagama (Menik Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2025-12-11 18:05:15 | Rathnapura (Kalu Ganga) | 1.51 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2025-12-11 18:05:10 | Baddegama (Gin Ganga) | 1.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-11 18:04:44 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | 0.200 | 🔺 Rising |
| 2025-12-11 18:04:39 | Peradeniya (Mahaweli Ganga) | 2.63 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2025-12-11 18:04:25 | Horowpothana (Yan Oya) | 4.30 | 🟢 Normal | -0.048 |  |
| 2025-12-11 18:04:22 | Hanwella (Kelani Ganga) | 1.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-11 18:04:18 | Nakkala (Kumbukkan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-11 18:03:51 | Thawalama (Gin Ganga) | 1.78 | 🟢 Normal | 0.240 | 🔺 Rising |
| 2025-12-11 18:03:27 | Norwood (Kelani Ganga) | 1.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-11 18:03:07 | Moraketiya (Walawe Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2025-12-11 18:03:04 | Panadugama (Nilwala Ganga) | 2.98 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2025-12-11 18:03:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.86 | 🟢 Normal | 0.000 |  |
| 2025-12-11 18:02:56 | Urawa (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.387 | 🔺 Rising |
| 2025-12-11 18:02:46 | Thanthirimale (Malwathu Oya) | 4.20 | 🟢 Normal | -0.033 |  |
| 2025-12-11 18:02:29 | Giriulla (Maha Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2025-12-11 18:02:22 | Galgamuwa (Mee Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-11 18:02:22 | Ellagawa (Kalu Ganga) | 5.01 | 🟢 Normal | 0.000 |  |
| 2025-12-11 18:02:15 | Moraketiya (Walawe Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2025-12-11 18:02:09 | Glencourse (Kelani Ganga) | 9.58 | 🟢 Normal | -0.054 |  |
| 2025-12-11 18:01:53 | Nawalapitiya (Mahaweli Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-11 18:01:43 | Badalgama (Maha Oya) | 2.55 | 🟢 Normal | 0.000 |  |
| 2025-12-11 18:01:37 | Putupaula (Kalu Ganga) | 0.91 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2025-12-11 18:01:36 | Kithulgala (Kelani Ganga) | 1.91 | 🟢 Normal | -0.040 |  |
| 2025-12-11 18:01:36 | Siyambalanduwa (Heda Oya) | 1.38 | 🟢 Normal | 0.275 | 🔺 Rising |
| 2025-12-11 18:01:21 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-11 18:01:18 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.095 |  |
| 2025-12-11 18:01:02 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-11 18:00:52 | Yaka Wewa (Ma Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2025-12-11 18:00:24 | Manampitiya (Mahaweli Ganga) | 1.98 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-11 18:05:57 | Padiyathalawa (Maduru Oya) | 2.73 | 🟢 Normal | 1.399 | 🔺 Rising |
| 2025-12-11 18:02:56 | Urawa (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.387 | 🔺 Rising |
| 2025-12-11 18:01:36 | Siyambalanduwa (Heda Oya) | 1.38 | 🟢 Normal | 0.275 | 🔺 Rising |
| 2025-12-11 18:03:51 | Thawalama (Gin Ganga) | 1.78 | 🟢 Normal | 0.240 | 🔺 Rising |
| 2025-12-11 15:01:10 | Weraganthota (Mahaweli Ganga) | -1.25 | 🟢 Normal | 0.226 | 🔺 Rising |
| 2025-12-11 18:04:44 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | 0.200 | 🔺 Rising |
| 2025-12-11 18:05:15 | Rathnapura (Kalu Ganga) | 1.51 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2025-12-11 18:04:39 | Peradeniya (Mahaweli Ganga) | 2.63 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2025-12-11 18:01:37 | Putupaula (Kalu Ganga) | 0.91 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2025-12-11 18:03:04 | Panadugama (Nilwala Ganga) | 2.98 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2025-12-11 15:04:23 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-11 18:26:44 | Thalgahagoda (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-11 18:07:03 | Pitabeddara (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-11 18:05:10 | Baddegama (Gin Ganga) | 1.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-11 18:04:22 | Hanwella (Kelani Ganga) | 1.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-11 18:03:27 | Norwood (Kelani Ganga) | 1.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-11 18:01:02 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-11 18:06:04 | Nakkala (Kumbukkan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-11 15:11:23 | Moragaswewa (Deduru Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2025-12-11 18:01:53 | Nawalapitiya (Mahaweli Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-11 18:00:52 | Yaka Wewa (Ma Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2025-12-11 18:02:29 | Giriulla (Maha Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2025-12-11 18:02:22 | Galgamuwa (Mee Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-11 18:10:07 | Magura (Kalu Ganga) | 1.67 | 🟢 Normal | 0.000 |  |
| 2025-12-11 18:02:22 | Ellagawa (Kalu Ganga) | 5.01 | 🟢 Normal | 0.000 |  |
| 2025-12-11 18:03:07 | Moraketiya (Walawe Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2025-12-11 18:08:24 | Dunamale (Aththanagalu Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2025-12-11 18:05:50 | Katharagama (Menik Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2025-12-11 18:01:43 | Badalgama (Maha Oya) | 2.55 | 🟢 Normal | 0.000 |  |
| 2025-12-11 18:07:58 | Holombuwa (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-11 18:00:24 | Manampitiya (Mahaweli Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2025-12-11 18:01:21 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-11 18:06:32 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-11 18:03:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.86 | 🟢 Normal | 0.000 |  |
| 2025-12-11 18:02:46 | Thanthirimale (Malwathu Oya) | 4.20 | 🟢 Normal | -0.033 |  |
| 2025-12-11 18:01:36 | Kithulgala (Kelani Ganga) | 1.91 | 🟢 Normal | -0.040 |  |
| 2025-12-11 18:04:25 | Horowpothana (Yan Oya) | 4.30 | 🟢 Normal | -0.048 |  |
| 2025-12-11 18:02:09 | Glencourse (Kelani Ganga) | 9.58 | 🟢 Normal | -0.054 |  |
| 2025-12-11 18:01:18 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.095 |  |

## River Water Level Charts by Station

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)