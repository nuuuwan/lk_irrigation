# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--06_09:02:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **10,613 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-06 09:02:49 | Kuda Oya (Kirindi Oya) | 1.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-06 09:02:45 | Horowpothana (Yan Oya) | 2.00 | 🟢 Normal | -0.010 |  |
| 2025-12-06 09:02:45 | Urawa (Nilwala Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-06 09:02:45 | Nakkala (Kumbukkan Oya) | 1.42 | 🟢 Normal | -0.010 |  |
| 2025-12-06 09:02:31 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-06 09:02:23 | Putupaula (Kalu Ganga) | 1.15 | 🟢 Normal | -0.081 |  |
| 2025-12-06 09:02:21 | Moraketiya (Walawe Ganga) | 1.73 | 🟢 Normal | 0.000 |  |
| 2025-12-06 09:02:21 | Manampitiya (Mahaweli Ganga) | 2.05 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2025-12-06 09:02:15 | Siyambalanduwa (Heda Oya) | 1.01 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2025-12-06 09:02:14 | Katharagama (Menik Ganga) | 0.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-06 09:02:14 | Baddegama (Gin Ganga) | 2.66 | 🟢 Normal | -0.010 |  |
| 2025-12-06 09:01:52 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.096 |  |
| 2025-12-06 09:01:23 | Yaka Wewa (Ma Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-06 09:00:55 | Giriulla (Maha Oya) | 1.95 | 🟢 Normal | -0.010 |  |
| 2025-12-06 09:00:41 | Nawalapitiya (Mahaweli Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2025-12-06 09:00:17 | Thalgahagoda (Nilwala Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-06 08:28:49 | Manampitiya (Mahaweli Ganga) | 2.02 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2025-12-06 08:20:50 | Padiyathalawa (Maduru Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-06 08:20:45 | Thanthirimale (Malwathu Oya) | 6.91 | 🟠 Minor Flood | 0.032 | 🔺 Rising |
| 2025-12-06 08:20:15 | Yaka Wewa (Ma Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-06 08:14:20 | Thalgahagoda (Nilwala Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-06 08:12:38 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | -0.004 |  |
| 2025-12-06 08:12:20 | Urawa (Nilwala Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-06 08:11:44 | Glencourse (Kelani Ganga) | 10.44 | 🟢 Normal | 0.000 |  |
| 2025-12-06 08:09:43 | Weraganthota (Mahaweli Ganga) | -0.12 | 🟢 Normal | -0.055 |  |
| 2025-12-06 08:08:38 | Pitabeddara (Nilwala Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-06 08:07:43 | Galgamuwa (Mee Oya) | 1.55 | 🟢 Normal | -36.000 |  |
| 2025-12-06 08:07:42 | Galgamuwa (Mee Oya) | 1.56 | 🟢 Normal | -36.000 |  |
| 2025-12-06 08:07:41 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | -0.029 |  |
| 2025-12-06 08:07:09 | Siyambalanduwa (Heda Oya) | 0.98 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2025-12-06 08:05:55 | Magura (Kalu Ganga) | 3.97 | 🟢 Normal | -0.119 |  |
| 2025-12-06 08:05:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-06 08:05:02 | Panadugama (Nilwala Ganga) | 4.12 | 🟢 Normal | -0.072 |  |
| 2025-12-06 08:04:52 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.096 |  |
| 2025-12-06 08:04:50 | Badalgama (Maha Oya) | 3.00 | 🟢 Normal | -0.040 |  |
| 2025-12-06 08:04:50 | Dunamale (Aththanagalu Oya) | 2.10 | 🟢 Normal | -0.020 |  |
| 2025-12-06 08:04:38 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2025-12-06 08:04:38 | Ellagawa (Kalu Ganga) | 6.38 | 🟢 Normal | -0.019 |  |
| 2025-12-06 08:04:00 | Thawalama (Gin Ganga) | 1.95 | 🟢 Normal | -0.239 |  |
| 2025-12-06 08:03:54 | Moraketiya (Walawe Ganga) | 1.73 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-06 08:20:45 | Thanthirimale (Malwathu Oya) | 6.91 | 🟠 Minor Flood | 0.032 | 🔺 Rising |
| 2025-12-06 09:02:21 | Manampitiya (Mahaweli Ganga) | 2.05 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2025-12-06 09:02:15 | Siyambalanduwa (Heda Oya) | 1.01 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2025-12-06 08:05:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-06 09:02:49 | Kuda Oya (Kirindi Oya) | 1.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-06 09:02:14 | Katharagama (Menik Ganga) | 0.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-06 09:02:31 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-06 09:00:41 | Nawalapitiya (Mahaweli Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2025-12-06 09:01:23 | Yaka Wewa (Ma Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-06 08:08:38 | Pitabeddara (Nilwala Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-06 08:03:21 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-06 08:04:38 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2025-12-06 08:20:50 | Padiyathalawa (Maduru Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-06 08:11:44 | Glencourse (Kelani Ganga) | 10.44 | 🟢 Normal | 0.000 |  |
| 2025-12-06 09:02:21 | Moraketiya (Walawe Ganga) | 1.73 | 🟢 Normal | 0.000 |  |
| 2025-12-06 09:02:45 | Urawa (Nilwala Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-06 09:00:17 | Thalgahagoda (Nilwala Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-06 07:05:12 | Thanamalwila (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2025-12-06 08:12:38 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | -0.004 |  |
| 2025-12-06 09:02:45 | Horowpothana (Yan Oya) | 2.00 | 🟢 Normal | -0.010 |  |
| 2025-12-06 09:02:14 | Baddegama (Gin Ganga) | 2.66 | 🟢 Normal | -0.010 |  |
| 2025-12-06 09:02:45 | Nakkala (Kumbukkan Oya) | 1.42 | 🟢 Normal | -0.010 |  |
| 2025-12-06 09:00:55 | Giriulla (Maha Oya) | 1.95 | 🟢 Normal | -0.010 |  |
| 2025-12-06 08:04:38 | Ellagawa (Kalu Ganga) | 6.38 | 🟢 Normal | -0.019 |  |
| 2025-12-06 08:04:50 | Dunamale (Aththanagalu Oya) | 2.10 | 🟢 Normal | -0.020 |  |
| 2025-12-06 08:07:41 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | -0.029 |  |
| 2025-12-06 08:04:50 | Badalgama (Maha Oya) | 3.00 | 🟢 Normal | -0.040 |  |
| 2025-12-06 08:03:43 | Holombuwa (Kelani Ganga) | 0.91 | 🟢 Normal | -0.041 |  |
| 2025-12-06 08:03:22 | Hanwella (Kelani Ganga) | 3.12 | 🟢 Normal | -0.052 |  |
| 2025-12-06 08:09:43 | Weraganthota (Mahaweli Ganga) | -0.12 | 🟢 Normal | -0.055 |  |
| 2025-12-06 08:05:02 | Panadugama (Nilwala Ganga) | 4.12 | 🟢 Normal | -0.072 |  |
| 2025-12-06 08:03:53 | Rathnapura (Kalu Ganga) | 2.28 | 🟢 Normal | -0.073 |  |
| 2025-12-06 09:02:23 | Putupaula (Kalu Ganga) | 1.15 | 🟢 Normal | -0.081 |  |
| 2025-12-06 09:01:52 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.096 |  |
| 2025-12-06 08:05:55 | Magura (Kalu Ganga) | 3.97 | 🟢 Normal | -0.119 |  |
| 2025-12-06 08:04:00 | Thawalama (Gin Ganga) | 1.95 | 🟢 Normal | -0.239 |  |
| 2025-12-06 08:07:43 | Galgamuwa (Mee Oya) | 1.55 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)