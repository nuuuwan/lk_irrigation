# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--14_09:19:07-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **287,509 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Panadugama — Alert; 🟡 Magura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-14 09:19:07 | Panadugama (Nilwala Ganga) | 5.96 | 🟡 Alert | 0.000 |  |
| 2026-10-14 09:11:36 | Thawalama (Gin Ganga) | 2.60 | 🟢 Normal | -0.087 |  |
| 2026-10-14 09:11:29 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-10-14 09:10:22 | Urawa (Nilwala Ganga) | 1.11 | 🟢 Normal | -0.032 |  |
| 2026-10-14 09:09:14 | Magura (Kalu Ganga) | 5.36 | 🟡 Alert | -0.033 |  |
| 2026-10-14 09:08:29 | Glencourse (Kelani Ganga) | 10.95 | 🟢 Normal | -0.067 |  |
| 2026-10-14 09:07:35 | Rathnapura (Kalu Ganga) | 3.94 | 🟢 Normal | -0.067 |  |
| 2026-10-14 09:07:33 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-10-14 09:07:29 | Holombuwa (Kelani Ganga) | 0.88 | 🟢 Normal | -0.020 |  |
| 2026-10-14 09:06:51 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-10-14 09:06:09 | Badalgama (Maha Oya) | 2.93 | 🟢 Normal | -0.021 |  |
| 2026-10-14 09:05:45 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-14 09:05:33 | Thanamalwila (Kirindi Oya) | 0.93 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-10-14 09:05:24 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.090 |  |
| 2026-10-14 09:05:19 | Panadugama (Nilwala Ganga) | 5.96 | 🟡 Alert | 0.000 |  |
| 2026-10-14 09:05:16 | Pitabeddara (Nilwala Ganga) | 2.10 | 🟢 Normal | -0.092 |  |
| 2026-10-14 09:04:52 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-10-14 09:04:29 | Wellawaya (Kirindi Oya) | 0.99 | 🟢 Normal | -0.029 |  |
| 2026-10-14 09:04:29 | Baddegama (Gin Ganga) | 2.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-14 09:04:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.34 | 🟡 Alert | 0.195 | 🔺 Rising |
| 2026-10-14 09:04:08 | Moraketiya (Walawe Ganga) | 1.32 | 🟢 Normal | -0.019 |  |
| 2026-10-14 09:03:25 | Moragaswewa (Deduru Oya) | 0.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-14 09:03:19 | Putupaula (Kalu Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-10-14 09:03:11 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-14 09:03:10 | Nawalapitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-10-14 09:03:04 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-14 09:03:00 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-10-14 09:02:54 | Hanwella (Kelani Ganga) | 3.13 | 🟢 Normal | -0.020 |  |
| 2026-10-14 09:02:51 | Giriulla (Maha Oya) | 1.56 | 🟢 Normal | -0.030 |  |
| 2026-10-14 09:02:49 | Peradeniya (Mahaweli Ganga) | 3.00 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-14 09:02:44 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | -0.010 |  |
| 2026-10-14 09:02:36 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | -0.052 |  |
| 2026-10-14 09:02:34 | Dunamale (Aththanagalu Oya) | 2.35 | 🟢 Normal | -0.010 |  |
| 2026-10-14 09:02:16 | Thanthirimale (Malwathu Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-10-14 09:02:16 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -0.040 |  |
| 2026-10-14 09:02:12 | Ellagawa (Kalu Ganga) | 7.76 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-14 09:02:02 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-14 09:01:36 | Thalgahagoda (Nilwala Ganga) | 1.73 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-14 09:01:26 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-10-14 09:01:17 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-14 09:01:36 | Thalgahagoda (Nilwala Ganga) | 1.73 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-14 09:04:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.34 | 🟡 Alert | 0.195 | 🔺 Rising |
| 2026-10-14 09:19:07 | Panadugama (Nilwala Ganga) | 5.96 | 🟡 Alert | 0.000 |  |
| 2026-10-14 09:09:14 | Magura (Kalu Ganga) | 5.36 | 🟡 Alert | -0.033 |  |
| 2026-10-14 09:05:33 | Thanamalwila (Kirindi Oya) | 0.93 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-10-14 09:03:11 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-14 09:02:12 | Ellagawa (Kalu Ganga) | 7.76 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-14 09:02:49 | Peradeniya (Mahaweli Ganga) | 3.00 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-14 09:04:29 | Baddegama (Gin Ganga) | 2.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-14 09:03:25 | Moragaswewa (Deduru Oya) | 0.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-14 09:03:00 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-10-14 09:03:10 | Nawalapitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-10-14 09:02:02 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-14 08:01:01 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-10-14 09:06:51 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-10-14 09:07:33 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-10-14 09:05:45 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-14 09:03:04 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-14 09:03:19 | Putupaula (Kalu Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-10-14 09:02:16 | Thanthirimale (Malwathu Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-10-14 09:11:29 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-10-14 09:04:52 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-10-14 09:01:26 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-10-14 09:02:34 | Dunamale (Aththanagalu Oya) | 2.35 | 🟢 Normal | -0.010 |  |
| 2026-10-14 09:02:44 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | -0.010 |  |
| 2026-10-14 09:04:08 | Moraketiya (Walawe Ganga) | 1.32 | 🟢 Normal | -0.019 |  |
| 2026-10-14 09:02:54 | Hanwella (Kelani Ganga) | 3.13 | 🟢 Normal | -0.020 |  |
| 2026-10-14 09:07:29 | Holombuwa (Kelani Ganga) | 0.88 | 🟢 Normal | -0.020 |  |
| 2026-10-14 09:06:09 | Badalgama (Maha Oya) | 2.93 | 🟢 Normal | -0.021 |  |
| 2026-10-14 09:04:29 | Wellawaya (Kirindi Oya) | 0.99 | 🟢 Normal | -0.029 |  |
| 2026-10-14 09:02:51 | Giriulla (Maha Oya) | 1.56 | 🟢 Normal | -0.030 |  |
| 2026-10-14 09:10:22 | Urawa (Nilwala Ganga) | 1.11 | 🟢 Normal | -0.032 |  |
| 2026-10-14 09:02:16 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -0.040 |  |
| 2026-10-14 09:02:36 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | -0.052 |  |
| 2026-10-14 09:07:35 | Rathnapura (Kalu Ganga) | 3.94 | 🟢 Normal | -0.067 |  |
| 2026-10-14 09:08:29 | Glencourse (Kelani Ganga) | 10.95 | 🟢 Normal | -0.067 |  |
| 2026-10-14 09:11:36 | Thawalama (Gin Ganga) | 2.60 | 🟢 Normal | -0.087 |  |
| 2026-10-14 09:05:24 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.090 |  |
| 2026-10-14 09:05:16 | Pitabeddara (Nilwala Ganga) | 2.10 | 🟢 Normal | -0.092 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)