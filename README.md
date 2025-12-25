# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--25_08:04:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **27,308 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-25 08:04:42 | Glencourse (Kelani Ganga) | 9.04 | 🟢 Normal | 0.000 |  |
| 2025-12-25 08:04:39 | Rathnapura (Kalu Ganga) | 1.88 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-25 08:03:49 | Thawalama (Gin Ganga) | 2.64 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2025-12-25 08:03:39 | Hanwella (Kelani Ganga) | 0.74 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-25 08:03:35 | Deraniyagala (Kelani Ganga) | 0.53 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2025-12-25 08:02:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.66 | 🟢 Normal | 0.000 |  |
| 2025-12-25 08:02:55 | Nawalapitiya (Mahaweli Ganga) | 0.89 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-25 08:02:51 | Weraganthota (Mahaweli Ganga) | -1.02 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-25 08:02:49 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2025-12-25 08:02:41 | Badalgama (Maha Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2025-12-25 08:02:34 | Thanthirimale (Malwathu Oya) | 1.95 | 🟢 Normal | -0.010 |  |
| 2025-12-25 08:02:16 | Ellagawa (Kalu Ganga) | 4.95 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2025-12-25 08:02:02 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2025-12-25 08:01:57 | Horowpothana (Yan Oya) | 2.23 | 🟢 Normal | 0.000 |  |
| 2025-12-25 08:01:55 | Dunamale (Aththanagalu Oya) | 0.79 | 🟢 Normal | -0.010 |  |
| 2025-12-25 08:01:53 | Nakkala (Kumbukkan Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-25 08:01:39 | Horowpothana (Yan Oya) | 2.23 | 🟢 Normal | 0.000 |  |
| 2025-12-25 08:01:07 | Giriulla (Maha Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-25 08:01:07 | Moragaswewa (Deduru Oya) | 0.64 | 🟢 Normal | -0.015 |  |
| 2025-12-25 08:00:43 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2025-12-25 07:59:45 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2025-12-25 07:59:41 | Manampitiya (Mahaweli Ganga) | 1.73 | 🟢 Normal | -0.032 |  |
| 2025-12-25 07:44:15 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2025-12-25 07:36:27 | Panadugama (Nilwala Ganga) | 3.00 | 🟢 Normal | -0.013 |  |
| 2025-12-25 07:26:05 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2025-12-25 07:26:05 | Pitabeddara (Nilwala Ganga) | 0.92 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2025-12-25 07:20:03 | Moragaswewa (Deduru Oya) | 0.65 | 🟢 Normal | -0.015 |  |
| 2025-12-25 07:17:58 | Giriulla (Maha Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-25 07:16:33 | Urawa (Nilwala Ganga) | 1.06 | 🟢 Normal | -0.051 |  |
| 2025-12-25 07:15:06 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2025-12-25 07:13:30 | Galgamuwa (Mee Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2025-12-25 07:12:56 | Magura (Kalu Ganga) | 2.03 | 🟢 Normal | -0.034 |  |
| 2025-12-25 07:12:38 | Weraganthota (Mahaweli Ganga) | -1.07 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-25 07:12:29 | Holombuwa (Kelani Ganga) | 0.57 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2025-12-25 07:11:47 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2025-12-25 07:08:37 | Nawalapitiya (Mahaweli Ganga) | 0.88 | 🟢 Normal | 0.011 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-25 08:00:43 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2025-12-25 08:03:49 | Thawalama (Gin Ganga) | 2.64 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2025-12-25 08:03:35 | Deraniyagala (Kelani Ganga) | 0.53 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2025-12-25 08:02:51 | Weraganthota (Mahaweli Ganga) | -1.02 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-25 08:02:16 | Ellagawa (Kalu Ganga) | 4.95 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2025-12-25 07:04:35 | Baddegama (Gin Ganga) | 1.67 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-25 08:03:39 | Hanwella (Kelani Ganga) | 0.74 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-25 07:12:29 | Holombuwa (Kelani Ganga) | 0.57 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2025-12-25 07:02:48 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-25 08:04:39 | Rathnapura (Kalu Ganga) | 1.88 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-25 07:26:05 | Pitabeddara (Nilwala Ganga) | 0.92 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2025-12-25 07:59:45 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2025-12-25 08:02:02 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2025-12-25 08:02:55 | Nawalapitiya (Mahaweli Ganga) | 0.89 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-25 07:01:46 | Thanamalwila (Kirindi Oya) | 1.00 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-25 08:02:49 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2025-12-25 08:01:53 | Nakkala (Kumbukkan Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-25 08:01:07 | Giriulla (Maha Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-25 08:01:57 | Horowpothana (Yan Oya) | 2.23 | 🟢 Normal | 0.000 |  |
| 2025-12-25 07:13:30 | Galgamuwa (Mee Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2025-12-25 07:05:40 | Padiyathalawa (Maduru Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-25 08:04:42 | Glencourse (Kelani Ganga) | 9.04 | 🟢 Normal | 0.000 |  |
| 2025-12-25 07:44:15 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2025-12-25 08:02:41 | Badalgama (Maha Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2025-12-25 08:02:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.66 | 🟢 Normal | 0.000 |  |
| 2025-12-25 07:02:21 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | -0.010 |  |
| 2025-12-25 08:02:34 | Thanthirimale (Malwathu Oya) | 1.95 | 🟢 Normal | -0.010 |  |
| 2025-12-25 07:00:57 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | -0.010 |  |
| 2025-12-25 08:01:55 | Dunamale (Aththanagalu Oya) | 0.79 | 🟢 Normal | -0.010 |  |
| 2025-12-25 07:36:27 | Panadugama (Nilwala Ganga) | 3.00 | 🟢 Normal | -0.013 |  |
| 2025-12-25 08:01:07 | Moragaswewa (Deduru Oya) | 0.64 | 🟢 Normal | -0.015 |  |
| 2025-12-25 07:04:33 | Putupaula (Kalu Ganga) | 0.79 | 🟢 Normal | -0.029 |  |
| 2025-12-25 07:59:41 | Manampitiya (Mahaweli Ganga) | 1.73 | 🟢 Normal | -0.032 |  |
| 2025-12-25 07:12:56 | Magura (Kalu Ganga) | 2.03 | 🟢 Normal | -0.034 |  |
| 2025-12-25 07:00:23 | Thalgahagoda (Nilwala Ganga) | 0.68 | 🟢 Normal | -0.050 |  |
| 2025-12-25 07:16:33 | Urawa (Nilwala Ganga) | 1.06 | 🟢 Normal | -0.051 |  |
| 2025-12-25 07:01:14 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.061 |  |
| 2025-12-25 07:05:18 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | -0.082 |  |
| 2025-12-25 07:05:08 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | -0.236 |  |

## River Water Level Charts by Station

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)