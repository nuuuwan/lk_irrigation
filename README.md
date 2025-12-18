# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--19_04:26:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **21,848 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-19 04:26:30 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | -0.071 |  |
| 2025-12-19 04:19:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.30 | 🟢 Normal | -0.031 |  |
| 2025-12-19 04:17:04 | Dunamale (Aththanagalu Oya) | 1.36 | 🟢 Normal | -0.009 |  |
| 2025-12-19 04:12:01 | Glencourse (Kelani Ganga) | 9.19 | 🟢 Normal | 0.245 | 🔺 Rising |
| 2025-12-19 04:10:15 | Katharagama (Menik Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2025-12-19 04:10:13 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2025-12-19 04:08:35 | Thalgahagoda (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-19 04:07:26 | Rathnapura (Kalu Ganga) | 1.16 | 🟢 Normal | -0.010 |  |
| 2025-12-19 04:07:15 | Nakkala (Kumbukkan Oya) | 1.76 | 🟢 Normal | -0.057 |  |
| 2025-12-19 04:06:41 | Thanamalwila (Kirindi Oya) | 1.16 | 🟢 Normal | -0.009 |  |
| 2025-12-19 04:05:02 | Manampitiya (Mahaweli Ganga) | 4.95 | 🟠 Minor Flood | -0.037 |  |
| 2025-12-19 04:04:34 | Siyambalanduwa (Heda Oya) | 1.25 | 🟢 Normal | -0.058 |  |
| 2025-12-19 04:04:29 | Badalgama (Maha Oya) | 2.70 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2025-12-19 04:03:14 | Peradeniya (Mahaweli Ganga) | 2.62 | 🟢 Normal | -0.021 |  |
| 2025-12-19 04:03:14 | Nawalapitiya (Mahaweli Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2025-12-19 04:03:11 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-19 04:03:09 | Horowpothana (Yan Oya) | 5.77 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2025-12-19 04:02:55 | Pitabeddara (Nilwala Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2025-12-19 04:02:43 | Thaldena (Mahaweli Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-19 04:02:41 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2025-12-19 04:02:40 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-19 04:02:29 | Hanwella (Kelani Ganga) | 1.04 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-19 04:02:27 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.171 | 🔺 Rising |
| 2025-12-19 04:02:22 | Magura (Kalu Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2025-12-19 04:02:13 | Giriulla (Maha Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2025-12-19 04:02:01 | Yaka Wewa (Ma Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2025-12-19 04:01:38 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-19 04:01:14 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2025-12-19 04:01:06 | Ellagawa (Kalu Ganga) | 4.93 | 🟢 Normal | -0.011 |  |
| 2025-12-19 04:00:40 | Thawalama (Gin Ganga) | 1.34 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-19 04:05:02 | Manampitiya (Mahaweli Ganga) | 4.95 | 🟠 Minor Flood | -0.037 |  |
| 2025-12-18 18:06:17 | Thanthirimale (Malwathu Oya) | 5.40 | 🟡 Alert | 0.074 | 🔺 Rising |
| 2025-12-19 04:12:01 | Glencourse (Kelani Ganga) | 9.19 | 🟢 Normal | 0.245 | 🔺 Rising |
| 2025-12-19 04:02:27 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.171 | 🔺 Rising |
| 2025-12-18 18:02:47 | Weraganthota (Mahaweli Ganga) | 1.45 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-19 04:10:13 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2025-12-19 04:04:29 | Badalgama (Maha Oya) | 2.70 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2025-12-19 04:03:09 | Horowpothana (Yan Oya) | 5.77 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2025-12-19 04:02:29 | Hanwella (Kelani Ganga) | 1.04 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-19 03:01:13 | Moragaswewa (Deduru Oya) | 1.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-18 18:06:01 | Galgamuwa (Mee Oya) | 1.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-19 04:08:35 | Thalgahagoda (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-19 04:02:40 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-19 04:02:01 | Yaka Wewa (Ma Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2025-12-19 04:02:13 | Giriulla (Maha Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2025-12-19 04:02:22 | Magura (Kalu Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2025-12-19 03:16:00 | Panadugama (Nilwala Ganga) | 2.71 | 🟢 Normal | 0.000 |  |
| 2025-12-19 04:01:14 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2025-12-19 04:01:38 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-19 04:02:43 | Thaldena (Mahaweli Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-19 04:10:15 | Katharagama (Menik Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2025-12-19 04:03:11 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-19 03:12:41 | Urawa (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-19 03:02:42 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-19 04:17:04 | Dunamale (Aththanagalu Oya) | 1.36 | 🟢 Normal | -0.009 |  |
| 2025-12-19 04:06:41 | Thanamalwila (Kirindi Oya) | 1.16 | 🟢 Normal | -0.009 |  |
| 2025-12-19 04:02:55 | Pitabeddara (Nilwala Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2025-12-19 04:03:14 | Nawalapitiya (Mahaweli Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2025-12-19 04:07:26 | Rathnapura (Kalu Ganga) | 1.16 | 🟢 Normal | -0.010 |  |
| 2025-12-19 04:02:41 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2025-12-19 04:01:06 | Ellagawa (Kalu Ganga) | 4.93 | 🟢 Normal | -0.011 |  |
| 2025-12-19 04:00:40 | Thawalama (Gin Ganga) | 1.34 | 🟢 Normal | -0.011 |  |
| 2025-12-19 04:03:14 | Peradeniya (Mahaweli Ganga) | 2.62 | 🟢 Normal | -0.021 |  |
| 2025-12-19 02:09:20 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | -0.029 |  |
| 2025-12-19 04:19:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.30 | 🟢 Normal | -0.031 |  |
| 2025-12-19 03:03:18 | Padiyathalawa (Maduru Oya) | 1.80 | 🟢 Normal | -0.051 |  |
| 2025-12-19 04:07:15 | Nakkala (Kumbukkan Oya) | 1.76 | 🟢 Normal | -0.057 |  |
| 2025-12-19 04:04:34 | Siyambalanduwa (Heda Oya) | 1.25 | 🟢 Normal | -0.058 |  |
| 2025-12-19 04:26:30 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | -0.071 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)