# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--11_21:11:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **285,282 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-11 21:11:12 | Deraniyagala (Kelani Ganga) | 1.13 | 🟢 Normal | -0.223 |  |
| 2026-10-11 21:09:39 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-11 21:09:22 | Thawalama (Gin Ganga) | 3.50 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-10-11 21:08:58 | Norwood (Kelani Ganga) | 1.19 | 🟢 Normal | -0.124 |  |
| 2026-10-11 21:08:40 | Baddegama (Gin Ganga) | 2.12 | 🟢 Normal | -0.020 |  |
| 2026-10-11 21:07:27 | Katharagama (Menik Ganga) | 0.03 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-10-11 21:06:40 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.088 |  |
| 2026-10-11 21:06:20 | Putupaula (Kalu Ganga) | 1.21 | 🟢 Normal | -0.040 |  |
| 2026-10-11 21:05:55 | Magura (Kalu Ganga) | 2.91 | 🟢 Normal | 0.271 | 🔺 Rising |
| 2026-10-11 21:05:33 | Holombuwa (Kelani Ganga) | 2.09 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-10-11 21:05:21 | Nakkala (Kumbukkan Oya) | 0.96 | 🟢 Normal | -0.009 |  |
| 2026-10-11 21:04:57 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.185 | 🔺 Rising |
| 2026-10-11 21:04:07 | Urawa (Nilwala Ganga) | 1.26 | 🟢 Normal | 0.271 | 🔺 Rising |
| 2026-10-11 21:04:07 | Hanwella (Kelani Ganga) | 2.87 | 🟢 Normal | 0.160 | 🔺 Rising |
| 2026-10-11 21:03:58 | Ellagawa (Kalu Ganga) | 7.04 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-11 21:03:56 | Panadugama (Nilwala Ganga) | 4.48 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-10-11 21:03:54 | Kithulgala (Kelani Ganga) | 2.00 | 🟢 Normal | -0.149 |  |
| 2026-10-11 21:03:50 | Thalgahagoda (Nilwala Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-10-11 21:03:40 | Giriulla (Maha Oya) | 2.16 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-10-11 21:03:31 | Badalgama (Maha Oya) | 3.31 | 🟢 Normal | -0.043 |  |
| 2026-10-11 21:03:11 | Pitabeddara (Nilwala Ganga) | 1.86 | 🟢 Normal | 0.184 | 🔺 Rising |
| 2026-10-11 21:03:02 | Rathnapura (Kalu Ganga) | 2.38 | 🟢 Normal | 0.232 | 🔺 Rising |
| 2026-10-11 21:02:43 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | -0.020 |  |
| 2026-10-11 21:02:33 | Moragaswewa (Deduru Oya) | 1.91 | 🟢 Normal | -0.089 |  |
| 2026-10-11 21:02:18 | Glencourse (Kelani Ganga) | 11.82 | 🟢 Normal | 0.345 | 🔺 Rising |
| 2026-10-11 21:02:16 | Thanamalwila (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-10-11 21:02:13 | Wellawaya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-11 21:01:54 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-11 21:01:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.24 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-10-11 21:01:41 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-11 21:01:26 | Nawalapitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-11 21:01:25 | Dunamale (Aththanagalu Oya) | 2.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-11 21:01:13 | Moraketiya (Walawe Ganga) | 1.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-11 21:01:03 | Peradeniya (Mahaweli Ganga) | 2.68 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-11 21:00:40 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-10-11 21:00:11 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-11 21:02:18 | Glencourse (Kelani Ganga) | 11.82 | 🟢 Normal | 0.345 | 🔺 Rising |
| 2026-10-11 21:04:07 | Urawa (Nilwala Ganga) | 1.26 | 🟢 Normal | 0.271 | 🔺 Rising |
| 2026-10-11 21:05:55 | Magura (Kalu Ganga) | 2.91 | 🟢 Normal | 0.271 | 🔺 Rising |
| 2026-10-11 21:03:02 | Rathnapura (Kalu Ganga) | 2.38 | 🟢 Normal | 0.232 | 🔺 Rising |
| 2026-10-11 21:04:57 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.185 | 🔺 Rising |
| 2026-10-11 21:03:11 | Pitabeddara (Nilwala Ganga) | 1.86 | 🟢 Normal | 0.184 | 🔺 Rising |
| 2026-10-11 21:04:07 | Hanwella (Kelani Ganga) | 2.87 | 🟢 Normal | 0.160 | 🔺 Rising |
| 2026-10-11 21:03:56 | Panadugama (Nilwala Ganga) | 4.48 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-10-11 21:09:22 | Thawalama (Gin Ganga) | 3.50 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-10-11 21:01:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.24 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-10-11 21:03:40 | Giriulla (Maha Oya) | 2.16 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-10-11 21:05:33 | Holombuwa (Kelani Ganga) | 2.09 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-10-11 21:07:27 | Katharagama (Menik Ganga) | 0.03 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-10-11 21:01:41 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-11 21:01:26 | Nawalapitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-11 21:01:03 | Peradeniya (Mahaweli Ganga) | 2.68 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-11 21:03:58 | Ellagawa (Kalu Ganga) | 7.04 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-11 21:02:13 | Wellawaya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-11 21:01:13 | Moraketiya (Walawe Ganga) | 1.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-11 18:00:16 | Thanthirimale (Malwathu Oya) | 1.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-11 21:01:25 | Dunamale (Aththanagalu Oya) | 2.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-11 21:01:54 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-11 21:09:39 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-11 18:06:55 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-10-11 21:00:11 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-10-11 21:03:50 | Thalgahagoda (Nilwala Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-10-11 21:02:16 | Thanamalwila (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-10-11 21:05:21 | Nakkala (Kumbukkan Oya) | 0.96 | 🟢 Normal | -0.009 |  |
| 2026-10-11 18:02:15 | Weraganthota (Mahaweli Ganga) | -3.17 | 🟢 Normal | -0.010 |  |
| 2026-10-11 21:00:40 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-10-11 21:08:40 | Baddegama (Gin Ganga) | 2.12 | 🟢 Normal | -0.020 |  |
| 2026-10-11 21:02:43 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | -0.020 |  |
| 2026-10-11 21:06:20 | Putupaula (Kalu Ganga) | 1.21 | 🟢 Normal | -0.040 |  |
| 2026-10-11 21:03:31 | Badalgama (Maha Oya) | 3.31 | 🟢 Normal | -0.043 |  |
| 2026-10-11 21:06:40 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.088 |  |
| 2026-10-11 21:02:33 | Moragaswewa (Deduru Oya) | 1.91 | 🟢 Normal | -0.089 |  |
| 2026-10-11 21:08:58 | Norwood (Kelani Ganga) | 1.19 | 🟢 Normal | -0.124 |  |
| 2026-10-11 21:03:54 | Kithulgala (Kelani Ganga) | 2.00 | 🟢 Normal | -0.149 |  |
| 2026-10-11 21:11:12 | Deraniyagala (Kelani Ganga) | 1.13 | 🟢 Normal | -0.223 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)