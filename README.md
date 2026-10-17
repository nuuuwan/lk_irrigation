# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--18_03:22:38-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **290,909 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Panadugama — Minor Flood; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **43** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-18 03:22:38 | Moragaswewa (Deduru Oya) | 1.16 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-18 03:22:27 | Horowpothana (Yan Oya) | 2.94 | 🟢 Normal | 108.000 | 🔺 Rising |
| 2026-10-18 03:22:26 | Horowpothana (Yan Oya) | 2.91 | 🟢 Normal | 108.000 | 🔺 Rising |
| 2026-10-18 03:22:25 | Horowpothana (Yan Oya) | 2.88 | 🟢 Normal | 108.000 | 🔺 Rising |
| 2026-10-18 03:17:25 | Kithulgala (Kelani Ganga) | 2.18 | 🟢 Normal | 0.278 | 🔺 Rising |
| 2026-10-18 03:16:36 | Norwood (Kelani Ganga) | 1.35 | 🟢 Normal | -0.034 |  |
| 2026-10-18 03:15:21 | Rathnapura (Kalu Ganga) | 4.99 | 🟢 Normal | -0.303 |  |
| 2026-10-18 03:12:15 | Wellawaya (Kirindi Oya) | 1.36 | 🟢 Normal | -0.033 |  |
| 2026-10-18 03:10:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.40 | 🟡 Alert | -1.029 |  |
| 2026-10-18 03:10:16 | Thanamalwila (Kirindi Oya) | 1.03 | 🟢 Normal | -252.000 |  |
| 2026-10-18 03:10:15 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | -252.000 |  |
| 2026-10-18 03:09:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.42 | 🟡 Alert | -1.029 |  |
| 2026-10-18 03:07:36 | Ellagawa (Kalu Ganga) | 7.56 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-10-18 03:07:14 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-10-18 03:07:04 | Panadugama (Nilwala Ganga) | 6.21 | 🟠 Minor Flood | -0.011 |  |
| 2026-10-18 03:06:52 | Holombuwa (Kelani Ganga) | 1.44 | 🟢 Normal | -0.088 |  |
| 2026-10-18 03:06:29 | Glencourse (Kelani Ganga) | 12.80 | 🟢 Normal | -0.216 |  |
| 2026-10-18 03:06:05 | Dunamale (Aththanagalu Oya) | 2.60 | 🟢 Normal | -0.060 |  |
| 2026-10-18 03:05:58 | Giriulla (Maha Oya) | 2.94 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-10-18 03:05:44 | Baddegama (Gin Ganga) | 3.10 | 🟢 Normal | 0.000 |  |
| 2026-10-18 03:05:01 | Hanwella (Kelani Ganga) | 4.51 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-10-18 03:04:52 | Putupaula (Kalu Ganga) | 2.03 | 🟢 Normal | -0.010 |  |
| 2026-10-18 03:04:25 | Thaldena (Mahaweli Ganga) | 0.82 | 🟢 Normal | -0.127 |  |
| 2026-10-18 03:04:23 | Magura (Kalu Ganga) | 2.43 | 🟢 Normal | -180.000 |  |
| 2026-10-18 03:04:22 | Padiyathalawa (Maduru Oya) | 1.30 | 🟢 Normal | -0.059 |  |
| 2026-10-18 03:04:22 | Magura (Kalu Ganga) | 2.48 | 🟢 Normal | -180.000 |  |
| 2026-10-18 03:04:04 | Moraketiya (Walawe Ganga) | 1.57 | 🟢 Normal | -0.010 |  |
| 2026-10-18 03:03:56 | Badalgama (Maha Oya) | 2.92 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-18 03:03:45 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-10-18 03:03:20 | Deraniyagala (Kelani Ganga) | 0.99 | 🟢 Normal | -0.091 |  |
| 2026-10-18 03:03:07 | Manampitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-18 03:03:06 | Manampitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-18 03:02:26 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-10-18 03:02:24 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-10-18 03:02:21 | Peradeniya (Mahaweli Ganga) | 3.82 | 🟢 Normal | -0.339 |  |
| 2026-10-18 03:02:19 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-10-18 03:01:59 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-10-18 03:01:54 | Pitabeddara (Nilwala Ganga) | 2.98 | 🟢 Normal | -0.072 |  |
| 2026-10-18 03:01:41 | Moragaswewa (Deduru Oya) | 1.15 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-18 03:01:30 | Thawalama (Gin Ganga) | 3.96 | 🟢 Normal | -0.038 |  |
| 2026-10-18 03:00:56 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-10-18 03:00:49 | Thalgahagoda (Nilwala Ganga) | 2.03 | 🟠 Minor Flood | 0.011 | 🔺 Rising |
| 2026-10-18 03:00:06 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-18 03:00:49 | Thalgahagoda (Nilwala Ganga) | 2.03 | 🟠 Minor Flood | 0.011 | 🔺 Rising |
| 2026-10-18 03:07:04 | Panadugama (Nilwala Ganga) | 6.21 | 🟠 Minor Flood | -0.011 |  |
| 2026-10-18 03:10:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.40 | 🟡 Alert | -1.029 |  |
| 2026-10-18 03:22:27 | Horowpothana (Yan Oya) | 2.94 | 🟢 Normal | 108.000 | 🔺 Rising |
| 2026-10-18 03:17:25 | Kithulgala (Kelani Ganga) | 2.18 | 🟢 Normal | 0.278 | 🔺 Rising |
| 2026-10-18 03:05:01 | Hanwella (Kelani Ganga) | 4.51 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-10-18 03:02:26 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-10-18 03:07:36 | Ellagawa (Kalu Ganga) | 7.56 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-10-18 03:05:58 | Giriulla (Maha Oya) | 2.94 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-10-18 03:22:38 | Moragaswewa (Deduru Oya) | 1.16 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-18 03:03:56 | Badalgama (Maha Oya) | 2.92 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-17 18:02:22 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | 0.000 |  |
| 2026-10-18 03:00:56 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-10-18 03:02:24 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-10-18 03:07:14 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-10-18 03:05:44 | Baddegama (Gin Ganga) | 3.10 | 🟢 Normal | 0.000 |  |
| 2026-10-18 03:00:06 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-10-18 03:03:45 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-10-18 03:03:07 | Manampitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-18 03:02:19 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-10-17 21:21:56 | Galgamuwa (Mee Oya) | 1.54 | 🟢 Normal | -0.009 |  |
| 2026-10-18 03:04:52 | Putupaula (Kalu Ganga) | 2.03 | 🟢 Normal | -0.010 |  |
| 2026-10-18 03:04:04 | Moraketiya (Walawe Ganga) | 1.57 | 🟢 Normal | -0.010 |  |
| 2026-10-18 03:12:15 | Wellawaya (Kirindi Oya) | 1.36 | 🟢 Normal | -0.033 |  |
| 2026-10-18 03:16:36 | Norwood (Kelani Ganga) | 1.35 | 🟢 Normal | -0.034 |  |
| 2026-10-18 03:01:30 | Thawalama (Gin Ganga) | 3.96 | 🟢 Normal | -0.038 |  |
| 2026-10-17 18:01:56 | Thanthirimale (Malwathu Oya) | 2.41 | 🟢 Normal | -0.040 |  |
| 2026-10-18 02:09:12 | Urawa (Nilwala Ganga) | 1.75 | 🟢 Normal | -0.040 |  |
| 2026-10-18 03:04:22 | Padiyathalawa (Maduru Oya) | 1.30 | 🟢 Normal | -0.059 |  |
| 2026-10-18 03:06:05 | Dunamale (Aththanagalu Oya) | 2.60 | 🟢 Normal | -0.060 |  |
| 2026-10-18 03:01:54 | Pitabeddara (Nilwala Ganga) | 2.98 | 🟢 Normal | -0.072 |  |
| 2026-10-18 03:06:52 | Holombuwa (Kelani Ganga) | 1.44 | 🟢 Normal | -0.088 |  |
| 2026-10-18 03:03:20 | Deraniyagala (Kelani Ganga) | 0.99 | 🟢 Normal | -0.091 |  |
| 2026-10-18 03:04:25 | Thaldena (Mahaweli Ganga) | 0.82 | 🟢 Normal | -0.127 |  |
| 2026-10-18 03:06:29 | Glencourse (Kelani Ganga) | 12.80 | 🟢 Normal | -0.216 |  |
| 2026-10-18 03:15:21 | Rathnapura (Kalu Ganga) | 4.99 | 🟢 Normal | -0.303 |  |
| 2026-10-18 03:02:21 | Peradeniya (Mahaweli Ganga) | 3.82 | 🟢 Normal | -0.339 |  |
| 2026-10-18 03:04:23 | Magura (Kalu Ganga) | 2.43 | 🟢 Normal | -180.000 |  |
| 2026-10-18 03:10:16 | Thanamalwila (Kirindi Oya) | 1.03 | 🟢 Normal | -252.000 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)