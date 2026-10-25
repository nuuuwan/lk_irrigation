# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--26_03:04:31-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **298,071 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Norwood — Alert; 🟡 Rathnapura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **22** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-26 03:04:31 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-10-26 03:04:25 | Kithulgala (Kelani Ganga) | 2.22 | 🟢 Normal | 0.175 | 🔺 Rising |
| 2026-10-26 03:04:01 | Giriulla (Maha Oya) | 3.17 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2026-10-26 03:03:53 | Panadugama (Nilwala Ganga) | 4.74 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-10-26 03:03:39 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-26 03:03:33 | Pitabeddara (Nilwala Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-10-26 03:03:23 | Nakkala (Kumbukkan Oya) | 1.23 | 🟢 Normal | -0.058 |  |
| 2026-10-26 03:03:22 | Glencourse (Kelani Ganga) | 12.47 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-10-26 03:02:45 | Nawalapitiya (Mahaweli Ganga) | 1.91 | 🟢 Normal | -0.071 |  |
| 2026-10-26 03:02:42 | Horowpothana (Yan Oya) | 2.33 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-26 03:02:29 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-26 03:02:23 | Thalgahagoda (Nilwala Ganga) | 1.10 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-26 03:02:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.65 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-26 03:02:17 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-10-26 03:01:56 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-26 03:01:40 | Dunamale (Aththanagalu Oya) | 3.10 | 🟢 Normal | 0.000 |  |
| 2026-10-26 03:01:05 | Moragaswewa (Deduru Oya) | 2.78 | 🟢 Normal | 0.308 | 🔺 Rising |
| 2026-10-26 03:01:04 | Moraketiya (Walawe Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-10-26 02:58:19 | Baddegama (Gin Ganga) | 2.46 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-10-26 02:40:28 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | 0.175 | 🔺 Rising |
| 2026-10-26 02:36:08 | Thanamalwila (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-10-26 02:29:50 | Holombuwa (Kelani Ganga) | 1.60 | 🟢 Normal | -0.115 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-26 01:49:40 | Norwood (Kelani Ganga) | 1.57 | 🟡 Alert | -0.023 |  |
| 2026-10-26 02:07:05 | Rathnapura (Kalu Ganga) | 6.05 | 🟡 Alert | -0.068 |  |
| 2026-10-26 03:01:05 | Moragaswewa (Deduru Oya) | 2.78 | 🟢 Normal | 0.308 | 🔺 Rising |
| 2026-10-26 03:04:25 | Kithulgala (Kelani Ganga) | 2.22 | 🟢 Normal | 0.175 | 🔺 Rising |
| 2026-10-26 02:01:41 | Magura (Kalu Ganga) | 3.80 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-10-26 02:08:33 | Hanwella (Kelani Ganga) | 3.81 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-10-26 03:04:01 | Giriulla (Maha Oya) | 3.17 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2026-10-25 18:03:46 | Galgamuwa (Mee Oya) | 1.82 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-10-26 02:01:17 | Ellagawa (Kalu Ganga) | 7.95 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-10-26 02:05:36 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-10-26 02:09:45 | Badalgama (Maha Oya) | 3.62 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-10-26 03:03:22 | Glencourse (Kelani Ganga) | 12.47 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-10-26 03:02:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.65 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-26 03:03:53 | Panadugama (Nilwala Ganga) | 4.74 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-10-26 02:58:19 | Baddegama (Gin Ganga) | 2.46 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-10-26 03:02:23 | Thalgahagoda (Nilwala Ganga) | 1.10 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-26 03:01:56 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-26 02:01:15 | Peradeniya (Mahaweli Ganga) | 3.64 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-26 02:02:01 | Thawalama (Gin Ganga) | 3.25 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-26 01:05:48 | Putupaula (Kalu Ganga) | 1.64 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-26 03:03:39 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-26 03:02:42 | Horowpothana (Yan Oya) | 2.33 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-26 03:02:29 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-26 00:03:51 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-10-26 03:03:33 | Pitabeddara (Nilwala Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-10-26 03:01:04 | Moraketiya (Walawe Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-10-26 03:04:31 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-10-26 03:01:40 | Dunamale (Aththanagalu Oya) | 3.10 | 🟢 Normal | 0.000 |  |
| 2026-10-26 02:01:28 | Manampitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-10-25 18:02:16 | Thanthirimale (Malwathu Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-10-26 01:03:29 | Urawa (Nilwala Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-10-26 02:36:08 | Thanamalwila (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-10-26 00:08:55 | Padiyathalawa (Maduru Oya) | 0.26 | 🟢 Normal | -0.009 |  |
| 2026-10-26 03:02:17 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-10-26 03:03:23 | Nakkala (Kumbukkan Oya) | 1.23 | 🟢 Normal | -0.058 |  |
| 2026-10-25 18:03:32 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | -0.069 |  |
| 2026-10-26 03:02:45 | Nawalapitiya (Mahaweli Ganga) | 1.91 | 🟢 Normal | -0.071 |  |
| 2026-10-26 02:29:50 | Holombuwa (Kelani Ganga) | 1.60 | 🟢 Normal | -0.115 |  |
| 2026-10-26 02:05:08 | Deraniyagala (Kelani Ganga) | 1.57 | 🟢 Normal | -0.208 |  |

## River Water Level Charts by Station

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)