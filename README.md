# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--20_21:04:07-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **23,382 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **28** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-20 21:04:07 | Thanamalwila (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-20 21:03:53 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2025-12-20 21:03:39 | Giriulla (Maha Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-20 21:03:38 | Urawa (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2025-12-20 21:03:19 | Padiyathalawa (Maduru Oya) | 1.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-20 21:02:39 | Hanwella (Kelani Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2025-12-20 21:02:36 | Siyambalanduwa (Heda Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2025-12-20 21:02:31 | Thawalama (Gin Ganga) | 1.44 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2025-12-20 21:02:18 | Moragaswewa (Deduru Oya) | 1.77 | 🟢 Normal | -0.010 |  |
| 2025-12-20 21:02:09 | Badalgama (Maha Oya) | 2.42 | 🟢 Normal | -0.010 |  |
| 2025-12-20 21:01:46 | Nakkala (Kumbukkan Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-20 21:01:37 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-20 21:01:25 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2025-12-20 21:01:24 | Glencourse (Kelani Ganga) | 8.91 | 🟢 Normal | -0.021 |  |
| 2025-12-20 21:01:15 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-20 21:01:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.87 | 🟢 Normal | -0.020 |  |
| 2025-12-20 21:00:45 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-20 21:00:37 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-20 21:00:17 | Nawalapitiya (Mahaweli Ganga) | 0.92 | 🟢 Normal | -0.010 |  |
| 2025-12-20 20:12:01 | Urawa (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2025-12-20 20:10:05 | Magura (Kalu Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2025-12-20 20:08:05 | Thaldena (Mahaweli Ganga) | 0.99 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-20 20:07:37 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2025-12-20 20:07:30 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2025-12-20 20:06:37 | Giriulla (Maha Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-20 20:06:05 | Panadugama (Nilwala Ganga) | 2.88 | 🟢 Normal | 0.136 | 🔺 Rising |
| 2025-12-20 20:06:00 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | -0.024 |  |
| 2025-12-20 20:05:55 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-20 20:03:32 | Manampitiya (Mahaweli Ganga) | 3.13 | 🟡 Alert | 0.000 |  |
| 2025-12-20 20:01:43 | Horowpothana (Yan Oya) | 6.23 | 🟡 Alert | -0.010 |  |
| 2025-12-20 18:01:20 | Thanthirimale (Malwathu Oya) | 5.30 | 🟡 Alert | -0.050 |  |
| 2025-12-20 19:05:26 | Weraganthota (Mahaweli Ganga) | 0.00 | 🟢 Normal | 0.545 | 🔺 Rising |
| 2025-12-20 20:06:05 | Panadugama (Nilwala Ganga) | 2.88 | 🟢 Normal | 0.136 | 🔺 Rising |
| 2025-12-20 21:03:38 | Urawa (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2025-12-20 20:01:33 | Peradeniya (Mahaweli Ganga) | 2.50 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2025-12-20 21:02:31 | Thawalama (Gin Ganga) | 1.44 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2025-12-20 20:02:58 | Rathnapura (Kalu Ganga) | 1.54 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2025-12-20 21:01:25 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2025-12-20 20:08:05 | Thaldena (Mahaweli Ganga) | 0.99 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-20 21:03:19 | Padiyathalawa (Maduru Oya) | 1.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-20 20:03:51 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-20 21:00:37 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-20 21:01:46 | Nakkala (Kumbukkan Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-20 21:01:37 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-20 21:03:39 | Giriulla (Maha Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-20 18:04:10 | Galgamuwa (Mee Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2025-12-20 20:10:05 | Magura (Kalu Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2025-12-20 20:02:24 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-20 20:01:26 | Ellagawa (Kalu Ganga) | 4.62 | 🟢 Normal | 0.000 |  |
| 2025-12-20 21:00:45 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-20 21:03:53 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2025-12-20 20:07:37 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2025-12-20 21:01:15 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-20 21:04:07 | Thanamalwila (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-20 20:05:02 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | -0.005 |  |
| 2025-12-20 21:02:36 | Siyambalanduwa (Heda Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2025-12-20 21:02:18 | Moragaswewa (Deduru Oya) | 1.77 | 🟢 Normal | -0.010 |  |
| 2025-12-20 21:02:09 | Badalgama (Maha Oya) | 2.42 | 🟢 Normal | -0.010 |  |
| 2025-12-20 21:02:39 | Hanwella (Kelani Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2025-12-20 20:01:54 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | -0.010 |  |
| 2025-12-20 21:00:17 | Nawalapitiya (Mahaweli Ganga) | 0.92 | 🟢 Normal | -0.010 |  |
| 2025-12-20 21:01:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.87 | 🟢 Normal | -0.020 |  |
| 2025-12-20 21:01:24 | Glencourse (Kelani Ganga) | 8.91 | 🟢 Normal | -0.021 |  |
| 2025-12-20 20:06:00 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | -0.024 |  |
| 2025-12-20 20:02:10 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | -0.040 |  |
| 2025-12-20 20:02:06 | Dunamale (Aththanagalu Oya) | 1.00 | 🟢 Normal | -0.041 |  |
| 2025-12-20 20:01:19 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.067 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)