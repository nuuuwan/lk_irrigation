# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--29_09:16:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **30,921 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-29 09:16:03 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-29 09:15:09 | Panadugama (Nilwala Ganga) | 2.44 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-29 09:13:06 | Magura (Kalu Ganga) | 1.07 | 🟢 Normal | -0.009 |  |
| 2025-12-29 09:07:37 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-29 09:07:35 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-29 09:06:09 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2025-12-29 09:05:50 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.026 |  |
| 2025-12-29 09:05:15 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | -0.010 |  |
| 2025-12-29 09:04:56 | Manampitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-29 09:04:55 | Galgamuwa (Mee Oya) | 0.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-29 09:04:23 | Rathnapura (Kalu Ganga) | 0.88 | 🟢 Normal | -0.011 |  |
| 2025-12-29 09:04:21 | Hanwella (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-29 09:04:03 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-29 09:04:02 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-29 09:03:39 | Glencourse (Kelani Ganga) | 8.76 | 🟢 Normal | 0.000 |  |
| 2025-12-29 09:03:34 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-29 09:03:33 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-29 09:03:18 | Weraganthota (Mahaweli Ganga) | -1.53 | 🟢 Normal | 0.537 | 🔺 Rising |
| 2025-12-29 09:03:16 | Padiyathalawa (Maduru Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-29 09:03:12 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | 0.300 | 🔺 Rising |
| 2025-12-29 09:03:11 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-29 09:03:06 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-29 09:02:59 | Deraniyagala (Kelani Ganga) | 0.36 | 🟢 Normal | -0.050 |  |
| 2025-12-29 09:02:59 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | -0.011 |  |
| 2025-12-29 09:02:53 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-29 09:02:53 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.030 |  |
| 2025-12-29 09:02:52 | Badalgama (Maha Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2025-12-29 09:02:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.96 | 🟢 Normal | -0.010 |  |
| 2025-12-29 09:02:21 | Ellagawa (Kalu Ganga) | 4.43 | 🟢 Normal | -0.010 |  |
| 2025-12-29 09:02:16 | Moragaswewa (Deduru Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2025-12-29 09:02:14 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-29 09:02:11 | Weraganthota (Mahaweli Ganga) | -1.54 | 🟢 Normal | 0.537 | 🔺 Rising |
| 2025-12-29 09:01:38 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-29 09:01:33 | Thanamalwila (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-29 09:01:24 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-29 09:01:22 | Nakkala (Kumbukkan Oya) | 1.03 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-29 09:01:19 | Horowpothana (Yan Oya) | 1.47 | 🟢 Normal | 0.000 |  |
| 2025-12-29 09:01:06 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-29 09:01:05 | Thanthirimale (Malwathu Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2025-12-29 09:00:05 | Siyambalanduwa (Heda Oya) | 0.64 | 🟢 Normal | 0.011 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-29 09:03:18 | Weraganthota (Mahaweli Ganga) | -1.53 | 🟢 Normal | 0.537 | 🔺 Rising |
| 2025-12-29 09:03:12 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | 0.300 | 🔺 Rising |
| 2025-12-29 09:04:02 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-29 09:03:33 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-29 09:01:22 | Nakkala (Kumbukkan Oya) | 1.03 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-29 09:00:05 | Siyambalanduwa (Heda Oya) | 0.64 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-29 09:04:55 | Galgamuwa (Mee Oya) | 0.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-29 09:15:09 | Panadugama (Nilwala Ganga) | 2.44 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-29 09:01:38 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-29 09:01:24 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-29 09:03:06 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-29 09:02:53 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-29 09:16:03 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-29 09:01:19 | Horowpothana (Yan Oya) | 1.47 | 🟢 Normal | 0.000 |  |
| 2025-12-29 09:01:06 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-29 09:03:11 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-29 09:04:21 | Hanwella (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-29 09:07:37 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-29 09:03:16 | Padiyathalawa (Maduru Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-29 09:03:39 | Glencourse (Kelani Ganga) | 8.76 | 🟢 Normal | 0.000 |  |
| 2025-12-29 09:03:34 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-29 09:02:14 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-29 09:02:52 | Badalgama (Maha Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2025-12-29 09:06:09 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2025-12-29 09:04:56 | Manampitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-29 09:01:05 | Thanthirimale (Malwathu Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2025-12-29 08:07:06 | Urawa (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2025-12-29 09:04:03 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-29 09:01:33 | Thanamalwila (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-29 09:13:06 | Magura (Kalu Ganga) | 1.07 | 🟢 Normal | -0.009 |  |
| 2025-12-29 09:05:15 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | -0.010 |  |
| 2025-12-29 09:02:16 | Moragaswewa (Deduru Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2025-12-29 09:02:21 | Ellagawa (Kalu Ganga) | 4.43 | 🟢 Normal | -0.010 |  |
| 2025-12-29 09:02:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.96 | 🟢 Normal | -0.010 |  |
| 2025-12-29 09:04:23 | Rathnapura (Kalu Ganga) | 0.88 | 🟢 Normal | -0.011 |  |
| 2025-12-29 09:02:59 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | -0.011 |  |
| 2025-12-29 09:05:50 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.026 |  |
| 2025-12-29 09:02:53 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.030 |  |
| 2025-12-29 09:02:59 | Deraniyagala (Kelani Ganga) | 0.36 | 🟢 Normal | -0.050 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)