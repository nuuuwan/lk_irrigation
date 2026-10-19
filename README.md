# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--19_05:25:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **291,876 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **17** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-19 05:25:18 | Magura (Kalu Ganga) | 2.14 | 🟢 Normal | -0.061 |  |
| 2026-10-19 05:23:32 | Kithulgala (Kelani Ganga) | 2.13 | 🟢 Normal | -0.008 |  |
| 2026-10-19 05:15:16 | Holombuwa (Kelani Ganga) | 0.99 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-10-19 05:13:01 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-10-19 05:12:44 | Thalgahagoda (Nilwala Ganga) | 1.98 | 🟠 Minor Flood | -0.009 |  |
| 2026-10-19 05:12:03 | Putupaula (Kalu Ganga) | 1.64 | 🟢 Normal | -0.053 |  |
| 2026-10-19 05:10:59 | Baddegama (Gin Ganga) | 2.78 | 🟢 Normal | -0.019 |  |
| 2026-10-19 05:09:47 | Deraniyagala (Kelani Ganga) | 1.04 | 🟢 Normal | -7.500 |  |
| 2026-10-19 05:09:23 | Deraniyagala (Kelani Ganga) | 1.09 | 🟢 Normal | -7.500 |  |
| 2026-10-19 05:07:49 | Rathnapura (Kalu Ganga) | 3.81 | 🟢 Normal | -0.129 |  |
| 2026-10-19 05:07:40 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-10-19 05:06:50 | Glencourse (Kelani Ganga) | 11.60 | 🟢 Normal | -0.135 |  |
| 2026-10-19 05:06:19 | Norwood (Kelani Ganga) | 1.42 | 🟢 Normal | -0.040 |  |
| 2026-10-19 05:06:17 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-19 05:05:41 | Magura (Kalu Ganga) | 2.16 | 🟢 Normal | -0.061 |  |
| 2026-10-19 05:05:31 | Badalgama (Maha Oya) | 2.76 | 🟢 Normal | -0.011 |  |
| 2026-10-19 05:05:20 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | -0.009 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-19 05:12:44 | Thalgahagoda (Nilwala Ganga) | 1.98 | 🟠 Minor Flood | -0.009 |  |
| 2026-10-19 05:01:50 | Panadugama (Nilwala Ganga) | 5.60 | 🟡 Alert | -3.176 |  |
| 2026-10-19 05:01:51 | Thaldena (Mahaweli Ganga) | 1.30 | 🟢 Normal | 414.000 | 🔺 Rising |
| 2026-10-19 05:03:22 | Giriulla (Maha Oya) | 1.59 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-10-19 05:13:01 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-10-19 05:15:16 | Holombuwa (Kelani Ganga) | 0.99 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-10-19 05:01:21 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-10-19 05:07:40 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-10-19 05:00:13 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-10-19 05:06:17 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-19 05:23:32 | Kithulgala (Kelani Ganga) | 2.13 | 🟢 Normal | -0.008 |  |
| 2026-10-19 05:05:20 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | -0.009 |  |
| 2026-10-19 05:02:41 | Wellawaya (Kirindi Oya) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-10-18 18:05:26 | Galgamuwa (Mee Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-10-19 05:02:09 | Thawalama (Gin Ganga) | 2.49 | 🟢 Normal | -0.010 |  |
| 2026-10-19 05:02:37 | Horowpothana (Yan Oya) | 2.21 | 🟢 Normal | -0.010 |  |
| 2026-10-19 04:01:48 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-10-19 05:05:31 | Badalgama (Maha Oya) | 2.76 | 🟢 Normal | -0.011 |  |
| 2026-10-19 04:22:20 | Pitabeddara (Nilwala Ganga) | 2.18 | 🟢 Normal | -0.019 |  |
| 2026-10-19 05:10:59 | Baddegama (Gin Ganga) | 2.78 | 🟢 Normal | -0.019 |  |
| 2026-10-19 05:02:10 | Thanamalwila (Kirindi Oya) | 1.38 | 🟢 Normal | -0.020 |  |
| 2026-10-18 18:01:11 | Thanthirimale (Malwathu Oya) | 1.62 | 🟢 Normal | -0.030 |  |
| 2026-10-19 05:01:19 | Ellagawa (Kalu Ganga) | 7.30 | 🟢 Normal | -0.030 |  |
| 2026-10-19 05:01:19 | Dunamale (Aththanagalu Oya) | 2.10 | 🟢 Normal | -0.031 |  |
| 2026-10-19 04:01:49 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | -0.040 |  |
| 2026-10-19 05:06:19 | Norwood (Kelani Ganga) | 1.42 | 🟢 Normal | -0.040 |  |
| 2026-10-19 05:02:09 | Hanwella (Kelani Ganga) | 3.79 | 🟢 Normal | -0.044 |  |
| 2026-10-19 05:04:10 | Moragaswewa (Deduru Oya) | 2.20 | 🟢 Normal | -0.049 |  |
| 2026-10-18 18:00:10 | Weraganthota (Mahaweli Ganga) | -2.73 | 🟢 Normal | -0.050 |  |
| 2026-10-19 05:01:05 | Peradeniya (Mahaweli Ganga) | 2.95 | 🟢 Normal | -0.051 |  |
| 2026-10-19 05:12:03 | Putupaula (Kalu Ganga) | 1.64 | 🟢 Normal | -0.053 |  |
| 2026-10-19 04:04:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.42 | 🟢 Normal | -0.057 |  |
| 2026-10-19 04:04:01 | Urawa (Nilwala Ganga) | 1.15 | 🟢 Normal | -0.061 |  |
| 2026-10-19 05:25:18 | Magura (Kalu Ganga) | 2.14 | 🟢 Normal | -0.061 |  |
| 2026-10-19 05:01:41 | Manampitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | -0.091 |  |
| 2026-10-19 05:03:01 | Moraketiya (Walawe Ganga) | 1.40 | 🟢 Normal | -0.098 |  |
| 2026-10-19 05:07:49 | Rathnapura (Kalu Ganga) | 3.81 | 🟢 Normal | -0.129 |  |
| 2026-10-19 05:06:50 | Glencourse (Kelani Ganga) | 11.60 | 🟢 Normal | -0.135 |  |
| 2026-10-19 05:09:47 | Deraniyagala (Kelani Ganga) | 1.04 | 🟢 Normal | -7.500 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)