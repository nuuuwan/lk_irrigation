# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--12_13:16:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **285,878 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-12 13:16:30 | Moraketiya (Walawe Ganga) | 1.05 | 🟢 Normal | -0.040 |  |
| 2026-10-12 13:11:04 | Peradeniya (Mahaweli Ganga) | 2.40 | 🟢 Normal | -0.095 |  |
| 2026-10-12 13:10:02 | Deraniyagala (Kelani Ganga) | 0.68 | 🟢 Normal | -0.009 |  |
| 2026-10-12 13:09:08 | Rathnapura (Kalu Ganga) | 2.50 | 🟢 Normal | -0.180 |  |
| 2026-10-12 13:08:41 | Putupaula (Kalu Ganga) | 1.70 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-12 13:08:39 | Magura (Kalu Ganga) | 2.44 | 🟢 Normal | -0.051 |  |
| 2026-10-12 13:08:35 | Glencourse (Kelani Ganga) | 11.11 | 🟢 Normal | -0.029 |  |
| 2026-10-12 13:07:36 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-12 13:07:36 | Baddegama (Gin Ganga) | 2.64 | 🟢 Normal | -0.020 |  |
| 2026-10-12 13:06:53 | Badalgama (Maha Oya) | 3.47 | 🟢 Normal | -0.059 |  |
| 2026-10-12 13:06:36 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | -0.009 |  |
| 2026-10-12 13:05:12 | Urawa (Nilwala Ganga) | 0.94 | 🟢 Normal | -0.040 |  |
| 2026-10-12 13:05:09 | Panadugama (Nilwala Ganga) | 4.60 | 🟢 Normal | -0.010 |  |
| 2026-10-12 13:04:50 | Holombuwa (Kelani Ganga) | 1.01 | 🟢 Normal | -0.009 |  |
| 2026-10-12 13:04:00 | Dunamale (Aththanagalu Oya) | 2.70 | 🟢 Normal | -0.048 |  |
| 2026-10-12 13:03:52 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | -0.020 |  |
| 2026-10-12 13:03:29 | Weraganthota (Mahaweli Ganga) | -3.21 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-12 13:03:28 | Pitabeddara (Nilwala Ganga) | 1.44 | 🟢 Normal | -0.050 |  |
| 2026-10-12 13:03:09 | Moragaswewa (Deduru Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-12 13:02:51 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-10-12 13:02:48 | Hanwella (Kelani Ganga) | 3.38 | 🟢 Normal | -0.070 |  |
| 2026-10-12 13:02:37 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-12 13:02:34 | Ellagawa (Kalu Ganga) | 7.18 | 🟢 Normal | -0.051 |  |
| 2026-10-12 13:02:33 | Thalgahagoda (Nilwala Ganga) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-10-12 13:02:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.08 | 🟡 Alert | -0.020 |  |
| 2026-10-12 13:02:21 | Giriulla (Maha Oya) | 2.11 | 🟢 Normal | -0.060 |  |
| 2026-10-12 13:02:16 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-10-12 13:02:13 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | -0.020 |  |
| 2026-10-12 13:02:12 | Thanamalwila (Kirindi Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-10-12 13:02:07 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-10-12 13:01:56 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-10-12 13:01:51 | Thanthirimale (Malwathu Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-10-12 13:01:51 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-10-12 13:01:45 | Thawalama (Gin Ganga) | 2.27 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-10-12 13:01:26 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.129 |  |
| 2026-10-12 13:00:45 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-12 13:00:44 | Nakkala (Kumbukkan Oya) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-10-12 13:00:38 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-12 13:02:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.08 | 🟡 Alert | -0.020 |  |
| 2026-10-12 13:01:56 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-10-12 13:01:45 | Thawalama (Gin Ganga) | 2.27 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-10-12 13:02:37 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-12 13:03:29 | Weraganthota (Mahaweli Ganga) | -3.21 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-12 13:08:41 | Putupaula (Kalu Ganga) | 1.70 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-12 13:02:16 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-10-12 13:03:09 | Moragaswewa (Deduru Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-12 13:02:07 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-10-12 13:07:36 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-12 13:00:45 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-12 13:02:51 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-10-12 13:01:51 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-10-12 12:04:17 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-10-12 13:01:51 | Thanthirimale (Malwathu Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-10-12 13:10:02 | Deraniyagala (Kelani Ganga) | 0.68 | 🟢 Normal | -0.009 |  |
| 2026-10-12 13:06:36 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | -0.009 |  |
| 2026-10-12 13:04:50 | Holombuwa (Kelani Ganga) | 1.01 | 🟢 Normal | -0.009 |  |
| 2026-10-12 13:05:09 | Panadugama (Nilwala Ganga) | 4.60 | 🟢 Normal | -0.010 |  |
| 2026-10-12 13:02:12 | Thanamalwila (Kirindi Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-10-12 13:00:44 | Nakkala (Kumbukkan Oya) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-10-12 13:02:33 | Thalgahagoda (Nilwala Ganga) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-10-12 13:07:36 | Baddegama (Gin Ganga) | 2.64 | 🟢 Normal | -0.020 |  |
| 2026-10-12 13:03:52 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | -0.020 |  |
| 2026-10-12 13:00:38 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | -0.020 |  |
| 2026-10-12 13:02:13 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | -0.020 |  |
| 2026-10-12 13:08:35 | Glencourse (Kelani Ganga) | 11.11 | 🟢 Normal | -0.029 |  |
| 2026-10-12 13:05:12 | Urawa (Nilwala Ganga) | 0.94 | 🟢 Normal | -0.040 |  |
| 2026-10-12 13:16:30 | Moraketiya (Walawe Ganga) | 1.05 | 🟢 Normal | -0.040 |  |
| 2026-10-12 13:04:00 | Dunamale (Aththanagalu Oya) | 2.70 | 🟢 Normal | -0.048 |  |
| 2026-10-12 13:03:28 | Pitabeddara (Nilwala Ganga) | 1.44 | 🟢 Normal | -0.050 |  |
| 2026-10-12 13:08:39 | Magura (Kalu Ganga) | 2.44 | 🟢 Normal | -0.051 |  |
| 2026-10-12 13:02:34 | Ellagawa (Kalu Ganga) | 7.18 | 🟢 Normal | -0.051 |  |
| 2026-10-12 13:06:53 | Badalgama (Maha Oya) | 3.47 | 🟢 Normal | -0.059 |  |
| 2026-10-12 13:02:21 | Giriulla (Maha Oya) | 2.11 | 🟢 Normal | -0.060 |  |
| 2026-10-12 13:02:48 | Hanwella (Kelani Ganga) | 3.38 | 🟢 Normal | -0.070 |  |
| 2026-10-12 13:11:04 | Peradeniya (Mahaweli Ganga) | 2.40 | 🟢 Normal | -0.095 |  |
| 2026-10-12 13:01:26 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.129 |  |
| 2026-10-12 13:09:08 | Rathnapura (Kalu Ganga) | 2.50 | 🟢 Normal | -0.180 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)