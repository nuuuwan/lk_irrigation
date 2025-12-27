# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--27_13:16:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **29,299 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-27 13:16:02 | Panadugama (Nilwala Ganga) | 2.75 | 🟢 Normal | -0.020 |  |
| 2025-12-27 13:10:06 | Magura (Kalu Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2025-12-27 13:09:39 | Thawalama (Gin Ganga) | 1.50 | 🟢 Normal | -0.009 |  |
| 2025-12-27 13:07:29 | Thalgahagoda (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.036 |  |
| 2025-12-27 13:07:08 | Manampitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | -0.020 |  |
| 2025-12-27 13:06:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.93 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2025-12-27 13:06:06 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2025-12-27 13:05:37 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | -0.020 |  |
| 2025-12-27 13:05:35 | Dunamale (Aththanagalu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-27 13:05:22 | Siyambalanduwa (Heda Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-27 13:04:42 | Thanamalwila (Kirindi Oya) | 0.81 | 🟢 Normal | -0.019 |  |
| 2025-12-27 13:04:33 | Urawa (Nilwala Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2025-12-27 13:04:30 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-27 13:04:23 | Galgamuwa (Mee Oya) | 0.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-27 13:04:01 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-27 13:03:59 | Weraganthota (Mahaweli Ganga) | 1.58 | 🟢 Normal | 1.616 | 🔺 Rising |
| 2025-12-27 13:03:57 | Rathnapura (Kalu Ganga) | 1.00 | 🟢 Normal | -0.014 |  |
| 2025-12-27 13:03:39 | Nawalapitiya (Mahaweli Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2025-12-27 13:03:27 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2025-12-27 13:03:16 | Yaka Wewa (Ma Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-27 13:03:00 | Hanwella (Kelani Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2025-12-27 13:03:00 | Glencourse (Kelani Ganga) | 8.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-27 13:02:55 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-27 13:02:54 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2025-12-27 13:02:54 | Nakkala (Kumbukkan Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-27 13:02:54 | Kithulgala (Kelani Ganga) | 1.49 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-27 13:02:49 | Pitabeddara (Nilwala Ganga) | 0.77 | 🟢 Normal | -0.020 |  |
| 2025-12-27 13:02:42 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | -0.041 |  |
| 2025-12-27 13:02:35 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | -0.020 |  |
| 2025-12-27 13:02:27 | Deraniyagala (Kelani Ganga) | 0.38 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2025-12-27 13:02:27 | Ellagawa (Kalu Ganga) | 4.52 | 🟢 Normal | -0.011 |  |
| 2025-12-27 13:02:24 | Padiyathalawa (Maduru Oya) | 0.95 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2025-12-27 13:02:23 | Nakkala (Kumbukkan Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-27 13:02:10 | Giriulla (Maha Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-27 13:01:24 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | -0.010 |  |
| 2025-12-27 13:00:56 | Thanthirimale (Malwathu Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2025-12-27 13:00:43 | Horowpothana (Yan Oya) | 1.72 | 🟢 Normal | -0.010 |  |
| 2025-12-27 13:00:24 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2025-12-27 12:21:53 | Rathnapura (Kalu Ganga) | 1.01 | 🟢 Normal | -0.014 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-27 13:03:59 | Weraganthota (Mahaweli Ganga) | 1.58 | 🟢 Normal | 1.616 | 🔺 Rising |
| 2025-12-27 13:06:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.93 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2025-12-27 13:02:27 | Deraniyagala (Kelani Ganga) | 0.38 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2025-12-27 13:06:06 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2025-12-27 13:02:24 | Padiyathalawa (Maduru Oya) | 0.95 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2025-12-27 13:02:54 | Kithulgala (Kelani Ganga) | 1.49 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-27 13:03:00 | Glencourse (Kelani Ganga) | 8.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-27 13:04:23 | Galgamuwa (Mee Oya) | 0.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-27 13:02:54 | Nakkala (Kumbukkan Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-27 13:03:16 | Yaka Wewa (Ma Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-27 13:02:10 | Giriulla (Maha Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-27 13:10:06 | Magura (Kalu Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2025-12-27 13:02:55 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-27 13:04:30 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-27 13:05:22 | Siyambalanduwa (Heda Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-27 13:05:35 | Dunamale (Aththanagalu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-27 13:03:27 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2025-12-27 12:06:13 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | 0.000 |  |
| 2025-12-27 13:00:56 | Thanthirimale (Malwathu Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2025-12-27 13:04:01 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-27 13:09:39 | Thawalama (Gin Ganga) | 1.50 | 🟢 Normal | -0.009 |  |
| 2025-12-27 13:02:54 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2025-12-27 13:03:39 | Nawalapitiya (Mahaweli Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2025-12-27 13:04:33 | Urawa (Nilwala Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2025-12-27 13:01:24 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | -0.010 |  |
| 2025-12-27 13:03:00 | Hanwella (Kelani Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2025-12-27 13:00:24 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2025-12-27 13:00:43 | Horowpothana (Yan Oya) | 1.72 | 🟢 Normal | -0.010 |  |
| 2025-12-27 13:02:27 | Ellagawa (Kalu Ganga) | 4.52 | 🟢 Normal | -0.011 |  |
| 2025-12-27 13:03:57 | Rathnapura (Kalu Ganga) | 1.00 | 🟢 Normal | -0.014 |  |
| 2025-12-27 13:04:42 | Thanamalwila (Kirindi Oya) | 0.81 | 🟢 Normal | -0.019 |  |
| 2025-12-27 13:05:37 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | -0.020 |  |
| 2025-12-27 13:02:49 | Pitabeddara (Nilwala Ganga) | 0.77 | 🟢 Normal | -0.020 |  |
| 2025-12-27 13:02:35 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | -0.020 |  |
| 2025-12-27 13:16:02 | Panadugama (Nilwala Ganga) | 2.75 | 🟢 Normal | -0.020 |  |
| 2025-12-27 13:07:08 | Manampitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | -0.020 |  |
| 2025-12-27 13:07:29 | Thalgahagoda (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.036 |  |
| 2025-12-27 13:02:42 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | -0.041 |  |
| 2025-12-27 12:02:22 | Putupaula (Kalu Ganga) | 0.44 | 🟢 Normal | -0.132 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)