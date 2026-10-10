# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--10_10:10:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **283,957 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Dunamale — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-10 10:10:10 | Magura (Kalu Ganga) | 2.09 | 🟢 Normal | -0.027 |  |
| 2026-10-10 10:09:42 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | -0.018 |  |
| 2026-10-10 10:09:15 | Moraketiya (Walawe Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-10-10 10:08:12 | Thawalama (Gin Ganga) | 1.93 | 🟢 Normal | -0.168 |  |
| 2026-10-10 10:07:53 | Giriulla (Maha Oya) | 3.60 | 🟢 Normal | -0.119 |  |
| 2026-10-10 10:07:01 | Holombuwa (Kelani Ganga) | 1.21 | 🟢 Normal | -0.030 |  |
| 2026-10-10 10:06:34 | Urawa (Nilwala Ganga) | 0.80 | 🟢 Normal | -0.028 |  |
| 2026-10-10 10:06:11 | Pitabeddara (Nilwala Ganga) | 1.55 | 🟢 Normal | -0.052 |  |
| 2026-10-10 10:05:51 | Putupaula (Kalu Ganga) | 1.18 | 🟢 Normal | -0.038 |  |
| 2026-10-10 10:05:45 | Glencourse (Kelani Ganga) | 11.22 | 🟢 Normal | -0.048 |  |
| 2026-10-10 10:05:41 | Baddegama (Gin Ganga) | 2.31 | 🟢 Normal | -0.030 |  |
| 2026-10-10 10:05:37 | Badalgama (Maha Oya) | 4.72 | 🟢 Normal | -0.067 |  |
| 2026-10-10 10:05:24 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-10 10:05:22 | Panadugama (Nilwala Ganga) | 4.40 | 🟢 Normal | -0.049 |  |
| 2026-10-10 10:05:16 | Peradeniya (Mahaweli Ganga) | 3.00 | 🟢 Normal | -0.291 |  |
| 2026-10-10 10:05:15 | Hanwella (Kelani Ganga) | 3.53 | 🟢 Normal | -0.096 |  |
| 2026-10-10 10:05:11 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-10-10 10:04:56 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | -0.010 |  |
| 2026-10-10 10:04:35 | Norwood (Kelani Ganga) | 1.04 | 🟢 Normal | -0.025 |  |
| 2026-10-10 10:03:53 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-10-10 10:03:51 | Dunamale (Aththanagalu Oya) | 3.36 | 🟡 Alert | 0.000 |  |
| 2026-10-10 10:03:43 | Moragaswewa (Deduru Oya) | 2.47 | 🟢 Normal | 0.000 |  |
| 2026-10-10 10:03:39 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | -0.010 |  |
| 2026-10-10 10:03:22 | Thanthirimale (Malwathu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-10 10:03:22 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | -0.031 |  |
| 2026-10-10 10:03:21 | Ellagawa (Kalu Ganga) | 7.09 | 🟢 Normal | -0.010 |  |
| 2026-10-10 10:03:11 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-10 10:03:02 | Thanamalwila (Kirindi Oya) | 0.79 | 🟢 Normal | -0.011 |  |
| 2026-10-10 10:02:40 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.010 |  |
| 2026-10-10 10:02:30 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | -0.091 |  |
| 2026-10-10 10:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.74 | 🟢 Normal | -0.043 |  |
| 2026-10-10 10:02:12 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | -0.043 |  |
| 2026-10-10 10:01:59 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-10 10:01:17 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-10 10:01:02 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | -11718.000 |  |
| 2026-10-10 10:01:02 | Rathnapura (Kalu Ganga) | 2.83 | 🟢 Normal | -0.099 |  |
| 2026-10-10 10:01:00 | Weraganthota (Mahaweli Ganga) | 3.26 | 🟢 Normal | -11718.000 |  |
| 2026-10-10 10:01:00 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-10-10 10:00:48 | Nawalapitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-10 10:03:51 | Dunamale (Aththanagalu Oya) | 3.36 | 🟡 Alert | 0.000 |  |
| 2026-10-10 10:03:53 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-10-10 10:01:59 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-10 10:03:11 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-10 10:05:24 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-10 10:03:43 | Moragaswewa (Deduru Oya) | 2.47 | 🟢 Normal | 0.000 |  |
| 2026-10-10 10:05:11 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-10-10 09:08:29 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-10 10:09:15 | Moraketiya (Walawe Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-10-10 10:03:22 | Thanthirimale (Malwathu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-10 10:01:17 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-10 10:03:39 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | -0.010 |  |
| 2026-10-10 10:03:21 | Ellagawa (Kalu Ganga) | 7.09 | 🟢 Normal | -0.010 |  |
| 2026-10-10 10:00:48 | Nawalapitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-10-10 10:02:40 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.010 |  |
| 2026-10-10 10:04:56 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | -0.010 |  |
| 2026-10-10 10:01:00 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-10-10 10:03:02 | Thanamalwila (Kirindi Oya) | 0.79 | 🟢 Normal | -0.011 |  |
| 2026-10-10 10:09:42 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | -0.018 |  |
| 2026-10-10 10:04:35 | Norwood (Kelani Ganga) | 1.04 | 🟢 Normal | -0.025 |  |
| 2026-10-10 10:10:10 | Magura (Kalu Ganga) | 2.09 | 🟢 Normal | -0.027 |  |
| 2026-10-10 10:06:34 | Urawa (Nilwala Ganga) | 0.80 | 🟢 Normal | -0.028 |  |
| 2026-10-10 10:05:41 | Baddegama (Gin Ganga) | 2.31 | 🟢 Normal | -0.030 |  |
| 2026-10-10 10:07:01 | Holombuwa (Kelani Ganga) | 1.21 | 🟢 Normal | -0.030 |  |
| 2026-10-10 10:03:22 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | -0.031 |  |
| 2026-10-10 10:05:51 | Putupaula (Kalu Ganga) | 1.18 | 🟢 Normal | -0.038 |  |
| 2026-10-10 10:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.74 | 🟢 Normal | -0.043 |  |
| 2026-10-10 10:02:12 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | -0.043 |  |
| 2026-10-10 10:05:45 | Glencourse (Kelani Ganga) | 11.22 | 🟢 Normal | -0.048 |  |
| 2026-10-10 10:05:22 | Panadugama (Nilwala Ganga) | 4.40 | 🟢 Normal | -0.049 |  |
| 2026-10-10 10:06:11 | Pitabeddara (Nilwala Ganga) | 1.55 | 🟢 Normal | -0.052 |  |
| 2026-10-10 10:05:37 | Badalgama (Maha Oya) | 4.72 | 🟢 Normal | -0.067 |  |
| 2026-10-10 10:02:30 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | -0.091 |  |
| 2026-10-10 10:05:15 | Hanwella (Kelani Ganga) | 3.53 | 🟢 Normal | -0.096 |  |
| 2026-10-10 10:01:02 | Rathnapura (Kalu Ganga) | 2.83 | 🟢 Normal | -0.099 |  |
| 2026-10-10 10:07:53 | Giriulla (Maha Oya) | 3.60 | 🟢 Normal | -0.119 |  |
| 2026-10-10 10:08:12 | Thawalama (Gin Ganga) | 1.93 | 🟢 Normal | -0.168 |  |
| 2026-10-10 10:05:16 | Peradeniya (Mahaweli Ganga) | 3.00 | 🟢 Normal | -0.291 |  |
| 2026-10-10 10:01:02 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | -11718.000 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)