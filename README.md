# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--23_18:10:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **268,981 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Baddegama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-23 18:10:48 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | -0.009 |  |
| 2026-09-23 18:09:35 | Thalgahagoda (Nilwala Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-09-23 18:09:27 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-23 18:08:23 | Dunamale (Aththanagalu Oya) | 2.46 | 🟢 Normal | -0.036 |  |
| 2026-09-23 18:07:06 | Holombuwa (Kelani Ganga) | 1.18 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-09-23 18:06:29 | Giriulla (Maha Oya) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-09-23 18:06:13 | Glencourse (Kelani Ganga) | 12.50 | 🟢 Normal | -0.050 |  |
| 2026-09-23 18:05:19 | Deraniyagala (Kelani Ganga) | 1.95 | 🟢 Normal | -0.040 |  |
| 2026-09-23 18:04:36 | Hanwella (Kelani Ganga) | 4.69 | 🟢 Normal | -0.041 |  |
| 2026-09-23 18:03:57 | Badalgama (Maha Oya) | 2.66 | 🟢 Normal | -0.010 |  |
| 2026-09-23 18:03:57 | Norwood (Kelani Ganga) | 0.91 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-23 18:03:48 | Rathnapura (Kalu Ganga) | 3.93 | 🟢 Normal | 0.142 | 🔺 Rising |
| 2026-09-23 18:03:42 | Nawalapitiya (Mahaweli Ganga) | 2.57 | 🟢 Normal | 0.000 |  |
| 2026-09-23 18:03:31 | Thanthirimale (Malwathu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-23 18:03:22 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | -0.010 |  |
| 2026-09-23 18:03:06 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-23 18:02:41 | Thawalama (Gin Ganga) | 2.77 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-09-23 18:02:28 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-23 18:02:26 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-23 18:02:17 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-23 18:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.89 | 🟠 Minor Flood | -0.020 |  |
| 2026-09-23 18:02:08 | Kithulgala (Kelani Ganga) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-09-23 18:02:06 | Putupaula (Kalu Ganga) | 2.81 | 🟢 Normal | -0.020 |  |
| 2026-09-23 18:01:58 | Thanamalwila (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-09-23 18:01:53 | Baddegama (Gin Ganga) | 3.67 | 🟡 Alert | -0.011 |  |
| 2026-09-23 18:01:52 | Kuda Oya (Kirindi Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-09-23 18:01:50 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.096 |  |
| 2026-09-23 18:01:44 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-23 18:01:38 | Manampitiya (Mahaweli Ganga) | -0.24 | 🟢 Normal | -0.010 |  |
| 2026-09-23 18:01:34 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | -0.020 |  |
| 2026-09-23 18:01:33 | Ellagawa (Kalu Ganga) | 7.88 | 🟢 Normal | -0.023 |  |
| 2026-09-23 18:01:26 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-23 18:01:18 | Magura (Kalu Ganga) | 3.91 | 🟢 Normal | -0.061 |  |
| 2026-09-23 18:01:14 | Peradeniya (Mahaweli Ganga) | 3.10 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-09-23 18:01:10 | Pitabeddara (Nilwala Ganga) | 1.46 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-09-23 18:00:49 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-09-23 18:00:33 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | -0.021 |  |
| 2026-09-23 18:00:11 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-09-23 17:53:42 | Kuda Oya (Kirindi Oya) | 1.00 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-23 18:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.89 | 🟠 Minor Flood | -0.020 |  |
| 2026-09-23 18:01:53 | Baddegama (Gin Ganga) | 3.67 | 🟡 Alert | -0.011 |  |
| 2026-09-23 18:03:48 | Rathnapura (Kalu Ganga) | 3.93 | 🟢 Normal | 0.142 | 🔺 Rising |
| 2026-09-23 18:01:14 | Peradeniya (Mahaweli Ganga) | 3.10 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-09-23 18:01:10 | Pitabeddara (Nilwala Ganga) | 1.46 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-09-23 18:07:06 | Holombuwa (Kelani Ganga) | 1.18 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-09-23 18:02:41 | Thawalama (Gin Ganga) | 2.77 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-09-23 18:03:57 | Norwood (Kelani Ganga) | 0.91 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-23 18:02:08 | Kithulgala (Kelani Ganga) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-09-23 18:09:27 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-23 18:03:06 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-23 18:03:42 | Nawalapitiya (Mahaweli Ganga) | 2.57 | 🟢 Normal | 0.000 |  |
| 2026-09-23 18:01:44 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-23 18:02:17 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-23 18:00:49 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-09-23 18:02:26 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-23 18:02:28 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-23 18:03:31 | Thanthirimale (Malwathu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-23 17:04:00 | Urawa (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-09-23 18:09:35 | Thalgahagoda (Nilwala Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-09-23 18:01:52 | Kuda Oya (Kirindi Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-09-23 18:01:58 | Thanamalwila (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-09-23 18:10:48 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | -0.009 |  |
| 2026-09-23 18:06:29 | Giriulla (Maha Oya) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-09-23 18:03:22 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | -0.010 |  |
| 2026-09-23 18:01:38 | Manampitiya (Mahaweli Ganga) | -0.24 | 🟢 Normal | -0.010 |  |
| 2026-09-23 18:03:57 | Badalgama (Maha Oya) | 2.66 | 🟢 Normal | -0.010 |  |
| 2026-09-23 18:00:11 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-09-23 17:23:23 | Panadugama (Nilwala Ganga) | 4.28 | 🟢 Normal | -0.014 |  |
| 2026-09-23 18:01:34 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | -0.020 |  |
| 2026-09-23 18:02:06 | Putupaula (Kalu Ganga) | 2.81 | 🟢 Normal | -0.020 |  |
| 2026-09-23 18:00:33 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | -0.021 |  |
| 2026-09-23 18:01:33 | Ellagawa (Kalu Ganga) | 7.88 | 🟢 Normal | -0.023 |  |
| 2026-09-23 18:08:23 | Dunamale (Aththanagalu Oya) | 2.46 | 🟢 Normal | -0.036 |  |
| 2026-09-23 18:05:19 | Deraniyagala (Kelani Ganga) | 1.95 | 🟢 Normal | -0.040 |  |
| 2026-09-23 18:04:36 | Hanwella (Kelani Ganga) | 4.69 | 🟢 Normal | -0.041 |  |
| 2026-09-23 18:06:13 | Glencourse (Kelani Ganga) | 12.50 | 🟢 Normal | -0.050 |  |
| 2026-09-23 18:01:18 | Magura (Kalu Ganga) | 3.91 | 🟢 Normal | -0.061 |  |
| 2026-09-23 18:01:50 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.096 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)