# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--18_06:38:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **291,017 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Panadugama — Minor Flood; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-18 06:38:12 | Galgamuwa (Mee Oya) | 0.70 | 🟢 Normal | -0.091 |  |
| 2026-10-18 06:09:21 | Hanwella (Kelani Ganga) | 4.46 | 🟢 Normal | -0.054 |  |
| 2026-10-18 06:09:12 | Badalgama (Maha Oya) | 3.65 | 🟢 Normal | 0.000 |  |
| 2026-10-18 06:09:06 | Urawa (Nilwala Ganga) | 1.57 | 🟢 Normal | -0.020 |  |
| 2026-10-18 06:09:03 | Padiyathalawa (Maduru Oya) | 1.00 | 🟢 Normal | -0.221 |  |
| 2026-10-18 06:08:36 | Kithulgala (Kelani Ganga) | 2.19 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-10-18 06:08:22 | Holombuwa (Kelani Ganga) | 1.34 | 🟢 Normal | -0.058 |  |
| 2026-10-18 06:07:55 | Thalgahagoda (Nilwala Ganga) | 2.03 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-18 06:07:01 | Moraketiya (Walawe Ganga) | 1.35 | 🟢 Normal | -0.061 |  |
| 2026-10-18 06:06:48 | Peradeniya (Mahaweli Ganga) | 3.42 | 🟢 Normal | -0.057 |  |
| 2026-10-18 06:06:17 | Pitabeddara (Nilwala Ganga) | 2.50 | 🟢 Normal | -0.286 |  |
| 2026-10-18 06:06:02 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-10-18 06:05:48 | Dunamale (Aththanagalu Oya) | 2.46 | 🟢 Normal | -0.041 |  |
| 2026-10-18 06:05:45 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | -0.059 |  |
| 2026-10-18 06:05:24 | Magura (Kalu Ganga) | 2.38 | 🟢 Normal | -36.000 |  |
| 2026-10-18 06:05:22 | Magura (Kalu Ganga) | 2.40 | 🟢 Normal | -36.000 |  |
| 2026-10-18 06:05:07 | Rathnapura (Kalu Ganga) | 4.35 | 🟢 Normal | -0.171 |  |
| 2026-10-18 06:05:05 | Giriulla (Maha Oya) | 2.45 | 🟢 Normal | -0.163 |  |
| 2026-10-18 06:04:50 | Thawalama (Gin Ganga) | 3.65 | 🟢 Normal | -0.194 |  |
| 2026-10-18 06:04:41 | Thaldena (Mahaweli Ganga) | 0.63 | 🟢 Normal | -0.038 |  |
| 2026-10-18 06:04:36 | Glencourse (Kelani Ganga) | 12.14 | 🟢 Normal | -0.196 |  |
| 2026-10-18 06:04:13 | Baddegama (Gin Ganga) | 3.12 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-18 06:03:56 | Deraniyagala (Kelani Ganga) | 0.97 | 🟢 Normal | -0.050 |  |
| 2026-10-18 06:03:30 | Thanamalwila (Kirindi Oya) | 1.28 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-18 06:03:29 | Putupaula (Kalu Ganga) | 2.00 | 🟢 Normal | -0.010 |  |
| 2026-10-18 06:03:27 | Moragaswewa (Deduru Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-10-18 06:03:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.32 | 🟡 Alert | -0.253 |  |
| 2026-10-18 06:02:57 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | -0.010 |  |
| 2026-10-18 06:02:56 | Norwood (Kelani Ganga) | 1.35 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-18 06:02:44 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-10-18 06:02:40 | Manampitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | -0.029 |  |
| 2026-10-18 06:02:36 | Panadugama (Nilwala Ganga) | 6.08 | 🟠 Minor Flood | -0.061 |  |
| 2026-10-18 06:02:36 | Badalgama (Maha Oya) | 3.65 | 🟢 Normal | 0.000 |  |
| 2026-10-18 06:01:33 | Horowpothana (Yan Oya) | 2.99 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-18 06:01:23 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-10-18 06:01:14 | Weraganthota (Mahaweli Ganga) | -2.22 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-10-18 06:00:57 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-10-18 06:00:35 | Wellawaya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-10-18 06:00:27 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-10-18 05:58:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.34 | 🟡 Alert | -0.253 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-18 06:07:55 | Thalgahagoda (Nilwala Ganga) | 2.03 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-18 06:02:36 | Panadugama (Nilwala Ganga) | 6.08 | 🟠 Minor Flood | -0.061 |  |
| 2026-10-18 06:03:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.32 | 🟡 Alert | -0.253 |  |
| 2026-10-18 06:01:14 | Weraganthota (Mahaweli Ganga) | -2.22 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-10-18 05:05:47 | Ellagawa (Kalu Ganga) | 7.66 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-10-18 06:03:30 | Thanamalwila (Kirindi Oya) | 1.28 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-18 06:01:33 | Horowpothana (Yan Oya) | 2.99 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-18 06:02:56 | Norwood (Kelani Ganga) | 1.35 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-18 06:04:13 | Baddegama (Gin Ganga) | 3.12 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-18 06:08:36 | Kithulgala (Kelani Ganga) | 2.19 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-10-18 06:00:35 | Wellawaya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-10-18 06:00:57 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-10-18 06:02:44 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-10-18 06:00:27 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-10-18 06:09:12 | Badalgama (Maha Oya) | 3.65 | 🟢 Normal | 0.000 |  |
| 2026-10-18 06:06:02 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-10-18 06:03:27 | Moragaswewa (Deduru Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-10-18 06:03:29 | Putupaula (Kalu Ganga) | 2.00 | 🟢 Normal | -0.010 |  |
| 2026-10-18 06:01:23 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-10-18 06:02:57 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | -0.010 |  |
| 2026-10-18 06:09:06 | Urawa (Nilwala Ganga) | 1.57 | 🟢 Normal | -0.020 |  |
| 2026-10-18 06:02:40 | Manampitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | -0.029 |  |
| 2026-10-18 06:04:41 | Thaldena (Mahaweli Ganga) | 0.63 | 🟢 Normal | -0.038 |  |
| 2026-10-17 18:01:56 | Thanthirimale (Malwathu Oya) | 2.41 | 🟢 Normal | -0.040 |  |
| 2026-10-18 06:05:48 | Dunamale (Aththanagalu Oya) | 2.46 | 🟢 Normal | -0.041 |  |
| 2026-10-18 06:03:56 | Deraniyagala (Kelani Ganga) | 0.97 | 🟢 Normal | -0.050 |  |
| 2026-10-18 06:09:21 | Hanwella (Kelani Ganga) | 4.46 | 🟢 Normal | -0.054 |  |
| 2026-10-18 06:06:48 | Peradeniya (Mahaweli Ganga) | 3.42 | 🟢 Normal | -0.057 |  |
| 2026-10-18 06:08:22 | Holombuwa (Kelani Ganga) | 1.34 | 🟢 Normal | -0.058 |  |
| 2026-10-18 06:05:45 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | -0.059 |  |
| 2026-10-18 06:07:01 | Moraketiya (Walawe Ganga) | 1.35 | 🟢 Normal | -0.061 |  |
| 2026-10-18 06:38:12 | Galgamuwa (Mee Oya) | 0.70 | 🟢 Normal | -0.091 |  |
| 2026-10-18 06:05:05 | Giriulla (Maha Oya) | 2.45 | 🟢 Normal | -0.163 |  |
| 2026-10-18 06:05:07 | Rathnapura (Kalu Ganga) | 4.35 | 🟢 Normal | -0.171 |  |
| 2026-10-18 06:04:50 | Thawalama (Gin Ganga) | 3.65 | 🟢 Normal | -0.194 |  |
| 2026-10-18 06:04:36 | Glencourse (Kelani Ganga) | 12.14 | 🟢 Normal | -0.196 |  |
| 2026-10-18 06:09:03 | Padiyathalawa (Maduru Oya) | 1.00 | 🟢 Normal | -0.221 |  |
| 2026-10-18 06:06:17 | Pitabeddara (Nilwala Ganga) | 2.50 | 🟢 Normal | -0.286 |  |
| 2026-10-18 06:05:24 | Magura (Kalu Ganga) | 2.38 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)