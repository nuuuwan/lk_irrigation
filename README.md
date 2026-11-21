# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--21_22:22:17-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **322,179 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-21 22:22:17 | Urawa (Nilwala Ganga) | 1.26 | 🟢 Normal | -0.016 |  |
| 2026-11-21 22:11:44 | Thaldena (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-11-21 22:11:14 | Giriulla (Maha Oya) | 2.31 | 🟢 Normal | -0.129 |  |
| 2026-11-21 22:09:49 | Thawalama (Gin Ganga) | 1.87 | 🟢 Normal | -0.009 |  |
| 2026-11-21 22:09:42 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | -41.844 |  |
| 2026-11-21 22:09:34 | Thanamalwila (Kirindi Oya) | 1.76 | 🟢 Normal | -0.020 |  |
| 2026-11-21 22:07:08 | Nawalapitiya (Mahaweli Ganga) | 3.00 | 🟢 Normal | -41.844 |  |
| 2026-11-21 22:06:22 | Dunamale (Aththanagalu Oya) | 1.48 | 🟢 Normal | -0.040 |  |
| 2026-11-21 22:05:48 | Norwood (Kelani Ganga) | 0.95 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-11-21 22:05:30 | Rathnapura (Kalu Ganga) | 1.83 | 🟢 Normal | -0.039 |  |
| 2026-11-21 22:05:28 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-11-21 22:05:19 | Hanwella (Kelani Ganga) | 1.57 | 🟢 Normal | -0.069 |  |
| 2026-11-21 22:05:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.44 | 🟢 Normal | -0.019 |  |
| 2026-11-21 22:04:49 | Badalgama (Maha Oya) | 2.79 | 🟢 Normal | -1.100 |  |
| 2026-11-21 22:04:22 | Baddegama (Gin Ganga) | 1.74 | 🟢 Normal | -0.029 |  |
| 2026-11-21 22:03:49 | Glencourse (Kelani Ganga) | 9.42 | 🟢 Normal | -0.059 |  |
| 2026-11-21 22:03:44 | Moraketiya (Walawe Ganga) | 2.97 | 🟢 Normal | 0.000 |  |
| 2026-11-21 22:03:02 | Ellagawa (Kalu Ganga) | 5.77 | 🟢 Normal | -0.097 |  |
| 2026-11-21 22:03:01 | Panadugama (Nilwala Ganga) | 4.53 | 🟢 Normal | -0.043 |  |
| 2026-11-21 22:02:55 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-11-21 22:02:39 | Moragaswewa (Deduru Oya) | 0.47 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-11-21 22:02:28 | Kuda Oya (Kirindi Oya) | 2.12 | 🟢 Normal | -0.029 |  |
| 2026-11-21 22:02:27 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-11-21 22:02:19 | Holombuwa (Kelani Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-11-21 22:02:16 | Putupaula (Kalu Ganga) | 0.84 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-11-21 22:02:09 | Deraniyagala (Kelani Ganga) | 0.51 | 🟢 Normal | -0.050 |  |
| 2026-11-21 22:01:33 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-21 22:01:30 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-11-21 22:01:19 | Manampitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-11-21 22:01:07 | Horowpothana (Yan Oya) | 1.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-21 22:01:05 | Magura (Kalu Ganga) | 1.70 | 🟢 Normal | -0.052 |  |
| 2026-11-21 22:00:20 | Wellawaya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.020 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-21 22:05:28 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-11-21 22:02:39 | Moragaswewa (Deduru Oya) | 0.47 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-11-21 22:11:44 | Thaldena (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-11-21 22:05:48 | Norwood (Kelani Ganga) | 0.95 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-11-21 21:05:24 | Peradeniya (Mahaweli Ganga) | 2.97 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-11-21 22:02:16 | Putupaula (Kalu Ganga) | 0.84 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-11-21 22:00:20 | Wellawaya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-21 22:01:07 | Horowpothana (Yan Oya) | 1.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-21 22:02:27 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-11-21 18:00:46 | Weraganthota (Mahaweli Ganga) | -2.40 | 🟢 Normal | 0.000 |  |
| 2026-11-21 22:01:30 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-11-21 22:01:33 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-21 18:00:19 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-11-21 21:05:52 | Pitabeddara (Nilwala Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-11-19 14:01:52⌛ | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-11-21 22:03:44 | Moraketiya (Walawe Ganga) | 2.97 | 🟢 Normal | 0.000 |  |
| 2026-11-21 21:02:01 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-21 22:02:55 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-11-21 18:02:22 | Thanthirimale (Malwathu Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-21 21:05:52 | Thalgahagoda (Nilwala Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-11-21 22:09:49 | Thawalama (Gin Ganga) | 1.87 | 🟢 Normal | -0.009 |  |
| 2026-11-21 22:02:19 | Holombuwa (Kelani Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-11-21 22:01:19 | Manampitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-11-21 22:22:17 | Urawa (Nilwala Ganga) | 1.26 | 🟢 Normal | -0.016 |  |
| 2026-11-21 22:05:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.44 | 🟢 Normal | -0.019 |  |
| 2026-11-21 22:09:34 | Thanamalwila (Kirindi Oya) | 1.76 | 🟢 Normal | -0.020 |  |
| 2026-11-21 22:04:22 | Baddegama (Gin Ganga) | 1.74 | 🟢 Normal | -0.029 |  |
| 2026-11-21 22:02:28 | Kuda Oya (Kirindi Oya) | 2.12 | 🟢 Normal | -0.029 |  |
| 2026-11-21 22:05:30 | Rathnapura (Kalu Ganga) | 1.83 | 🟢 Normal | -0.039 |  |
| 2026-11-21 22:06:22 | Dunamale (Aththanagalu Oya) | 1.48 | 🟢 Normal | -0.040 |  |
| 2026-11-21 22:03:01 | Panadugama (Nilwala Ganga) | 4.53 | 🟢 Normal | -0.043 |  |
| 2026-11-21 22:02:09 | Deraniyagala (Kelani Ganga) | 0.51 | 🟢 Normal | -0.050 |  |
| 2026-11-21 22:01:05 | Magura (Kalu Ganga) | 1.70 | 🟢 Normal | -0.052 |  |
| 2026-11-21 22:03:49 | Glencourse (Kelani Ganga) | 9.42 | 🟢 Normal | -0.059 |  |
| 2026-11-21 22:05:19 | Hanwella (Kelani Ganga) | 1.57 | 🟢 Normal | -0.069 |  |
| 2026-11-21 22:03:02 | Ellagawa (Kalu Ganga) | 5.77 | 🟢 Normal | -0.097 |  |
| 2026-11-21 22:11:14 | Giriulla (Maha Oya) | 2.31 | 🟢 Normal | -0.129 |  |
| 2026-11-21 22:04:49 | Badalgama (Maha Oya) | 2.79 | 🟢 Normal | -1.100 |  |
| 2026-11-21 22:09:42 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | -41.844 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

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

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)