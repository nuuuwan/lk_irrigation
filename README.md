# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--12_16:08:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **15,995 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-12 16:08:46 | Glencourse (Kelani Ganga) | 9.92 | 🟢 Normal | -0.009 |  |
| 2025-12-12 16:08:39 | Weraganthota (Mahaweli Ganga) | -0.98 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2025-12-12 16:08:39 | Holombuwa (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2025-12-12 16:08:30 | Dunamale (Aththanagalu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-12 16:08:25 | Rathnapura (Kalu Ganga) | 2.44 | 🟢 Normal | -0.135 |  |
| 2025-12-12 16:07:49 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.000 |  |
| 2025-12-12 16:07:01 | Thanamalwila (Kirindi Oya) | 1.27 | 🟢 Normal | -0.083 |  |
| 2025-12-12 16:06:19 | Horowpothana (Yan Oya) | 6.35 | 🟡 Alert | 0.037 | 🔺 Rising |
| 2025-12-12 16:06:17 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.000 |  |
| 2025-12-12 16:06:15 | Siyambalanduwa (Heda Oya) | 1.01 | 🟢 Normal | -0.009 |  |
| 2025-12-12 16:06:14 | Putupaula (Kalu Ganga) | 0.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-12 16:06:12 | Manampitiya (Mahaweli Ganga) | 3.19 | 🟡 Alert | -0.040 |  |
| 2025-12-12 16:06:05 | Galgamuwa (Mee Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-12 16:05:41 | Badalgama (Maha Oya) | 2.55 | 🟢 Normal | 0.000 |  |
| 2025-12-12 16:05:05 | Giriulla (Maha Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2025-12-12 16:04:04 | Deraniyagala (Kelani Ganga) | 0.55 | 🟢 Normal | -0.088 |  |
| 2025-12-12 16:03:03 | Thaldena (Mahaweli Ganga) | 0.83 | 🟢 Normal | -0.010 |  |
| 2025-12-12 16:03:03 | Kuda Oya (Kirindi Oya) | 1.74 | 🟢 Normal | -0.010 |  |
| 2025-12-12 16:03:01 | Nakkala (Kumbukkan Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2025-12-12 16:03:01 | Moragaswewa (Deduru Oya) | 1.55 | 🟢 Normal | -0.022 |  |
| 2025-12-12 16:02:50 | Hanwella (Kelani Ganga) | 1.75 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-12 16:02:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.23 | 🟢 Normal | -0.041 |  |
| 2025-12-12 16:02:47 | Holombuwa (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2025-12-12 16:02:27 | Baddegama (Gin Ganga) | 1.85 | 🟢 Normal | -0.010 |  |
| 2025-12-12 16:02:09 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2025-12-12 16:01:42 | Yaka Wewa (Ma Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-12 16:01:40 | Wellawaya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2025-12-12 16:01:29 | Katharagama (Menik Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2025-12-12 16:01:27 | Moraketiya (Walawe Ganga) | 1.15 | 🟢 Normal | -0.030 |  |
| 2025-12-12 16:01:27 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2025-12-12 16:01:25 | Pitabeddara (Nilwala Ganga) | 1.01 | 🟢 Normal | -0.104 |  |
| 2025-12-12 16:01:11 | Ellagawa (Kalu Ganga) | 6.34 | 🟢 Normal | -0.062 |  |
| 2025-12-12 16:00:35 | Padiyathalawa (Maduru Oya) | 1.44 | 🟢 Normal | -0.011 |  |
| 2025-12-12 16:00:11 | Nawalapitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.015 |  |
| 2025-12-12 15:17:10 | Panadugama (Nilwala Ganga) | 3.98 | 🟢 Normal | -0.076 |  |
| 2025-12-12 15:15:25 | Pitabeddara (Nilwala Ganga) | 1.09 | 🟢 Normal | -0.104 |  |
| 2025-12-12 15:10:40 | Urawa (Nilwala Ganga) | 0.77 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-12 16:06:19 | Horowpothana (Yan Oya) | 6.35 | 🟡 Alert | 0.037 | 🔺 Rising |
| 2025-12-12 16:06:12 | Manampitiya (Mahaweli Ganga) | 3.19 | 🟡 Alert | -0.040 |  |
| 2025-12-12 15:01:09 | Magura (Kalu Ganga) | 2.49 | 🟢 Normal | 1.244 | 🔺 Rising |
| 2025-12-12 16:08:39 | Weraganthota (Mahaweli Ganga) | -0.98 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2025-12-12 16:01:27 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2025-12-12 15:01:32 | Peradeniya (Mahaweli Ganga) | 2.40 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2025-12-12 16:02:50 | Hanwella (Kelani Ganga) | 1.75 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-12 15:07:11 | Thanthirimale (Malwathu Oya) | 4.32 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2025-12-12 16:06:14 | Putupaula (Kalu Ganga) | 0.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-12 16:07:49 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.000 |  |
| 2025-12-12 16:01:40 | Wellawaya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2025-12-12 16:01:42 | Yaka Wewa (Ma Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-12 16:05:05 | Giriulla (Maha Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2025-12-12 16:06:05 | Galgamuwa (Mee Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-12 16:08:30 | Dunamale (Aththanagalu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-12 16:01:29 | Katharagama (Menik Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2025-12-12 16:05:41 | Badalgama (Maha Oya) | 2.55 | 🟢 Normal | 0.000 |  |
| 2025-12-12 16:08:39 | Holombuwa (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2025-12-12 15:04:29 | Thawalama (Gin Ganga) | 1.77 | 🟢 Normal | 0.000 |  |
| 2025-12-12 15:10:40 | Urawa (Nilwala Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2025-12-12 15:01:22 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-12 16:08:46 | Glencourse (Kelani Ganga) | 9.92 | 🟢 Normal | -0.009 |  |
| 2025-12-12 16:06:15 | Siyambalanduwa (Heda Oya) | 1.01 | 🟢 Normal | -0.009 |  |
| 2025-12-12 16:03:01 | Nakkala (Kumbukkan Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2025-12-12 16:03:03 | Thaldena (Mahaweli Ganga) | 0.83 | 🟢 Normal | -0.010 |  |
| 2025-12-12 16:02:09 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2025-12-12 16:03:03 | Kuda Oya (Kirindi Oya) | 1.74 | 🟢 Normal | -0.010 |  |
| 2025-12-12 16:02:27 | Baddegama (Gin Ganga) | 1.85 | 🟢 Normal | -0.010 |  |
| 2025-12-12 16:00:35 | Padiyathalawa (Maduru Oya) | 1.44 | 🟢 Normal | -0.011 |  |
| 2025-12-12 16:00:11 | Nawalapitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.015 |  |
| 2025-12-12 16:03:01 | Moragaswewa (Deduru Oya) | 1.55 | 🟢 Normal | -0.022 |  |
| 2025-12-12 16:01:27 | Moraketiya (Walawe Ganga) | 1.15 | 🟢 Normal | -0.030 |  |
| 2025-12-12 16:02:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.23 | 🟢 Normal | -0.041 |  |
| 2025-12-12 16:01:11 | Ellagawa (Kalu Ganga) | 6.34 | 🟢 Normal | -0.062 |  |
| 2025-12-12 15:17:10 | Panadugama (Nilwala Ganga) | 3.98 | 🟢 Normal | -0.076 |  |
| 2025-12-12 16:07:01 | Thanamalwila (Kirindi Oya) | 1.27 | 🟢 Normal | -0.083 |  |
| 2025-12-12 16:04:04 | Deraniyagala (Kelani Ganga) | 0.55 | 🟢 Normal | -0.088 |  |
| 2025-12-12 16:01:25 | Pitabeddara (Nilwala Ganga) | 1.01 | 🟢 Normal | -0.104 |  |
| 2025-12-12 16:08:25 | Rathnapura (Kalu Ganga) | 2.44 | 🟢 Normal | -0.135 |  |

## River Water Level Charts by Station

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)