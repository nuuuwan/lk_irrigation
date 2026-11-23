# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--24_03:15:55-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **324,106 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-24 03:15:55 | Holombuwa (Kelani Ganga) | 1.38 | 🟢 Normal | -0.307 |  |
| 2026-11-24 03:14:01 | Panadugama (Nilwala Ganga) | 3.67 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-11-24 03:13:48 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | -0.005 |  |
| 2026-11-24 03:13:20 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-11-24 03:13:18 | Ellagawa (Kalu Ganga) | 5.09 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-11-24 03:13:16 | Ellagawa (Kalu Ganga) | 5.08 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-11-24 03:08:23 | Hanwella (Kelani Ganga) | 2.00 | 🟢 Normal | 0.430 | 🔺 Rising |
| 2026-11-24 03:07:22 | Magura (Kalu Ganga) | 2.18 | 🟢 Normal | -1.091 |  |
| 2026-11-24 03:06:38 | Norwood (Kelani Ganga) | 0.86 | 🟢 Normal | -0.019 |  |
| 2026-11-24 03:06:12 | Wellawaya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-24 03:06:10 | Rathnapura (Kalu Ganga) | 2.14 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-11-24 03:05:49 | Baddegama (Gin Ganga) | 1.78 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-24 03:04:59 | Dunamale (Aththanagalu Oya) | 1.70 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-11-24 03:04:38 | Urawa (Nilwala Ganga) | 1.89 | 🟢 Normal | -0.076 |  |
| 2026-11-24 03:04:29 | Glencourse (Kelani Ganga) | 11.90 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-24 03:04:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.26 | 🟢 Normal | 0.973 | 🔺 Rising |
| 2026-11-24 03:04:00 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-11-24 03:03:50 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-11-24 03:03:44 | Peradeniya (Mahaweli Ganga) | 2.94 | 🟢 Normal | -0.066 |  |
| 2026-11-24 03:03:14 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-11-24 03:03:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.24 | 🟢 Normal | 0.973 | 🔺 Rising |
| 2026-11-24 03:03:12 | Putupaula (Kalu Ganga) | 0.93 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-11-24 03:02:56 | Thawalama (Gin Ganga) | 1.97 | 🟢 Normal | -0.010 |  |
| 2026-11-24 03:02:33 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-11-24 03:02:32 | Manampitiya (Mahaweli Ganga) | 1.06 | 🟢 Normal | -0.020 |  |
| 2026-11-24 03:02:24 | Moragaswewa (Deduru Oya) | 0.78 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-11-24 03:02:18 | Badalgama (Maha Oya) | 2.94 | 🟢 Normal | 0.217 | 🔺 Rising |
| 2026-11-24 03:02:18 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | -0.003 |  |
| 2026-11-24 03:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.18 | 🟢 Normal | 0.973 | 🔺 Rising |
| 2026-11-24 03:01:54 | Thanamalwila (Kirindi Oya) | 1.19 | 🟢 Normal | -0.013 |  |
| 2026-11-24 03:01:52 | Magura (Kalu Ganga) | 2.28 | 🟢 Normal | -1.091 |  |
| 2026-11-24 03:01:50 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.049 |  |
| 2026-11-24 03:01:45 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-24 03:01:34 | Pitabeddara (Nilwala Ganga) | 1.19 | 🟢 Normal | -0.022 |  |
| 2026-11-24 03:01:15 | Giriulla (Maha Oya) | 4.59 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-11-24 03:01:14 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-11-24 03:00:53 | Thalgahagoda (Nilwala Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-11-24 03:00:43 | Moraketiya (Walawe Ganga) | 2.20 | 🟢 Normal | -0.033 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-24 03:13:18 | Ellagawa (Kalu Ganga) | 5.09 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-11-24 03:04:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.26 | 🟢 Normal | 0.973 | 🔺 Rising |
| 2026-11-24 03:08:23 | Hanwella (Kelani Ganga) | 2.00 | 🟢 Normal | 0.430 | 🔺 Rising |
| 2026-11-24 03:02:18 | Badalgama (Maha Oya) | 2.94 | 🟢 Normal | 0.217 | 🔺 Rising |
| 2026-11-24 03:03:50 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-11-24 03:04:59 | Dunamale (Aththanagalu Oya) | 1.70 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-11-24 03:01:15 | Giriulla (Maha Oya) | 4.59 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-11-24 03:14:01 | Panadugama (Nilwala Ganga) | 3.67 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-11-24 03:03:12 | Putupaula (Kalu Ganga) | 0.93 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-11-24 03:02:24 | Moragaswewa (Deduru Oya) | 0.78 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-11-24 03:04:29 | Glencourse (Kelani Ganga) | 11.90 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-24 03:04:00 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-11-24 03:06:10 | Rathnapura (Kalu Ganga) | 2.14 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-11-24 03:05:49 | Baddegama (Gin Ganga) | 1.78 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-24 03:06:12 | Wellawaya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-24 00:04:06 | Horowpothana (Yan Oya) | 2.19 | 🟢 Normal | 0.005 |  |
| 2026-11-24 03:01:14 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-11-24 03:01:45 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-23 18:05:14 | Galgamuwa (Mee Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-11-24 03:13:20 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-11-24 03:00:53 | Thalgahagoda (Nilwala Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-11-24 03:02:18 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | -0.003 |  |
| 2026-11-24 03:13:48 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | -0.005 |  |
| 2026-11-24 02:15:16 | Nawalapitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | -0.008 |  |
| 2026-11-24 03:02:33 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-11-24 03:02:56 | Thawalama (Gin Ganga) | 1.97 | 🟢 Normal | -0.010 |  |
| 2026-11-24 03:01:54 | Thanamalwila (Kirindi Oya) | 1.19 | 🟢 Normal | -0.013 |  |
| 2026-11-24 03:06:38 | Norwood (Kelani Ganga) | 0.86 | 🟢 Normal | -0.019 |  |
| 2026-11-24 03:02:32 | Manampitiya (Mahaweli Ganga) | 1.06 | 🟢 Normal | -0.020 |  |
| 2026-11-23 18:02:13 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | -0.020 |  |
| 2026-11-22 17:02:02⌛ | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | -0.022 |  |
| 2026-11-24 03:01:34 | Pitabeddara (Nilwala Ganga) | 1.19 | 🟢 Normal | -0.022 |  |
| 2026-11-24 03:00:43 | Moraketiya (Walawe Ganga) | 2.20 | 🟢 Normal | -0.033 |  |
| 2026-11-24 03:01:50 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.049 |  |
| 2026-11-23 18:00:35 | Weraganthota (Mahaweli Ganga) | -2.49 | 🟢 Normal | -0.050 |  |
| 2026-11-24 03:03:44 | Peradeniya (Mahaweli Ganga) | 2.94 | 🟢 Normal | -0.066 |  |
| 2026-11-24 03:04:38 | Urawa (Nilwala Ganga) | 1.89 | 🟢 Normal | -0.076 |  |
| 2026-11-24 03:15:55 | Holombuwa (Kelani Ganga) | 1.38 | 🟢 Normal | -0.307 |  |
| 2026-11-24 03:07:22 | Magura (Kalu Ganga) | 2.18 | 🟢 Normal | -1.091 |  |

## River Water Level Charts by Station

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)