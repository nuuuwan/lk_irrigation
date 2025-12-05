# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--06_05:03:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **10,469 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-06 05:03:18 | Hanwella (Kelani Ganga) | 3.22 | 🟢 Normal | -0.041 |  |
| 2025-12-06 05:03:16 | Thawalama (Gin Ganga) | 2.92 | 🟢 Normal | -324.000 |  |
| 2025-12-06 05:03:14 | Thawalama (Gin Ganga) | 3.10 | 🟢 Normal | -324.000 |  |
| 2025-12-06 05:02:41 | Horowpothana (Yan Oya) | 2.05 | 🟢 Normal | -0.022 |  |
| 2025-12-06 05:02:36 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | -0.005 |  |
| 2025-12-06 05:02:35 | Thanamalwila (Kirindi Oya) | 1.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-06 05:02:31 | Yaka Wewa (Ma Oya) | 0.86 | 🟢 Normal | -6.091 |  |
| 2025-12-06 05:02:26 | Giriulla (Maha Oya) | 1.98 | 🟢 Normal | -0.010 |  |
| 2025-12-06 05:02:00 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | -0.011 |  |
| 2025-12-06 05:01:19 | Kithulgala (Kelani Ganga) | 1.91 | 🟢 Normal | 0.000 |  |
| 2025-12-06 05:01:10 | Nakkala (Kumbukkan Oya) | 1.42 | 🟢 Normal | -0.180 |  |
| 2025-12-06 05:01:06 | Siyambalanduwa (Heda Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-06 05:01:03 | Badalgama (Maha Oya) | 3.02 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2025-12-06 04:28:10 | Thalgahagoda (Nilwala Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-06 04:18:23 | Moraketiya (Walawe Ganga) | 1.18 | 🟢 Normal | -0.005 |  |
| 2025-12-06 04:16:04 | Kuda Oya (Kirindi Oya) | 1.63 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-06 04:15:12 | Rathnapura (Kalu Ganga) | 2.57 | 🟢 Normal | -0.062 |  |
| 2025-12-06 04:10:23 | Baddegama (Gin Ganga) | 2.62 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2025-12-06 04:07:54 | Putupaula (Kalu Ganga) | 1.22 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2025-12-06 04:07:18 | Horowpothana (Yan Oya) | 2.07 | 🟢 Normal | -0.022 |  |
| 2025-12-06 04:07:01 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | -0.011 |  |
| 2025-12-06 04:06:55 | Thanthirimale (Malwathu Oya) | 6.80 | 🟠 Minor Flood | 0.019 | 🔺 Rising |
| 2025-12-06 04:05:44 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2025-12-06 04:05:32 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-06 04:05:25 | Dunamale (Aththanagalu Oya) | 2.20 | 🟢 Normal | -0.032 |  |
| 2025-12-06 04:05:00 | Hanwella (Kelani Ganga) | 3.26 | 🟢 Normal | -0.041 |  |
| 2025-12-06 04:04:39 | Glencourse (Kelani Ganga) | 10.56 | 🟢 Normal | -0.021 |  |
| 2025-12-06 04:04:36 | Badalgama (Maha Oya) | 2.96 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2025-12-06 04:04:26 | Katharagama (Menik Ganga) | 0.64 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-06 04:06:55 | Thanthirimale (Malwathu Oya) | 6.80 | 🟠 Minor Flood | 0.019 | 🔺 Rising |
| 2025-12-06 03:04:29 | Magura (Kalu Ganga) | 4.49 | 🟡 Alert | 0.094 | 🔺 Rising |
| 2025-12-05 18:01:43 | Manampitiya (Mahaweli Ganga) | 1.90 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2025-12-06 04:07:54 | Putupaula (Kalu Ganga) | 1.22 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2025-12-06 05:01:03 | Badalgama (Maha Oya) | 3.02 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2025-12-05 18:04:31 | Galgamuwa (Mee Oya) | 0.79 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2025-12-06 04:02:01 | Nagalagam Street (Kelani Ganga) | 0.94 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2025-12-06 04:01:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.20 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2025-12-06 04:10:23 | Baddegama (Gin Ganga) | 2.62 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2025-12-05 16:03:28 | Thaldena (Mahaweli Ganga) | 0.84 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-06 05:02:35 | Thanamalwila (Kirindi Oya) | 1.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-06 04:16:04 | Kuda Oya (Kirindi Oya) | 1.63 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-06 05:01:19 | Kithulgala (Kelani Ganga) | 1.91 | 🟢 Normal | 0.000 |  |
| 2025-12-06 03:01:05 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2025-12-06 04:05:44 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2025-12-06 04:02:28 | Ellagawa (Kalu Ganga) | 6.42 | 🟢 Normal | 0.000 |  |
| 2025-12-06 03:03:46 | Padiyathalawa (Maduru Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-06 05:01:06 | Siyambalanduwa (Heda Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-06 04:04:26 | Katharagama (Menik Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-06 04:05:32 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-06 04:28:10 | Thalgahagoda (Nilwala Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-06 04:18:23 | Moraketiya (Walawe Ganga) | 1.18 | 🟢 Normal | -0.005 |  |
| 2025-12-06 05:02:36 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | -0.005 |  |
| 2025-12-06 03:17:34 | Panadugama (Nilwala Ganga) | 4.31 | 🟢 Normal | -0.006 |  |
| 2025-12-06 05:02:26 | Giriulla (Maha Oya) | 1.98 | 🟢 Normal | -0.010 |  |
| 2025-12-06 05:02:00 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | -0.011 |  |
| 2025-12-06 04:04:39 | Glencourse (Kelani Ganga) | 10.56 | 🟢 Normal | -0.021 |  |
| 2025-12-06 05:02:41 | Horowpothana (Yan Oya) | 2.05 | 🟢 Normal | -0.022 |  |
| 2025-12-06 04:03:09 | Urawa (Nilwala Ganga) | 0.69 | 🟢 Normal | -0.024 |  |
| 2025-12-06 04:05:25 | Dunamale (Aththanagalu Oya) | 2.20 | 🟢 Normal | -0.032 |  |
| 2025-12-06 05:03:18 | Hanwella (Kelani Ganga) | 3.22 | 🟢 Normal | -0.041 |  |
| 2025-12-06 04:15:12 | Rathnapura (Kalu Ganga) | 2.57 | 🟢 Normal | -0.062 |  |
| 2025-12-06 04:01:00 | Pitabeddara (Nilwala Ganga) | 0.95 | 🟢 Normal | -0.064 |  |
| 2025-12-05 18:05:43 | Weraganthota (Mahaweli Ganga) | -1.58 | 🟢 Normal | -0.177 |  |
| 2025-12-06 05:01:10 | Nakkala (Kumbukkan Oya) | 1.42 | 🟢 Normal | -0.180 |  |
| 2025-12-06 05:02:31 | Yaka Wewa (Ma Oya) | 0.86 | 🟢 Normal | -6.091 |  |
| 2025-12-06 05:03:16 | Thawalama (Gin Ganga) | 2.92 | 🟢 Normal | -324.000 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)