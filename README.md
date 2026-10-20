# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--20_15:09:07-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **293,189 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thalgahagoda — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-20 15:09:07 | Baddegama (Gin Ganga) | 1.88 | 🟢 Normal | -0.030 |  |
| 2026-10-20 15:08:00 | Urawa (Nilwala Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-10-20 15:07:23 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-10-20 15:07:19 | Moragaswewa (Deduru Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-10-20 15:06:48 | Dunamale (Aththanagalu Oya) | 1.74 | 🟢 Normal | -0.084 |  |
| 2026-10-20 15:06:41 | Magura (Kalu Ganga) | 1.78 | 🟢 Normal | -0.010 |  |
| 2026-10-20 15:06:08 | Horowpothana (Yan Oya) | 2.06 | 🟢 Normal | -0.029 |  |
| 2026-10-20 15:06:03 | Rathnapura (Kalu Ganga) | 2.14 | 🟢 Normal | -0.029 |  |
| 2026-10-20 15:05:50 | Norwood (Kelani Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-10-20 15:05:36 | Thalgahagoda (Nilwala Ganga) | 1.64 | 🟡 Alert | -0.010 |  |
| 2026-10-20 15:05:25 | Kithulgala (Kelani Ganga) | 2.11 | 🟢 Normal | 0.196 | 🔺 Rising |
| 2026-10-20 15:04:58 | Holombuwa (Kelani Ganga) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-10-20 15:04:51 | Urawa (Nilwala Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-10-20 15:04:07 | Thawalama (Gin Ganga) | 2.15 | 🟢 Normal | -0.052 |  |
| 2026-10-20 15:04:03 | Moraketiya (Walawe Ganga) | 1.11 | 🟢 Normal | -0.009 |  |
| 2026-10-20 15:03:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.04 | 🟢 Normal | -0.069 |  |
| 2026-10-20 15:03:36 | Hanwella (Kelani Ganga) | 2.70 | 🟢 Normal | -0.020 |  |
| 2026-10-20 15:03:14 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-20 15:03:11 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-10-20 15:02:59 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | -0.039 |  |
| 2026-10-20 15:02:58 | Giriulla (Maha Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-10-20 15:02:44 | Manampitiya (Mahaweli Ganga) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-10-20 15:02:37 | Badalgama (Maha Oya) | 2.60 | 🟢 Normal | 0.000 |  |
| 2026-10-20 15:02:34 | Glencourse (Kelani Ganga) | 10.76 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-10-20 15:02:16 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | -0.020 |  |
| 2026-10-20 15:02:11 | Thanamalwila (Kirindi Oya) | 1.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-20 15:02:08 | Panadugama (Nilwala Ganga) | 4.53 | 🟢 Normal | -0.020 |  |
| 2026-10-20 15:02:01 | Wellawaya (Kirindi Oya) | 1.21 | 🟢 Normal | -0.030 |  |
| 2026-10-20 15:02:00 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-10-20 15:01:56 | Pitabeddara (Nilwala Ganga) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-10-20 15:01:56 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-20 15:01:50 | Ellagawa (Kalu Ganga) | 6.10 | 🟢 Normal | -0.051 |  |
| 2026-10-20 15:01:46 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | -0.011 |  |
| 2026-10-20 15:01:38 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-20 15:01:11 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | 0.000 |  |
| 2026-10-20 15:00:59 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-10-20 15:00:44 | Galgamuwa (Mee Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-10-20 15:00:44 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | -0.030 |  |
| 2026-10-20 15:00:41 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-10-20 15:00:37 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.061 |  |
| 2026-10-20 15:00:09 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | -0.143 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-20 15:05:36 | Thalgahagoda (Nilwala Ganga) | 1.64 | 🟡 Alert | -0.010 |  |
| 2026-10-20 15:05:25 | Kithulgala (Kelani Ganga) | 2.11 | 🟢 Normal | 0.196 | 🔺 Rising |
| 2026-10-20 15:02:34 | Glencourse (Kelani Ganga) | 10.76 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-10-20 15:02:11 | Thanamalwila (Kirindi Oya) | 1.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-20 15:07:19 | Moragaswewa (Deduru Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-10-20 15:01:38 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-20 15:02:58 | Giriulla (Maha Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-10-20 15:00:44 | Galgamuwa (Mee Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-10-20 15:05:50 | Norwood (Kelani Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-10-20 15:07:23 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-10-20 15:01:56 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-20 15:03:14 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-20 15:02:37 | Badalgama (Maha Oya) | 2.60 | 🟢 Normal | 0.000 |  |
| 2026-10-20 15:02:00 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-10-20 15:01:11 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | 0.000 |  |
| 2026-10-20 15:08:00 | Urawa (Nilwala Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-10-20 15:03:11 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-10-20 15:04:03 | Moraketiya (Walawe Ganga) | 1.11 | 🟢 Normal | -0.009 |  |
| 2026-10-20 15:04:58 | Holombuwa (Kelani Ganga) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-10-20 15:02:44 | Manampitiya (Mahaweli Ganga) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-10-20 15:00:41 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-10-20 15:01:56 | Pitabeddara (Nilwala Ganga) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-10-20 15:06:41 | Magura (Kalu Ganga) | 1.78 | 🟢 Normal | -0.010 |  |
| 2026-10-20 15:01:46 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | -0.011 |  |
| 2026-10-20 15:03:36 | Hanwella (Kelani Ganga) | 2.70 | 🟢 Normal | -0.020 |  |
| 2026-10-20 15:02:16 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | -0.020 |  |
| 2026-10-20 15:02:08 | Panadugama (Nilwala Ganga) | 4.53 | 🟢 Normal | -0.020 |  |
| 2026-10-20 15:06:03 | Rathnapura (Kalu Ganga) | 2.14 | 🟢 Normal | -0.029 |  |
| 2026-10-20 15:06:08 | Horowpothana (Yan Oya) | 2.06 | 🟢 Normal | -0.029 |  |
| 2026-10-20 15:02:01 | Wellawaya (Kirindi Oya) | 1.21 | 🟢 Normal | -0.030 |  |
| 2026-10-20 15:09:07 | Baddegama (Gin Ganga) | 1.88 | 🟢 Normal | -0.030 |  |
| 2026-10-20 15:00:44 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | -0.030 |  |
| 2026-10-20 15:02:59 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | -0.039 |  |
| 2026-10-20 15:01:50 | Ellagawa (Kalu Ganga) | 6.10 | 🟢 Normal | -0.051 |  |
| 2026-10-20 15:04:07 | Thawalama (Gin Ganga) | 2.15 | 🟢 Normal | -0.052 |  |
| 2026-10-20 15:00:37 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.061 |  |
| 2026-10-20 15:03:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.04 | 🟢 Normal | -0.069 |  |
| 2026-10-20 15:06:48 | Dunamale (Aththanagalu Oya) | 1.74 | 🟢 Normal | -0.084 |  |
| 2026-10-20 15:00:09 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | -0.143 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)