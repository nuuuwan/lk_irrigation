# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--12_20:14:47-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **16,146 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-12 20:14:47 | Magura (Kalu Ganga) | 2.42 | 🟢 Normal | -0.022 |  |
| 2025-12-12 20:14:07 | Baddegama (Gin Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2025-12-12 20:08:35 | Giriulla (Maha Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2025-12-12 20:08:24 | Kithulgala (Kelani Ganga) | 1.95 | 🟢 Normal | 0.139 | 🔺 Rising |
| 2025-12-12 20:08:00 | Putupaula (Kalu Ganga) | 1.13 | 🟢 Normal | -0.019 |  |
| 2025-12-12 20:07:20 | Holombuwa (Kelani Ganga) | 0.70 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-12 20:07:03 | Thalgahagoda (Nilwala Ganga) | 0.92 | 🟢 Normal | -0.010 |  |
| 2025-12-12 20:06:26 | Peradeniya (Mahaweli Ganga) | 2.55 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2025-12-12 20:06:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.11 | 🟢 Normal | -0.029 |  |
| 2025-12-12 20:06:04 | Hanwella (Kelani Ganga) | 1.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-12 20:05:59 | Urawa (Nilwala Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2025-12-12 20:05:57 | Norwood (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2025-12-12 20:05:31 | Siyambalanduwa (Heda Oya) | 0.98 | 🟢 Normal | -0.009 |  |
| 2025-12-12 20:05:13 | Manampitiya (Mahaweli Ganga) | 2.88 | 🟢 Normal | -0.113 |  |
| 2025-12-12 20:04:44 | Rathnapura (Kalu Ganga) | 2.50 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2025-12-12 20:04:17 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-12 20:03:18 | Padiyathalawa (Maduru Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2025-12-12 20:03:07 | Badalgama (Maha Oya) | 2.53 | 🟢 Normal | -0.010 |  |
| 2025-12-12 20:02:56 | Thanamalwila (Kirindi Oya) | 1.21 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-12 20:02:44 | Padiyathalawa (Maduru Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2025-12-12 20:02:31 | Nakkala (Kumbukkan Oya) | 1.27 | 🟢 Normal | -0.010 |  |
| 2025-12-12 20:02:20 | Kuda Oya (Kirindi Oya) | 1.72 | 🟢 Normal | -0.010 |  |
| 2025-12-12 20:02:09 | Katharagama (Menik Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2025-12-12 20:01:55 | Moragaswewa (Deduru Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2025-12-12 20:01:51 | Dunamale (Aththanagalu Oya) | 1.19 | 🟢 Normal | -0.011 |  |
| 2025-12-12 20:01:43 | Yaka Wewa (Ma Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-12 20:01:34 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-12 20:01:22 | Ellagawa (Kalu Ganga) | 6.07 | 🟢 Normal | -0.061 |  |
| 2025-12-12 20:01:19 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.062 |  |
| 2025-12-12 20:01:01 | Nawalapitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-12 20:00:46 | Thawalama (Gin Ganga) | 2.18 | 🟢 Normal | 0.000 |  |
| 2025-12-12 20:00:21 | Glencourse (Kelani Ganga) | 9.85 | 🟢 Normal | -0.088 |  |
| 2025-12-12 20:00:11 | Moraketiya (Walawe Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-12 19:46:41 | Glencourse (Kelani Ganga) | 9.87 | 🟢 Normal | -0.088 |  |
| 2025-12-12 19:41:42 | Thaldena (Mahaweli Ganga) | 0.81 | 🟢 Normal | -0.006 |  |
| 2025-12-12 19:20:57 | Magura (Kalu Ganga) | 2.44 | 🟢 Normal | -0.022 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-12 19:10:21 | Horowpothana (Yan Oya) | 6.38 | 🟡 Alert | 0.000 |  |
| 2025-12-12 20:08:24 | Kithulgala (Kelani Ganga) | 1.95 | 🟢 Normal | 0.139 | 🔺 Rising |
| 2025-12-12 20:06:26 | Peradeniya (Mahaweli Ganga) | 2.55 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2025-12-12 20:04:44 | Rathnapura (Kalu Ganga) | 2.50 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2025-12-12 20:07:20 | Holombuwa (Kelani Ganga) | 0.70 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-12 20:02:56 | Thanamalwila (Kirindi Oya) | 1.21 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-12 20:06:04 | Hanwella (Kelani Ganga) | 1.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-12 20:01:34 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-12 20:01:55 | Moragaswewa (Deduru Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2025-12-12 20:01:01 | Nawalapitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-12 20:01:43 | Yaka Wewa (Ma Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-12 20:08:35 | Giriulla (Maha Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2025-12-12 18:09:46 | Galgamuwa (Mee Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-12 19:00:14 | Pitabeddara (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-12 20:05:57 | Norwood (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2025-12-12 20:04:17 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-12 20:14:07 | Baddegama (Gin Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2025-12-12 20:03:18 | Padiyathalawa (Maduru Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2025-12-12 20:00:11 | Moraketiya (Walawe Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-12 20:02:09 | Katharagama (Menik Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2025-12-12 18:03:10 | Thanthirimale (Malwathu Oya) | 4.35 | 🟢 Normal | 0.000 |  |
| 2025-12-12 20:00:46 | Thawalama (Gin Ganga) | 2.18 | 🟢 Normal | 0.000 |  |
| 2025-12-12 19:41:42 | Thaldena (Mahaweli Ganga) | 0.81 | 🟢 Normal | -0.006 |  |
| 2025-12-12 20:05:31 | Siyambalanduwa (Heda Oya) | 0.98 | 🟢 Normal | -0.009 |  |
| 2025-12-12 20:07:03 | Thalgahagoda (Nilwala Ganga) | 0.92 | 🟢 Normal | -0.010 |  |
| 2025-12-12 20:05:59 | Urawa (Nilwala Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2025-12-12 20:02:20 | Kuda Oya (Kirindi Oya) | 1.72 | 🟢 Normal | -0.010 |  |
| 2025-12-12 20:02:31 | Nakkala (Kumbukkan Oya) | 1.27 | 🟢 Normal | -0.010 |  |
| 2025-12-12 20:03:07 | Badalgama (Maha Oya) | 2.53 | 🟢 Normal | -0.010 |  |
| 2025-12-12 20:01:51 | Dunamale (Aththanagalu Oya) | 1.19 | 🟢 Normal | -0.011 |  |
| 2025-12-12 20:08:00 | Putupaula (Kalu Ganga) | 1.13 | 🟢 Normal | -0.019 |  |
| 2025-12-12 20:14:47 | Magura (Kalu Ganga) | 2.42 | 🟢 Normal | -0.022 |  |
| 2025-12-12 20:06:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.11 | 🟢 Normal | -0.029 |  |
| 2025-12-12 20:01:22 | Ellagawa (Kalu Ganga) | 6.07 | 🟢 Normal | -0.061 |  |
| 2025-12-12 20:01:19 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.062 |  |
| 2025-12-12 20:00:21 | Glencourse (Kelani Ganga) | 9.85 | 🟢 Normal | -0.088 |  |
| 2025-12-12 19:05:48 | Panadugama (Nilwala Ganga) | 3.79 | 🟢 Normal | -0.091 |  |
| 2025-12-12 18:01:38 | Weraganthota (Mahaweli Ganga) | -1.25 | 🟢 Normal | -0.106 |  |
| 2025-12-12 20:05:13 | Manampitiya (Mahaweli Ganga) | 2.88 | 🟢 Normal | -0.113 |  |

## River Water Level Charts by Station

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)