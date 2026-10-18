# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--18_21:31:55-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **291,599 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Panadugama — Alert; 🟡 Norwood — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-18 21:31:55 | Panadugama (Nilwala Ganga) | 5.67 | 🟡 Alert | 0.000 |  |
| 2026-10-18 21:12:15 | Moragaswewa (Deduru Oya) | 2.65 | 🟢 Normal | 0.000 |  |
| 2026-10-18 21:11:36 | Norwood (Kelani Ganga) | 1.75 | 🟡 Alert | -0.018 |  |
| 2026-10-18 21:09:11 | Pitabeddara (Nilwala Ganga) | 2.40 | 🟢 Normal | 0.000 |  |
| 2026-10-18 21:07:50 | Panadugama (Nilwala Ganga) | 5.67 | 🟡 Alert | 0.000 |  |
| 2026-10-18 21:06:45 | Putupaula (Kalu Ganga) | 1.83 | 🟢 Normal | -0.009 |  |
| 2026-10-18 21:06:43 | Hanwella (Kelani Ganga) | 3.15 | 🟢 Normal | -0.046 |  |
| 2026-10-18 21:06:19 | Magura (Kalu Ganga) | 2.21 | 🟢 Normal | -0.013 |  |
| 2026-10-18 21:06:04 | Baddegama (Gin Ganga) | 3.03 | 🟢 Normal | -0.030 |  |
| 2026-10-18 21:05:53 | Kithulgala (Kelani Ganga) | 2.21 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-10-18 21:05:36 | Badalgama (Maha Oya) | 2.91 | 🟢 Normal | -0.031 |  |
| 2026-10-18 21:05:19 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-18 21:04:35 | Dunamale (Aththanagalu Oya) | 2.15 | 🟢 Normal | -0.051 |  |
| 2026-10-18 21:04:28 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | -0.009 |  |
| 2026-10-18 21:03:49 | Thalgahagoda (Nilwala Ganga) | 2.01 | 🟠 Minor Flood | -0.011 |  |
| 2026-10-18 21:03:23 | Deraniyagala (Kelani Ganga) | 1.57 | 🟢 Normal | -0.370 |  |
| 2026-10-18 21:03:23 | Moragaswewa (Deduru Oya) | 2.65 | 🟢 Normal | 0.000 |  |
| 2026-10-18 21:03:08 | Urawa (Nilwala Ganga) | 1.44 | 🟢 Normal | -0.043 |  |
| 2026-10-18 21:03:05 | Manampitiya (Mahaweli Ganga) | 1.09 | 🟢 Normal | -0.011 |  |
| 2026-10-18 21:02:59 | Wellawaya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-18 21:02:56 | Thawalama (Gin Ganga) | 2.50 | 🟢 Normal | -0.021 |  |
| 2026-10-18 21:02:53 | Glencourse (Kelani Ganga) | 11.60 | 🟢 Normal | 0.477 | 🔺 Rising |
| 2026-10-18 21:02:51 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-10-18 21:02:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.62 | 🟢 Normal | -0.022 |  |
| 2026-10-18 21:02:31 | Giriulla (Maha Oya) | 1.58 | 🟢 Normal | -0.030 |  |
| 2026-10-18 21:02:20 | Pitabeddara (Nilwala Ganga) | 2.40 | 🟢 Normal | 0.000 |  |
| 2026-10-18 21:02:16 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-10-18 21:02:10 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-18 21:02:02 | Yaka Wewa (Ma Oya) | 0.00 | 🟢 Normal | -0.579 |  |
| 2026-10-18 21:01:55 | Moraketiya (Walawe Ganga) | 1.82 | 🟢 Normal | -0.113 |  |
| 2026-10-18 21:01:52 | Peradeniya (Mahaweli Ganga) | 3.26 | 🟢 Normal | 0.265 | 🔺 Rising |
| 2026-10-18 21:01:36 | Ellagawa (Kalu Ganga) | 7.41 | 🟢 Normal | -0.031 |  |
| 2026-10-18 21:01:35 | Nawalapitiya (Mahaweli Ganga) | 1.44 | 🟢 Normal | -0.075 |  |
| 2026-10-18 21:01:05 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.093 |  |
| 2026-10-18 21:00:56 | Horowpothana (Yan Oya) | 2.58 | 🟢 Normal | -0.082 |  |
| 2026-10-18 21:00:12 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-10-18 21:00:10 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-18 21:03:49 | Thalgahagoda (Nilwala Ganga) | 2.01 | 🟠 Minor Flood | -0.011 |  |
| 2026-10-18 21:31:55 | Panadugama (Nilwala Ganga) | 5.67 | 🟡 Alert | 0.000 |  |
| 2026-10-18 21:11:36 | Norwood (Kelani Ganga) | 1.75 | 🟡 Alert | -0.018 |  |
| 2026-10-18 21:02:53 | Glencourse (Kelani Ganga) | 11.60 | 🟢 Normal | 0.477 | 🔺 Rising |
| 2026-10-18 20:05:05 | Rathnapura (Kalu Ganga) | 4.63 | 🟢 Normal | 0.293 | 🔺 Rising |
| 2026-10-18 21:01:52 | Peradeniya (Mahaweli Ganga) | 3.26 | 🟢 Normal | 0.265 | 🔺 Rising |
| 2026-10-18 21:05:53 | Kithulgala (Kelani Ganga) | 2.21 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-10-18 21:02:59 | Wellawaya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-18 21:02:51 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-10-18 21:12:15 | Moragaswewa (Deduru Oya) | 2.65 | 🟢 Normal | 0.000 |  |
| 2026-10-18 21:09:11 | Pitabeddara (Nilwala Ganga) | 2.40 | 🟢 Normal | 0.000 |  |
| 2026-10-18 21:00:10 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-10-18 21:02:10 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-18 21:05:19 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-18 21:00:12 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-10-18 21:06:45 | Putupaula (Kalu Ganga) | 1.83 | 🟢 Normal | -0.009 |  |
| 2026-10-18 21:04:28 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | -0.009 |  |
| 2026-10-18 20:04:24 | Padiyathalawa (Maduru Oya) | 0.35 | 🟢 Normal | -0.009 |  |
| 2026-10-18 18:05:26 | Galgamuwa (Mee Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-10-18 21:02:16 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-10-18 21:03:05 | Manampitiya (Mahaweli Ganga) | 1.09 | 🟢 Normal | -0.011 |  |
| 2026-10-18 21:06:19 | Magura (Kalu Ganga) | 2.21 | 🟢 Normal | -0.013 |  |
| 2026-10-18 21:02:56 | Thawalama (Gin Ganga) | 2.50 | 🟢 Normal | -0.021 |  |
| 2026-10-18 21:02:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.62 | 🟢 Normal | -0.022 |  |
| 2026-10-18 21:02:31 | Giriulla (Maha Oya) | 1.58 | 🟢 Normal | -0.030 |  |
| 2026-10-18 21:06:04 | Baddegama (Gin Ganga) | 3.03 | 🟢 Normal | -0.030 |  |
| 2026-10-18 18:01:11 | Thanthirimale (Malwathu Oya) | 1.62 | 🟢 Normal | -0.030 |  |
| 2026-10-18 21:05:36 | Badalgama (Maha Oya) | 2.91 | 🟢 Normal | -0.031 |  |
| 2026-10-18 21:01:36 | Ellagawa (Kalu Ganga) | 7.41 | 🟢 Normal | -0.031 |  |
| 2026-10-18 21:03:08 | Urawa (Nilwala Ganga) | 1.44 | 🟢 Normal | -0.043 |  |
| 2026-10-18 21:06:43 | Hanwella (Kelani Ganga) | 3.15 | 🟢 Normal | -0.046 |  |
| 2026-10-18 18:00:10 | Weraganthota (Mahaweli Ganga) | -2.73 | 🟢 Normal | -0.050 |  |
| 2026-10-18 21:04:35 | Dunamale (Aththanagalu Oya) | 2.15 | 🟢 Normal | -0.051 |  |
| 2026-10-18 21:01:35 | Nawalapitiya (Mahaweli Ganga) | 1.44 | 🟢 Normal | -0.075 |  |
| 2026-10-18 21:00:56 | Horowpothana (Yan Oya) | 2.58 | 🟢 Normal | -0.082 |  |
| 2026-10-18 21:01:05 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.093 |  |
| 2026-10-18 21:01:55 | Moraketiya (Walawe Ganga) | 1.82 | 🟢 Normal | -0.113 |  |
| 2026-10-18 21:03:23 | Deraniyagala (Kelani Ganga) | 1.57 | 🟢 Normal | -0.370 |  |
| 2026-10-18 21:02:02 | Yaka Wewa (Ma Oya) | 0.00 | 🟢 Normal | -0.579 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)