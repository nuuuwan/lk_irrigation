# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--18_21:25:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **21,606 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-18 21:25:03 | Dunamale (Aththanagalu Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2025-12-18 21:09:29 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2025-12-18 21:08:47 | Rathnapura (Kalu Ganga) | 1.21 | 🟢 Normal | -0.010 |  |
| 2025-12-18 21:08:40 | Glencourse (Kelani Ganga) | 9.18 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2025-12-18 21:08:18 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | -0.009 |  |
| 2025-12-18 21:08:00 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.029 |  |
| 2025-12-18 21:07:03 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | -0.009 |  |
| 2025-12-18 21:06:14 | Ellagawa (Kalu Ganga) | 4.93 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2025-12-18 21:06:10 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-18 21:06:00 | Peradeniya (Mahaweli Ganga) | 2.88 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-18 21:05:41 | Katharagama (Menik Ganga) | 0.27 | 🟢 Normal | -0.010 |  |
| 2025-12-18 21:05:41 | Giriulla (Maha Oya) | 1.39 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-18 21:05:31 | Panadugama (Nilwala Ganga) | 2.73 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2025-12-18 21:05:14 | Thawalama (Gin Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-18 21:05:03 | Badalgama (Maha Oya) | 2.47 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2025-12-18 21:04:53 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-18 21:04:48 | Deraniyagala (Kelani Ganga) | 0.52 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2025-12-18 21:04:35 | Moragaswewa (Deduru Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-18 21:04:11 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-18 21:03:53 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.012 |  |
| 2025-12-18 21:03:46 | Pitabeddara (Nilwala Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-18 21:03:10 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | -0.010 |  |
| 2025-12-18 21:03:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.12 | 🟢 Normal | -0.022 |  |
| 2025-12-18 21:02:38 | Hanwella (Kelani Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-18 21:02:10 | Thaldena (Mahaweli Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2025-12-18 21:02:06 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-18 21:02:04 | Padiyathalawa (Maduru Oya) | 1.99 | 🟢 Normal | -0.234 |  |
| 2025-12-18 21:01:55 | Yaka Wewa (Ma Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2025-12-18 21:01:35 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | -0.010 |  |
| 2025-12-18 21:01:33 | Nawalapitiya (Mahaweli Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2025-12-18 21:01:20 | Magura (Kalu Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2025-12-18 21:01:18 | Siyambalanduwa (Heda Oya) | 1.49 | 🟢 Normal | -0.031 |  |
| 2025-12-18 21:01:04 | Horowpothana (Yan Oya) | 5.39 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2025-12-18 21:00:46 | Urawa (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-18 21:00:38 | Manampitiya (Mahaweli Ganga) | 4.83 | 🟠 Minor Flood | 0.051 | 🔺 Rising |
| 2025-12-18 21:00:19 | Nakkala (Kumbukkan Oya) | 2.26 | 🟢 Normal | -0.100 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-18 21:00:38 | Manampitiya (Mahaweli Ganga) | 4.83 | 🟠 Minor Flood | 0.051 | 🔺 Rising |
| 2025-12-18 18:06:17 | Thanthirimale (Malwathu Oya) | 5.40 | 🟡 Alert | 0.074 | 🔺 Rising |
| 2025-12-18 21:04:48 | Deraniyagala (Kelani Ganga) | 0.52 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2025-12-18 21:06:14 | Ellagawa (Kalu Ganga) | 4.93 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2025-12-18 21:01:04 | Horowpothana (Yan Oya) | 5.39 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2025-12-18 18:02:47 | Weraganthota (Mahaweli Ganga) | 1.45 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-18 21:09:29 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2025-12-18 21:08:40 | Glencourse (Kelani Ganga) | 9.18 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2025-12-18 21:05:41 | Giriulla (Maha Oya) | 1.39 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-18 21:06:00 | Peradeniya (Mahaweli Ganga) | 2.88 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-18 21:05:31 | Panadugama (Nilwala Ganga) | 2.73 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2025-12-18 21:05:03 | Badalgama (Maha Oya) | 2.47 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2025-12-18 21:00:46 | Urawa (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-18 18:06:01 | Galgamuwa (Mee Oya) | 1.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-18 21:04:11 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-18 21:06:10 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-18 21:04:35 | Moragaswewa (Deduru Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-18 21:01:20 | Magura (Kalu Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2025-12-18 21:03:46 | Pitabeddara (Nilwala Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-18 21:02:06 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-18 21:02:38 | Hanwella (Kelani Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-18 21:04:53 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-18 21:25:03 | Dunamale (Aththanagalu Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2025-12-18 21:05:14 | Thawalama (Gin Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-18 21:08:18 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | -0.009 |  |
| 2025-12-18 21:07:03 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | -0.009 |  |
| 2025-12-18 21:01:33 | Nawalapitiya (Mahaweli Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2025-12-18 21:05:41 | Katharagama (Menik Ganga) | 0.27 | 🟢 Normal | -0.010 |  |
| 2025-12-18 21:03:10 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | -0.010 |  |
| 2025-12-18 21:08:47 | Rathnapura (Kalu Ganga) | 1.21 | 🟢 Normal | -0.010 |  |
| 2025-12-18 21:02:10 | Thaldena (Mahaweli Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2025-12-18 21:01:55 | Yaka Wewa (Ma Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2025-12-18 21:01:35 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | -0.010 |  |
| 2025-12-18 21:03:53 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.012 |  |
| 2025-12-18 21:03:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.12 | 🟢 Normal | -0.022 |  |
| 2025-12-18 21:08:00 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.029 |  |
| 2025-12-18 21:01:18 | Siyambalanduwa (Heda Oya) | 1.49 | 🟢 Normal | -0.031 |  |
| 2025-12-18 21:00:19 | Nakkala (Kumbukkan Oya) | 2.26 | 🟢 Normal | -0.100 |  |
| 2025-12-18 21:02:04 | Padiyathalawa (Maduru Oya) | 1.99 | 🟢 Normal | -0.234 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)