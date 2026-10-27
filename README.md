# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--27_07:16:04-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **299,153 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Dunamale — Minor Flood; 🟠 Rathnapura — Minor Flood; 🟠 Panadugama — Minor Flood; 🟡 Baddegama — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-27 07:16:04 | Urawa (Nilwala Ganga) | 1.88 | 🟢 Normal | -0.018 |  |
| 2026-10-27 07:12:32 | Baddegama (Gin Ganga) | 3.87 | 🟡 Alert | 0.026 | 🔺 Rising |
| 2026-10-27 07:11:55 | Horowpothana (Yan Oya) | 2.65 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-10-27 07:11:01 | Moraketiya (Walawe Ganga) | 2.27 | 🟢 Normal | -0.027 |  |
| 2026-10-27 07:09:01 | Rathnapura (Kalu Ganga) | 8.62 | 🟠 Minor Flood | -0.037 |  |
| 2026-10-27 07:08:53 | Glencourse (Kelani Ganga) | 14.02 | 🟢 Normal | -0.196 |  |
| 2026-10-27 07:07:44 | Holombuwa (Kelani Ganga) | 2.00 | 🟢 Normal | -0.044 |  |
| 2026-10-27 07:07:37 | Moragaswewa (Deduru Oya) | 5.28 | 🟡 Alert | 0.000 |  |
| 2026-10-27 07:06:34 | Badalgama (Maha Oya) | 5.69 | 🟡 Alert | -0.066 |  |
| 2026-10-27 07:05:54 | Thanthirimale (Malwathu Oya) | 2.98 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-10-27 07:05:53 | Manampitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | -0.048 |  |
| 2026-10-27 07:05:45 | Panadugama (Nilwala Ganga) | 6.48 | 🟠 Minor Flood | -0.049 |  |
| 2026-10-27 07:05:39 | Giriulla (Maha Oya) | 4.22 | 🟢 Normal | -0.192 |  |
| 2026-10-27 07:05:21 | Putupaula (Kalu Ganga) | 3.20 | 🟡 Alert | -0.028 |  |
| 2026-10-27 07:04:45 | Nakkala (Kumbukkan Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-10-27 07:04:44 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-10-27 07:04:34 | Norwood (Kelani Ganga) | 1.55 | 🟡 Alert | -0.049 |  |
| 2026-10-27 07:04:22 | Nawalapitiya (Mahaweli Ganga) | 1.86 | 🟢 Normal | -0.030 |  |
| 2026-10-27 07:04:10 | Hanwella (Kelani Ganga) | 6.63 | 🟢 Normal | -0.057 |  |
| 2026-10-27 07:03:54 | Galgamuwa (Mee Oya) | 4.23 | 🟢 Normal | 0.000 |  |
| 2026-10-27 07:03:49 | Kuda Oya (Kirindi Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-27 07:03:17 | Ellagawa (Kalu Ganga) | 9.83 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-27 07:03:17 | Thawalama (Gin Ganga) | 4.86 | 🟡 Alert | -0.177 |  |
| 2026-10-27 07:03:11 | Wellawaya (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-10-27 07:03:09 | Dunamale (Aththanagalu Oya) | 4.77 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-10-27 07:03:08 | Thaldena (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-10-27 07:02:59 | Peradeniya (Mahaweli Ganga) | 3.75 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-27 07:02:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.20 | 🟠 Minor Flood | 0.108 | 🔺 Rising |
| 2026-10-27 07:02:45 | Nagalagam Street (Kelani Ganga) | 1.10 | 🟢 Normal | -0.097 |  |
| 2026-10-27 07:02:40 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | -0.031 |  |
| 2026-10-27 07:02:37 | Thanamalwila (Kirindi Oya) | 1.28 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-10-27 07:02:20 | Kithulgala (Kelani Ganga) | 2.33 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-10-27 07:02:08 | Deraniyagala (Kelani Ganga) | 1.44 | 🟢 Normal | -0.053 |  |
| 2026-10-27 07:01:35 | Pitabeddara (Nilwala Ganga) | 3.26 | 🟢 Normal | -0.256 |  |
| 2026-10-27 07:01:34 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-10-27 07:00:42 | Magura (Kalu Ganga) | 5.32 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-10-27 07:00:40 | Yaka Wewa (Ma Oya) | 0.82 | 🟢 Normal | -0.021 |  |
| 2026-10-27 07:00:21 | Weraganthota (Mahaweli Ganga) | -2.80 | 🟢 Normal | -0.158 |  |
| 2026-10-27 06:39:38 | Galgamuwa (Mee Oya) | 4.23 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-27 07:02:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.20 | 🟠 Minor Flood | 0.108 | 🔺 Rising |
| 2026-10-27 07:03:09 | Dunamale (Aththanagalu Oya) | 4.77 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-10-27 07:09:01 | Rathnapura (Kalu Ganga) | 8.62 | 🟠 Minor Flood | -0.037 |  |
| 2026-10-27 07:05:45 | Panadugama (Nilwala Ganga) | 6.48 | 🟠 Minor Flood | -0.049 |  |
| 2026-10-27 07:12:32 | Baddegama (Gin Ganga) | 3.87 | 🟡 Alert | 0.026 | 🔺 Rising |
| 2026-10-27 07:00:42 | Magura (Kalu Ganga) | 5.32 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-10-27 06:05:48 | Thalgahagoda (Nilwala Ganga) | 1.59 | 🟡 Alert | 0.019 | 🔺 Rising |
| 2026-10-27 07:07:37 | Moragaswewa (Deduru Oya) | 5.28 | 🟡 Alert | 0.000 |  |
| 2026-10-27 07:05:21 | Putupaula (Kalu Ganga) | 3.20 | 🟡 Alert | -0.028 |  |
| 2026-10-27 07:04:34 | Norwood (Kelani Ganga) | 1.55 | 🟡 Alert | -0.049 |  |
| 2026-10-27 07:06:34 | Badalgama (Maha Oya) | 5.69 | 🟡 Alert | -0.066 |  |
| 2026-10-27 07:03:17 | Thawalama (Gin Ganga) | 4.86 | 🟡 Alert | -0.177 |  |
| 2026-10-27 07:02:37 | Thanamalwila (Kirindi Oya) | 1.28 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-10-27 07:11:55 | Horowpothana (Yan Oya) | 2.65 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-10-27 07:02:20 | Kithulgala (Kelani Ganga) | 2.33 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-10-27 07:05:54 | Thanthirimale (Malwathu Oya) | 2.98 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-10-27 07:03:17 | Ellagawa (Kalu Ganga) | 9.83 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-27 07:02:59 | Peradeniya (Mahaweli Ganga) | 3.75 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-27 07:03:11 | Wellawaya (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-10-27 07:04:45 | Nakkala (Kumbukkan Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-10-27 07:03:54 | Galgamuwa (Mee Oya) | 4.23 | 🟢 Normal | 0.000 |  |
| 2026-10-27 07:04:44 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-10-27 07:01:34 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-10-27 07:03:08 | Thaldena (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-10-27 07:03:49 | Kuda Oya (Kirindi Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-27 07:16:04 | Urawa (Nilwala Ganga) | 1.88 | 🟢 Normal | -0.018 |  |
| 2026-10-27 07:00:40 | Yaka Wewa (Ma Oya) | 0.82 | 🟢 Normal | -0.021 |  |
| 2026-10-27 07:11:01 | Moraketiya (Walawe Ganga) | 2.27 | 🟢 Normal | -0.027 |  |
| 2026-10-27 07:04:22 | Nawalapitiya (Mahaweli Ganga) | 1.86 | 🟢 Normal | -0.030 |  |
| 2026-10-27 07:02:40 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | -0.031 |  |
| 2026-10-27 07:07:44 | Holombuwa (Kelani Ganga) | 2.00 | 🟢 Normal | -0.044 |  |
| 2026-10-27 07:05:53 | Manampitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | -0.048 |  |
| 2026-10-27 07:02:08 | Deraniyagala (Kelani Ganga) | 1.44 | 🟢 Normal | -0.053 |  |
| 2026-10-27 07:04:10 | Hanwella (Kelani Ganga) | 6.63 | 🟢 Normal | -0.057 |  |
| 2026-10-27 07:02:45 | Nagalagam Street (Kelani Ganga) | 1.10 | 🟢 Normal | -0.097 |  |
| 2026-10-27 07:00:21 | Weraganthota (Mahaweli Ganga) | -2.80 | 🟢 Normal | -0.158 |  |
| 2026-10-27 07:05:39 | Giriulla (Maha Oya) | 4.22 | 🟢 Normal | -0.192 |  |
| 2026-10-27 07:08:53 | Glencourse (Kelani Ganga) | 14.02 | 🟢 Normal | -0.196 |  |
| 2026-10-27 07:01:35 | Pitabeddara (Nilwala Ganga) | 3.26 | 🟢 Normal | -0.256 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)