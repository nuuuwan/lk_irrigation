# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--11_18:10:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **285,174 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-11 18:10:32 | Deraniyagala (Kelani Ganga) | 1.54 | 🟢 Normal | 0.600 | 🔺 Rising |
| 2026-10-11 18:08:36 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | -0.010 |  |
| 2026-10-11 18:07:51 | Panadugama (Nilwala Ganga) | 3.93 | 🟢 Normal | 0.156 | 🔺 Rising |
| 2026-10-11 18:06:55 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-10-11 18:06:21 | Baddegama (Gin Ganga) | 2.18 | 🟢 Normal | -0.020 |  |
| 2026-10-11 18:06:06 | Norwood (Kelani Ganga) | 1.47 | 🟢 Normal | -0.059 |  |
| 2026-10-11 18:06:00 | Urawa (Nilwala Ganga) | 0.83 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2026-10-11 18:04:51 | Holombuwa (Kelani Ganga) | 1.34 | 🟢 Normal | 0.340 | 🔺 Rising |
| 2026-10-11 18:04:39 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-10-11 18:04:12 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-10-11 18:04:01 | Hanwella (Kelani Ganga) | 2.70 | 🟢 Normal | -0.043 |  |
| 2026-10-11 18:03:49 | Rathnapura (Kalu Ganga) | 1.93 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-11 18:03:42 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.032 |  |
| 2026-10-11 18:03:29 | Badalgama (Maha Oya) | 3.44 | 🟢 Normal | -0.039 |  |
| 2026-10-11 18:02:59 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-11 18:02:58 | Ellagawa (Kalu Ganga) | 6.51 | 🟢 Normal | 0.213 | 🔺 Rising |
| 2026-10-11 18:02:47 | Magura (Kalu Ganga) | 2.35 | 🟢 Normal | -0.027 |  |
| 2026-10-11 18:02:40 | Thanamalwila (Kirindi Oya) | 1.25 | 🟢 Normal | -0.019 |  |
| 2026-10-11 18:02:39 | Putupaula (Kalu Ganga) | 1.30 | 🟢 Normal | -0.021 |  |
| 2026-10-11 18:02:36 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | -0.029 |  |
| 2026-10-11 18:02:28 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-10-11 18:02:25 | Giriulla (Maha Oya) | 2.13 | 🟢 Normal | -0.021 |  |
| 2026-10-11 18:02:15 | Weraganthota (Mahaweli Ganga) | -3.17 | 🟢 Normal | -0.010 |  |
| 2026-10-11 18:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.23 | 🟢 Normal | -0.034 |  |
| 2026-10-11 18:02:12 | Thawalama (Gin Ganga) | 2.69 | 🟢 Normal | 0.508 | 🔺 Rising |
| 2026-10-11 18:01:58 | Dunamale (Aththanagalu Oya) | 2.30 | 🟢 Normal | -0.084 |  |
| 2026-10-11 18:01:48 | Glencourse (Kelani Ganga) | 10.69 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-10-11 18:01:41 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-11 18:01:36 | Pitabeddara (Nilwala Ganga) | 1.43 | 🟢 Normal | 0.156 | 🔺 Rising |
| 2026-10-11 18:01:33 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-10-11 18:01:21 | Moragaswewa (Deduru Oya) | 2.16 | 🟢 Normal | -0.120 |  |
| 2026-10-11 18:01:17 | Nakkala (Kumbukkan Oya) | 0.93 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-10-11 18:01:13 | Manampitiya (Mahaweli Ganga) | -0.27 | 🟢 Normal | -0.030 |  |
| 2026-10-11 18:01:12 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-10-11 18:01:08 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.053 |  |
| 2026-10-11 18:01:07 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-10-11 18:00:40 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-10-11 18:00:23 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-11 18:00:16 | Thanthirimale (Malwathu Oya) | 1.12 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-11 18:10:32 | Deraniyagala (Kelani Ganga) | 1.54 | 🟢 Normal | 0.600 | 🔺 Rising |
| 2026-10-11 18:02:12 | Thawalama (Gin Ganga) | 2.69 | 🟢 Normal | 0.508 | 🔺 Rising |
| 2026-10-11 18:04:51 | Holombuwa (Kelani Ganga) | 1.34 | 🟢 Normal | 0.340 | 🔺 Rising |
| 2026-10-11 18:02:58 | Ellagawa (Kalu Ganga) | 6.51 | 🟢 Normal | 0.213 | 🔺 Rising |
| 2026-10-11 18:07:51 | Panadugama (Nilwala Ganga) | 3.93 | 🟢 Normal | 0.156 | 🔺 Rising |
| 2026-10-11 18:01:36 | Pitabeddara (Nilwala Ganga) | 1.43 | 🟢 Normal | 0.156 | 🔺 Rising |
| 2026-10-11 18:06:00 | Urawa (Nilwala Ganga) | 0.83 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2026-10-11 18:01:48 | Glencourse (Kelani Ganga) | 10.69 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-10-11 18:01:07 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-10-11 18:01:12 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-10-11 18:01:17 | Nakkala (Kumbukkan Oya) | 0.93 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-10-11 18:03:49 | Rathnapura (Kalu Ganga) | 1.93 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-11 18:00:16 | Thanthirimale (Malwathu Oya) | 1.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-11 18:01:41 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-11 18:00:23 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-11 18:06:55 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-10-11 18:04:12 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-10-11 18:02:59 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-11 18:02:28 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-10-11 18:00:40 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-10-11 18:01:33 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-10-11 18:02:15 | Weraganthota (Mahaweli Ganga) | -3.17 | 🟢 Normal | -0.010 |  |
| 2026-10-11 18:04:39 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-10-11 18:08:36 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | -0.010 |  |
| 2026-10-11 18:02:40 | Thanamalwila (Kirindi Oya) | 1.25 | 🟢 Normal | -0.019 |  |
| 2026-10-11 18:06:21 | Baddegama (Gin Ganga) | 2.18 | 🟢 Normal | -0.020 |  |
| 2026-10-11 18:02:39 | Putupaula (Kalu Ganga) | 1.30 | 🟢 Normal | -0.021 |  |
| 2026-10-11 18:02:25 | Giriulla (Maha Oya) | 2.13 | 🟢 Normal | -0.021 |  |
| 2026-10-11 18:02:47 | Magura (Kalu Ganga) | 2.35 | 🟢 Normal | -0.027 |  |
| 2026-10-11 18:02:36 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | -0.029 |  |
| 2026-10-11 18:01:13 | Manampitiya (Mahaweli Ganga) | -0.27 | 🟢 Normal | -0.030 |  |
| 2026-10-11 18:03:42 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.032 |  |
| 2026-10-11 18:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.23 | 🟢 Normal | -0.034 |  |
| 2026-10-11 18:03:29 | Badalgama (Maha Oya) | 3.44 | 🟢 Normal | -0.039 |  |
| 2026-10-11 18:04:01 | Hanwella (Kelani Ganga) | 2.70 | 🟢 Normal | -0.043 |  |
| 2026-10-11 18:01:08 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.053 |  |
| 2026-10-11 18:06:06 | Norwood (Kelani Ganga) | 1.47 | 🟢 Normal | -0.059 |  |
| 2026-10-11 18:01:58 | Dunamale (Aththanagalu Oya) | 2.30 | 🟢 Normal | -0.084 |  |
| 2026-10-11 18:01:21 | Moragaswewa (Deduru Oya) | 2.16 | 🟢 Normal | -0.120 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)